# Cloudflare architecture and release checks

## Choose the target

- Use Pages for a straightforward static site and its supported functions workflow.
- Use Workers Static Assets when a Worker must own routing or provide narrow same-origin APIs.
- Prefer static rendering for content-led sites. Do not switch an entire site to SSR for one form.
- Validate configuration against the installed Wrangler version and current Cloudflare documentation before deployment.

## Runtime boundaries

- Send ordinary routes to static assets.
- Route only explicit API or specialized media paths through Worker logic.
- Validate method, origin, content type, size, fields, consent, and abuse controls on form endpoints.
- Return honest error states; do not show success until downstream delivery succeeds or is explicitly queued.
- Store secrets in bindings and preserve mail, verification, and security-related DNS records during cutover.

## SEO and routing

- Set one canonical origin and an explicit apex/`www` policy.
- Preserve clean historical URLs or add specific permanent redirects.
- Generate and verify canonicals, metadata, structured data, sitemap, robots, and a real 404.
- Test unknown URLs and redirect chains in production.

## Release evidence

- Production build succeeds and contains expected routes.
- Preview deployment works through the actual Cloudflare runtime.
- Critical pages, local assets, forms, APIs, and error paths work.
- Desktop and narrow-mobile browser checks pass.
- Canonical hostname behavior and TLS are correct.
- Active Worker/deployment version and rollback target are recorded.
- Production HTML and asset hashes correspond to the intended release.
