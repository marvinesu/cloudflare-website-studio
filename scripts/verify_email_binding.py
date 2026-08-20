#!/usr/bin/env python3
"""Verify Wrangler Email Service destinations against Cloudflare account state."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import tomllib
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any


def strip_jsonc(text: str) -> str:
    """Remove JSONC comments and trailing commas without changing string data."""
    output: list[str] = []
    index = 0
    in_string = False
    escaped = False
    while index < len(text):
        char = text[index]
        next_char = text[index + 1] if index + 1 < len(text) else ""
        if in_string:
            output.append(char)
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == '"':
                in_string = False
            index += 1
            continue
        if char == '"':
            in_string = True
            output.append(char)
            index += 1
            continue
        if char == "/" and next_char == "/":
            index += 2
            while index < len(text) and text[index] not in "\r\n":
                index += 1
            continue
        if char == "/" and next_char == "*":
            index += 2
            while index + 1 < len(text) and text[index : index + 2] != "*/":
                index += 1
            index += 2
            continue
        output.append(char)
        index += 1
    return re.sub(r",\s*([}\]])", r"\1", "".join(output))


def find_config(project_root: Path, explicit: str | None) -> Path:
    if explicit:
        candidate = Path(explicit).expanduser().resolve()
        if not candidate.is_file():
            raise FileNotFoundError(f"Wrangler config not found: {candidate}")
        return candidate
    for name in ("wrangler.jsonc", "wrangler.json", "wrangler.toml"):
        candidate = project_root / name
        if candidate.is_file():
            return candidate
    raise FileNotFoundError(f"No Wrangler config found under {project_root}")


def load_config(path: Path) -> dict[str, Any]:
    if path.suffix.lower() == ".toml":
        with path.open("rb") as handle:
            return tomllib.load(handle)
    return json.loads(strip_jsonc(path.read_text(encoding="utf-8")))


def binding_groups(config: dict[str, Any]) -> list[tuple[str, list[dict[str, Any]]]]:
    groups: list[tuple[str, list[dict[str, Any]]]] = []
    top_level = config.get("send_email")
    if isinstance(top_level, list):
        groups.append(("default", [item for item in top_level if isinstance(item, dict)]))
    environments = config.get("env")
    if isinstance(environments, dict):
        for name, environment in environments.items():
            if not isinstance(environment, dict):
                continue
            entries = environment.get("send_email")
            if isinstance(entries, list):
                groups.append((f"env.{name}", [item for item in entries if isinstance(item, dict)]))
    return groups


def configured_destinations(groups: list[tuple[str, list[dict[str, Any]]]]) -> tuple[set[str], list[str]]:
    addresses: set[str] = set()
    unrestricted: list[str] = []
    for environment, bindings in groups:
        for binding in bindings:
            name = str(binding.get("name") or "unnamed")
            fixed = binding.get("destination_address")
            allowed = binding.get("allowed_destination_addresses")
            if isinstance(fixed, str) and fixed.strip():
                addresses.add(fixed.strip().lower())
            if isinstance(allowed, list):
                addresses.update(str(item).strip().lower() for item in allowed if str(item).strip())
            if not fixed and not allowed:
                unrestricted.append(f"{environment}:{name}")
    return addresses, unrestricted


def fetch_verified_destinations(account_id: str, token: str) -> set[str]:
    verified: set[str] = set()
    page = 1
    while True:
        query = urllib.parse.urlencode({"verified": "true", "per_page": 50, "page": page})
        url = f"https://api.cloudflare.com/client/v4/accounts/{account_id}/email/routing/addresses?{query}"
        request = urllib.request.Request(url, headers={"Authorization": f"Bearer {token}", "Accept": "application/json"})
        try:
            with urllib.request.urlopen(request, timeout=20) as response:
                payload = json.load(response)
        except urllib.error.HTTPError as error:
            body = error.read().decode("utf-8", errors="replace")
            raise RuntimeError(f"Cloudflare API returned HTTP {error.code}: {body[:300]}") from error
        except urllib.error.URLError as error:
            raise RuntimeError(f"Cloudflare API request failed: {error.reason}") from error
        if not payload.get("success"):
            raise RuntimeError(f"Cloudflare API rejected the request: {payload.get('errors', [])}")
        for item in payload.get("result") or []:
            if item.get("verified") and item.get("email"):
                verified.add(str(item["email"]).strip().lower())
        info = payload.get("result_info") or {}
        total_pages = int(info.get("total_pages") or 1)
        if page >= total_pages:
            break
        page += 1
    return verified


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Verify Cloudflare Email Service destinations configured by Wrangler.")
    parser.add_argument("project_root", nargs="?", default=".", help="Project containing wrangler.jsonc/json/toml")
    parser.add_argument("--config", help="Explicit Wrangler config path")
    parser.add_argument("--account-id", default=os.getenv("CLOUDFLARE_ACCOUNT_ID"), help="Cloudflare account ID or CLOUDFLARE_ACCOUNT_ID")
    parser.add_argument("--token-env", default="CLOUDFLARE_API_TOKEN", help="Environment variable containing a read-capable API token")
    parser.add_argument("--offline", action="store_true", help="List configured restrictions without calling Cloudflare")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = Path(args.project_root).expanduser().resolve()
    try:
        config_path = find_config(root, args.config)
        groups = binding_groups(load_config(config_path))
    except (FileNotFoundError, json.JSONDecodeError, tomllib.TOMLDecodeError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        return 1
    if not groups:
        print(f"NOT_APPLICABLE: no send_email bindings in {config_path}")
        return 0
    addresses, unrestricted = configured_destinations(groups)
    print(f"Config: {config_path}")
    if addresses:
        print("Configured restricted destinations: " + ", ".join(sorted(addresses)))
    if unrestricted:
        print("REVIEW: unrestricted bindings require runtime recipient and delivery verification: " + ", ".join(unrestricted))
    if args.offline:
        print("OFFLINE: account-level verification was not checked")
        return 0
    token = os.getenv(args.token_env)
    if not args.account_id or not token:
        print(f"BLOCKED: provide --account-id/CLOUDFLARE_ACCOUNT_ID and {args.token_env} to verify account state", file=sys.stderr)
        return 2
    try:
        verified = fetch_verified_destinations(args.account_id, token)
    except RuntimeError as error:
        print(f"BLOCKED: {error}", file=sys.stderr)
        return 2
    missing = sorted(addresses - verified)
    if missing:
        print("FAIL: unverified or missing Cloudflare destinations: " + ", ".join(missing), file=sys.stderr)
        return 1
    if addresses:
        print("PASS: every restricted destination is verified in the Cloudflare account")
    if unrestricted:
        print("PASS_WITH_REVIEW: configured restrictions passed; observe an approved end-to-end send for unrestricted recipients")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
