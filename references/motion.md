# Professional web motion playbook

## Decide whether motion belongs

Pass every candidate through this gate:

1. **Frequency:** remove animation from keyboard actions and extremely frequent workflows; keep repeated UI nearly instant.
2. **Purpose:** name feedback, spatial continuity, state indication, jarring-change prevention, explanation, or rare delight.
3. **Budget:** keep routine UI under roughly 300ms; marketing explanation may be longer when it does not block action.
4. **Function:** never move data or controls the user is trying to read or operate merely for style.

The goal is visible craft, not maximum movement.

## Choose a motion level

- **Restrained:** product UI and repeated workflows. Fast transitions, press feedback, menus, overlays, state continuity.
- **Expressive:** default for marketing, portfolio, editorial, and service sites. Coordinated hero, varied reveals, tactile controls, navigation motion, and one memorable interaction.
- **Cinematic:** campaigns and storytelling pages. One signature sequence with controlled pacing and progressive enhancement.

## Build a shared system

Extend existing tokens. Otherwise start with:

```css
:root {
  --motion-press: 140ms;
  --motion-ui: 220ms;
  --motion-reveal: 520ms;
  --ease-out: cubic-bezier(.23, 1, .32, 1);
  --ease-in-out: cubic-bezier(.77, 0, .175, 1);
  --ease-drawer: cubic-bezier(.32, .72, 0, 1);
  --reveal-distance: 20px;
  --stagger-step: 55ms;
}
```

Use ease-out for entry/exit, ease-in-out for movement/morphing, ease for simple color, and linear for continuous progress. Never use ease-in for ordinary UI entry. Make exits faster than entrances.

## Choose the cheapest capable tool

1. CSS transition for hover, press, focus, and controlled state changes
2. CSS `@starting-style` for simple mount entry
3. CSS animation for predetermined sequences that must remain smooth during load
4. WAAPI for programmatic, hardware-friendly sequencing without a library
5. Motion/GSAP only for gestures, springs, layout/exit orchestration, pinning, or complex story sequences

Do not add a large animation library for a fade. Reuse a library already in the project when appropriate.

## Evaluate references and third-party assets

Treat a reference site as a design problem to analyze, not a component to clone. Extract the narrative structure, pacing, spatial behavior, and interaction purpose; then implement an original composition with project content and tokens.

Before adding external code, icons, Lottie JSON, Rive files, videos, fonts, or motion presets:

1. Open the original source and current license. Do not infer permission from “free,” a demo page, or public source visibility.
2. Record source URL, author/package, pinned version or retrieval date, license, required attribution, local files, modifications, and final credit location in `website-plan/motion-license-ledger.md`.
3. Prefer local, versioned assets over runtime third-party embeds. Do not hotlink an animation library or asset unless the privacy, availability, CSP, and performance tradeoff is approved.
4. Do not redistribute assets whose license permits end-use but prohibits template or library redistribution. A reusable skill may document the workflow without bundling the asset.
5. If provenance or permission is unclear, reproduce only the high-level idea with original CSS, SVG, canvas, or generated media.

For Lottie, inspect JSON size, image/font dependencies, renderer, autoplay/loop behavior, and accessible fallback. Lazy-load below-the-fold players, pause them offscreen and when the document is hidden, and avoid a player dependency for a small icon that CSS or SVG can express. For animated icons, retain a text label or accessible name and keep state meaning available without movement.

## Create distinct motion categories

### Hero choreography

Sequence headline, supporting copy, CTA, and primary media according to hierarchy. Keep the CTA clickable immediately. Use line/word splitting only on high-value display text and preserve accessible text.

### Navigation and menus

Animate active indicators and menu geometry with reversible transitions. Anchor popovers to their trigger using correct transform origin. Keep modals centered. Never hide a sticky header while focus is inside it or the mobile menu is open.

### Section and media reveals

Choose movement that matches composition: clip/mask for image unveiling, small translation for hierarchy, scale for depth, or directional movement tied to the layout. Do not apply the same fade-up to every section.

### CTA and control feedback

Use subtle press scale around `0.97`, visible focus, and honest loading/success/error transitions. Gate hover effects:

```css
@media (hover: hover) and (pointer: fine) {
  .button:hover { transform: translateY(-2px); }
}
```

### Signature interaction

Create at most one dominant interaction per page: scroll-driven product explanation, sticky stack, comparison reveal, controlled horizontal narrative, pointer-responsive material, or spatial transition. Tie it to the message, not fashion.

For scroll stories, keep the primary CTA outside the pinned sequence, make each chapter reachable as semantic HTML, avoid scroll-jacking, and preserve a readable stacked flow when motion is reduced or JavaScript fails. On small screens, verify sticky scenes do not collide with mobile docks, assistants, browser chrome, or the on-screen keyboard.

## Engineering rules

- Prefer transform and opacity. Use clip-path deliberately. Avoid animating width, height, margin, padding, top, or left except justified cases such as measured accordions.
- Never use `transition: all` or enter from `scale(0)`.
- Use transitions for rapidly retriggered UI so interruption retargets smoothly; use springs for gestures that must preserve velocity.
- Enter and exit through coherent paths.
- Keep stagger steps around 30-80ms and never block interaction until a stagger finishes.
- Use direct transforms for performance; avoid high-frequency inherited CSS variable updates across large subtrees.
- Pause continuous effects offscreen and when the document is hidden.
- Clean up observers, listeners, timers, RAF loops, ScrollTriggers, split text, and animation instances across route changes.
- Give scroll and pointer effects an explicit input boundary; do not hijack wheel/touch navigation or make content depend on hover.
- Budget third-party motion separately from core page JavaScript. Record compressed player, asset, and media weight; reject an effect whose cost is disproportionate to its communication value.
- Test animations under CPU load and inspect uncertain motion at 2-5x duration or frame by frame.

## Reduced motion and static resilience

Core content must be visible before JavaScript and if initialization fails. Under `prefers-reduced-motion: reduce`, preserve useful opacity/color feedback but remove large translation, parallax, zoom, rotation, scrubbing, and continuous motion. Never leave content stuck in a hidden pre-animation state.

## Acceptance report

Report the declared motion level, purpose of each category, tokens/tools used, asset/license ledger, bundle cost, rejected candidates, and results for first load, repeated navigation, interruption, exit, mobile, touch, reduced motion, no-JavaScript visibility, background/offscreen pausing, and cleanup.
