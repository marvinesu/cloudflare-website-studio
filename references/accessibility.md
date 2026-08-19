# Accessibility baseline

Treat accessibility as an implementation constraint, not a final overlay. Target WCAG 2.2 AA unless the project has a stricter contractual or legal requirement. Record the target, exceptions, evidence, and remediation owner in `website-plan/accessibility-plan.md`.

## Build the accessible page first

- Use semantic landmarks, one meaningful `main`, logical headings, descriptive links, and a working skip link.
- Set the document language and support reflow at 320 CSS px and text zoom at 200% without loss of content or operation.
- Keep DOM order, reading order, visual order, and keyboard order aligned. Never use positive `tabindex` to repair layout.
- Give every control an accessible name that contains its visible label. Use native elements before ARIA.
- Keep focus visible and unobscured by sticky headers, mobile docks, notifications, dialogs, or floating controls.
- Make pointer targets at least 24 by 24 CSS px or provide the WCAG spacing/equivalent exception; prefer 44 by 44 for primary touch controls.
- Do not use color alone for state. Verify text, non-text, focus, placeholder, disabled, and error contrast in every theme.
- Give informative images useful alt text; use empty alt text for decorative images. Do not repeat adjacent captions.
- Provide captions/transcripts for meaningful media and a non-drag alternative for sliders, maps, reorder controls, and carousels.
- Associate form labels, instructions, errors, and status messages programmatically. Move focus or announce updates when needed without stealing focus unnecessarily.
- Preserve content and primary actions without animation JavaScript. Respect `prefers-reduced-motion` and provide a persistent pause mechanism for non-essential automatic motion that runs longer than five seconds.

Automated checks are evidence, not conformance. Complete keyboard and rendered-browser testing on representative route families.

## Ship a first-party accessibility menu

For marketing and lead-generation sites, include a lightweight first-party accessibility menu by default unless the repository already provides an equivalent approved control or the owner explicitly declines it. Never load a third-party accessibility overlay, badge script, or service.

The menu supplements the accessible baseline; it does not repair inaccessible markup. Include:

- Bigger text using a root class and a bounded relative scale
- High contrast using project tokens/classes without hiding imagery or destroying focus indicators
- Readable system font with increased spacing that still passes reflow and text-spacing tests
- Highlight links with a non-color cue
- Pause animations that disables non-essential CSS and script-driven motion
- Reset all

Use one persisted object such as `a11y-preferences` in `localStorage`. Apply saved root classes in a small inline head script before first paint to avoid a flash. Reinitialize event wiring on `DOMContentLoaded` and the framework client-router event (for Astro, `astro:page-load`) without duplicating listeners.

The floating trigger must have a visible focus state, a minimum 44 by 44 CSS px target, `aria-haspopup="dialog"`, current `aria-expanded`, `aria-controls`, and an explicit accessible name. Place it where it cannot cover the primary CTA, mobile dock, chat, cookie control, or focused content.

Prefer the native `dialog` element for a modal panel. On open, move focus inside; keep `Tab` and `Shift+Tab` inside; close on `Escape`; provide a visible close control; and return focus to the trigger. If the panel is intentionally non-modal, do not set `aria-modal="true"` or trap focus. Toggle buttons must expose state with `aria-pressed` or a correctly implemented switch pattern.

Do not use whole-page CSS filters as the only high-contrast implementation when they make product imagery, maps, or fixed layers unusable. Do not use OpenDyslexic unless it is locally licensed and the user requests it; a legible system sans-serif is the safe default.

## Test the complete experience

Test at minimum:

1. Keyboard-only navigation from browser chrome into the page and back
2. Trigger, dialog focus loop, Escape, close, and focus return
3. Every setting independently, in combination, after reload, and after client navigation
4. Reset and corrupted/missing `localStorage`
5. 200% zoom, 320 CSS px reflow, increased text spacing, and long translated labels
6. Sticky/floating collision and focus-not-obscured behavior on narrow mobile
7. `prefers-reduced-motion` plus the in-page pause setting
8. Form labels, errors, consent, success/failure announcements, and loading state
9. Slider/carousel buttons, swipe alternatives, autoplay pause, and current-slide announcement
10. A representative screen-reader pass when release risk warrants it

Block release for inaccessible primary navigation, conversion controls, forms, dialogs, or content that disappears at zoom/reflow. Record any remaining non-critical defect with severity, route, reproduction steps, and owner.

## Primary references

- [WCAG 2.2](https://www.w3.org/TR/WCAG22/)
- [WAI-ARIA Authoring Practices: Modal Dialog](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/)
- [WCAG 2.2: Pause, Stop, Hide](https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide)
- [WCAG 2.2: Focus Not Obscured](https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum)
