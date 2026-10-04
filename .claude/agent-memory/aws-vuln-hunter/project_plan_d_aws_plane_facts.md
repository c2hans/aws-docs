---
name: plan-d-aws-plane-facts
description: Plan D variant-analysis results porting RDS AWS-plane defect shapes (D1 trust-asymmetry, D2 managed-policy secrets/KMS gap, D3 sub-field authz gap, D8 SigV2 downgrade) to other AWS services — confirmed/refuted with oracles
metadata:
  type: project
---

Plan D (`/work/dbresearch/plans/PLAN-D_...`) run 2026-09-27, accts self 183174222929 / foreign 289531347876. All read-only, zero-billable. Ports RDS DB-context findings to the wider service catalog.

**AWS-D1 (confused-deputy trust-asymmetry, doc/weak-default, account-operator+AWS-sample-fix). CONFIRMED same-corpus contradiction for 4 services** — setup-doc trust sample omits aws:SourceArn/SourceAccount while the SAME service ships a cross-service-confused-deputy-prevention.md recommending them, and an AWS service assumes the role driven by a customer-nameable resource:
- MWAA `mwaa/latest/userguide/mwaa-create-role.md` ~L313-323 (airflow/airflow-env.amazonaws.com execution role).
- DMS `dms/.../CHAP_Target.DynamoDB.md` L65-70, CHAP_Target.Kinesis/Redshift, CHAP_Endpoints.Creating.IAMRDS (dms.amazonaws.com target-endpoint roles). Note DMS confused-deputy support only 3.4.7+.
- SageMaker `sagemaker/latest/dg/sagemaker-roles.md` L411-418 (canonical sagemaker.amazonaws.com execution role); 30+ OMIT files in that corpus.
- EventBridge `eventbridge/.../eb-targets.md` L163-170 (events.amazonaws.com target-invoke role).
- OpenSearch = NUANCED/honest: its confused-deputy page L15 EXPLICITLY states snapshot-role trust does NOT support the keys (documented carve-out, not a contradiction). Other OSIS integration roles omit but support-status unverified.
- Batch = benign: ec2/spotfleet trusts don't need SourceArn (resource you own); batch.amazonaws.com is a service-linked role. Crude 6/7 count was false-positive.
- Method: `grep -rl sts:AssumeRole <svc>/`, filter files with the primary service principal, flag SourceArn/SourceAccount presence. Adjudicate per-file: only bites when a SERVICE assumes driven by a customer-nameable resource.

**AWS-D2 (managed-policy secrets/KMS account-scoping gap, live-provable, aws-security).**
- CONFIRMED: `SecretsManagerReadWrite` v6 Sid=BasePermissions = `secretsmanager:*` on Resource:"*", NO condition. SimulateCustomPolicy: PutResourcePolicy/GetSecretValue/PutSecretValue/DeleteSecret on FOREIGN-acct secret ARN all `allowed`. Broader than AmazonRDSDataFullAccess (all secrets, not just rds-db-credentials/*). Same KMS-gate severity discriminator applies (end-to-end x-acct read needs CMK allowing foreign acct). GetPolicy RequestId 01772f8a..., GetPolicyVersion 69052b1d..., Simulate b3d2b164...
- SECONDARY: `AmazonSageMakerFullAccess` v29 Sid=AllowReadOnlySecretManagerActions = GetSecretValue/DescribeSecret on * gated ONLY by `secretsmanager:ResourceTag/SageMaker=true` (tag, not account) — no aws:ResourceAccount. Weaker (tag-gated). AmazonSageMakerCanvasFullAccess same tag pattern.
- DEFENDED (negatives, good): AWS Backup (ForBackup/Restores/S3) KMS all guarded by kms:ViaService + kms:GrantIsForAWSResource; AppFlowFullAccess secrets gated by aws:CalledVia appflow + owningService tag, KMS by ViaService. These are the CORRECT pattern.

**AWS-D3 (sub-field authz granularity gap, SAR+simulate). CONFIRMED fail-open:**
- `ec2:ModifyInstanceAttribute` — SAR list_ec2.md L3726: NO condition key. Gates UserData(boot RCE)/Groups(SGs)/DisableApiStop/InstanceType. Can't Deny one sub-field.
- `lambda:UpdateFunctionConfiguration` — SAR list_lambda.md L619: only iam:PassRole scoped; action itself no sub-field key. Gates Environment/Layers/VpcConfig/Runtime.
- Oracle: Allow action + Deny{StringEquals made-up-subfield-key} WITHOUT feeding ctx → still `allowed` (Deny can't match absent key). CAUTION: if you feed ContextEntries with the fake key, simulate returns explicitDeny (false result) — do NOT supply ctx for this test.

**AWS-D8 (legacy SigV2/HmacSHA1 downgrade, one crafted signed GET each). CONFIRMED 7/8:**
- ACCEPTED (200, SHA1 & SHA256; tamper→403 SignatureDoesNotMatch = sigs genuinely verified): ec2, sqs, sns, elasticloadbalancing, monitoring(CloudWatch), autoscaling, cloudformation.
- REFUTED: SES (email.us-east-1) → 403 MissingAuthenticationToken for SigV2 (enforces SigV4). Not all legacy endpoints uniform.
- NO `aws:SignatureVersion`/`aws:SignatureMethod` global key exists (corpus grep empty; IAM global-key list has only aws:SecureTransport). Unmitigatable via IAM/SCP = the finding. NOTE: S3 uniquely DOES have per-service `s3:signatureversion`/`s3:signatureAge` keys (list_s3.md) — query-API services do not.
- SigV2 signer recipe: StringToSign=GET\n<host-lc>\n/\n<sorted url-enc query incl AWSAccessKeyId,SignatureVersion=2,SignatureMethod,Timestamp,Action,Version>; HMAC-SHA1/256; append &Signature=urlenc(b64). See /tmp equivalents.

**AWS-D9 (note-only): sweep-action authz decoupling CONFIRMED via SAR** — `account:DisableRegion` only cond key = account:TargetRegion (region name); disables/suspends all services' resources in a region, decoupled from per-service delete Deny. `ec2:DisableImageBlockPublicAccess` no cond key, account-wide Permissions-mgmt re-exposing public AMIs.
**AWS-D5 (mechanism map, no calls): CloudTrail-silent minters** = S3 presign, `eks get-token` (STS GetCallerIdentity presign), CloudFront signed URLs/cookies (keypair, no API), STS presigned URLs — all client-side-signed, no mint-time API → no CloudTrail. Contrast `ecr get-login-password` (calls GetAuthorizationToken → logged).
