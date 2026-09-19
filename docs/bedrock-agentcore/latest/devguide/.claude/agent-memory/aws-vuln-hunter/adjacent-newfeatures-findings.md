---
name: adjacent-newfeatures-findings
description: Run vh-adjacent-20260917 results — GuardDuty Custom Detection Rules (C-H3/C-H1) REFUTED, Customer Profiles AssociateStreamForSegments confused-deputy (Target B) REFUTED, Connect ACXD (A1/A2/A3/A6) BLOCKED-unreachable
metadata:
  type: project
---

# Run vh-adjacent-20260917 (2026-09-17) — Adjacent New Features

Plan: `/work/aws-docs/Adjacent-NewFeatures-attack-research-plan.md`. Accounts A=`default`=183174222929 ("self"/attacker), B=`awsbb2`=289531347876 ("foreign"/victim). No AWS Org. Both `user/research-admin` (over-privileged). All resources tagged `vh-run-id=vh-adjacent-20260917`. **Teardown verified clean (both accounts back to pre-run state).**

## Verdicts summary
- **C-H3 GuardDuty cross-account association IDOR — REFUTED.**
- **C-H1 GuardDuty UpdateCustomDetectionRuleOrgConfiguration authZ asymmetry — REFUTED (no asymmetry).**
- **Target B Customer Profiles AssociateStreamForSegments confused deputy — REFUTED (server-side guard).**
- **ACXD A1/A2/A3/A6 — BLOCKED (surface unreachable; doc-gap/surface-unconfirmed).**
- No findings. No confirmed vulnerabilities or misconfigurations.

---

## C-H3 — GuardDuty Custom Detection Rule association IDOR (TEST FIRST) — REFUTED
SDK botocore 1.43.95 has all 12 `*CustomDetectionRule*` ops. Requires an enabled detector (created one in each acct). 35 AWS-owned managed rules available (RuleIds identical across accounts, ARN `arn:aws:guardduty::aws:detection-rule/custom/<id>`, no account segment).

Setup: victim B `CreateCustomDetectionRuleAssociation(RuleId='admin-policy-attached-to-role', Mode='DRY_RUN')` →
`AssociationId=21448986-18b4-482a-8fbb-2e2d14203b3d`, `Arn=arn:aws:guardduty:us-east-1:289531347876:detection-rule/custom/admin-policy-attached-to-role/association/21448986-...`, `AccountId=289531347876`.

Attacker A (183174222929), URI carries only `{RuleId}/{AssociationId}` (no accountId):
- `GetCustomDetectionRuleAssociation(RuleId, B_AID)` → **404 ResourceNotFoundException "Association not found"** (reqid ff0aa2c6-2b74-4fff-bb11-014432b01665).
- `UpdateCustomDetectionRuleAssociation(RuleId, B_AID, Mode='LIVE')` → **404 ResourceNotFoundException** (reqid 47b9b52a-...).
- `ListCustomDetectionRuleAssociations(RuleId)` → 200, `RuleAssociations: []` (attacker cannot see B's assoc).

Controls: attacker reads its OWN assoc → 200; victim B reading attacker's AID → 404 (symmetric); victim's original assoc still `DRY_RUN` (untampered). **Associations resolve within the caller's account despite the account-less URI. Account↔account boundary HELD.**

## C-H1 — UpdateCustomDetectionRuleOrgConfiguration authZ asymmetry — REFUTED
Get/List/Create/Update/Delete `*OrgConfiguration` (Get & Delete also require `Mode`) from non-delegated-admin A (no org) ALL return **400 AccessDeniedException "the caller is not authorized to call this API"** (reqids 3ae85f90, 5633cba4, 65b00a6f, 725e210f, 42296cc5). Update behaves identically to Create/Delete — the doc's missing "delegated administrator only" sentence on Update is NOT a live authZ gap. Service-enforced (admin IAM caller still denied because no org/delegated-admin).

## Target B — Customer Profiles AssociateStreamForSegments cross-account confused deputy — REFUTED
Doc gap CONFIRMED: `API_AssociateStreamForSegments.md` request syntax has NO `sts:ExternalId`/`aws:SourceAccount`/`aws:SourceArn`; `DestinationRoleArn` pattern `.*arn:aws:iam:.*:[0-9]+:.*` is unanchored; "allows Customer Profiles service principal to assume the role"; no `iam:PassRole`. BUT the **live service enforces the account boundary server-side**:

Setup: attacker A CP domain `vhadj20260917dom`; victim B Kinesis stream + IAM role trusting `profile.amazonaws.com` (kinesis PutRecord/PutRecords/DescribeStream, NO SourceAccount condition); attacker A self stream + self role (same trust).
- A domain + **B stream** + B role → **400 BadRequestException "The destination ARN ... is not a valid Kinesis Data Stream ARN"** (reqid 64da330d-...). (Same as prior run 2026-09-10-1.)
- A domain + A stream + **B role** → **403 AccessDeniedException "Cross-account pass role is not allowed."** ← decisive confused-deputy guard.
- A domain + A stream + A role (kinesis:* on stream) → **200** (reqid 32857d7b-...). Positive control: same-account path works; account-of-role/stream is the sole discriminator.

`profile.amazonaws.com` is the CP service principal; same-account role is assumed, cross-account role rejected with a dedicated error. **Confused deputy NOT exploitable; account↔account & confused-deputy boundaries HELD** despite the doc omission (cosmetic).

## ACXD (A1/A2/A3/A6) — BLOCKED (unreachable) — re-confirmed 2026-09-17
Same as run 2026-09-13-1 (see [[acxd-sagemaker-hyperpod-facts]]): `connect list-instances` EMPTY in BOTH accounts; all ACXD hosts NXDOMAIN (acxd.us-east-1.amazonaws.com, api.acxd.*, agentic-cx-designer.*, acxd.connect.*, connect-customer.*). `acxd_live_` token issuance is console/Connect-Customer-instance-gated, not obtainable from IAM creds. All four leads = precondition-blocked; the plan's battery remains well-scoped if a live tenant is ever provisioned.

## Look left/right (informational, not findings)
- `GetCustomDetectionRule` returns `Definition.Expression` (the AWS-owned SQL detection logic, e.g. `AdminPolicyAttachedToRole` → `eventSource='iam.amazonaws.com' AND eventName='AttachRolePolicy' AND requestParameters['policyArn'] LIKE '%:iam::aws:policy/AdministratorAccess' ...`). These are AWS-published, account-agnostic managed rules (ARN has no account) that customers must read to choose associations — intended/public content, no boundary crossed. NOT AWS-IP exposure worth flagging.

## Teardown ledger (all deleted + re-enumeration verified empty)
A: GD detector 7302963a70224880adf9dac30a2618e0; kinesis vh-adjacent-20260917-self-stream; role vh-adjacent-20260917-cp-self-role(+inline kw); CP domain vhadj20260917dom (stream disassociated first); transient own GD assoc e67999c2 (deleted mid-test).
B: GD detector 51688bf482b5440eada1125fa7555edf(+assoc 21448986); kinesis vh-adjacent-20260917-victim-stream; role vh-adjacent-20260917-cp-victim-role(+inline kinesis-write).
No config changes to pre-existing resources (both accounts had zero detectors/domains/streams/roles pre-run). No residual.
