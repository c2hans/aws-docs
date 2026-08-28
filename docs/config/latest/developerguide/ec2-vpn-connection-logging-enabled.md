---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/ec2-vpn-connection-logging-enabled.html
---

# ec2-vpn-connection-logging-enabled
<a name="ec2-vpn-connection-logging-enabled"></a>

Checks if AWS Site-to-Site VPN connections have Amazon CloudWatch logging enabled for both tunnels. The rule is NON\_COMPLIANT if a Site-to-Site VPN connection does not have CloudWatch logging enabled for either or both tunnels.

**Identifier:** EC2\_VPN\_CONNECTION\_LOGGING\_ENABLED

**Resource Types:** AWS::EC2::VPNConnection

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), Asia Pacific (Taipei), Canada West (Calgary), China (Ningxia) Region

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7d641c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
