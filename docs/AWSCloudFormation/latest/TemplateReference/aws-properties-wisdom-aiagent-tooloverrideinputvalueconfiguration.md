---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wisdom-aiagent-tooloverrideinputvalueconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Wisdom::AIAgent ToolOverrideInputValueConfiguration
<a name="aws-properties-wisdom-aiagent-tooloverrideinputvalueconfiguration"></a>

Configuration for overriding tool input values.

## Syntax
<a name="aws-properties-wisdom-aiagent-tooloverrideinputvalueconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wisdom-aiagent-tooloverrideinputvalueconfiguration-syntax.json"></a>

```
{
  "[Constant](#cfn-wisdom-aiagent-tooloverrideinputvalueconfiguration-constant)" : {{ToolOverrideConstantInputValue}}
}
```

### YAML
<a name="aws-properties-wisdom-aiagent-tooloverrideinputvalueconfiguration-syntax.yaml"></a>

```
  [Constant](#cfn-wisdom-aiagent-tooloverrideinputvalueconfiguration-constant): {{
    ToolOverrideConstantInputValue}}
```

## Properties
<a name="aws-properties-wisdom-aiagent-tooloverrideinputvalueconfiguration-properties"></a>

`Constant`  <a name="cfn-wisdom-aiagent-tooloverrideinputvalueconfiguration-constant"></a>
Constant input value configuration for tool override.
*Required*: Yes
*Type*: [ToolOverrideConstantInputValue](aws-properties-wisdom-aiagent-tooloverrideconstantinputvalue.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
