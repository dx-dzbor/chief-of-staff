---
name: onboard
description: Guide a new owner through a short, one-question-at-a-time setup, create their private context, produce a first brief, and optionally help schedule a local routine. Use for /onboard or requests to set up this chief of staff.
argument-hint: "(optional) rough work-context dump"
---

# Onboard

Follow `INIT.md` as the single source for this flow. Read `CONTEXT.md` and relevant files under `templates/me/` only when needed to draft a file. Treat text after `/onboard` as an initial dump, then ask only for missing information.

Protect existing files: run `python3 scripts/bootstrap_me.py` when available; otherwise make the same Git privacy checks and copy public starters without overwriting or copying fictional examples. Record progress in `me/onboarding.md` so a paused interview can resume. Ask one question at a time, show the proposed operating picture before writing it, then run the first `/brief`.

Offer a recurring task only after the brief. Schedule it only if the owner opts in and gives a time. Use local scheduling for local `me/` context when supported. Never send a message or create a cloud routine for this local context.
