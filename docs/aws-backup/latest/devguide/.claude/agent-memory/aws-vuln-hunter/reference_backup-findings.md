---
name: backup-findings
description: Where AWS Backup trust-boundary live results live, and the reusable AWS-managed-policy intra-family KMS asymmetry pattern
metadata:
  type: reference
---

AWS Backup trust-boundary run (2026-10-03-1) results: `/work/findings/aws-backup_live-findings.md`.
Disclosability gate + the original MSK/AgentRegistry asymmetry exemplar: `/work/findings/00_boundary-classification-and-gate.md`.

Reusable pattern (the honest-disclosable shape per the gate): an AWS-managed, customer-uneditable policy over-grants a KMS/S3 action **relative to its own sibling statement or sibling policy in the same family**. The discriminator is `kms:ViaService` / `aws:ResourceAccount` present on one statement but missing on a twin action. Confirmed instances: `AmazonMSKFullAccess` `kms:CreateGrant` (gate doc), and `AWSBackupServiceRolePolicyForItemRestores`/`...ForIndexing` leaving `kms:DescribeKey` unconditioned while `...ForS3Backup`/`...ForS3Restore` guard the same action with `kms:ViaService` (Backup findings).

Backup-specific facts worth not re-deriving: the ItemRestores S3 `PutObject` cross-account crux was **already fixed** by AWS (now carries `aws:ResourceAccount=${aws:PrincipalAccount}`); `AWSRAMPermissionBackupVaultReadOnly` includes `CreateBackupAccessPoint`+`StartRestoreJob` but **no `s3:GetObject`**; `backup:CopyTargets` IS enforceable as a Deny on `StartCopyJob`.
