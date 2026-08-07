# Production quality scorecard

Use this scorecard after implementation and before preview release. Evidence outranks scores: any blocking defect fails the gate even when the total is high.

Score each dimension from 0 to 4:

- **0 - absent:** not attempted or no evidence
- **1 - unsafe:** major omissions, unsupported claims, or broken behavior
- **2 - functional:** basic requirements work but important weaknesses remain
- **3 - production-ready:** complete, verified, accessible, and appropriate to the project
- **4 - exceptional:** distinctive, resilient, measurable, and unusually well executed

| Dimension | Evidence to inspect |
| --- | --- |
| Facts and claims | Fact ledger, source links, owner approval, consistency across copy/schema/forms |
| Research and strategy | Dated queries, audience language, competitive gaps, page-opportunity decisions |
| Architecture and links | Intent ownership, route families, navigation, contextual inbound links, no orphan pages |
| Content quality | Original usefulness, specificity, voice, scannability, question coverage, editorial approval |
| Visual design | Recognizable direction, tokens, typography, composition, imagery, responsive states |
| Motion | Purpose, variety, timing, interruption, cleanup, hover gating, reduced-motion behavior |
| SEO and AI discovery | Crawlable HTML, unique metadata, canonicals, schema truth, sitemap/robots, crawler policy |
| Accessibility and performance | Keyboard, focus, zoom, contrast, touch, image/loading behavior, performance evidence |
| Cloudflare security and operations | Runtime choice, bindings, secrets, forms, abuse controls, logs, version and rollback |
| Production verification | Canonical host, representative routes, form delivery, headers, errors, release record |

## Release rule

Preview release requires every applicable dimension to score at least 2 and no blocking defect. Production completion requires at least 30/40 overall, every applicable dimension at least 3, and direct production evidence. Mark an inapplicable dimension `N/A` and calculate the percentage against the available maximum; the production threshold remains 75%.

Blocking defects include fabricated or unapproved claims, exposed secrets, broken primary conversion, inaccessible critical controls, indexable preview environments, thin doorway pages, incorrect canonical/redirect behavior, failed server-side Turnstile validation, unverified form delivery, or an unexecutable rollback.

Record the score, evidence link, owner, and remediation for every dimension in `website-plan/qa-report.md`. A score is a decision aid, not a substitute for the detailed gates in `qa-release.md`.
