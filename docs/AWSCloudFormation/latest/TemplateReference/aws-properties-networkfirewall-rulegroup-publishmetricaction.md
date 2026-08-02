---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-networkfirewall-rulegroup-publishmetricaction.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NetworkFirewall::RuleGroup PublishMetricAction
<a name="aws-properties-networkfirewall-rulegroup-publishmetricaction"></a>

Stateless inspection criteria that publishes the specified metrics to Amazon CloudWatch for the matching packet. This setting defines a CloudWatch dimension value to be published.

## Syntax
<a name="aws-properties-networkfirewall-rulegroup-publishmetricaction-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-networkfirewall-rulegroup-publishmetricaction-syntax.json"></a>

```
{
  "[Dimensions](#cfn-networkfirewall-rulegroup-publishmetricaction-dimensions)" : {{[ Dimension, ... ]}}
}
```

### YAML
<a name="aws-properties-networkfirewall-rulegroup-publishmetricaction-syntax.yaml"></a>

```
  [Dimensions](#cfn-networkfirewall-rulegroup-publishmetricaction-dimensions): {{
    - Dimension}}
```

## Properties
<a name="aws-properties-networkfirewall-rulegroup-publishmetricaction-properties"></a>

`Dimensions`  <a name="cfn-networkfirewall-rulegroup-publishmetricaction-dimensions"></a>

*Required*: Yes
*Type*: Array of [Dimension](aws-properties-networkfirewall-rulegroup-dimension.md)
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
