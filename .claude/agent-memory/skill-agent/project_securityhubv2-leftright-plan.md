---
name: securityhubv2-leftright-plan
description: QB width plan for Security Hub Exposure/Remediation V2 + left-right sweep (vpc-lattice, lambda-web, identitystore, elbv2, elasticache, ssm) over IAM diff 8fbf00616f..HEAD
metadata:
  type: project
---

Attack-research plan at `/work/aws-docs/SecurityHubV2-plus-leftright-attack-research-plan.md` (10 leads, WIDTH pass).

Primary: Security Hub V2 `GetRemediationsV2` / `ListExposuresByRemediationV2` — pinned only to `hubv2*` + `aws:ResourceTag` (no account/finding condition key; field keys ASFFSyntaxPath/OCSFSyntaxPath exist but NOT wired to these actions). Crowns: cross-account exposure disclosure (exposure findings = another tenant's attack paths), member-vs-delegated-admin boundary on the read path.

Left-right crowns: vpc-lattice `AssociateViaAWSService` (Perms-mgmt confused deputy, no Source* key) + dropped `VpcId` condition key regression; new `lambda-web` client — `CreateWebFunctionEndpoint` (no condition key → unauth public endpoint, authType-NONE analog), `CreateWebFunction`+PassRole lambda.amazonaws.com privesc, web function resource-policy actions; `identitystore:UpdateIdentityStore` new write no keys.

Nulls: AmazonS3/cognito = no IAM-action change (doc churn only); datazone = 84 lines of actions DELETED (cleanup). Lambda-Web & SH V2 API-model bodies absent from mirror → doc-gap, confirm surface first.

**Why:** 2026-10-03 width "look left and right" tasking over newly-added AWS API actions. **How to apply:** reuse/extend this plan for these services, don't restart. Related: [[ec2-cli-reference-plan]].
