---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/ec2-client-vpn-connection-log-enabled.html
---

# ec2-client-vpn-connection-log-enabled
<a name="ec2-client-vpn-connection-log-enabled"></a>

Checks if AWS Client VPN endpoint has client connection logging enabled. The rule is NON\_COMPLIANT if 'Configuration.ConnectionLogOptions.Enabled' is set to false.

**Identifier:** EC2\_CLIENT\_VPN\_CONNECTION\_LOG\_ENABLED

**Resource Types:** AWS::EC2::ClientVpnEndpoint

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), Asia Pacific (Jakarta), Middle East (UAE), Asia Pacific (Hyderabad), Asia Pacific (Malaysia), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary), Europe (Spain), China (Ningxia) Region

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7d537c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
