---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wafv2-rulegroup-labelsummary.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WAFv2::RuleGroup LabelSummary
<a name="aws-properties-wafv2-rulegroup-labelsummary"></a>

List of labels used by one or more of the rules of a [AWS::WAFv2::RuleGroup](aws-resource-wafv2-rulegroup.md). This summary object is used for the following rule group lists:
+ `AvailableLabels` - Labels that rules add to matching requests. These labels are defined in the `RuleLabels` for a rule.
+ `ConsumedLabels` - Labels that rules match against. These labels are defined in a `LabelMatchStatement` specification, in the [Statement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-notstatement.html#cfn-wafv2-webacl-notstatement-statement) definition of a rule.

## Syntax
<a name="aws-properties-wafv2-rulegroup-labelsummary-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wafv2-rulegroup-labelsummary-syntax.json"></a>

```
{
  "[Name](#cfn-wafv2-rulegroup-labelsummary-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-wafv2-rulegroup-labelsummary-syntax.yaml"></a>

```
  [Name](#cfn-wafv2-rulegroup-labelsummary-name): {{String}}
```

## Properties
<a name="aws-properties-wafv2-rulegroup-labelsummary-properties"></a>

`Name`  <a name="cfn-wafv2-rulegroup-labelsummary-name"></a>
An individual label specification.
*Required*: No
*Type*: String
*Pattern*: `^[0-9A-Za-z_:-]{1,1024}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
