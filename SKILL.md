---
name: cloudflare-website-studio
description: Build, migrate, redesign, or improve production websites deployed with Cloudflare Pages or Workers. Use for new marketing sites, existing frontend modifications, WordPress-to-static/Astro migrations, Cloudflare deployment preparation, post-build design critique, visual polish, accessibility, responsive behavior, purposeful motion, performance, SEO preservation, forms, redirects, and production verification. Combines a migration-first delivery workflow with principles from Impeccable, Taste Skill, and Emil Kowalski's design engineering guidance.
---

# Cloudflare Website Studio

Treat the website as a production system and a designed experience. Preserve content, URLs, claims, integrations, and rollback before redesigning. Make design decisions from the site's actual audience and brand, then verify the built result in a browser and on Cloudflare.

## Choose the operating mode

- **Create:** define product and design direction, build the smallest complete site, then deploy.
- **Migrate:** inventory WordPress read-only, map every public URL and feature, rebuild, then cut over reversibly.
- **Improve:** audit the current implementation and rendered site, prioritize issues, modify in place, then compare before and after.
- **Review:** produce evidence-backed findings without editing unless the user also requests changes.

Read [references/workflow.md](references/workflow.md) for the required phase gates. Read [references/design-quality.md](references/design-quality.md) before changing visual design, interaction, or motion. Read [references/cloudflare.md](references/cloudflare.md) for Pages/Workers architecture and release checks.

See [references/sources.md](references/sources.md) for the upstream projects combined by this workflow and the responsibility assigned to each.

## Establish the contract

1. Inspect repository instructions, Git status, stack, build scripts, deployment configuration, and existing design tokens.
2. Identify the canonical domain, Cloudflare target, editable scope, source of truth, approval boundaries, and rollback path.
3. Classify the surface: marketing, editorial, ecommerce, product UI, or hybrid. Do not apply marketing-page patterns blindly to dashboards or transactional flows.
4. For an existing site, capture representative desktop and mobile states before edits. Audit real routes, not only the homepage.
5. For WordPress, keep the source read-only. Inventory pages, posts, media, menus, metadata, schema, forms, scripts, redirects, plugins, and DNS-related integrations.

Never infer business claims, locations, credentials, testimonials, prices, guarantees, or regulatory statements. Publish verified or explicitly owner-authorized facts only.

## Shape before building

Write a short design direction covering audience, desired feeling, visual references, anti-references, typography, palette, spacing, shape language, imagery, and motion intensity. Reuse a coherent existing system when one exists. If it does not, create a small token set before page-specific styling.

Prioritize in this order:

1. Correct content and task completion
2. Information architecture and hierarchy
3. Responsive layout and accessibility
4. Typography, color, imagery, and component consistency
5. Purposeful interaction and motion
6. Decorative delight

Do not redesign merely to make the work visibly different. Preserve distinctive, effective choices and fix the highest-impact weaknesses.

## Implement safely

- Prefer static output for content-led sites. Add Worker logic only for genuine server needs such as validated forms, authentication boundaries, or custom media behavior.
- Preserve every indexed URL or map it to a specific permanent redirect. Do not redirect all missing pages to the homepage.
- Keep essential copy and navigation in initial HTML. Treat JavaScript as enhancement.
- Use semantic elements, one logical H1, visible focus, keyboard operation, sufficient contrast, explicit image dimensions, and reduced-motion fallbacks.
- Centralize tokens and shared primitives. Avoid page-local style drift, unnecessary cards, generic three-column grids, default font choices, and decorative UI without content purpose.
- Make animation interruptible, brief, and motivated by feedback, state, hierarchy, or spatial continuity. Avoid `transition: all`, layout-property animation, bounce easing, and repeated motion on frequent actions.
- Preserve secrets in Cloudflare bindings or secrets. Never expose them in client bundles, logs, commits, or migration exports.

When the locally installed `impeccable`, `design-taste-frontend`, or `emil-design-eng` skill is available, load it for a focused deep pass. Resolve conflicts with this priority: user instructions, repository instructions, verified content/URL contracts, accessibility and functionality, established brand system, then aesthetic preference.

## Verify the result

Run `python scripts/site_preflight.py <project-root>` for a portable configuration check. Then run the project's own lint, typecheck, test, and production build commands.

Inspect the rendered result at representative desktop and true narrow-mobile widths. Test navigation, focus, Escape, forms, loading/error/empty states, overflow, content without JavaScript where relevant, reduced motion, and client-side navigation cleanup. Measure or inspect Core Web Vitals risks instead of guessing.

For deployment, verify the canonical public URL, critical routes, redirects, metadata, sitemap, robots, assets, forms, API error paths, apex/`www` policy, and rollback procedure. Upload logs alone are not proof of a successful release.

## Report

Lead with what changed and whether it is verified. Include affected routes/files, tests and build results, deployment status, limitations, and rollback information. For review-only work, rank findings by impact and include concrete before/after recommendations.
