---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/ec2-transit-gateway-auto-vpc-attach-disabled.html
---

# ec2-transit-gateway-auto-vpc-attach-disabled
<a name="ec2-transit-gateway-auto-vpc-attach-disabled"></a>

Checks if Amazon Elastic Compute Cloud (Amazon EC2) Transit Gateways have 'AutoAcceptSharedAttachments' enabled. The rule is NON\_COMPLIANT for a Transit Gateway if 'AutoAcceptSharedAttachments' is set to 'enable'.

**Identifier:** EC2\_TRANSIT\_GATEWAY\_AUTO\_VPC\_ATTACH\_DISABLED

**Resource Types:** AWS::EC2::TransitGateway

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China (Beijing), Asia Pacific (Osaka), Asia Pacific (Melbourne), AWS GovCloud (US-East), AWS GovCloud (US-West), Israel (Tel Aviv), Asia Pacific (Taipei), China (Ningxia) Region

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7d633c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
