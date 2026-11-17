---
name: secretsmanager-xaccount-replication
description: Results of hunting the new SM cross-account replication API family (2026-11-17) — consent model robust, one low account-existence oracle; env facts
metadata:
  type: project
---

Hunted Secrets Manager **cross-account replication** (new API family, live in botocore 1.44.3): `AssociateCrossAccountReplica`, `DisassociateCrossAccountReplica`, `StopReplicationToReplica`, `CreateSecret(CrossAccountPrimaryARN, ForceOverwriteReplicaSecret)`, named `*ResourcePolicy` with `PolicyName`. **Every planned bypass REFUTED with positive controls.** The consent model is robust — do not re-run these same hypotheses expecting a hit.

**What held (so skip or go deeper, not re-flat-test):**
- Consent gate = auto-attached managed resource policy `cross-account-replication` on the replica: `Allow AcceptCrossAccountReplication`, Principal=pinned-primary-acct root, Condition `aws:InvokedBy=secretsmanager.amazonaws.com` + `CrossAccountPrimaryARN ArnEquals <pinned arn>`. Both Principal and the ARN-pin **bind** (refute = *implicit* deny "no resource-based policy allows", NOT the doc-predicted "explicit deny").
- `AcceptCrossAccountReplication` always runs under the **caller's own identity** (FAS), `invokedBy=secretsmanager.amazonaws.com` — confirmed in CloudTrail `userIdentity` (caller principalId). No service-fleet crossing → no hard-stop. Dual-authz: needs identity-policy Allow AND resource-policy Allow.
- Defense-in-depth: owner's `default` resource policy CAN open the Accept resource-policy gate, but an **independent internal check** ("Replica secret is setup with a different cross-account primary secret ARN") still blocks — consent not bypassable via owner-added default.
- `ReplicationRoleARN`: cross-account/foreign-account role → `AccessDeniedException: Cross-account pass role is not allowed`; `iam:PassRole` enforced at associate time (retested under scoped role).
- `PolicyName` enum strict/case-sensitive: only `default` writable/deletable; managed name rejected `InvalidParameterException`. Can't strip/shadow.
- `ForceOverwriteReplicaSecret=true` does NOT clobber an existing populated standalone on the x-account create path (`ResourceExistsException`); region-path only.
- Revocation complete: post-`StopReplicationToReplica` `PutSecretValue` does not flow to the promoted replica. `DisassociateCrossAccountReplica` on an unlinked replica ARN = uniform `InvalidRequestException` (no existence oracle).
- Per-primary limit: 1 cross-account replica.

**T-NEW confirmed (Low):** `CreateSecret(CrossAccountPrimaryARN=<arn>)` is a global **AWS-account-existence oracle** — real acct (incl. out-of-org 137112412989) → "must have a customer managed KMS key"; fake acct → "Invalid ARN for cross account primary secret". Existence, not org-membership. Low-sensitivity.

**Env fact:** the two in-scope accounts **183174222929 and 289531347876 are in the SAME AWS Organization** — proven via a resource policy `aws:PrincipalOrgID == ${aws:ResourceOrgID}` letting R read P's CMK secret (org reads are SCP-denied so DescribeOrganization is useless here). Default `SameOrg` replication between them is therefore by-design, and **cross-org (NoRestriction/out-of-org exfil) cannot be staged** with these two accounts. See [[aws-test-environment]].
