---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/cloudformation-termination-protection-check.html
---

# cloudformation-termination-protection-check
<a name="cloudformation-termination-protection-check"></a>

Checks if an AWS CloudFormation stack has termination protection enabled. This rule is NON\_COMPLIANT if termination protection is not enabled on a CloudFormation stack.

**Identifier:** CLOUDFORMATION\_TERMINATION\_PROTECTION\_CHECK

**Resource Types:** AWS::CloudFormation::Stack

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (Jakarta), Middle East (UAE), Asia Pacific (Hyderabad), Asia Pacific (Malaysia), Asia Pacific (Melbourne), Israel (Tel Aviv), Canada West (Calgary), Europe (Spain), Europe (Zurich) Region

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7d299c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
