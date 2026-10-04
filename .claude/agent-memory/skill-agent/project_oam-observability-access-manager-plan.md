---
name: oam-observability-access-manager-plan
description: security-questionbuilder attack-research plan for CloudWatch Observability Access Manager (OAM) cross-account sink/link surface
metadata:
  type: project
---

Attack-research plan for **CloudWatch Observability Access Manager (OAM)** at
`/work/aws-docs/OAM-ObservabilityAccessManager-attack-research-plan.md` (7 leads).

**Service shape:** cross-account telemetry *access-control* plane. Monitoring account creates Sink + resource-based SinkPolicy (`PutSinkPolicy`, the sole attach gate); source account creates Link (`CreateLink`, owns ResourceTypes/Filter/LabelTemplate). Data flows source→monitoring. ARNs: `oam:region:acct:sink/{uuid}` and `link/{uuid}` (random UUID = NOT enumerable). `SinkIdentifier` accepts ARN-or-bare-id (naming-form ambiguity).

**Crown leads (all directly A↔B testable; A=183174222929, B=289531347876):**
1. ListAttachedLinks IDOR — source B enumerates ALL other tenants attached to A's sink (LinkArn=acct ids + Label=account names/emails); sink policy grants sources only CreateLink/UpdateLink, never reads. HIGH.
2. GetSinkPolicy/GetSink/GetLink cross-account read IDOR. Med-High.
3. Revocation incompleteness — after A tightens sink policy to drop B, does B's existing link keep delivering / UpdateLink still 200? (docs: "to remove a link, do so from source account" → no monitoring-side revoke). Med-High.
4. Sink-policy guardrail gap — no Block-Public-Access equiv, `Principal:"*"` accepted, and oam actions have NO aws:SourceAccount/SourceArn condition keys (empty cols in list_oam.md) so no SCP guardrail possible; + ForAllValues:StringEquals oam:ResourceTypes vacuous-truth fail-open. Customer open policy = footgun (down-rate); missing guardrail = AWS defect (Medium).

**Also:** Area 5 naming-form/UpdateLink-vs-CreateLink parity; Area 6 LabelTemplate source-identity spoofing + stored XSS in monitoring console; Area 7 Filter query-DSL parser (low, doc-gap).

**Out of scope:** org mgmt acct 532876697804 → org-keyed (PrincipalOrgID/org-path) sink policies can't be exercised. Nulls: no PassRole (no roleArn input anywhere), no SSRF, no KMS, no upload, no JWT/edge/cache/attestation triggers.

Reuse, don't restart. Related: [[securityhubv2-leftright-plan]] (another cross-account disclosure-via-missing-account-condition-key shape).
