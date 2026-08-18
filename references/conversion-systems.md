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

## Build short forms that can be trusted

Ask only for fields required to route and respond. For local services, a useful default is name, phone, optional email, service, city/ZIP or service address, timing, short description, and explicit contact consent.

Client-side validation improves usability but never replaces server validation. On the Worker:

- allow only intended methods and same-origin requests;
- enforce content type and byte limits before parsing;
- normalize and bound every field;
- reject invalid phone/email formats and missing consent;
- use a honeypot, elapsed-time check, and platform rate limiting or Turnstile based on abuse risk;
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

Do not put addresses, API tokens, or SMTP credentials in client code. If Email Service is not ready, fail closed and keep the call fallback visible. Never treat a `200` from the form endpoint as proof of inbox delivery without observing the actual send result.

## Prevent competing overlays

Treat sticky headers, review bars, mobile docks, chat launchers, cookie notices, and promotional prompts as one layer system. On narrow screens, show no more than one nonessential floating control above the primary call/text dock. Collapse assistants to an icon-sized launcher and test the open panel at 390px or narrower.

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

Useful events include call click placement, text click placement, assistant open, assistant category choice, form start, validation failure category, form delivery success, and service-area check. Avoid logging field values, exact addresses, phone numbers, emails, or message bodies.

Verify event names and destinations in a non-production environment when possible. Analytics must fail open without blocking calls, forms, navigation, or assistant state.
