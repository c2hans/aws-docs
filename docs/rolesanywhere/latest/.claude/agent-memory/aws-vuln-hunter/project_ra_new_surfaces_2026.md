---
name: ra-new-surfaces-2026
description: IAM Roles Anywhere surfaces that shipped AFTER the 2026-09-30 live run and remain untested — top priority for the next hunt
metadata:
  type: project
---

The live run behind [[ra-enforced-boundaries]] was 2026-09-30. Two significant surfaces shipped after it and were NOT exercised then. Prioritize these on the next hunt (full plan: `../../userguide/rolesanywhere-attack-research-plan.md`).

**1. Automatic CDP revocation checking — shipped 2026-11-04 (12 days before this plan).**
- **Why:** `crlDpRevocationEnabled` on a trust anchor makes RA, on every CreateSession, read CRL-distribution-point URLs *straight out of the attacker-presented cert* and fetch them server-side from an AWS fleet identity. Zero AWS-side curation ("you don't import or register them"). Only guard documented: host "resolves to public IP addresses and is reachable from the internet"; HTTP/HTTPS; port 80/443; no redirects; ≤2048-char URL; ≤1 MB CRL; ≤5 URLs/cert; refresh ≤30 min; fail-closed if no valid CRL.
- **How to apply:** This is SSRF-shaped from AWS's own fleet — **HARD STOP + disclose** if a fetch reaches link-local/metadata/internal. Attacker needs only an own-CA trust anchor + own EE cert (no victim). Top sub-leads (doc-gaps, need live confirm): (a) DNS-rebinding between the public-IP check and the fetch / 30-min refresh — docs never state re-validation on refresh; (b) blind timing oracle — "first-time download during CreateSession adds latency," cache hit vs miss distinguishable → port/host reachability probe; (c) fleet DoS/amplification — "for each cert in the chain, for each distribution point" × 5 URLs, no documented per-caller throttle for the fetch subsystem. Expect BLIND only: CDP CRLs "are not created as resources… you can't view," so no content reflection.

**2. ML-DSA post-quantum signing — added 2026-02-27.**
- **Why:** New native PQC parser (`AWS4-X509-MLDSA`, ML-DSA-44/65/87) fed an attacker-controlled cert + signature blob. `algorithmMismatch` is a *detection* field present only on SUCCESSFUL auths — not stated to hard-reject.
- **How to apply:** A single successful CreateSession CloudTrail event with `algorithmMismatch:true` refutes "mismatch = hard reject" (verification-bypass lead). Also fuzz malformed/truncated/wrong-level ML-DSA blobs for crash/exhaustion.

**Also worth a pass (not strictly new but under-tested):**
- Signature-coverage gap: only `host` is unconditionally signature-checked; `x-amz-x509`/`-chain`/`x-amz-date`/`content-type` checked "only when they appear" and merely logged in `missingSignedHeaders` (emitted only on success) — possible unsigned-identity-header swap. Confirm reject-vs-log.
- `postEmptyBody` canonicalization divergence: CreateSession params accepted in BOTH query string and JSON body; query path uses a "non-conforming" canonicalization → signed-vs-executed param smuggling (profileArn/roleArn/trustAnchorArn).
- `sourceType=SELF_SIGNED_REPOSITORY` — API-only trust-anchor type, absent from console/prose; characterize what it trusts.
- ImportCrl `crlData` cap = 300,000 bytes (NOT 1 MB; 1 MB is CDP-only).
