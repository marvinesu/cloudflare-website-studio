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
- Existing-site work includes a matched source-versus-current route/section/navigation/form/media comparison; high-value source strengths are preserved or intentionally replaced
- Social destinations and business-directory links are source-verified; no profile URL is guessed from a business name
- No separate AI-only copy, fake author/reviewer, automatically refreshed date, special AI schema, forced content chunking, or default `llms.txt` claim

## Visual and responsive

- Representative route from every family inspected
- Desktop, tablet, breakpoint boundaries, 390px or narrower, and content extremes tested
- No horizontal overflow, clipping, sticky/floating collisions, or hidden CTA
- 200% zoom, keyboard order, focus, Escape, labels, errors, contrast, and touch targets pass
- Images have correct crop, dimensions, loading behavior, and alt treatment
- Logo, hero, font, and representative route-family images load through both preview and custom hosts and render with nonzero natural dimensions in the browser
- Source and current pages are compared at matched desktop and narrow-mobile viewports; section count alone is not treated as visual quality evidence
- Empty, loading, success, error, and long-content states are intentional

## Accessibility

- WCAG target and exceptions are recorded in `website-plan/accessibility-plan.md`
- Document language, landmarks, heading order, skip link, labels, names, descriptions, and status announcements pass
- Keyboard order follows the interface; focus is visible, returns after dialogs, and is not obscured by sticky/floating layers
- Navigation, primary CTA, forms, sliders, dialogs, maps, and media operate without dragging, hover, or touch-only gestures
- 320 CSS px reflow, 200% zoom, increased text spacing, contrast, non-color state cues, and target sizing pass
- Automatic motion can be paused when required; reduced-motion behavior preserves content and comprehension
- First-party accessibility preferences apply before paint, persist after reload/navigation, combine safely, and reset correctly
- No third-party accessibility overlay or badge script is present
- Automated findings are reviewed manually; a passing scanner is not reported as WCAG conformance

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
- Each route exposes one intentional primary lead flow; duplicate vendor/first-party forms and competing chat/form overlays are absent or explicitly justified
- Qualification assistants are manual, use a consistent server-validated data model, require consent, preserve direct contact fallback, and pass modal/non-modal keyboard behavior
- Turnstile-protected forms validate tokens with Siteverify on the server, check configured hostname/action, and reject expired, reused, or failed tokens
- Endpoint abuse controls, payload limits, and dependency fail-open/fail-closed behavior are documented and tested
- Logs show no unaccounted exceptions; tracing/monitoring configured according to risk
- Logs and traces contain no secrets or unnecessary personal form data

## Production

- Canonical homepage and representative internal routes return intended content and assets
- Apex/`www`, TLS, redirects, headers, and cache behavior are correct
- Active deployment/version and Git SHA match intended release
- The released version was built from the recorded commit, verified on a non-indexable preview, uploaded/tagged as that exact artifact, promoted with a known traffic allocation, and reverified after triggers/custom domains were synchronized
- APIs and forms work on every served hostname
- CDN/cache differences are distinguished from deployment failure using asset hashes and response headers
- Rollback target and procedure are recorded and executable
- Rollback compatibility with current data schemas and bound resources is proven; gradual releases include skew tests and stop conditions when used

Do not declare completion from upload logs, a single screenshot, a passing automated accessibility scan, a `200` form response, or one CDN point of presence.
