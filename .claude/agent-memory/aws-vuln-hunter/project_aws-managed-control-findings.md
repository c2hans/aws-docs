---
name: aws-managed-control-findings
description: Confirmed completeness/escape defects in AWS-managed quarantine policies and permissions boundaries (sweeps 1-2)
metadata:
  type: project
---

The high-yield bug class in this engagement = **incompleteness/escape gaps in AWS-managed, customer-uneditable control policies** (quarantine Deny policies + AWS-shipped permissions boundaries). These pass the disclosure gates by construction (defeat an AWS-operated control). Confirmed live:

**AWSCompromisedKeyQuarantineV4** (auto-attached on leaked-key detection) — denies a primary but not its twin:
- `s3:GetObject` denied / `s3:GetObjectVersion` allowed (sweep-1 validated); `s3:ListBucket` denied / `s3:ListObjectVersions` allowed (F2) — together a full enumerate→read S3 exfil in un-denied actions, even on non-versioned buckets (versionId `null`).
- `ecr:GetAuthorizationToken` denied / `ecr:BatchGetImage`+`GetDownloadUrlForLayer` allowed → raw presigned layer pull (F3).
- `cloudtrail:StopLogging`/`DeleteTrail` denied / `UpdateTrail`+`PutEventSelectors` allowed → anti-forensics (F4).
- `iam:ListUsers` denied / `iam:GetAccountAuthorizationDetails` allowed (low, recon).
- `secretsmanager:GetSecretValue` denied / `BatchGetSecretValue` HELD (per-secret service re-auth — paper twin, excluded).

**AWSCODAPermissionsBoundary** (v1, 2026-11-06) — boundary fails to bind (F1, High): allows `iam:AttachRolePolicy`/`PutRolePolicy`/`UpdateAssumeRolePolicy`/`sts:AssumeRole` on `*`, so a bounded role pivots through any unbounded role and sheds its ceiling; also omits the user-boundary verbs (`DeleteUserPermissionsBoundary`/`PutUserPermissionsBoundary`/`AttachUserPolicy`). Contrast: `SageMakerStudioProjectUserRolePermissionsBoundary` explicitly denies `iam:AttachRolePolicy` — AWS knows the pattern, omitted it in CODA.

**AmazonSecurityLakePermissionsBoundary** (v2) — no `aws:ResourceAccount` pin; only a global `aws-security-data-lake*` S3 name-prefix NotResource → cross-account reach (confused-deputy, F6, Medium).

**AmazonBedrockStudioPermissionsBoundary** (v1) — `bedrock:Retrieve` capped (ResourceAccount+tag) but twin `bedrock:RetrieveAndGenerate` is `Resource:*` no-condition (F5, authorization-layer gap; end-to-end may be service-re-authed).

**Not deployed in this partition** (documented but `NoSuchEntity`): `AmazonDataZoneProjectRolePermissionsBoundary`, `AmazonDataZoneProjectDeploymentPermissionsBoundary` — blocks any test needing the real artifact.

**Why:** method that works — attach the AWS boundary to a canary role whose identity is Allow-`*` so the boundary is the only ceiling, then escape using only boundary-permitted actions; and confirm every quarantine twin LIVE (simulate is only a screen; BatchGetSecretValue looked allowed but was closed by per-call re-auth). See [[aws-test-environment]].
