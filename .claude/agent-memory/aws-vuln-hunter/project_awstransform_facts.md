---
name: awstransform-facts
description: AWS Transform (GenAI migration fleet) live-env + doc-artifact findings — R1 privesc doc defect CONFIRMED, R2 cross-acct KMS REFUTED, data-plane unreachable
metadata:
  type: project
---

AWS Transform run 2026-10-02-1 (plan `/work/aws-docs/AWSTransform-attack-research-plan.md`, accounts 183174222929 self / 289531347876 foreign, both research-admin us-east-1). AWS Transform = GenAI agentic migration/modernization fleet; IAM namespaces `transform` + `transform-custom`.

**Data/control plane unreachable.** `transform.us-east-1.amazonaws.com` is genuine NXDOMAIN (confirmed via socket.gethostbyname; control `sts.us-east-1.amazonaws.com` resolves). No account appears enabled for Transform. So all data-plane leads (prompt-injection P2, cross-tenant job/workspace P4, live legs of PassRole/SSRF P3/P5) were BLOCKED, not fabricated. **Why:** service not provisioned in either test account. **How to apply:** re-probe DNS/SDK availability before re-attempting any Transform data-plane lead; if still NXDOMAIN, stay BLOCKED.

**R1 CONFIRMED (confirmed-vulnerability, routing account-operator).** The doc IAM sample "Allow administrators to accept a connector request" (anchor `id-based-policy-examples-admin-connector`, `/work/aws-docs/docs/transform/latest/userguide/security_iam_id-based-policy-examples.md` lines 82-129) grants `iam:CreateRole`+`iam:AttachRolePolicy`+`iam:PassRole` on `role/service-role/AWSTransform-*` with NO `iam:PolicyARN` condition and no permissions boundary → full within-account privesc. Live-proved: scoped principal minted `service-role/AWSTransform-evil-*` + attached `AdministratorAccess` (both 200); non-`AWSTransform-*` names denied 403 (name prefix is the only gate). Finding at `/work/findings/AWSTransform-R1-admin-connector-sample-privesc.md`. Severity High. **How to apply:** this is a doc-artifact defect in a copy/paste sample, NOT an AWS-managed policy; remediation = add iam:PolicyARN ArnEquals / PermissionsBoundary / PassedToService conditions.

**R2 REFUTED (cross-account KMS).** SQL-mod CMK doc sample (`data-encryption.md` lines 109-204) uses Principal `arn:aws:iam::111122223333:root` + condition `aws:PrincipalArn: arn:aws:iam::*:role/*AWSTransform*`. Live: B's `*AWSTransform*`-named role doing cross-account Decrypt → AccessDeniedException (400). **Why:** KMS cross-account needs the Principal element to name the *external* account; a condition key on PrincipalArn cannot grant cross-account on its own. The `::*:` wildcard in the condition is scary-looking but inert because Principal binds to owner account root. **How to apply:** don't flag `aws:PrincipalArn: ::*:` wildcards in KMS key policies as cross-account unless Principal also delegates to a foreign account.

**Managed policies all tightly scoped (audited via GetPolicyVersion).** 15 Transform AWS-managed policies; all use `aws:ResourceAccount: ${aws:PrincipalAccount}`. SLR AWSServiceRoleForAWSTransform has only 3 read-only sso actions (NOT sso:* — refutes R6). AWSTransformInfrastructureExecutorAccessEC2 gates ssm:SendCommand AWS-RunShellScript via `ssm:resourceTag/atx-remote-infra: true`. NetworkMigration/ServerMigration StsCrossAccountAssumeRole use ExternalId `${aws:PrincipalAccount}:workspace/${aws:PrincipalTag/WorkspaceId}` + `aws:ResourceOrgID` (refutes B2 — not a bare workspace id).

**B1 (connector trust) refuted-as-cross-tenant, informational.** Connector trust uses `Principal:{Service:transform.amazonaws.com}` + `Condition StringEquals aws:SourceAccount` with no `aws:SourceArn`. SourceAccount pins the tenant so it's not cross-tenant exploitable; the missing SourceArn is an informational confused-deputy hardening gap only.

**Residual:** KMS key 06aee270-4157-4d6b-93ae-f991856c3fb0 in PendingDeletion (7-day window, created for R2 test) — expected, no action needed. Everything else torn down + re-enumeration clean.
