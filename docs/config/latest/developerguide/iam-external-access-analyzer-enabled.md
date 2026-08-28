---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/iam-external-access-analyzer-enabled.html
---

# iam-external-access-analyzer-enabled
<a name="iam-external-access-analyzer-enabled"></a>

Checks if an IAM Access Analyzer for external access is activated in your account per region. The rule is NON\_COMPLIANT if there are no analyzers for external access in the region or if the 'status' attribute is not set to 'ACTIVE'.

**Identifier:** IAM\_EXTERNAL\_ACCESS\_ANALYZER\_ENABLED

**Resource Types:** AWS::::Account

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except China (Beijing), AWS GovCloud (US-East), AWS GovCloud (US-West), Asia Pacific (Taipei), Canada West (Calgary), China (Ningxia) Region

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7d917c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
