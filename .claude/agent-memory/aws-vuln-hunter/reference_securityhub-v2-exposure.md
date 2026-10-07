---
name: securityhub-v2-exposure
description: Security Hub V2 exposure-management surface — enablement state in the test accounts, DA-gate behavior, and which leads are perma-blocked
metadata:
  type: reference
---

Security Hub V2 exposure-management delta (observed live 2026-10-06, run 20261006-shub).
See full evidence: `/work/findings/securityhub-exposure-hunter-20261006.md`. Prior docs-only pass:
`/work/findings/securityhub-remediationv2-hunter.md`.

**Enablement ground truth (both [[agentcore-env]] accounts):**
- `DescribeSecurityHubV2` -> ResourceNotFoundException(404): **SH V2 hub NOT enabled** in 183174222929 or 289531347876.
- `DescribeHub`(v1) -> InvalidAccessException(401): v1 not enabled either.
- `ListAggregatorsV2` / `GetConnectorV2` -> ConflictException "Security Hub V2 is not enabled".
- `BatchImportFindings` -> AccessDeniedException even under AdministratorAccess (no default product subscription / hub off) — ingest seam cannot be exercised without enabling SH, which the mandate forbids (teardown would require a disable).
- Both accounts are members of org **o-pf2hyvtase**; `organizations:*` is SCP-denied (not "org not in use") -> cannot see/set DA state.
- Net: exposure-generation pipeline is **inert**. L1(inject/attribution), L2(enum filter), L6(guidance), L7(connector), L8(aggregator) are **BLOCKED:precondition** until SH V2 + DA + upstream signals exist. Don't force them.

**Settled verdicts (don't re-hunt unless enablement changes):**
- `ListFreeTrialStatusesV2`: works WITHOUT SH V2. DA-only gate HOLDS — any non-own AccountIds value (sibling/unrelated-real/nonexistent) returns identical `ValidationException "Organization not found: 'o-pf2hyvtase'"`. No target-keyed existence oracle. Error leaks only the CALLER's own org id (not the target's). L3 = REFUTED.
- `DescribeSecurityHubV2` IS authorization-enforced (403 against `arn:...:hubv2` under a scoped role denying it) despite the API Reference omitting AccessDeniedException from its Errors list — that omission is a pure doc bug. L4 = REFUTED.
- New V2 read verbs (GetRemediationsV2/ListExposuresByRemediationV2/ListFreeTrialStatusesV2) resolve to the single per-account `hubv2*` resource with only `aws:ResourceTag/${TagKey}`; `securityhub:TargetAccount` exists only for BatchImportFindings. Cannot IAM-scope reads by account/target/finding — AWS authz-model limitation, Low/informational, NOT a vuln. L5 = CONFIRMED-observation.

**Technique:** scoped-down principal test = create role trusted by `user/research-admin`, inline policy with explicit Deny on the target action + Allow one unrelated action to prove creds valid; assume and compare 403-vs-404-vs-200. Worked cleanly for L4.
