---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/guardduty-eks-protection-audit-enabled.html
---

# guardduty-eks-protection-audit-enabled
<a name="guardduty-eks-protection-audit-enabled"></a>

Checks if Audit Log Monitoring for Amazon Elastic Kubernetes Service (Amazon EKS) is enabled for an Amazon GuardDuty detector in your account. The rule is NON\_COMPLIANT if the EKS Audit Log Monitoring feature is not enabled for your account.

**Identifier:** GUARDDUTY\_EKS\_PROTECTION\_AUDIT\_ENABLED

**Resource Types:** AWS::GuardDuty::Detector

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except China (Beijing), China (Ningxia) Region

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7d895c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
