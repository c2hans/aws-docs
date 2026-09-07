---
name: route53-media-ssrf-egress-guards
description: Confirmed egress-guard behavior of Route53 health-checker fleet and MediaTailor/MediaLive media fetchers (SSRF pattern hunt bundle C4/C5, 2026-09-07)
metadata:
  type: project
---

Bundle C4/C5 of the SSRF pattern hunt (`/work/ssrf-pattern-hunt-plan.md`) was executed 2026-09-07;
result in `/work/findings/23-route53-media-ssrf-egress-guard-holds.md`. Verdict: dangerous SSRF
REFUTED (no internal/link-local/service-plane reach), Low-severity AWS-egress primitive CONFIRMED.

**Why:** these AWS-managed fleets fetch customer-supplied URLs from AWS-owned egress — same pattern as
the agent-registry finding — but all enforce sound internal-IP guards, so severity is capped at Low.

**How to apply (reusable facts for future SSRF hunts):**
- Route53 health checker: egress `15.177.0.0/18`; UA `Amazon-Route53-Health-Check-Service (ref <HCID>...)`
  — leaks the health-check ID to the target. `IPAddress` field rejects internal literals at create
  (`InvalidInput ... is forbidden`); FQDN path is accepted at create but the fleet re-resolves + blocks
  internal on EVERY probe (`GetHealthCheckStatus` → `Failure: Resolved IP: X. ...restricted or private`).
  No DNS-rebind window. `HTTP_STR_MATCH`+SearchString = 1-bit readable oracle; `TCP` type = port-connect
  oracle. All public-target-only.
- MediaTailor: origin (`VideoContentSourceUrl`) fetched from AWS us-east-1 egress, UA `curl/8.5.0`;
  session endpoints are UNAUTHENTICATED (but PutPlaybackConfiguration needs IAM). Origin HLS/DASH manifest
  content reflected VERBATIM to caller (readable, manifest-shaped). Internal reach blocked fast — use a
  TIMING oracle to discriminate (internal ~0.3-0.5s block vs public connect ~1.3s vs public-blackhole
  timeout ~2.3s; error string is identical 504 for all, so timing is the only discriminator).
- MediaLive `CreateInput` URL_PULL accepts internal URLs at config time (State=DETACHED, no fetch);
  pull-time guard only testable with a RUNNING channel (cost) — deferred/untested.
- Both accounts admin: A 183174222929, B 289531347876. See [[agent-registry-fromurl-readable-ssrf]].
