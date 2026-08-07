# Motion playbook

## Choose a level

- **Restrained:** product UI, utilities, repeated workflows. Use fast state transitions, press feedback, menus, overlays, and essential spatial continuity.
- **Expressive:** default for marketing, portfolio, editorial, and service websites. Add a coordinated entrance, varied section or media reveals, tactile CTAs, navigation motion, and one memorable interaction when content supports it.
- **Cinematic:** launches, campaigns, or storytelling pages where motion is part of the concept. Add one signature sequence with careful pacing and progressive enhancement.

Never equate "more animation" with repeating `opacity + translateY` on every element. Vary motion by semantic role and preserve a common timing language.

## Build the system

Define reusable tokens near the project's design tokens:

```css
:root {
  --motion-fast: 160ms;
  --motion-base: 240ms;
  --motion-slow: 480ms;
  --ease-out: cubic-bezier(.16, 1, .3, 1);
  --ease-in-out: cubic-bezier(.65, 0, .35, 1);
  --reveal-distance: 20px;
  --stagger-step: 55ms;
}
```

Adapt values to the brand. Keep frequent UI at roughly 120-250ms. Longer sequences must communicate hierarchy or story without blocking interaction.

## Select distinct categories

- **Hero:** orchestrate headline, supporting copy, CTA, and key media with hierarchy-aware timing. Keep primary action usable immediately.
- **Section/media reveal:** use clip-path, mask, scale, or directional movement that relates to the layout. Reveal once unless repetition communicates state.
- **Navigation:** animate menu geometry, active indicators, or overlay state with correct transform origin and reversible transitions.
- **CTA feedback:** add hover, press, focus, loading, success, and error feedback. Gate hover effects behind `(hover: hover) and (pointer: fine)`.
- **Cards and media:** use subtle image scale, parallax, spotlight, depth, or content transition only when the component invites exploration.
- **Text:** use line or word reveals sparingly for major editorial moments, never for routine reading or accessibility-critical copy.
- **Signature interaction:** tie scroll progress, pointer position, comparison, stacking, or scene changes directly to the site's message.

## Engineering rules

- Prefer transform and opacity; use clip-path deliberately and test paint cost.
- Prefer CSS transitions for predetermined, interruptible UI. Use WAAPI or a motion library for stateful orchestration, gestures, or dynamic sequencing.
- Use ease-out for entrances/exits, ease-in-out for movement, ease for color, and linear for continuous progress.
- Make exits faster than entrances and preserve velocity for interruptible gestures.
- Avoid `transition: all`, `scale(0)`, default center origin for anchored popovers, unbounded scroll listeners, and animations that hide essential initial HTML.
- Clean up observers, timers, RAF callbacks, and animation instances across client-side navigation.
- Pause or reduce continuous effects offscreen and on hidden tabs.

## Reduced motion

Keep useful opacity and color feedback while removing large translation, parallax, zoom, rotation, and scrubbed movement. Do not simply disable content visibility or leave elements stuck in pre-animation states.

## Motion acceptance report

Report:

1. Declared motion level and rationale
2. Motion categories changed
3. Shared tokens or primitives introduced
4. Desktop, narrow-mobile, touch, interruption, and reduced-motion checks
5. Any intentionally unanimated surfaces and why
