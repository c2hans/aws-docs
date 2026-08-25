---
name: aws-doc-vuln-hunt-method
description: How the user wants AWS documentation-derived vuln hunts done — status labels, testnet-only, HARD STOP on service-plane, no fabricated confirms
metadata:
  type: feedback
---

For AWS vuln-hunt tasks driven from the docs mirror, the user wants each lead reported as:
Claim → exact doc evidence (quoted sentence/field) → confirm/refute analysis → **explicit status**
(DOC-CONFIRMED-SHAPE | DOC-REFUTED | NEEDS-LIVE-TEST, with the minimal live test + expected observation) →
severity-if-true. Rank the final report by *realistic* severity, and give a concrete "what to test live (testnet)" section for the top 2-3.

**Why:** engagement rules — no live target and no source are available, money is the asset, and over-claiming a
live confirm is a hard error. Live testing (when it happens) is testnet / disposable-wallet / few-cents only.

**How to apply:**
- Never present a hypothesis as a confirmed live bug; never fabricate PoC output.
- HARD STOP: if evidence points at an AWS service-plane identity (signing fleet, AWS's own ResourceRetrievalRole
  session), stop developing, preserve, flag. (In the payments hunt this did NOT trigger — ResourceRetrievalRole is customer-owned.)
- Independently sanity-check the requester's own doc claims and correct anything wrong (e.g. "IDs are enumerable" was false).
- Deliver as one markdown report file AND summarize in the final message. Related: [[agentcore-payments-hunt]].
