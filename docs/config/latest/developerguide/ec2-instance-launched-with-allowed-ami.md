---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/ec2-instance-launched-with-allowed-ami.html
---

# ec2-instance-launched-with-allowed-ami
<a name="ec2-instance-launched-with-allowed-ami"></a>

Checks if running or stopped EC2 instances were launched with Amazon Machine Images (AMIs) that meet your Allowed AMIs criteria. The rule is NON\_COMPLIANT if an AMI doesn't meet the Allowed AMIs criteria and the Allowed AMIs settings isn't disabled.

**Identifier:** EC2\_INSTANCE\_LAUNCHED\_WITH\_ALLOWED\_AMI

**Resource Types:** AWS::EC2::Instance

**Trigger type:** Configuration changes and Periodic

**AWS Region:** All supported AWS regions

**Parameters:**

InstanceStateNameList (Optional)Type: CSV
Comma-separate list of Amazon EC2 instance states for the rule to check. Valid values are "running" and "stopped".

## AWS CloudFormation template
<a name="w2aac20c16c17b7d555c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
