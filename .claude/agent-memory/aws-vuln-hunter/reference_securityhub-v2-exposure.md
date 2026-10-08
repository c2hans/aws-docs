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

**GetRemediationsV2 / ListExposuresByRemediationV2 UID-scoping (run 2026-10-07-1, LEAD-H):**
- `EnableSecurityHubV2(Tags={...})` IS member-reachable in both accts (returns HubV2Arn `.../hubv2/<uuid>`), REVERSIBLE via `DisableSecurityHubV2()` (no params) — clean teardown restores pre-run RNFE state. ~10s propagation: for the first few sec post-enable the V2 ops still return 403 "Security Hub V2 is not enabled" (eventual consistency — re-test with delay, don't call it refuted).
- Once enabled, UID-scoping behavior (all under own hub, with crafted UIDs — no real foreign UID obtainable):
  - `TargetUid` nonexistent (random / self-acct-arn-flavored / foreign-B-acct-arn-flavored / whitespace / 1-char) => **uniform 404 RNFE "Remediation target not found"**. NO account-keyed divergence — the account field embedded in a UID string is not read to make an existence/ownership decision. No cross-account enumeration oracle on nonexistent inputs.
  - `MetadataUid` any nonexistent => 200 `{Items:[]}` (query semantics, empty). No leak.
  - Only divergence is INPUT-FORMAT: len==2048 TargetUid => **500 InternalServerException** (minor server robustness bug — oversized-but-valid-length crashes); len>2048 => 400 ValidationException "must be between 1 and 2048 characters". These are format oracles, not UID-existence/ownership oracles.
  - `GetRemediationsV2(TargetUid=x, MetadataUid=y)` => 400 "You can only provide either"; no-arg => 200 own-account `{Items:[]}`.
- Cross-account IDOR (Claim 1) = **DOC-GAP**: exposure-finding pipeline INERT in both sandbox accts (post-enable `GetRemediationsV2()` no-arg => empty in A and B) — no exposure findings generate without upstream analysis signals, so no real foreign UID exists to pivot on. Enumeration-oracle sub-claim = **REFUTED** (only input-format divergence, no account discrimination). Delegated-admin all-members path still DOC-GAP (org SCP-denied).

**Re-confirmed run 2026-10-08-1 (plan _run1008b H1), now covering `ListExposuresByRemediationV2` explicitly:** behavior STABLE/identical. `ListExposuresByRemediationV2(TargetUid=x)` and `GetRemediationsV2(TargetUid=x)` from B => **uniform 404 RNFE "Remediation target not found"** for foreign-A-acct-flavored ARN, self-B-acct-flavored ARN, AND random strings — the account embedded in the opaque UID is NOT consulted; resolution is pure existence-against-the-caller's-own-hub. No AccessDenied-vs-NotFound split, no 200 leak, no latency delta. `MetadataUid=foreign` => 200 `{Items:[]}`. Live behavior = evidence of hub-resource-scoped tenant isolation (not a leak). H1 settled **REFUTED** (enum oracle) / DOC-GAP (true cross-member read unobservable from 2 standalone accts; needs Org+DA+live findings). Full results: `/work/aws-docs/_run1008b/results/security-services.md`. Don't re-run unless an Org with live exposure findings becomes available.
