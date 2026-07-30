---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-evaluator-numericalscaledefinition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Evaluator NumericalScaleDefinition
<a name="aws-properties-bedrockagentcore-evaluator-numericalscaledefinition"></a>

 The definition of a numerical rating scale option that provides a numeric value with its description for evaluation scoring.

## Syntax
<a name="aws-properties-bedrockagentcore-evaluator-numericalscaledefinition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-evaluator-numericalscaledefinition-syntax.json"></a>

```
{
  "[Definition](#cfn-bedrockagentcore-evaluator-numericalscaledefinition-definition)" : {{String}},
  "[Label](#cfn-bedrockagentcore-evaluator-numericalscaledefinition-label)" : {{String}},
  "[Value](#cfn-bedrockagentcore-evaluator-numericalscaledefinition-value)" : {{Number}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-evaluator-numericalscaledefinition-syntax.yaml"></a>

```
  [Definition](#cfn-bedrockagentcore-evaluator-numericalscaledefinition-definition): {{String}}
  [Label](#cfn-bedrockagentcore-evaluator-numericalscaledefinition-label): {{String}}
  [Value](#cfn-bedrockagentcore-evaluator-numericalscaledefinition-value): {{Number}}
```

## Properties
<a name="aws-properties-bedrockagentcore-evaluator-numericalscaledefinition-properties"></a>

`Definition`  <a name="cfn-bedrockagentcore-evaluator-numericalscaledefinition-definition"></a>
 The description that explains what this numerical rating represents and when it should be used.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Label`  <a name="cfn-bedrockagentcore-evaluator-numericalscaledefinition-label"></a>
 The label or name that describes this numerical rating option.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-bedrockagentcore-evaluator-numericalscaledefinition-value"></a>
 The numerical value for this rating scale option.
*Required*: Yes
*Type*: Number
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
