---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/iam-user-group-membership-check.html
---

# iam-user-group-membership-check
<a name="iam-user-group-membership-check"></a>

Checks whether IAM users are members of at least one IAM group.

**Identifier:** IAM\_USER\_GROUP\_MEMBERSHIP\_CHECK

**Resource Types:** AWS::IAM::User

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), Asia Pacific (Thailand), Middle East (UAE), Asia Pacific (Hyderabad), Asia Pacific (Malaysia), Asia Pacific (Melbourne), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary), Europe (Spain), Europe (Zurich) Region

**Parameters:**

groupNames (Optional)Type: CSV
Comma-separated list of IAM groups in which IAM users must be members.
This rule does not support group names with commas.

## AWS CloudFormation template
<a name="w2aac20c16c17b7d951c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
