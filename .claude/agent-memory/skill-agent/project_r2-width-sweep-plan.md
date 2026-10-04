---
name: r2-width-sweep-plan
description: R2 multi-service width/"look left-right" attack plan across 11 services whose IAM actions changed this sync window; crowns CP DestinationRoleArn + backup-search export + elemental PutFeedPolicy.
metadata:
  type: project
---

Width-sweep attack-research plan at `/work/aws-docs/R2-WidthSweep-attack-research-plan.md` (11 services, ~24 leads, 1-3 per service, NEW boundary-crossing actions only).

**Top leads (ranked):**
1. customer-profiles `AssociateStreamForSegments` — `DestinationRoleArn` (pattern `.*arn:aws:iam:.*:[0-9]+:.*`) + `DestinationArn` Kinesis both accept any account; no SourceArn → cross-account PII delivery + confused deputy. A↔B testable. CRITICAL. (extends [[customerprofiles-segments-plan]])
2. backup-search `StartSearchResultExportJob` — `S3ExportSpecification.DestinationBucket` has NO `ExpectedBucketOwner` (asymmetric vs kinesis CreateChannel which has it) → cross-account exfil of backup metadata. HIGH.
3. elemental-inference `PutFeedPolicy` — feed resource-policy fail-open (prior finding: wildcard). HIGH-CRIT.
4. securityagent `ListActorMessages` — reads actor MFA messages → ATO primitive. CRITICAL but service-plane adjacent (HARD STOP risk).
5. quicksight `Update*Permissions` + OAuthClientApplication + PassTopic + StartExtensionInstallation — cross-namespace/account BI share. HIGH.

**Notable AWS-defect:** observabilityadmin (CloudWatch Omni) `CreateDatasetIntegration` PassRole possible-values include `test.logs.amazonaws.com` (test principal in prod IAM ref).

**Why:** R2 sync-window diff sweep requested as breadth pass. **How to apply:** reuse/extend this plan for these services; kinesis CreateChannel defers to [[streams-s3-delivery-plan]]; invoicing largely needs OOS payer acct 532876697804.
