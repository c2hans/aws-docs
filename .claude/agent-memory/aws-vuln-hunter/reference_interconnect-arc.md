---
name: interconnect-arc
description: interconnect activationKey redaction-asymmetry (CONFIRMED vuln) + arc-region-switch externalId echo (boundary-dependent) test methods and verdicts
metadata:
  type: reference
---

Both `interconnect` and `arc-region-switch` are in botocore 1.43.108 AND live-deployed in the test accounts (us-east-1). Use `/work/.venv/bin/python` (botocore lives in that venv, NOT in `python3 -I`'s path).

## interconnect — activationKey redaction asymmetry — OWNER-SCOPED → misconfiguration/hygiene only (NOT a cross-account vuln)
- `GetConnection` AND `DeleteConnection` return the full `Connection` incl. **cleartext `activationKey`** (base64 bearer token, ~352 bytes, decodes to `{"connect…`). `ListConnections` items OMIT activationKey+ownerAccount (narrower shape). `DescribeConnectionProposal` *consumes* activationKey as INPUT (not an echo).
- CloudTrail masks it: CreateConnection event `responseElements.connection.activationKey = "HIDDEN_DUE_TO_SECURITY_REASONS"` (observed on live event, same resource). The mask-vs-echo asymmetry is real.
- **DECISIVE: GetConnection is OWNER-SCOPED.** A non-owner account (even the designated `remoteAccount` party) calling `GetConnection(<foreign id>)` gets `ResourceNotFoundException` (HTTP 400), NEVER the key — verified both when remoteAccount=the caller and remoteAccount=unrelated. Foreign-real vs bogus id both return ResourceNotFound (no AccessDenied existence oracle; service masks foreign resources as not-found = good posture). So the echo only ever reaches the owner = documented/intended; the finding collapses to intra-account redaction-hygiene, NOT a standalone cross-account disclosure. Don't over-rate the mask-vs-echo asymmetry without an owner-boundary test.
- activationKey is NOT rotatable (UpdateConnection input = identifier/description/bandwidth/clientToken only) → no-vault gate passes.
- Read-vs-accept split is REAL under a scoped role: `interconnect:GetConnection` alone → GetConnection allowed, AcceptConnectionProposal + all mutating = implicitDeny (iam:SimulatePrincipalPolicy). The scoped run is the finding.
- **Canary recipe (cheap/free):** `directconnect:CreateDirectConnectGateway` (free logical obj) → `interconnect:CreateConnection(bandwidth=1Gbps, attachPoint={directConnectGateway:<id>}, environmentId=mce-aws-oci-iad-prod, remoteAccount={identifier:<in-scope acct>})`. remoteAccount.identifier is REQUIRED; use the 2nd in-scope account. Connection lands in `requested` state (never accepted) with activationKey. Teardown: `DeleteConnection` (also echoes the key — bonus). HARD STOP: never call AcceptConnectionProposal (consummates AWS↔partner peering).

## arc-region-switch — externalId/crossAccountRole echo — boundary-dependent
- `GetPlan`/`GetPlanInRegion`/`GetPlanExecution` return `plan.workflows[].steps[].executionBlockConfiguration.<cfg>.{crossAccountRole,externalId}` in cleartext. ~18 config types carry the pair.
- CloudTrail does NOT mask externalId (observed CreatePlan event logs `"externalId":"..."` cleartext). AWS asserts it secret only via field-doc label "secret key" → weakens to confused-deputy hygiene.
- **Replay model (verified vs canary roles in both in-scope accts):** externalId is only the discriminator when the target role trusts the orchestrator ACCOUNT (M1: trust acct-A-root + sts:ExternalId → correct=ASSUMED, wrong/missing=AccessDenied). If the role trusts only `arc-region-switch.amazonaws.com` + ExternalId (M2, AWS-recommended), A cannot assume regardless of externalId. So impact hinges on target trust shape; no ARC userguide in mirror to confirm which AWS recommends.
- **Canary plan recipe:** CreatePlan requires workflows (one per region for activePassive), executionRole (trust `arc-region-switch.amazonaws.com`), name, regions, recoveryApproach. Minimal externalId carrier = a step `executionBlockType=ARCRoutingControl` with `arcRoutingControlConfig.{crossAccountRole,externalId,regionAndRoutingControls={region:[{routingControlArn,state:On}]}}`. ARC accepts a crossAccountRole pointing at ANY account with no consent/existence check (trust-on-write, informational).

Full evidence: `/work/variant-analysis/widen5/HUNT-interconnect-arc.md`.
