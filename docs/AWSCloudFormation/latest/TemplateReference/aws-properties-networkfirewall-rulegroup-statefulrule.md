---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-networkfirewall-rulegroup-statefulrule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NetworkFirewall::RuleGroup StatefulRule
<a name="aws-properties-networkfirewall-rulegroup-statefulrule"></a>

A single Suricata rules specification, for use in a stateful rule group. Use this option to specify a simple Suricata rule with protocol, source and destination, ports, direction, and rule options. For information about the Suricata `Rules` format, see [Rules Format](https://suricata.readthedocs.io/en/suricata-7.0.8/rules/intro.html).

## Syntax
<a name="aws-properties-networkfirewall-rulegroup-statefulrule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-networkfirewall-rulegroup-statefulrule-syntax.json"></a>

```
{
  "[Action](#cfn-networkfirewall-rulegroup-statefulrule-action)" : {{String}},
  "[Header](#cfn-networkfirewall-rulegroup-statefulrule-header)" : {{Header}},
  "[RuleOptions](#cfn-networkfirewall-rulegroup-statefulrule-ruleoptions)" : {{[ RuleOption, ... ]}}
}
```

### YAML
<a name="aws-properties-networkfirewall-rulegroup-statefulrule-syntax.yaml"></a>

```
  [Action](#cfn-networkfirewall-rulegroup-statefulrule-action): {{String}}
  [Header](#cfn-networkfirewall-rulegroup-statefulrule-header): {{
    Header}}
  [RuleOptions](#cfn-networkfirewall-rulegroup-statefulrule-ruleoptions): {{
    - RuleOption}}
```

## Properties
<a name="aws-properties-networkfirewall-rulegroup-statefulrule-properties"></a>

`Action`  <a name="cfn-networkfirewall-rulegroup-statefulrule-action"></a>
Defines what Network Firewall should do with the packets in a traffic flow when the flow matches the stateful rule criteria. For all actions, Network Firewall performs the specified action and discontinues stateful inspection of the traffic flow.
The actions for a stateful rule are defined as follows:
+ **PASS** - Permits the packets to go to the intended destination.
+ **DROP** - Blocks the packets from going to the intended destination and sends an alert log message, if alert logging is configured in the firewall logging configuration.
+ **ALERT** - Sends an alert log message, if alert logging is configured in the firewall logging configuration.

  You can use this action to test a rule that you intend to use to drop traffic. You can enable the rule with `ALERT` action, verify in the logs that the rule is filtering as you want, then change the action to `DROP`.
+ **REJECT** - Drops traffic that matches the conditions of the stateful rule, and sends a TCP reset packet back to sender of the packet. A TCP reset packet is a packet with no payload and an RST bit contained in the TCP header flags. REJECT is available only for TCP traffic. This option doesn't support FTP or IMAP protocols.
*Required*: Yes
*Type*: String
*Allowed values*: `PASS | DROP | ALERT | REJECT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Header`  <a name="cfn-networkfirewall-rulegroup-statefulrule-header"></a>
The stateful inspection criteria for this rule, used to inspect traffic flows.
*Required*: Yes
*Type*: [Header](aws-properties-networkfirewall-rulegroup-header.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RuleOptions`  <a name="cfn-networkfirewall-rulegroup-statefulrule-ruleoptions"></a>
Additional settings for a stateful rule, provided as keywords and settings.
*Required*: Yes
*Type*: Array of [RuleOption](aws-properties-networkfirewall-rulegroup-ruleoption.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
