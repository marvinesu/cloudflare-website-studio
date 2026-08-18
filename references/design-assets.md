# Design assets and icon systems

## Icon selection

- Use one coherent icon family and weight per site unless the design direction documents a reason to mix.
- Map one icon to one stable concept. Prefer familiar symbols for call, location, home, business, vehicle, key, repair, form, and guidance.
- Keep text labels. Never make an unfamiliar icon the only way to understand a service or action.
- Use icons to improve scanning in service grids, process steps, contact methods, and compact trust markers. Do not place an icon beside every paragraph or heading.
- Let brand colors, container geometry, scale, and motion customize the family without distorting the glyph.

## Flaticon UIcons workflow

1. Check the current official UIcons getting-started page and package registry; do not assume their displayed versions match.
2. Prefer the npm package for reproducible builds. Pin the resolved version and import only the selected style/weight.
3. Verify every chosen class exists in the installed stylesheet.
4. Render decorative icons with `aria-hidden="true"`. Give functional icon-only controls an accessible name.
5. Keep the visible credit `UIcons by Flaticon` linked to `https://www.flaticon.com/uicons` unless a recorded license explicitly removes attribution.
6. Add `website-plan/icon-license-ledger.md` with library, version, asset purpose, license requirement, credit location, and verification date.
7. Check the built asset size and rendered fallback behavior. Do not let a large unused icon bundle silently damage performance.

Do not copy individual Flaticon assets into reusable templates or redistribute them as a standalone icon pack. Keep source and license provenance with the project that uses them.

## Image provenance

For stock, client-supplied, generated, or commissioned imagery, record source and permitted use. Generated images may illustrate a service category but must not be presented as a completed job, employee, storefront, vehicle, certification, or other documentary proof unless that claim is true and approved.

## QA

- Confirm icons render at representative desktop and narrow-mobile widths.
- Confirm the page remains understandable if the icon font fails to load.
- Confirm icon-only controls work with keyboard, focus, and accessible names.
- Confirm reduced motion disables non-essential icon animation.
- Confirm the attribution is visible and the license ledger matches production.
