---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-networkfirewall-rulegroup-rulevariables.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NetworkFirewall::RuleGroup RuleVariables
<a name="aws-properties-networkfirewall-rulegroup-rulevariables"></a>

Settings that are available for use in the rules in the rule group where this is defined.

## Syntax
<a name="aws-properties-networkfirewall-rulegroup-rulevariables-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-networkfirewall-rulegroup-rulevariables-syntax.json"></a>

```
{
  "[IPSets](#cfn-networkfirewall-rulegroup-rulevariables-ipsets)" : {{{{{Key}}: {{Value}}, ...}}},
  "[PortSets](#cfn-networkfirewall-rulegroup-rulevariables-portsets)" : {{{{{Key}}: {{Value}}, ...}}}
}
```

### YAML
<a name="aws-properties-networkfirewall-rulegroup-rulevariables-syntax.yaml"></a>

```
  [IPSets](#cfn-networkfirewall-rulegroup-rulevariables-ipsets): {{
    {{Key}}: {{Value}}}}
  [PortSets](#cfn-networkfirewall-rulegroup-rulevariables-portsets): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-properties-networkfirewall-rulegroup-rulevariables-properties"></a>

`IPSets`  <a name="cfn-networkfirewall-rulegroup-rulevariables-ipsets"></a>
A list of IP addresses and address ranges, in CIDR notation.
*Required*: No
*Type*: Object of [IPSet](aws-properties-networkfirewall-rulegroup-ipset.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PortSets`  <a name="cfn-networkfirewall-rulegroup-rulevariables-portsets"></a>
A list of port ranges.
*Required*: No
*Type*: Object of [PortSet](aws-properties-networkfirewall-rulegroup-portset.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
