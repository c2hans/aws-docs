---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-computeoptimizer-automationrule-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ComputeOptimizer::AutomationRule Tag
<a name="aws-properties-computeoptimizer-automationrule-tag"></a>

A key-value pair used to categorize and organize AWS resources and automation rules.

## Syntax
<a name="aws-properties-computeoptimizer-automationrule-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-computeoptimizer-automationrule-tag-syntax.json"></a>

```
{
  "[Key](#cfn-computeoptimizer-automationrule-tag-key)" : {{String}},
  "[Value](#cfn-computeoptimizer-automationrule-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-computeoptimizer-automationrule-tag-syntax.yaml"></a>

```
  [Key](#cfn-computeoptimizer-automationrule-tag-key): {{String}}
  [Value](#cfn-computeoptimizer-automationrule-tag-value): {{String}}
```

## Properties
<a name="aws-properties-computeoptimizer-automationrule-tag-properties"></a>

`Key`  <a name="cfn-computeoptimizer-automationrule-tag-key"></a>
The tag key, which can be up to 128 characters long.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w\s\.\-\:\/\=\+\@]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-computeoptimizer-automationrule-tag-value"></a>
The tag value, which can be up to 256 characters long.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w\s\.\-\:\/\=\+\@]*$`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
