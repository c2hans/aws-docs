---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/guardduty-s3-protection-enabled.html
---

# guardduty-s3-protection-enabled
<a name="guardduty-s3-protection-enabled"></a>

Checks if S3 Protection is enabled for an Amazon GuardDuty Detector in your account. The rule is NON\_COMPLIANT if the S3 Protection feature in Amazon GuardDuty is not enabled for your account.

**Identifier:** GUARDDUTY\_S3\_PROTECTION\_ENABLED

**Resource Types:** AWS::GuardDuty::Detector

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except China (Beijing), China (Ningxia) Region

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7d911c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
