---
name: continuum-odb-enablement
description: Continuum and Oracle Database@AWS (odb) enablement gates observed live — what blocks write-plane testing in the two in-scope accounts
metadata:
  type: project
---

Both `continuum` and `odb` are present in boto3 1.44.3 and reachable, but their write/resource planes are gated in BOTH in-scope accounts (183174222929, 289531347876) as of 2026-11-17 — this blocks the Critical leads and is an AWS-side gate, not tester privilege (both are AdministratorAccess).

**Continuum** — account-level service-side **write-gate**: every mutating op (Create/Update/Delete Integration, StartIntegrationAuthorization, Create/Update/Delete Environment, Update/Delete Collector, CreateCodeScan, PutResourcePolicy) returns `AccessDeniedException: "The request could not be completed."` — a generic deny distinct from the normal IAM "not authorized to perform" message, present for admin, identical in us-east-1 and us-west-2 (account-level, not regional). Read/Get/List ops are NOT gated and reach business logic (e.g. `GetIntegration(fake)` → `ResourceNotFoundException`). So IDOR/confused-deputy/OAuth leads (C1/C2/C3) are could-not-test until the write-plane is enrolled/allowlisted. `GetCollectorDataAccessAuthorization` (caller-supplied `accountId`) and `GetResourcePolicy`/`PutResourcePolicy` on `collectors/*` (plural) ARNs are reachable reads but account-scoped / deny cleanly cross-account (refuted as IDOR). New `gitlab` provider carries a plaintext `accessToken` (watch item).

**odb** — **not onboarded**: every resource op returns `AccessDeniedException: "...account isn't onboarded to the service..."` BEFORE input validation. `GetOciOnboardingStatus`: default=`PENDING_LINK_GENERATION`, awsbb2=`NOT_STARTED` (returns ONLY `{status}` — no ociUrl/token leak, O4b clean). Onboarding needs an OCI/Marketplace tenancy link = hard-stop OCI plane + Exadata cost → out of scope. Blocks all peering/VM-cluster/storage leads live.

**Static-confirmable without enablement:** the `odb` SDK shape `PeeredCidr` pattern ends `\/(?:[1-2][0-9]|3[0-2]|[0-9])` — the `[0-9]` alt accepts `/0` (matches the documented CIDR loosening, W2-ODB6); live server acceptance still untestable. `S3Details` output omits `externalId` (matches doc). See [[aws-test-environment]].
