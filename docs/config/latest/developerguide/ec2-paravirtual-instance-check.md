---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/ec2-paravirtual-instance-check.html
---

# ec2-paravirtual-instance-check
<a name="ec2-paravirtual-instance-check"></a>

Checks if the virtualization type of an EC2 instance is paravirtual. This rule is NON\_COMPLIANT for an EC2 instance if 'virtualizationType' is set to 'paravirtual'.

**Identifier:** EC2\_PARAVIRTUAL\_INSTANCE\_CHECK

**Resource Types:** AWS::EC2::Instance

**Trigger type:** Configuration changes

**AWS Region:** Only available in China (Beijing), Europe (Ireland), Europe (Frankfurt), South America (Sao Paulo), US East (N. Virginia), Asia Pacific (Tokyo), US West (Oregon), US West (N. California), Asia Pacific (Singapore), Asia Pacific (Sydney) Region

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7d603c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
