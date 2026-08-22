# Human content and SEO playbook

For any local-service business, also read [local-service-growth.md](local-service-growth.md) and run its research, location-page, internal-link, and AI-discovery workflow before finalizing pages.

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

## Run an editorial production pipeline

Do not publish first-draft model output. For every important page:

1. **Source pack:** collect approved business facts, first-hand notes, customer questions, project evidence, authoritative sources, and prohibited claims.
2. **Brief:** define audience state, intent, page promise, proof, objections, conversion action, internal links, and update owner.
3. **Outline:** make every section answer a real decision question; remove sections that exist only to hold keywords.
4. **Draft:** write from the source pack without copying competitor language.
5. **Fact pass:** verify every name, number, location, credential, price, timeline, safety statement, and citation against its source.
6. **Voice pass:** read aloud; remove template rhythm, repeated transitions, empty claims, and abrupt keyword insertion.
7. **Usefulness pass:** add first-hand detail, examples, constraints, alternatives, images/video, or practical next steps that commodity summaries lack.
8. **Web pass:** verify headings, links, metadata, schema, alt text, mobile readability, and conversion clarity in the rendered page.
9. **Human approval:** require owner/domain review for claims, regulated/safety content, testimonials, and high-value pages.

Record author/reviewer and meaningful reviewed/updated dates when accurate. Do not add fake bylines or automatically refresh dates without substantive review.

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

## Generative and AI search visibility

Treat AI visibility as an extension of search and entity quality, not a separate content factory.

- Create non-commodity pages with first-hand expertise, original local evidence, clear sourcing, and useful media.
- Keep public content crawlable, indexable, eligible for snippets, and technically understandable.
- Use clear headings, concise definitions, tables, lists, and direct answers only where they help people; do not unnaturally split every paragraph into "AI chunks."
- Cover the topic and decision completely instead of creating pages for every synonym or possible fan-out query.
- Keep entity facts consistent across site copy, schema, Business Profiles, contact pages, and authoritative third-party listings.
- Do not add special "AI schema." Structured data supports ordinary search features and entity clarity but is not required for generative answers.
- Do not rewrite separate copy "for AI." One accurate, useful canonical page should serve people, search, and citation systems.
- Treat `llms.txt` as optional for systems that may consume it; Google currently ignores it for ranking and generative-search visibility.
- Make browser-agent tasks operable with semantic controls, accessible names, predictable forms, clear validation, and no unnecessary interaction traps.

Measure instead of promising: Google Search Console generative-AI reporting when available, Bing Webmaster Tools AI citations/grounding queries, `utm_source=chatgpt.com` referrals, assisted conversions, cited URLs, lead quality, and crawl/index health. Citation count is not the same as ranking, authority, or revenue.

## Verification

- Inspect generated HTML, not only client DOM.
- Crawl every generated route and validate titles, descriptions, canonicals, H1 count, status, internal links, images, schema syntax, sitemap, robots, and redirects.
- Test representative pages with JavaScript disabled when static visibility is expected.
- Validate schema with official tooling and check live canonical behavior.
- Confirm preview deployments return `X-Robots-Tag: noindex` or equivalent.
- After launch, monitor index coverage, crawl errors, Core Web Vitals, query/page performance, and unexpected canonical selection.
- Verify public pages are accessible to the search/AI crawlers the owner intends to allow; test robots.txt and Cloudflare bot/WAF behavior separately from browser access.
- Track AI referrals when identifiable, but do not promise inclusion, ranking, citation, or generated-answer placement.

Pre-release checks do not replace the live-domain review. Once the exact release is on the main domain, run [post-launch-seo.md](post-launch-seo.md) and record the canonical-host evidence before declaring production complete.

## Official references

- https://developers.google.com/search/docs/fundamentals/seo-starter-guide
- https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics
- https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls
- https://developers.google.com/search/docs/crawling-indexing/sitemaps/overview
- https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data
- https://developers.google.com/search/docs/fundamentals/ai-optimization-guide
- https://developers.google.com/search/docs/fundamentals/using-gen-ai-content
- https://help.openai.com/en/articles/12627856-publishers-and-developers-faq
- https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview
