# Human content and SEO playbook

## Start with evidence

Collect verified source material before writing:

- real services/products and their boundaries;
- audience questions, objections, vocabulary, and decision criteria;
- process, materials, methods, timelines, and limitations;
- approved locations and service areas;
- credentials, people, proof, case studies, and testimonials with provenance;
- conversion goal and what happens after the action;
- existing query/page performance when available.

Create a claim ledger. Mark each claim verified, owner-authorized, ambiguous, or unsupported. Publish only the first two.

## Humanize through editorial judgment

Do not try to evade AI detectors. Produce text a careful human editor would approve:

- write to one identifiable reader and their current decision;
- use concrete nouns and verbs instead of abstract benefits;
- include useful constraints and tradeoffs, not universal perfection;
- vary sentence and paragraph length naturally;
- prefer real examples and observed details over adjectives;
- let headings carry meaning instead of decorative labels;
- remove repeated conclusions, throat-clearing intros, and empty transitions;
- keep terminology consistent, but do not repeat identical sentence templates;
- read the page aloud and revise unnatural rhythm;
- preserve the business's actual phrasing when it is clear and credible.

Common phrases to challenge: "unlock," "elevate," "revolutionize," "seamless," "cutting-edge," "tailored solutions," "in today's fast-paced world," "we are passionate," "your trusted partner," and "transform your vision." Keep one only when evidence and brand voice make it specific.

Avoid fake humanity: invented anecdotes, fake imperfections, unsupported first-person stories, fictional customer quotes, fabricated statistics, and random slang.

## Build the message hierarchy

For each page define:

1. search/user intent;
2. one-sentence page promise;
3. proof needed to believe it;
4. objections or questions to resolve;
5. primary next action;
6. related pages worth linking.

Make each section change the reader's understanding or decision. Delete filler sections.

## On-page and technical SEO

For every indexable route:

- render meaningful main content in initial HTML;
- use a unique, descriptive title and meta description;
- set a correct canonical in HTML;
- use one logical H1 and ordered headings;
- write descriptive internal link text;
- provide useful image alt text and empty alt for decoration;
- use absolute, production-correct Open Graph and social image URLs;
- add structured data only for visible, verified facts and the most specific applicable type;
- keep status codes correct: `200`, specific `301/308`, real `404/410`, and no soft 404s;
- include indexable canonical URLs in the sitemap and exclude redirects, errors, private, filtered, and preview URLs;
- keep robots directives intentional; do not use robots.txt as an access-control system;
- use `hreflang` only for real localized equivalents with reciprocal mappings.

Do not generate thin city/service combinations. A local page needs distinct, useful evidence: actual service details, logistics, local constraints, proof, FAQs, and authorized geography. A service area is not a physical office.

## WordPress migration SEO

- Export SEO plugin titles, descriptions, canonicals, schema, robots directives, social metadata, and redirects.
- Map every known public URL to preserve, specific redirect, or intentional retirement.
- Preserve valuable slugs unless a change has a measured reason.
- Rewrite builder markup into semantic content without dropping headings, links, captions, or meaningful media.
- Update claims consistently in visible copy, metadata, schema, RSS, forms, and generated HTML.
- Compare old and new route inventories and crawl the built output before cutover.

## Performance and search experience

Target good Core Web Vitals: LCP <= 2.5s, INP <= 200ms, CLS <= 0.1 at the 75th percentile where field data exists. Optimize the actual LCP resource, reserve media dimensions, reduce critical blocking work, limit client JavaScript, preload only critical assets, and keep animation from competing with loading and interaction.

## Verification

- Inspect generated HTML, not only client DOM.
- Crawl every generated route and validate titles, descriptions, canonicals, H1 count, status, internal links, images, schema syntax, sitemap, robots, and redirects.
- Test representative pages with JavaScript disabled when static visibility is expected.
- Validate schema with official tooling and check live canonical behavior.
- Confirm preview deployments return `X-Robots-Tag: noindex` or equivalent.
- After launch, monitor index coverage, crawl errors, Core Web Vitals, query/page performance, and unexpected canonical selection.

## Official references

- https://developers.google.com/search/docs/fundamentals/seo-starter-guide
- https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics
- https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls
- https://developers.google.com/search/docs/crawling-indexing/sitemaps/overview
- https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data
