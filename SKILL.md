---
name: cloudflare-website-studio
description: Create, migrate, redesign, improve, deploy, and operate visually distinctive production websites on Cloudflare Workers or Pages. Use for WordPress-to-Astro migrations, local-service businesses such as locksmiths and remodelers, automatic keyword and customer-question research, service and location page architecture, internal linking, AI-search discoverability, static and full-stack sites, Cloudflare architecture, Wrangler configuration, bindings, forms, redirects, domains, professional animation, responsive design, accessibility, performance, technical/on-page/local SEO, and natural human-centered copy. Includes audit, implementation, browser QA, rollback, and production verification workflows.
---

# Cloudflare Website Studio

Build a production website, not a mockup. Treat content truth, URLs, design, motion, SEO, runtime behavior, Cloudflare configuration, and rollback as one delivery system.

## Non-negotiable execution contract

Run the work as gated delivery, not one uninterrupted generation pass. Do not enter the next gate until the current gate has evidence. For a local-service build, the minimum gates are: verified business facts, dated demand research, keyword-to-page map, site architecture/internal links, content/design direction, implementation, local browser QA, Cloudflare preview, and production verification.

Create `website-plan/` in the target project and keep the applicable artifacts current:

```text
website-plan/
  project-brief.md
  fact-claim-ledger.md
  research-notes.md
  keyword-page-map.csv
  question-bank.md
  url-internal-link-map.csv
  location-qualification.csv
  content-briefs/
  design-direction.md
  motion-plan.md
  cloudflare-release.md
  qa-report.md
```

Do not publish research artifacts if they contain private business data, credentials, personal lead data, or licensed-tool exports that cannot be redistributed.

## Load the right references

Read only the references needed for the task, but always read every reference marked required for the chosen mode.

| Mode | Required references |
| --- | --- |
| Create or redesign | [visual-design.md](references/visual-design.md), [motion.md](references/motion.md), [content-seo.md](references/content-seo.md), [conversion-systems.md](references/conversion-systems.md), [qa-release.md](references/qa-release.md) |
| Improve an existing site | Same as create, plus [workflow.md](references/workflow.md) |
| WordPress migration | [migration.md](references/migration.md), [cloudflare-platform.md](references/cloudflare-platform.md), [content-seo.md](references/content-seo.md), [qa-release.md](references/qa-release.md) |
| Cloudflare setup or deployment | [cloudflare-platform.md](references/cloudflare-platform.md), [qa-release.md](references/qa-release.md) |
| Copy or SEO work | [content-seo.md](references/content-seo.md) |
| Animation work | [motion.md](references/motion.md) |
| Local-service business | [local-service-growth.md](references/local-service-growth.md), [content-seo.md](references/content-seo.md), [conversion-systems.md](references/conversion-systems.md), [visual-design.md](references/visual-design.md), [motion.md](references/motion.md), [qa-release.md](references/qa-release.md) |

Consult [sources.md](references/sources.md) when updating this skill or resolving provenance.

## Select the delivery mode

- **Create:** shape the business, content, visual system, routes, and Cloudflare target before implementation.
- **Migrate:** keep WordPress read-only, inventory everything, preserve URL and claim contracts, rebuild, preview, then cut over reversibly.
- **Improve:** capture the current site, audit code and rendered behavior, preserve what works, implement prioritized improvements, and compare before/after.
- **Review:** report evidence and recommendations without editing.
- **Deploy:** validate the existing build, configure the correct Cloudflare product, publish to preview, verify, then release with rollback.

## Establish the project contract

Before changing code:

1. Read repository instructions and inspect Git status, stack, commands, routes, content sources, design tokens, current motion, and Cloudflare configuration.
2. Identify the business, real audience, primary user action, canonical domain, target markets, approved claims, measurable success, scope, and non-goals.
3. Record the Cloudflare account/project/Worker, production branch, preview strategy, custom domains, bindings, secrets, DNS dependencies, and rollback target.
4. For existing sites, capture representative desktop and narrow-mobile states and inspect at least one page from every route family.
5. For migrations, create an explicit URL map, feature inventory, claim matrix, media inventory, integration inventory, and DNS inventory.

Never invent testimonials, clients, metrics, awards, locations, credentials, prices, guarantees, availability, or structured-data facts. Ask or omit.

## Auto-run local-service growth mode

When the business is a locksmith, remodeler, roofer, plumber, electrician, HVAC provider, landscaper, cleaner, contractor, or another location-based service, automatically load [local-service-growth.md](references/local-service-growth.md). Do not wait for the user to say "SEO."

Before finalizing the information architecture or copy:

1. Research the live search landscape for every verified core service and priority market.
2. Collect transactional, commercial, informational, local, emergency, and comparison intent; customer questions; vocabulary; SERP features; and competitor coverage gaps.
3. Produce a keyword-to-page map that prevents cannibalization.
4. Build service pages, qualified location pages, useful question-led resources, and contextual internal links.
5. Add search and AI-discovery foundations: crawlable HTML, canonical URLs, schema from verified facts, sitemaps, descriptive links, answer-ready passages, source attribution, crawler policy, and freshness workflows.
6. Reject thin programmatic location pages and unsupported local claims.

Research findings are evidence, not permission to copy competitors. Write original content from verified business knowledge and useful synthesis.

## Make architecture decisions deliberately

Choose the smallest runtime that satisfies the site:

- Prefer static HTML for content-led marketing, editorial, portfolio, and local-service websites.
- Use Cloudflare Pages for straightforward Git-connected static delivery and Pages Functions when its model fits.
- Use Workers Static Assets when Worker-owned routing, selective `/api/*` execution, middleware, authentication, or service bindings justify it.
- Keep assets asset-first. Route only paths that require compute through Worker-first behavior.
- Do not move an entire site to SSR because one form or endpoint is dynamic.
- Treat `wrangler.jsonc` as the source of truth for new Workers projects. Validate it against the installed Wrangler version and current official documentation.

## Shape a specific visual and editorial direction

Write a short design read before implementation:

```text
Audience: ...
Business promise: ...
Desired feeling: ...
Visual references / anti-references: ...
Typography and color logic: ...
Layout variance: 1-10
Motion intensity: 1-10
Content density: 1-10
Signature idea: ...
```

Preserve a strong existing brand. Otherwise create a compact token system for type, color, spacing, radii, shadows, layers, and motion. Make the site recognizable without its logo. If the design could be swapped onto an unrelated startup unchanged, it is not finished.

## Build in this order

1. Content truth, route model, and primary conversion path
2. Semantic initial HTML, metadata, schema, sitemap, robots, redirects, and 404
3. Tokens, typography, layout, navigation, footer, forms, and reusable primitives
4. Route families and responsive composition
5. Cloudflare runtime endpoints and bindings
6. Conversion interactions, call/chat/form routing, and honest delivery states
7. Professional motion system and signature interaction
8. Accessibility, resilience, performance, and SEO validation
9. Preview deployment, production cutover, verification, and rollback evidence

Keep core copy and navigation visible without animation JavaScript. Enhance progressively.

## Build an active conversion surface

Do not stop at an attractive brochure that only displays information. For lead-generation work, make the primary user action immediately operable and add only the interaction paths the business can actually service. Follow [conversion-systems.md](references/conversion-systems.md).

For urgent local services, keep `tel:` access persistent and let any assistant or chatbot qualify the situation before returning the visitor to a call. A scripted decision assistant is often safer and faster than a generative chat experience. It must disclose its limits, avoid estimates and availability promises, never request credentials or access codes, and preserve a direct call path at every state.

For scheduled work, use a short server-validated form with explicit consent, abuse controls, honest success/failure messages, and verified delivery. Prefer a narrow Cloudflare Worker endpoint. Use Cloudflare Email Service `send_email` bindings only after the sender domain and destination are verified; otherwise keep the form disabled or fail closed rather than claiming delivery.

## Enforce a professional motion pass

For marketing, portfolio, and service websites, do not finish with only generic fade-up reveals. Declare `restrained`, `expressive`, or `cinematic` motion. Default to expressive unless the brand or use frequency calls for restraint.

An expressive pass must address at least three distinct categories supported by the page: hero choreography, navigation/menu transitions, section or media reveals, CTA feedback, card/media interaction, typography treatment, state transitions, or one signature story-driven interaction. Repeated copies of one reveal count once.

Name the purpose of every animation: feedback, spatial continuity, state indication, preventing a jarring change, explanation, or rare delight. Reject motion that cannot name a purpose. Ship hover gating, interruption behavior, cleanup, and a meaningful reduced-motion variant with the implementation.

## Write for humans and search engines

Write from verified source material and real audience vocabulary. Prefer concrete nouns, specific verbs, proof, constraints, and useful details over inflated claims. Vary sentence length naturally, remove redundant intros, and make each section advance the reader's decision.

Avoid generic AI signals: vague superlatives, symmetrical three-card filler, repetitive headline formulas, fake quotations, fabricated precision, excessive em dashes, "in today's fast-paced world," "unlock," "elevate," "seamless," "cutting-edge," and paragraphs that say nothing testable. Do not attempt to game AI detectors. Humanize through truth, specificity, editorial judgment, and a consistent voice.

SEO must serve the same reader. Give every indexable page a distinct search intent, useful main content, unique title and description, canonical URL, one logical H1, meaningful internal links, appropriate schema, and crawlable initial HTML. Do not mass-generate thin location or service pages.

## Verify before completion

Run the portable audit:

```bash
python scripts/site_preflight.py <project-root>
```

Then run the project's format, lint, typecheck, tests, and production build. Inspect generated output and the rendered site. Test desktop, breakpoint boundaries, true narrow mobile, keyboard, touch, zoom, reduced motion, no-JavaScript visibility where relevant, forms, failures, redirects, 404, metadata, schema, sitemap, robots, and canonical behavior.

For local-service projects, run `python scripts/site_preflight.py <project-root> --local-service`. Use `--strict` when every finding must block CI. Score the completed implementation with [quality-scorecard.md](references/quality-scorecard.md); a blocking defect fails release regardless of the total.

Deploy to preview first. Verify the actual Cloudflare runtime, not only a framework dev server. Production completion requires the canonical URL, representative internal routes, API failures, real form delivery when approved, domain policy, security headers, logs/errors, active deployment/version, Git SHA, and rollback target.

## Report precisely

State what changed, the design and motion direction, routes and files affected, validation commands and results, preview/production status, known limitations, and rollback. Distinguish "built," "locally tested," "preview deployed," "production deployed," and "production verified."

Report each gate as `passed`, `failed`, `blocked`, or `not applicable`; never imply that an unrun gate passed.
