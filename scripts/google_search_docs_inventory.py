#!/usr/bin/env python3
"""Inventory the official Google Search Central documentation navigation."""

from __future__ import annotations

import argparse
import csv
import re
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass, asdict
from html import unescape
from html.parser import HTMLParser
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin, urlparse, urlunparse
from urllib.request import Request, urlopen


ROOT = "https://developers.google.com/search/docs"
USER_AGENT = "CloudflareWebsiteStudio-SearchDocsInventory/1.0"


class DocsParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[str] = []
        self.title = ""
        self.h1 = ""
        self.headings: list[str] = []
        self._capture: str | None = None
        self._buffer: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = {key.lower(): value or "" for key, value in attrs}
        tag = tag.lower()
        if tag == "a" and values.get("href"):
            self.links.append(values["href"])
        if tag in {"title", "h1", "h2", "h3"}:
            self._capture = tag
            self._buffer = []

    def handle_data(self, data: str) -> None:
        if self._capture:
            self._buffer.append(data)

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if tag != self._capture:
            return
        text = normalize_text(" ".join(self._buffer))
        if tag == "title":
            self.title = text
        elif tag == "h1" and not self.h1:
            self.h1 = text
        elif tag in {"h2", "h3"} and text:
            self.headings.append(text)
        self._capture = None
        self._buffer = []


@dataclass
class DocRecord:
    section: str
    tier: str
    status: int
    title: str
    h1: str
    last_updated: str
    url: str
    headings: str
    final_url: str
    error: str = ""


def normalize_text(value: str) -> str:
    return re.sub(r"\s+", " ", unescape(value)).strip()


def fetch(url: str) -> tuple[int, str, str]:
    request = Request(url, headers={"User-Agent": USER_AGENT, "Accept-Language": "en"})
    try:
        with urlopen(request, timeout=30) as response:
            return response.status, response.geturl(), response.read().decode("utf-8", "replace")
    except HTTPError as exc:
        return exc.code, exc.geturl(), exc.read().decode("utf-8", "replace")
    except (URLError, TimeoutError) as exc:
        return 0, url, str(exc)


def canonical_doc_url(href: str) -> str | None:
    absolute = urljoin(ROOT, href)
    parsed = urlparse(absolute)
    if parsed.netloc != "developers.google.com" or not parsed.path.startswith("/search/docs"):
        return None
    if parsed.path.startswith("/search/docs/guides/"):
        return None
    clean_path = parsed.path.rstrip("/") or "/search/docs"
    return urlunparse(("https", parsed.netloc, clean_path, "", "hl=en", ""))


def section_for(url: str) -> str:
    path = urlparse(url).path
    parts = path.split("/")
    return parts[3] if len(parts) > 3 else "overview"


def tier_for(url: str) -> str:
    path = urlparse(url).path
    conditional = (
        "/structured-data/",
        "/specialty/",
        "/amp",
        "/web-stories",
        "/package-tracking",
        "/flexible-sampling",
        "/prevent-images",
        "/pause-online-business",
    )
    return "conditional" if any(token in path for token in conditional) else "core"


def inspect_doc(url: str) -> DocRecord:
    status, final_url, body = fetch(url)
    if status != 200:
        return DocRecord(section_for(url), tier_for(url), status, "", "", "", url, "", final_url, normalize_text(body)[:240])
    parser = DocsParser()
    parser.feed(body)
    updated = re.search(r"Last updated\s*([^<\n]+?\(UTC\))", body, re.I)
    headings = " | ".join(dict.fromkeys(parser.headings))
    return DocRecord(
        section_for(url),
        tier_for(url),
        status,
        parser.title,
        parser.h1,
        normalize_text(updated.group(1)) if updated else "",
        url,
        headings,
        final_url,
    )


def discover() -> list[str]:
    status, _, body = fetch(f"{ROOT}?hl=en")
    if status != 200:
        raise RuntimeError(f"Unable to load documentation index: HTTP {status}")
    parser = DocsParser()
    parser.feed(body)
    urls = {url for href in parser.links if (url := canonical_doc_url(href))}
    return sorted(urls)


def write_csv(records: list[DocRecord], output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    fields = list(asdict(records[0]).keys()) if records else list(DocRecord.__annotations__)
    with output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(asdict(record) for record in records)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    parser.add_argument("--workers", type=int, default=6)
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()

    urls = discover()
    records: list[DocRecord] = []
    with ThreadPoolExecutor(max_workers=max(1, min(args.workers, 10))) as pool:
        futures = {pool.submit(inspect_doc, url): url for url in urls}
        for future in as_completed(futures):
            records.append(future.result())
    records.sort(key=lambda record: (record.section, record.url))

    if args.output:
        write_csv(records, args.output)

    failures = [record for record in records if record.status != 200]
    core = sum(record.tier == "core" for record in records)
    conditional = len(records) - core
    print(f"Google Search Central docs: {len(records)} total, {core} core, {conditional} conditional")
    print(f"HTTP failures: {len(failures)}")
    for record in failures:
        print(f"- {record.status} {record.url} {record.error}")
    return 1 if args.strict and failures else 0


if __name__ == "__main__":
    sys.exit(main())
