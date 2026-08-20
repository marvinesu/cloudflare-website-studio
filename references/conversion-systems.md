# Lead-generation interaction systems

Use this reference for marketing and local-service sites whose main job is to produce calls, consultations, quote requests, or scheduled-service leads.

## Define the conversion contract

Record before implementation:

- primary action and the situations where it is appropriate;
- secondary action and why it exists;
- what information the business needs before accepting a lead;
- what the visitor must never send;
- destination, owner, response expectation, and failure fallback;
- conversion events and privacy boundaries;
- abuse controls and delivery verification method.

Do not use every channel by default. Emergency or urgent services usually need a call-first path. High-consideration work may need a short qualification form. Chat is useful only when it reduces confusion or routes the visitor to the right human action.

## Ship call-only mode when calls are the workflow

Use call-only mode when the owner requests no chatbot, operators primarily handle urgent requests by phone, or chat would merely repeat a call instruction.

1. Keep contextual `tel:` links in the utility bar, header, hero, and relevant CTA sections.
2. Add one persistent floating call control with the business name or phone number in its accessible label.
3. On narrow screens, stretch it within safe side margins and reserve enough bottom padding that it does not hide the final content.
4. Use a restrained attention cue, stop continuous motion under `prefers-reduced-motion`, and keep the link immediately clickable.
5. Verify it at 390×844 and 320×568: fully visible, no horizontal overflow, no collision with menus, forms, browser chrome, or consent UI.
6. Track placement and page path only; never log the dialed number or visitor data.

Do not leave dormant chatbot markup, scripts, or launchers in call-only output. Do not stack a mobile dock, floating call button, timed popup, and chat launcher. One persistent floating call control is enough.

## Design a call-first assistant

Prefer a deterministic decision assistant when answers must remain safe, fast, and claim-controlled.

1. Open with one sentence explaining what it can do.
2. Offer three to five mutually exclusive situations written in customer language.
3. Return one short answer with preparation details and the next action.
4. Keep the phone link visible in every state.
5. Provide Start over and Escape/close behavior.
6. Announce state changes with `aria-live` without stealing focus unpredictably.
7. Track only category and CTA events, not free text, addresses, or personal details.

Never request lock codes, alarm credentials, passwords, payment data, identity documents, or other sensitive access information in chat. Do not let the assistant invent prices, availability, arrival times, credentials, or service coverage. Escalate ambiguity to a phone call.

If a generative assistant is genuinely required, define retrieval sources, allowed claims, refusal boundaries, transcript retention, human escalation, cost limits, latency/failure behavior, and prompt-injection defenses before implementation.

## Design a qualification assistant for scheduled work

Use a first-party qualification assistant when a visible consultation path helps visitors describe a higher-consideration project.

1. Open only after an explicit user action; never use a timer or automatic focus transfer.
2. Keep the flow to three short steps where practical: need/stage, location/timing/details, then contact/consent.
3. Use a native modal dialog with focus containment, Escape, a visible close control, and focus return, or deliberately use a non-modal panel without trapping focus. Do not mix the two patterns.
4. Submit to the same server-validated endpoint and success/failure contract as the primary form.
5. Require explicit contact consent and warn against sending payment data, identity documents, passwords, access codes, or credentials.
6. Keep a call or email alternative visible in the introduction and failure state.
7. Add multiple entry points when useful, but only one assistant instance and one data model.

Do not render an embedded vendor form and a first-party lead form as competing primary surfaces. If both must exist, document the distinct audience and route for each and verify that only the intended one appears on each page.

## Build short forms that can be trusted

Ask only for fields required to route and respond. For local services, a useful default is name, phone, optional email, service, city/ZIP or service address, timing, short description, and explicit contact consent.

Client-side validation improves usability but never replaces server validation. On the Worker:

- allow only intended methods and same-origin requests;
- enforce content type and byte limits before parsing;
- normalize and bound every field;
- reject invalid phone/email formats and missing consent;
- use honeypot and elapsed-time controls where appropriate, plus a native Cloudflare Rate Limiting binding on every public lead endpoint;
- invoke the rate limiter after field validation and before delivery, use a privacy-preserving stable key, return `429` with `Retry-After`, and do not substitute isolate-memory counters;
- add Turnstile when abuse risk warrants it and both client tokens and server-side Siteverify can be configured and tested;
- redact personal fields from logs;
- return stable, honest error messages with a call fallback;
- redirect or render a real success state only after downstream delivery succeeds or durable queuing is confirmed.

## Deliver through Cloudflare

Prefer Cloudflare Email Service for simple first-party notification email when the account and sender domain are ready.

1. Onboard the sending domain and verify its SPF/DKIM requirements.
2. Verify the destination address.
3. Add a `send_email` binding restricted by `destination_address` or an allowlist.
4. Build the message with Cloudflare's supported structured email API.
5. Use a sender on the onboarded domain and a safe reply-to policy.
6. Test an approved submission end to end and confirm inbox receipt.

Before preview and production, run `python scripts/verify_email_binding.py <project-root> --account-id <cloudflare-account-id>` with the token supplied through `CLOUDFLARE_API_TOKEN`. The script checks fixed and allowed recipients against Cloudflare's verified account-level destination list. Treat failure as a release blocker; do not replace this account-state check with Wrangler dry-run output.

Do not put addresses, API tokens, or SMTP credentials in client code. If Email Service is not ready, fail closed and keep the call fallback visible. Never treat a `200` from the form endpoint as proof of inbox delivery without observing the actual send result.

## Prevent competing overlays

Treat sticky headers, review bars, mobile docks, chat launchers, cookie notices, and promotional prompts as one layer system. In call-only mode, use one floating call control and no competing dock or launcher. When an assistant is justified, show no more than one nonessential floating control above the primary call/text dock, collapse it to an icon-sized launcher, and test the open panel at 390px or narrower.

Do not auto-open chat over first-viewport copy or emergency controls. Do not show a separate timed call popup when the page already has a call-first assistant. Respect safe areas and keyboard appearance.

## Add purposeful motion

Use motion to explain state and reinforce the conversion path:

- hero choreography establishes message order;
- assistant panel geometry shows where it came from;
- assistant answers transition as state changes;
- buttons provide immediate press/hover/focus feedback;
- a progress or section cue can provide spatial continuity on long pages.

Keep the call link immediately usable. Disable large movement and continuous effects for reduced motion. Never leave form or assistant content hidden when JavaScript fails.

## Measure without collecting excess data

Useful events include call click placement, text click placement, assistant open (when present), assistant category choice (when present), form start, validation failure category, form delivery success, and service-area check. Avoid logging field values, exact addresses, phone numbers, emails, or message bodies.

Verify event names and destinations in a non-production environment when possible. Analytics must fail open without blocking calls, forms, navigation, or assistant state.
