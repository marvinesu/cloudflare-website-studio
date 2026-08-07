# WordPress migration playbook

## Preserve source and rollback

Keep WordPress read-only. Prefer REST API, XML export, or an owner-provided backup. Reject arbitrary PHP, SQL, shell, plugin mutation, secret access, or broad filesystem access when narrower export is possible.

Record source URL, canonical target, repository, migration branch, prior production commit, Cloudflare project/Worker, domains, DNS, access method, approval boundaries, and rollback steps.

## Create migration artifacts

Maintain:

```text
migration/
  raw/                 sanitized immutable exports
  normalized/          deterministic target content
  reports/
    migration-brief.md
    source-manifest.json
    url-map.csv
    claim-matrix.md
    media-inventory.csv
    integration-inventory.md
    dns-inventory.md
    qa-report.md
    cutover-runbook.md
```

Do not commit credentials, backups, private customer data, raw logs, or unapproved source media.

## Discover completely

Inventory pages, posts, drafts, hierarchy, taxonomies, authors, custom post types, menus, media, builder data, templates, global styles, SEO plugin data, redirects, forms, analytics, consent, chat, search, ecommerce, memberships, embeds, scripts, plugins, and scheduled behavior.

Paginate exports, record counts and failures, checksum artifacts, and read them back. Export media metadata first; download only referenced, website-owned files in a resumable phase.

## Define three contracts

### URL contract

Assign every public/indexed URL: preserve, redirect to one specific equivalent, or intentional 404/410 with reason. Never redirect all unknown URLs to home.

### Claim contract

Mark every claim verified, owner-authorized, ambiguous, or unsupported. Remove stale claims from copy, metadata, schema, forms, and feeds. Separate service areas from physical offices.

### Feature contract

Assign every behavior: static HTML/CSS, accessible browser enhancement, narrow Worker endpoint, approved third party, or intentional removal with approval.

## Rebuild static-first

- Normalize content into typed collections/data.
- Sanitize imported HTML; remove scripts, event attributes, `srcdoc`, editor artifacts, tracking fragments, and unresolved WordPress dependencies.
- Preserve meaningful headings, links, lists, tables, captions, embeds, alt text, and author/date semantics.
- Centralize approved business facts and metadata.
- Use local optimized assets with dimensions and stable URLs.
- Keep core content visible without JavaScript.
- Add tests for route counts, mappings, claims, sanitizer behavior, generated metadata, and absent legacy fragments.

## Cut over reversibly

Deploy preview from the migration branch. Verify the full topology, then attach routes/domains or change exact web DNS records. Preserve non-web DNS. Keep WordPress available until production verification and owner review pass.

Record Worker/deployment version, routes/domains, Git SHA, old/new DNS values, rollback command/path, and production evidence.
