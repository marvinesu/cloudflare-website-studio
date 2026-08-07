# Gated delivery workflow

For every gate, record inputs, actions, evidence, unresolved risks, and one of `passed`, `failed`, `blocked`, or `not applicable`. A generated file is not evidence until read back or tested.

## 1. Discover

- Read repository guidance and inspect the existing system before proposing a replacement.
- Record routes, content types, design tokens, reusable components, integrations, analytics, forms, SEO data, and deployment configuration.
- For WordPress, export through read-only REST, XML, or owner-provided backups. Sanitize HTML and separate immutable raw data from normalized content.

**Pass:** scope, source of truth, business facts, existing system, authority, exclusions, and rollback are recorded without unsupported claims.

## 2. Define contracts

- Give every public URL one disposition: preserve, redirect to a specific equivalent, or intentionally retire.
- Give every dynamic behavior one disposition: static, browser enhancement, narrow Worker endpoint, approved third party, or intentional removal.
- Mark every public claim as verified, owner-authorized, ambiguous, or unsupported.
- Record DNS and rollback values before changing infrastructure.

**Pass:** every known URL, feature, claim, integration, and infrastructure dependency has a disposition.

## 3. Audit and shape

- Capture representative rendered states and identify the five highest-impact problems.
- Write a one-paragraph design direction and a compact token system.
- Plan page hierarchy and responsive behavior before styling individual sections.
- On redesigns, distinguish what to preserve, refine, replace, and remove.

For local services, complete dated search research, keyword/page ownership, question bank, location qualification, and internal-link architecture before writing page copy.

**Pass:** the intended audience, page architecture, content proof, visual system, motion level, success metrics, and acceptance criteria are explicit.

## 4. Build or modify

- Work through shared foundations first: tokens, layout, typography, navigation, buttons, forms, metadata, footer.
- Build route families and reusable content models rather than duplicating pages.
- Keep runtime scope narrow and test behavior changes with regressions where practical.
- Preserve unrelated user changes and keep migration artifacts and secrets out of Git.

Implement in vertical slices: one complete representative route family first, verify its content/design/runtime pattern, then scale the approved pattern. Do not mass-generate pages before the representative page passes.

**Pass:** all approved routes and behaviors exist, build successfully, and preserve the defined contracts.

## 5. Critique and polish

- Critique hierarchy, clarity, composition, emotional fit, and brand distinctiveness.
- Audit accessibility, responsiveness, robustness, performance, SEO, and edge cases.
- Polish spacing, typography, color, imagery, component states, and motion only after structural problems are resolved.
- Compare before and after at the same routes and viewport sizes.

Run at least two distinct reviews: one for user/content/design quality and one for technical/runtime/SEO quality. Fix verified high-impact findings and rerun the affected checks.

**Pass:** no P0/P1 issue remains, P2 limitations are explicit, and visual/motion decisions are verified in a browser.

## 6. Release

- Run lint, typecheck, tests, production build, generated-output checks, and secret scans.
- Test locally through the real Pages/Workers runtime when possible.
- Deploy to a preview before production; keep WordPress or the prior deployment available for rollback.
- Verify production from the canonical domain and record the active version, routes, limitations, and rollback.

**Pass:** preview evidence, production evidence, active version/SHA, domain behavior, monitoring, and rollback are recorded. Upload success alone fails this gate.
