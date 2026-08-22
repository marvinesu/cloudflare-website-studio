# Google search appearance and structured data

Use this reference for page metadata, rich-result eligibility, images/video, local business details, page experience, and search-result presentation. The source inventory contains 69 appearance pages reviewed on 2026-08-21; 43 are conditional feature/structured-data guides.

## Titles, headings, and site name

- Give every page a descriptive, concise, page-specific `<title>` in the page's primary language. Avoid vague, obsolete, boilerplate, repeated, exaggerated, and keyword-stuffed titles.
- Make the visible main title unambiguous and prominent, normally as the first logical H1. Keep `<title>`, H1, `og:title`, visible content, and inbound anchor context aligned without forcing exact duplication.
- Brand titles concisely. Do not repeat a long tagline on every route.
- Treat displayed title links as Google's automated choice. A correct `<title>` is an input, not a guaranteed rendering.
- Provide a consistent site name and homepage identity. Use `WebSite` data only when the values are accurate and the current Google documentation supports the implementation.

Sources:

- https://developers.google.com/search/docs/appearance/title-link
- https://developers.google.com/search/docs/appearance/site-names

## Favicon

- Use one stable favicon per hostname and declare it from the homepage with a supported `rel` value such as `icon`.
- Keep the file crawlable by Googlebot-Image and the homepage crawlable by Googlebot.
- Use a brand-representative square image. Google requires at least 8 × 8 pixels and recommends a size larger than 48 × 48 for quality across surfaces.
- Verify the deployed file returns 200 with the intended image content type. A valid implementation makes the site eligible but does not guarantee that Google will display it.

Source: https://developers.google.com/search/docs/appearance/favicon-in-search

## Snippets and descriptions

- Write a unique, accurate, human-readable meta description for every priority page. Summarize the specific page and include genuinely useful details; do not paste keyword lists.
- Google primarily generates snippets from page content and may use the meta description when it better describes the page. Do not promise exact snippet text or length.
- Keep important answer content visible without requiring an expansion control. Preserve useful fragment/deep-link behavior.
- Apply snippet controls only when the owner intends to restrict how content appears.

Source: https://developers.google.com/search/docs/appearance/snippet

## Images and video

- Use high-quality, relevant, original media near the text it supports. Provide descriptive filenames, surrounding context, width/height, responsive sources, and concise alt text for informative images; use empty alt for decoration.
- Keep important media crawlable and avoid embedding private client information in screenshots, filenames, alt text, captions, or metadata.
- For video, give the watch page useful primary content, a stable thumbnail, crawlable player/media, descriptive title/description, and applicable `VideoObject` data. Do not publish placeholder or decorative video schema.
- Add image/video sitemap extensions only when they improve discovery for real media assets.

Sources:

- https://developers.google.com/search/docs/appearance/google-images
- https://developers.google.com/search/docs/appearance/video

## Page experience

Evaluate the whole experience, not a single score: Core Web Vitals, mobile usability, HTTPS, accessibility, intrusive interstitials, visual stability, clear main content, navigation, and security. Field data and lab data are different evidence.

Use these performance targets where representative field data is available: LCP at or below 2.5 s, INP at or below 200 ms, and CLS at or below 0.1 at the 75th percentile. Do not describe Core Web Vitals or a Lighthouse score as the only ranking signal.

Avoid automatic promotional dialogs and interstitials that cover primary content. Keep consent or legally required dialogs proportionate and operable.

Sources:

- https://developers.google.com/search/docs/appearance/page-experience
- https://developers.google.com/search/docs/appearance/core-web-vitals
- https://developers.google.com/search/docs/appearance/avoid-intrusive-interstitials

## Structured-data eligibility contract

Before adding any entity or rich-result markup:

1. Identify a current Google-supported feature that matches the visible page.
2. Open the feature's current official guide from [google-search-central-inventory.csv](google-search-central-inventory.csv).
3. Confirm every required property and applicable policy.
4. Use visible, verified facts. Keep markup representative of the page and do not mark hidden, misleading, irrelevant, or fabricated content.
5. Prefer JSON-LD unless a project constraint requires another supported format.
6. Use stable canonical URLs and consistent `@id` references for the same entity.
7. Validate syntax and eligibility with the Rich Results Test or applicable Google report, then inspect live HTML.
8. Record warnings separately from errors and do not promise a rich result.

Do not create schema merely because Schema.org defines a type. Google support, eligibility, and required fields are feature-specific. Do not publish ratings without genuine visible reviews; do not self-mark unsupported review claims; do not describe a service-area business as a storefront; do not add fake FAQs or resurrect removed/limited rich-result types.

Sources:

- https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data
- https://developers.google.com/search/docs/appearance/structured-data/sd-policies
- https://developers.google.com/search/docs/appearance/structured-data/search-gallery

## Organization and local business

- Use homepage-scoped `Organization` markup for the business identity when supported by verified visible facts. Keep name, URL, logo, contact points, and `sameAs` references consistent.
- Use `LocalBusiness` or a subtype only for a real eligible business presence with the applicable visible name/address and other required facts. A service area alone is not a physical location.
- Do not invent office locations, storefronts, hours, phone numbers, departments, prices, ratings, or service areas to complete markup.
- Keep Google Business Profile details, visible contact copy, schema, social profiles, and authoritative listings consistent.

Sources:

- https://developers.google.com/search/docs/appearance/structured-data/organization
- https://developers.google.com/search/docs/appearance/structured-data/local-business
- https://developers.google.com/search/docs/appearance/establish-business-details

## Conditional feature router

Use the inventory rather than loading every feature guide. Search by the intended feature or entity, then open the official current URL:

```bash
rg -i "article|breadcrumb|event|job posting|local business|organization|product|review|video" references/google-search-central-inventory.csv
```

If no official supported feature matches the page, omit rich-result markup and keep only accurate entity data that has a clear purpose.
