# Google crawling and indexing

Use this reference for architecture, rendering, URL, sitemap, robots, migration, JavaScript, and production-host work. The source inventory contains 41 crawling/indexing pages reviewed on 2026-08-21.

## Discovery and link graph

- Use real `<a href>` links that resolve to usable URLs. Do not rely on click handlers, router-only attributes, or non-anchor elements for crawl-critical navigation.
- Give anchors concise, descriptive, natural text. Provide surrounding context; avoid empty, generic, keyword-stuffed, or chained links.
- Link every important page from at least one other page. For a managed lead-generation site, review one-inbound-link pages and prefer two or more useful contextual sources where genuine relationships exist.
- Keep navigation and important links available without requiring a gesture, carousel position, form submission, or client-only state.
- Qualify paid links with `rel="sponsored"` or `nofollow`; qualify user-generated links with `ugc` or `nofollow` when applicable.

Source: https://developers.google.com/search/docs/crawling-indexing/links-crawlable

## URLs, canonicals, duplicates, and redirects

- Use simple, descriptive, stable URLs with words meaningful to users. Prefer one consistent case, delimiter, trailing-slash, protocol, and host policy.
- Avoid session IDs, unstable parameters, unnecessary fragments, infinite filter spaces, and multiple URLs for the same primary content.
- Give every indexable page one absolute HTML canonical. Align internal links, redirects, sitemap URLs, `hreflang`, and structured-data IDs with the chosen canonical.
- Use a permanent server-side 301/308 for durable moves. Redirect each valuable old URL to the closest relevant replacement; do not mass-redirect unrelated URLs to the homepage.
- Preserve path and query when consolidating HTTP/HTTPS or `www`/apex unless a documented rule intentionally changes them.
- Keep redirect chains short, eliminate loops, and return a real 404/410 for removed content without a replacement.

Sources:

- https://developers.google.com/search/docs/crawling-indexing/url-structure
- https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls
- https://developers.google.com/search/docs/crawling-indexing/301-redirects

## Sitemaps

- Submit a sitemap or sitemap index URL, not an ordinary webpage or directory URL.
- Include only canonical, indexable, 200-status URLs that the site intends to appear in Search.
- Exclude redirects, errors, preview/studio hosts, private routes, APIs, search/filter URLs, and `noindex` pages.
- Use absolute URLs from one canonical host. Keep `<lastmod>` accurate only when a substantive page update occurred.
- Split large sitemaps and use an index when needed. Add image, video, or news extensions only when the content and project require them.
- Reference the canonical sitemap in `robots.txt`, make every sitemap return 200 XML, and verify it after production cutover.

A sitemap assists discovery but does not replace internal links or guarantee indexing.

Sources:

- https://developers.google.com/search/docs/crawling-indexing/sitemaps/overview
- https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap
- https://developers.google.com/search/docs/crawling-indexing/sitemaps/large-sitemaps

## Robots and index controls

- Use `robots.txt` to manage crawling, not to protect secrets and not as the primary way to remove an indexable URL.
- To prevent indexing, allow crawling and use `noindex` in a robots meta tag or `X-Robots-Tag`. Use authentication or access control for private content.
- Keep production pages free of preview `noindex`; make every temporary preview non-indexable at the edge.
- Verify syntax, user-agent grouping, path matching, and referenced sitemap URLs. Test Googlebot access independently from browser access and Cloudflare WAF/Bot controls.
- Use `nosnippet`, `max-snippet`, `max-image-preview`, `max-video-preview`, or `data-nosnippet` only for an explicit content-sharing decision.

Sources:

- https://developers.google.com/search/docs/crawling-indexing/robots/intro
- https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag
- https://developers.google.com/search/docs/crawling-indexing/control-what-you-share

## JavaScript and rendering

- Put unique titles, descriptions, canonicals, headings, links, and useful primary content in server-rendered or static HTML when practical.
- Use History API URLs that are stable and directly loadable. Do not depend on fragments for unique indexable pages.
- Return meaningful status behavior from the server or edge; client-rendered error messages on a 200 URL can become soft 404s.
- Ensure dynamically inserted links are real anchors, lazy-loaded images/videos appear after normal viewport interaction, and critical content is not gated behind unsupported user events.
- Do not use dynamic rendering as a default architecture. If a legacy workaround is unavoidable, keep bot/user content equivalent and plan removal.
- Inspect raw HTML, rendered HTML, URL Inspection output, blocked resources, console/network errors, and no-JavaScript behavior.

Sources:

- https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics
- https://developers.google.com/search/docs/crawling-indexing/javascript/fix-search-javascript
- https://developers.google.com/search/docs/crawling-indexing/javascript/lazy-loading

## Mobile-first and page parity

- Serve equivalent primary content, headings, metadata, robots directives, structured data, image alt text, and important links on mobile and desktop.
- Use responsive design and a valid viewport. Do not hide the main content or reduce mobile content to a thin version.
- Ensure fixed controls, interstitials, and animations do not obscure content or conversion paths.
- Keep mobile images and videos high quality and crawlable; use stable URLs and descriptive surrounding text.

Source: https://developers.google.com/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing

## Site moves and releases

- Inventory old URLs and inbound value, create a one-to-one redirect map, verify both properties when possible, and change one major dimension at a time.
- Deploy redirects, canonicals, internal links, sitemap, robots, analytics, and Search Console configuration coherently.
- Keep redirects long enough for users and search systems to adopt the move. Monitor old/new index coverage, crawl errors, traffic, and server logs.
- For hosting-only changes, lower operational risk with preview testing, DNS planning, cache checks, TLS verification, and a tested rollback.

Sources:

- https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes
- https://developers.google.com/search/docs/crawling-indexing/site-move-no-url-changes

## Specialized routing

Search [google-search-central-inventory.csv](google-search-central-inventory.csv) and open the matched official page when the project uses AMP, image/news/video sitemaps, locale-adaptive delivery, A/B testing, removals, crawl-rate controls, redacted information, non-HTML files, or another specialized mechanism.
