---
name: Project Aurora
status: active
coverage: full
slack_channels: [aurora-eng]
slack_people: [riley]
stakeholders: [sam]
email_filters:
  - subject_contains: "[Aurora]"
aliases: [aurora, project aurora, the ranker]
priority: P0
---

<!-- EXAMPLE FILE - fictional. Delete once you have your own projects. -->

## Overview

Aurora replaces the hand-tuned ranking heuristics with a learned model. The goal is a measurable
relevance lift without regressing latency, shipped behind a guardrail so it can be rolled back fast.

## Coverage Policy

Full. This is the current drive, so surface detail-level signals: model eval movement, latency
numbers, and anything stakeholder-authored.

## Current State

Eval v2 is ahead on relevance. Model and client work are ready. The gating risk is staffing on the
serving path, not model quality.

## Open Questions / Blockers

- Serving path is short one engineer; the launch date slips unless that is backfilled.
- Need a decision on the latency budget for the guardrail fallback.

## Plan / Next Steps

- Lock launch-blocking priorities with Riley before their time off.
- Raise the staffing gap with Sam as a resourcing issue, framed clearly as not a quality issue.

## Notes

### 2026-01-14

- Riley posted the eval v2 results; relevance up, latency flat. Thanked them in-channel.

### 2026-01-12

- Confirmed scope cut: deferring the personalization layer to a fast follow.
