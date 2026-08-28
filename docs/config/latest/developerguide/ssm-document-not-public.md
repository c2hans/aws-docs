---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/ssm-document-not-public.html
---

# ssm-document-not-public
<a name="ssm-document-not-public"></a>

Checks if AWS Systems Manager documents owned by the account are public. The rule is NON\_COMPLIANT if Systems Manager documents with the owner 'Self' are public.

**Identifier:** SSM\_DOCUMENT\_NOT\_PUBLIC

**Resource Types:** AWS::SSM::Document

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1551c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
