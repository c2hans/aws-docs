---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/netfw-stateless-rule-group-not-empty.html
---

# netfw-stateless-rule-group-not-empty
<a name="netfw-stateless-rule-group-not-empty"></a>

Checks if a Stateless Network Firewall Rule Group contains rules. The rule is NON\_COMPLIANT if there are no rules in a Stateless Network Firewall Rule Group.

**Identifier:** NETFW\_STATELESS\_RULE\_GROUP\_NOT\_EMPTY

**Resource Types:** AWS::NetworkFirewall::RuleGroup

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), Asia Pacific (Thailand), Asia Pacific (Malaysia), Mexico (Central), Asia Pacific (Taipei), Canada West (Calgary), China (Ningxia) Region

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1171c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
