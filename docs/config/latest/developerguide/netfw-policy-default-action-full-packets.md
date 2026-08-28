---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/netfw-policy-default-action-full-packets.html
---

# netfw-policy-default-action-full-packets
<a name="netfw-policy-default-action-full-packets"></a>

Checks if an AWS Network Firewall policy is configured with a user defined default stateless action for full packets. This rule is NON\_COMPLIANT if default stateless action for full packets does not match with user defined default stateless action.

**Identifier:** NETFW\_POLICY\_DEFAULT\_ACTION\_FULL\_PACKETS

**Resource Types:** AWS::NetworkFirewall::FirewallPolicy

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), Asia Pacific (Thailand), Asia Pacific (Malaysia), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Asia Pacific (Taipei), Canada West (Calgary), China (Ningxia) Region

**Parameters:**

statelessDefaultActionsType: CSV
Comma-separated list of values. You can select a max of two. Valid values include 'aws:pass', 'aws:drop', and 'aws:forward\_to\_sfe'.

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1167c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
