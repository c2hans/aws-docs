---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/guardduty-runtime-monitoring-enabled.html
---

# guardduty-runtime-monitoring-enabled
<a name="guardduty-runtime-monitoring-enabled"></a>

Checks if Runtime Monitoring is enabled for Amazon GuardDuty detector in your account or organization. The rule is NON\_COMPLIANT if Runtime Monitoring in GuardDuty is not enabled for your account or at least one member account in your organization.

**Identifier:** GUARDDUTY\_RUNTIME\_MONITORING\_ENABLED

**Resource Types:** AWS::GuardDuty::Detector

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except China (Beijing), AWS GovCloud (US-East), AWS GovCloud (US-West), Asia Pacific (Taipei), Canada West (Calgary), China (Ningxia) Region

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7d909c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
