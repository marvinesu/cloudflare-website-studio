#!/usr/bin/env python3
"""Read-only, cross-platform preflight for Cloudflare website projects."""

from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    if not root.is_dir():
        print(f"ERROR: project root does not exist: {root}")
        return 2

    checks: list[tuple[str, bool, str]] = []
    package = root / "package.json"
    checks.append(("package.json", package.is_file(), "JavaScript project manifest"))

    if package.is_file():
        try:
            data = json.loads(package.read_text(encoding="utf-8"))
            scripts = data.get("scripts", {})
            checks.extend(
                (f"script:{name}", name in scripts, "recommended project command")
                for name in ("build", "test", "lint")
            )
        except (OSError, json.JSONDecodeError) as exc:
            print(f"ERROR: cannot parse {package}: {exc}")
            return 2

    cloudflare_files = ["wrangler.jsonc", "wrangler.json", "wrangler.toml"]
    found_cf = [name for name in cloudflare_files if (root / name).is_file()]
    checks.append(("cloudflare-config", bool(found_cf), ", ".join(found_cf) or "no Wrangler config found"))

    public = root / "public"
    checks.append(("robots.txt", (public / "robots.txt").is_file(), "static robots policy"))
    checks.append(("404", any((root / p).is_file() for p in ("src/pages/404.astro", "src/pages/404.tsx", "src/pages/404.jsx", "public/404.html")), "intentional not-found page"))

    for name, passed, note in checks:
        print(f"{'PASS' if passed else 'WARN'}  {name}: {note}")

    warnings = sum(not passed for _, passed, _ in checks)
    print(f"\nPreflight complete: {len(checks) - warnings} passed, {warnings} warnings.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
