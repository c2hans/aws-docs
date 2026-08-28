---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/cognito-user-pool-deletion-protection-enabled.html
---

# cognito-user-pool-deletion-protection-enabled
<a name="cognito-user-pool-deletion-protection-enabled"></a>

Checks whether Amazon Cognito user pools has deletion protection enabled. This rule is NON\_COMPLIANT if a user pool has deletion protection disabled.

**Identifier:** COGNITO\_USER\_POOL\_DELETION\_PROTECTION\_ENABLED

**Resource Types:** AWS::Cognito::UserPool

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), Asia Pacific (Malaysia), AWS GovCloud (US-East), AWS GovCloud (US-West), Asia Pacific (Taipei), China (Ningxia) Region

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7d417c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
