---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/desired-instance-type.html
---

# desired-instance-type
<a name="desired-instance-type"></a>

Checks if your EC2 instances are of a specific instance type. The rule is NON\_COMPLIANT if an EC2 instance is not specified in the parameter list. For a list of supported EC2 instance types, see Instance types in the EC2 User Guide for Linux Instances.

**Identifier:** DESIRED\_INSTANCE\_TYPE

**Resource Types:** AWS::EC2::Instance

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

instanceTypeType: CSV
 Comma-separated list of EC2 instance types (for example, "t2.small, m4.large, i2.xlarge").

## AWS CloudFormation template
<a name="w2aac20c16c17b7d455c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
