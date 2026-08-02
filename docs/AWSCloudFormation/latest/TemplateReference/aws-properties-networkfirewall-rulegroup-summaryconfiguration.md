---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-networkfirewall-rulegroup-summaryconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NetworkFirewall::RuleGroup SummaryConfiguration
<a name="aws-properties-networkfirewall-rulegroup-summaryconfiguration"></a>

A complex type that specifies which Suricata rule metadata fields to use when displaying threat information. Contains:
+ `RuleOptions` - The Suricata rule options fields to extract and display

These settings affect how threat information appears in both the console and API responses. Summaries are available for rule groups you manage and for active threat defense AWS managed rule groups.

## Syntax
<a name="aws-properties-networkfirewall-rulegroup-summaryconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-networkfirewall-rulegroup-summaryconfiguration-syntax.json"></a>

```
{
  "[RuleOptions](#cfn-networkfirewall-rulegroup-summaryconfiguration-ruleoptions)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-networkfirewall-rulegroup-summaryconfiguration-syntax.yaml"></a>

```
  [RuleOptions](#cfn-networkfirewall-rulegroup-summaryconfiguration-ruleoptions): {{
    - String}}
```

## Properties
<a name="aws-properties-networkfirewall-rulegroup-summaryconfiguration-properties"></a>

`RuleOptions`  <a name="cfn-networkfirewall-rulegroup-summaryconfiguration-ruleoptions"></a>
Specifies the selected rule options returned by `DescribeRuleGroupSummary`.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
