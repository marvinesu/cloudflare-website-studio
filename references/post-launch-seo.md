# Canonical-domain SEO review

Run this gate only after the exact approved release is reachable on the main custom domain. Local builds and preview hosts remain necessary, but they cannot pass this gate because DNS, redirects, headers, cache, bot controls, and canonical-host behavior may differ in production.

Create or update `website-plan/post-launch-seo.md`. Record the review timestamp and timezone, canonical origin, tested apex/`www` variants, Git SHA, Cloudflare deployment/version, sitemap URL, tools used, evidence links, findings, fixes, rerun results, remaining risks, owner, and one status: `passed`, `failed`, `blocked`, or `not applicable`.

## Establish the live release identity

- Confirm the canonical domain serves the intended release and record its Git SHA and Cloudflare version.
- Test HTTP to HTTPS and apex/`www` behavior. Require one canonical host, path/query preservation where applicable, no loops, and no unnecessary redirect chains.
- Confirm representative HTML and content-hashed assets belong to the same release. Distinguish stale CDN/browser cache from a deployment mismatch before changing code.
- Search rendered HTML, generated feeds, sitemap entries, schema, Open Graph URLs, forms, and internal links for preview, `.workers.dev`, `.pages.dev`, studio, localhost, or retired-host leakage.

## Crawl the canonical host

Crawl every URL in the production sitemap and route inventory. For each indexable page verify:

- final status `200`, one intended canonical, indexable robots directives, unique useful title and description, one logical H1, crawlable main content, and production-correct social metadata;
- canonical, sitemap, internal-link, redirect, and `hreflang` consistency;
- valid structured-data syntax whose claims match visible, verified content;
- working internal links and essential images, with no soft 404, orphan priority page, mixed content, redirect loop, or accidental client-only content dependency.

Verify deliberate statuses for redirects, retired URLs, unknown routes, APIs, and private routes. Do not turn missing URLs into homepage `200` responses.

## Verify discovery controls at the edge

- Fetch `robots.txt` and every referenced sitemap from the canonical origin. Require `200`, the canonical host, and only intended indexable URLs.
- Confirm production HTML and asset responses do not inherit preview `noindex` or an unintended `X-Robots-Tag`.
- Test intended public pages with ordinary browser access and the crawler policies chosen for Googlebot, Bingbot, and OAI-SearchBot. Decide GPTBot training access separately.
- Inspect Cloudflare WAF, Bot Management, Access, geo rules, redirects, and JavaScript challenges when crawler access differs from browser access. Do not weaken security broadly to fix a narrow policy mistake.
- Treat Search Console, Bing Webmaster Tools, IndexNow, analytics, and business-profile connections as account-dependent. Verify readiness and existing ownership when access is available; do not create ownership, submit indexing requests, or change external profiles without authorization.

## Check live search experience and performance

- Run PageSpeed Insights or equivalent Lighthouse checks against the canonical homepage and at least one representative route from every materially different template. Test mobile first, then desktop.
- Record the tested URL, time, device profile, Performance, Accessibility, Best Practices, and SEO scores plus LCP, INP or TBT when INP is unavailable, CLS, and any field-data availability. Never present lab data as field data.
- Apply the project's performance budgets and investigate regressions in the real LCP resource, render-blocking work, font delivery, image dimensions, client JavaScript, third-party embeds, and animation.
- Recheck the primary conversion path, navigation, and structured content with JavaScript constrained or disabled where static visibility is expected.

## Resolve and close the gate

Block completion for accidental `noindex`, wrong or missing production canonicals, preview-host leakage, broken sitemap/robots, important `4xx`/`5xx`, redirect loops, soft 404s, untrue schema, inaccessible crawlable content, or an unintended crawler block. Treat missed project performance budgets and material metadata/internal-link defects as failures until fixed or explicitly accepted by the owner.

After a fix, commit it, rebuild, verify the exact artifact on a non-indexable preview when risk warrants, release it, and rerun every affected live check. Link the final evidence from `website-plan/cloudflare-release.md` and `website-plan/qa-report.md`. Keep the last known-good rollback available until the canonical-domain SEO gate passes.

Record a follow-up owner and observation window for index coverage, crawl errors, Core Web Vitals field data, query/page performance, unexpected canonical selection, and AI/search referral trends. Do not promise indexing, ranking, citation, or lead volume.

## Official references

- https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls
- https://developers.google.com/search/docs/crawling-indexing/sitemaps/overview
- https://developers.google.com/search/docs/crawling-indexing/robots/intro
- https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data
- https://developers.google.com/speed/docs/insights/v5/get-started
- https://help.openai.com/en/articles/12627856-publishers-and-developers-faq
