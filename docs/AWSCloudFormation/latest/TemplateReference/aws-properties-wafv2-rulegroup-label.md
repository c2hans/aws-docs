---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wafv2-rulegroup-label.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WAFv2::RuleGroup Label
<a name="aws-properties-wafv2-rulegroup-label"></a>

A single label container. This is used as an element of a label array in `RuleLabels` inside a rule.

## Syntax
<a name="aws-properties-wafv2-rulegroup-label-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wafv2-rulegroup-label-syntax.json"></a>

```
{
  "[Name](#cfn-wafv2-rulegroup-label-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-wafv2-rulegroup-label-syntax.yaml"></a>

```
  [Name](#cfn-wafv2-rulegroup-label-name): {{String}}
```

## Properties
<a name="aws-properties-wafv2-rulegroup-label-properties"></a>

`Name`  <a name="cfn-wafv2-rulegroup-label-name"></a>
The label string.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9A-Za-z_:-]{1,1024}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
