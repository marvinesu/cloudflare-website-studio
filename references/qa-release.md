# QA and release gates

Use [quality-scorecard.md](quality-scorecard.md) for the final scored decision. The checks below remain mandatory evidence and cannot be averaged away.

## Code and build

- Repository instructions followed; unrelated changes preserved
- Format/lint/typecheck/tests pass
- Production build succeeds with expected route count
- Dependency and secret scans reviewed
- Generated output contains no private exports, source maps, server files, or credentials
- Wrangler configuration validates against the installed version
- Local test uses the real Pages/Workers runtime where possible

## Content and SEO

- Every route has an approved disposition and correct status
- Titles, descriptions, canonicals, H1s, Open Graph, schema, sitemap, robots, RSS, and internal links validate
- Claims are verified and consistent across HTML, metadata, schema, forms, and feeds
- Redirects are specific, single-hop where practical, and loop-free
- Unknown routes return an intentional 404/410
- Preview URLs are non-indexable
- Local-service projects include a reviewed keyword-to-page map, question bank, qualified location-page table, and internal-link matrix
- Location pages contain unique local utility/proof and do not form thin service-city combinations
- Every important page has at least one crawlable contextual inbound link
- Intended AI/search crawlers are not accidentally blocked by robots.txt, Cloudflare WAF/bot rules, authentication, or JavaScript challenges
- OAI-SearchBot and GPTBot policies are decided separately; IndexNow/AI discovery is never reported as a ranking or citation guarantee
- Important pages passed source-pack, fact, voice, usefulness, rendered-web, and owner/domain review gates
- No separate AI-only copy, fake author/reviewer, automatically refreshed date, special AI schema, forced content chunking, or default `llms.txt` claim

## Visual and responsive

- Representative route from every family inspected
- Desktop, tablet, breakpoint boundaries, 390px or narrower, and content extremes tested
- No horizontal overflow, clipping, sticky/floating collisions, or hidden CTA
- 200% zoom, keyboard order, focus, Escape, labels, errors, contrast, and touch targets pass
- Images have correct crop, dimensions, loading behavior, and alt treatment
- Empty, loading, success, error, and long-content states are intentional

## Motion

- Motion level and purposes documented
- At least three distinct categories for an expressive marketing pass
- No `transition: all`, `scale(0)` entry, casual layout animation, or ungated hover motion
- Interruption, repeated triggers, exits, client navigation cleanup, and background/offscreen behavior tested
- Reduced-motion variant preserves content and state comprehension
- Core HTML stays visible if JavaScript or animation initialization fails
- Third-party motion code/assets have a current source, version or retrieval date, license, modification note, and visible attribution where required
- Scroll stories do not hijack wheel/touch input; semantic chapters remain readable and the primary CTA stays operable outside the pinned sequence
- Lottie/Rive/video players are locally controlled where practical, size-budgeted, lazy below the fold, paused offscreen/background, and replaced by a meaningful fallback

## Runtime and security

- Static paths remain asset-first unless intentionally protected/transformed
- APIs reject unsupported methods, origins, content types, oversized/invalid payloads, and abuse cases
- CORS and security headers match actual dependencies
- Secrets exist in bindings, not source or client bundles
- Forms show honest status and approved end-to-end delivery is observed
- Turnstile-protected forms validate tokens with Siteverify on the server, check configured hostname/action, and reject expired, reused, or failed tokens
- Endpoint abuse controls, payload limits, and dependency fail-open/fail-closed behavior are documented and tested
- Logs show no unaccounted exceptions; tracing/monitoring configured according to risk
- Logs and traces contain no secrets or unnecessary personal form data

## Production

- Canonical homepage and representative internal routes return intended content and assets
- Apex/`www`, TLS, redirects, headers, and cache behavior are correct
- Active deployment/version and Git SHA match intended release
- APIs and forms work on every served hostname
- CDN/cache differences are distinguished from deployment failure using asset hashes and response headers
- Rollback target and procedure are recorded and executable
- Rollback compatibility with current data schemas and bound resources is proven; gradual releases include skew tests and stop conditions when used

Do not declare completion from upload logs, a single screenshot, a `200` form response, or one CDN point of presence.
