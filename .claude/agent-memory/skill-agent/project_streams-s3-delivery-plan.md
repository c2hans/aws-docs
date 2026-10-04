---
name: streams-s3-delivery-plan
description: QB attack-research plan for Kinesis Data Streams direct delivery to S3 / S3 Tables (Iceberg), 2026-10-03-leftright sweep
metadata:
  type: project
---

Attack-research plan for the NEW Kinesis Data Streams "direct data delivery to S3 / S3 Tables (Apache Iceberg)" feature (net-new in origin/main..HEAD, pages `docs/streams/latest/dev/data-delivery*`).

File: `/work/aws-docs/_change-analysis/plans/2026-10-03-leftright/streams-s3-delivery-attack-research-plan.md`

**Why:** 2026-10-03-leftright width sweep (brief at `../plans/2026-10-03-leftright/_BRIEF.md`); documentation-only, hunter executes later against in-scope accts A=183174222929 / B=289531347876.

**How to apply:** Reuse, don't restart. Top 3 leads: (1) iam:PassRole enforcement at CreateChannel — IAM ref `list_kinesis.md` ln38 requires it, dev-guide `data-delivery-iam.md` ln15-24 omits it → possible under-privileged caller directs a role to egress stream data cross-account (general-purpose S3 supports cross-account dest); (2) ExpectedBucketOwner is caller-asserted, mismatch only caught at runtime (suspend) → ownership-binding/enumeration-oracle question; (3) SourceArn/SourceAccount trust conditions only "recommended" + shipped KMSForCreateTimeValidation statement uses StringEqualsIfExists ViaService with no EncryptionContext (Lens R/S). Writer is CUSTOMER's own role, not AWS fleet — HARD STOP applies, severity ceiling noted. Note: the sibling `service-managed-pk-*` pages in the same diff are a SEPARATE feature, out of scope for this plan.
