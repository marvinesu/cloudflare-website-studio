#!/usr/bin/env python3
"""Crawl a canonical production sitemap and report live SEO release defects."""

from __future__ import annotations

import argparse
import json
import re
import sys
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass
from html.parser import HTMLParser
from urllib.error import HTTPError, URLError
from urllib.parse import urldefrag, urljoin, urlparse
from urllib.request import Request, urlopen


USER_AGENT = "CloudflareWebsiteStudio-LiveSEO/1.0"
PREVIEW_HOST = re.compile(r"(?:localhost|\.workers\.dev|\.pages\.dev|studio\.)", re.I)
LOCAL_TYPES = {"LocalBusiness", "ProfessionalService"}


@dataclass
class Finding:
    severity: str
    code: str
    url: str
    detail: str


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.title = ""
        self.description = ""
        self.robots = ""
        self.canonicals: list[str] = []
        self.html_lang = ""
        self.viewport = ""
        self.h1_count = 0
        self.links: list[str] = []
        self.anchors: list[tuple[str, str]] = []
        self.images_without_alt = 0
        self.jsonld: list[str] = []
        self._capture_title = False
        self._capture_jsonld = False
        self._buffer: list[str] = []
        self._anchor_href: str | None = None
        self._anchor_name: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = {key.lower(): value or "" for key, value in attrs}
        names = {key.lower() for key, _ in attrs}
        tag = tag.lower()
        if tag == "html":
            self.html_lang = values.get("lang", "")
        elif tag == "title":
            self._capture_title = True
            self._buffer = []
        elif tag == "h1":
            self.h1_count += 1
        elif tag == "a" and values.get("href"):
            self.links.append(values["href"])
            self._anchor_href = values["href"]
            self._anchor_name = [values.get("aria-label", ""), values.get("title", "")]
        elif tag == "img":
            if "alt" not in names:
                self.images_without_alt += 1
            if self._anchor_href is not None:
                self._anchor_name.append(values.get("alt", ""))
        elif tag == "link" and "canonical" in values.get("rel", "").lower():
            self.canonicals.append(values.get("href", ""))
        elif tag == "meta":
            name = values.get("name", "").lower()
            if name == "description":
                self.description = values.get("content", "")
            elif name == "robots":
                self.robots = values.get("content", "")
            elif name == "viewport":
                self.viewport = values.get("content", "")
        elif tag == "script" and values.get("type", "").lower() == "application/ld+json":
            self._capture_jsonld = True
            self._buffer = []

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if tag == "title" and self._capture_title:
            self.title = "".join(self._buffer).strip()
            self._capture_title = False
            self._buffer = []
        elif tag == "script" and self._capture_jsonld:
            self.jsonld.append("".join(self._buffer).strip())
            self._capture_jsonld = False
            self._buffer = []
        elif tag == "a" and self._anchor_href is not None:
            self.anchors.append((self._anchor_href, " ".join(self._anchor_name).strip()))
            self._anchor_href = None
            self._anchor_name = []

    def handle_data(self, data: str) -> None:
        if self._capture_title or self._capture_jsonld:
            self._buffer.append(data)
        if self._anchor_href is not None:
            self._anchor_name.append(data)


def fetch(url: str) -> tuple[int, str, str, dict[str, str]]:
    request = Request(url, headers={"User-Agent": USER_AGENT, "Accept": "text/html,application/xml;q=0.9,*/*;q=0.8"})
    try:
        with urlopen(request, timeout=25) as response:
            body = response.read().decode(response.headers.get_content_charset() or "utf-8", "replace")
            return response.status, response.geturl(), body, dict(response.headers.items())
    except HTTPError as error:
        body = error.read().decode(error.headers.get_content_charset() or "utf-8", "replace")
        return error.code, error.geturl(), body, dict(error.headers.items())
    except URLError as error:
        raise RuntimeError(f"request failed for {url}: {error.reason}") from error


def sitemap_urls(sitemap_url: str, seen: set[str] | None = None) -> list[str]:
    seen = seen or set()
    if sitemap_url in seen:
        return []
    seen.add(sitemap_url)
    status, _, body, _ = fetch(sitemap_url)
    if status != 200:
        raise RuntimeError(f"sitemap returned {status}: {sitemap_url}")
    root = ET.fromstring(body)
    locations = [node.text.strip() for node in root.iter() if node.tag.endswith("loc") and node.text]
    if root.tag.endswith("sitemapindex"):
        urls: list[str] = []
        for location in locations:
            urls.extend(sitemap_urls(location, seen))
        return urls
    return locations


def schema_nodes(value: object) -> list[dict]:
    if isinstance(value, list):
        nodes: list[dict] = []
        for item in value:
            nodes.extend(schema_nodes(item))
        return nodes
    if not isinstance(value, dict):
        return []
    nodes = [value] if "@type" in value else []
    graph = value.get("@graph")
    if isinstance(graph, (list, dict)):
        nodes.extend(schema_nodes(graph))
    return nodes


def normalized_page_url(url: str) -> str:
    clean = urldefrag(url)[0]
    parsed = urlparse(clean)
    path = parsed.path or "/"
    if not path.endswith("/") and not re.search(r"/[^/]+\.[a-z0-9]+$", path, re.I):
        path += "/"
    return parsed._replace(path=path, query="", fragment="").geturl()


def run(origin: str, sitemap: str, max_pages: int) -> dict:
    origin = origin.rstrip("/")
    host = urlparse(origin).netloc.lower()
    findings: list[Finding] = []
    robots_url = f"{origin}/robots.txt"
    robots_status, _, robots_body, _ = fetch(robots_url)
    if robots_status != 200:
        findings.append(Finding("error", "robots-status", robots_url, f"returned {robots_status}"))
    elif re.search(r"User-agent:\s*\*[\s\S]{0,300}?Disallow:\s*/(?:\s|$)", robots_body, re.I):
        findings.append(Finding("error", "robots-block", robots_url, "blanket production crawl block detected"))
    else:
        declared_sitemaps = [match.strip() for match in re.findall(r"^Sitemap:\s*(\S+)", robots_body, re.I | re.M)]
        if sitemap not in declared_sitemaps:
            findings.append(Finding("warning", "robots-sitemap", robots_url, f"does not declare {sitemap}"))

    sitemap_entries = sitemap_urls(sitemap)
    if len(sitemap_entries) != len(set(sitemap_entries)):
        findings.append(Finding("warning", "sitemap-duplicates", sitemap, "duplicate URL entries detected"))
    urls = list(dict.fromkeys(sitemap_entries))[:max_pages]
    pages: dict[str, PageParser] = {}
    titles: defaultdict[str, list[str]] = defaultdict(list)
    descriptions: defaultdict[str, list[str]] = defaultdict(list)

    for requested in urls:
        if urlparse(requested).netloc.lower() != host:
            findings.append(Finding("error", "sitemap-host", requested, f"does not use canonical host {host}"))
        status, final_url, body, headers = fetch(requested)
        canonical_requested = normalized_page_url(requested)
        if status != 200:
            findings.append(Finding("error", "page-status", requested, f"returned {status}"))
            continue
        if normalized_page_url(final_url) != canonical_requested:
            findings.append(Finding("warning", "sitemap-redirect", requested, f"resolves to {final_url}"))
        robots_header = headers.get("X-Robots-Tag", "")
        if "noindex" in robots_header.lower():
            findings.append(Finding("error", "x-robots-noindex", requested, robots_header))
        parser = PageParser()
        parser.feed(body)
        pages[canonical_requested] = parser
        if not parser.html_lang:
            findings.append(Finding("warning", "html-lang", requested, "html lang attribute is missing"))
        if not parser.viewport:
            findings.append(Finding("warning", "mobile-viewport", requested, "viewport meta tag is missing"))
        if parser.h1_count != 1:
            findings.append(Finding("error", "h1-count", requested, f"found {parser.h1_count}"))
        if not parser.title:
            findings.append(Finding("error", "title-missing", requested, "title is empty"))
        else:
            titles[parser.title].append(requested)
        if not parser.description:
            findings.append(Finding("error", "description-missing", requested, "meta description is empty"))
        else:
            descriptions[parser.description].append(requested)
        if not parser.canonicals:
            findings.append(Finding("error", "canonical-missing", requested, "canonical link is absent"))
        else:
            if len(parser.canonicals) != 1:
                findings.append(Finding("error", "canonical-count", requested, f"found {len(parser.canonicals)} canonical links"))
            canonical = normalized_page_url(urljoin(requested, parser.canonicals[0]))
            if canonical != canonical_requested:
                findings.append(Finding("error", "canonical-mismatch", requested, f"declares {canonical}"))
            if urlparse(canonical).netloc.lower() != host:
                findings.append(Finding("error", "canonical-host", requested, f"declares {canonical}"))
        if "noindex" in parser.robots.lower():
            findings.append(Finding("error", "meta-noindex", requested, parser.robots))
        if PREVIEW_HOST.search(body):
            findings.append(Finding("error", "preview-host-leak", requested, "preview or retired host appears in HTML"))
        if parser.images_without_alt:
            findings.append(Finding("warning", "image-alt-missing", requested, f"{parser.images_without_alt} image(s) omit the alt attribute"))
        unnamed_links = [href for href, name in parser.anchors if href and not name and not href.startswith(("#", "javascript:"))]
        if unnamed_links:
            findings.append(Finding("warning", "link-name-missing", requested, f"{len(unnamed_links)} crawlable link(s) have no text or accessible label"))

        for raw in parser.jsonld:
            try:
                parsed = json.loads(raw)
            except json.JSONDecodeError as error:
                findings.append(Finding("error", "jsonld-syntax", requested, str(error)))
                continue
            for node in schema_nodes(parsed):
                raw_types = node.get("@type", [])
                types = {raw_types} if isinstance(raw_types, str) else set(raw_types)
                if types & LOCAL_TYPES and not node.get("address"):
                    findings.append(Finding("error", "localbusiness-address", requested, f"{', '.join(sorted(types))} has no verified address"))
                if types & LOCAL_TYPES and not node.get("name"):
                    findings.append(Finding("error", "localbusiness-name", requested, "LocalBusiness name is missing"))

    for title, members in titles.items():
        if len(members) > 1:
            findings.append(Finding("warning", "duplicate-title", members[0], f"used by {len(members)} sitemap pages: {title}"))
    for description, members in descriptions.items():
        if len(members) > 1:
            findings.append(Finding("warning", "duplicate-description", members[0], f"used by {len(members)} sitemap pages"))

    incoming: defaultdict[str, set[str]] = defaultdict(set)
    sitemap_set = set(pages)
    for source, parser in pages.items():
        for href in parser.links:
            target = normalized_page_url(urljoin(source, href))
            if target in sitemap_set and target != source:
                incoming[target].add(source)
    for page in sorted(sitemap_set):
        count = len(incoming[page])
        if count == 0 and page != normalized_page_url(f"{origin}/"):
            findings.append(Finding("error", "orphan-sitemap-page", page, "zero distinct internal inbound sources"))
        elif count == 1:
            findings.append(Finding("warning", "thin-internal-links", page, "one distinct internal inbound source"))

    return {
        "origin": origin,
        "sitemap": sitemap,
        "pages_in_sitemap": len(urls),
        "pages_crawled": len(pages),
        "summary": dict(Counter(finding.severity for finding in findings)),
        "findings": [asdict(finding) for finding in findings],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("origin", help="canonical production origin, for example https://example.com")
    parser.add_argument("--sitemap", help="sitemap or sitemap-index URL")
    parser.add_argument("--max-pages", type=int, default=500)
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--strict", action="store_true", help="fail for warnings as well as errors")
    args = parser.parse_args()
    sitemap = args.sitemap or f"{args.origin.rstrip('/')}/sitemap-index.xml"
    try:
        report = run(args.origin, sitemap, args.max_pages)
    except (RuntimeError, ET.ParseError) as error:
        print(f"Live SEO audit failed: {error}", file=sys.stderr)
        return 2
    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print(f"Live SEO audit: {report['origin']}")
        print(f"Crawled {report['pages_crawled']}/{report['pages_in_sitemap']} sitemap pages")
        for finding in report["findings"]:
            print(f"[{finding['severity'].upper()}] {finding['code']} {finding['url']} — {finding['detail']}")
        summary = report["summary"]
        print(f"Summary: {summary.get('error', 0)} error(s), {summary.get('warning', 0)} warning(s)")
    errors = report["summary"].get("error", 0)
    warnings = report["summary"].get("warning", 0)
    return 1 if errors or (args.strict and warnings) else 0


if __name__ == "__main__":
    raise SystemExit(main())
