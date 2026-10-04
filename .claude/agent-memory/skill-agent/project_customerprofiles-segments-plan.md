---
name: customerprofiles-segments-plan
description: security-questionbuilder attack-research plan for Connect Customer Profiles NEW segment-subscription/stream APIs (2026-09-01 sync); reuse, don't restart.
metadata:
  type: project
---

A boundary-first attack-research plan exists for **Amazon Connect Customer Profiles — Segment Subscription + Stream association APIs** (new in the 2026-09-01 sync), at `/work/aws-docs/_change-analysis/plans/customerprofiles-segments-attack-research-plan.md`.

**Why:** These 18 NEW `A`-status files (`AssociateStreamForSegments`, `Get/Put/Delete SegmentSubscription`, `ListSegmentSubscriptionEvents`, `GetStreamForSegments`, `BatchPutProfileObject*`, diversity configs) were never examined by the prior [[left-and-right-sweep]] — that sweep only dismissed CP *object-type mapping* as single-tenant. Do not treat CP as fully-swept.

**How to apply:** The TOP finding is a confused-deputy: `AssociateStreamForSegments` hands a caller-typed `DestinationRoleArn` (any-account pattern) to `profile.amazonaws.com` to assume, with NO `iam:PassRole` in the IAM auth table (contrast `CreateIntegrationWorkflow`) and NO confused-deputy-prevention link (contrast `CreateDomain`). Sibling `CreateEventStream` pins destination to "same region and AWS account"; the new twin drops it → cross-account PII egress. If re-tasked on CP, extend this plan rather than restart. Related plans tracked in [[ec2-cli-reference-plan]], [[agent-registry-plan]].
