---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/ec2-instances-in-vpc.html
---

# ec2-instances-in-vpc
<a name="ec2-instances-in-vpc"></a>

**Important**
For this rule, the rule identifier (INSTANCES\_IN\_VPC) and rule name (ec2-instances-in-vpc) are different.

Checks if your EC2 instances belong to a virtual private cloud (VPC). Optionally, you can specify the VPC ID to associate with your instances.

**Identifier:** INSTANCES\_IN\_VPC

**Resource Types:** AWS::EC2::Instance

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

vpcId (Optional)Type: String
VPC ID that contains these EC2 instances.

## AWS CloudFormation template
<a name="w2aac20c16c17b7d979c21"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
