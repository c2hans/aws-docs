---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-evaluator-evaluationdimension.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Evaluator EvaluationDimension
<a name="aws-properties-bedrockagentcore-evaluator-evaluationdimension"></a>

<a name="aws-properties-bedrockagentcore-evaluator-evaluationdimension-description"></a>The `EvaluationDimension` property type specifies Property description not available. for an [AWS::BedrockAgentCore::Evaluator](aws-resource-bedrockagentcore-evaluator.md).

## Syntax
<a name="aws-properties-bedrockagentcore-evaluator-evaluationdimension-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-evaluator-evaluationdimension-syntax.json"></a>

```
{
  "[DimensionInstruction](#cfn-bedrockagentcore-evaluator-evaluationdimension-dimensioninstruction)" : {{String}},
  "[DimensionName](#cfn-bedrockagentcore-evaluator-evaluationdimension-dimensionname)" : {{String}},
  "[DimensionRatingScale](#cfn-bedrockagentcore-evaluator-evaluationdimension-dimensionratingscale)" : {{DimensionRatingScale}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-evaluator-evaluationdimension-syntax.yaml"></a>

```
  [DimensionInstruction](#cfn-bedrockagentcore-evaluator-evaluationdimension-dimensioninstruction): {{String}}
  [DimensionName](#cfn-bedrockagentcore-evaluator-evaluationdimension-dimensionname): {{String}}
  [DimensionRatingScale](#cfn-bedrockagentcore-evaluator-evaluationdimension-dimensionratingscale): {{
    DimensionRatingScale}}
```

## Properties
<a name="aws-properties-bedrockagentcore-evaluator-evaluationdimension-properties"></a>

`DimensionInstruction`  <a name="cfn-bedrockagentcore-evaluator-evaluationdimension-dimensioninstruction"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `4000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DimensionName`  <a name="cfn-bedrockagentcore-evaluator-evaluationdimension-dimensionname"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z][a-zA-Z0-9_]{0,47}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DimensionRatingScale`  <a name="cfn-bedrockagentcore-evaluator-evaluationdimension-dimensionratingscale"></a>
Property description not available.
*Required*: Yes
*Type*: [DimensionRatingScale](aws-properties-bedrockagentcore-evaluator-dimensionratingscale.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
