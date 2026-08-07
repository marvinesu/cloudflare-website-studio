# Design quality standard

## Context first

Infer the audience, product lane, desired feeling, constraints, and existing brand language. Choose one coherent direction. Avoid mixing unrelated design systems or chasing novelty section by section.

## Composition

- Establish a clear first action and reading order.
- Use type scale, spacing, contrast, and alignment before adding containers.
- Vary layout intentionally across long marketing pages; do not repeat identical split sections or equal-card rows.
- Let content determine component choice. Do not force every idea into a card, pill, badge, or bento grid.
- Use real, relevant imagery or explicit placeholders. Do not fabricate product proof, logos, reviews, or screenshots.

## Visual system

- Define tokens for color, typography, spacing, radii, shadows, and motion.
- Use a deliberate typeface appropriate to the brand; preserve a strong existing type system.
- Maintain one accent strategy and sufficient text contrast.
- Keep radius and shadow language consistent. Prefer subtle translucent borders or shadows where separation is needed.
- Avoid common AI defaults: purple-blue gradients, excessive rounded cards, icon tiles above every heading, vague micro-labels, and ornamental metadata.

## Interaction and motion

- Animate only for feedback, state change, spatial continuity, hierarchy, or explanation.
- Use ease-out for entrances and exits, ease-in-out for on-screen movement, ease for simple color changes, and linear for continuous progress.
- Favor transform and opacity. Specify transition properties explicitly.
- Keep frequent actions immediate. Never delay keyboard-driven actions for spectacle.
- Give buttons clear hover, focus, active, disabled, loading, success, and error behavior as applicable.
- Respect `prefers-reduced-motion` and clean up listeners, observers, timers, and animation instances.

## Product resilience

- Test long text, localization expansion, missing images, empty data, errors, slow networks, and narrow widths.
- Keep touch targets comfortable, focus visible, and controls labeled.
- Avoid horizontal overflow, layout shift, and content hidden behind sticky or floating UI.
- Aim for LCP below 2.5 seconds, INP below 200 ms, and CLS below 0.1; measure when tooling is available.

## Final critique questions

1. Does the page communicate what it is and what to do next within seconds?
2. Does it feel specific to this business rather than transferable to any startup?
3. Are hierarchy and rhythm strong without decoration?
4. Is every interaction understandable with keyboard, touch, and reduced motion?
5. Are claims, imagery, and social proof real and traceable?
6. Is the most memorable detail also useful?
