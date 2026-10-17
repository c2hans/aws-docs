---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-evaluator-dimensionratingscale.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Evaluator DimensionRatingScale
<a name="aws-properties-bedrockagentcore-evaluator-dimensionratingscale"></a>

<a name="aws-properties-bedrockagentcore-evaluator-dimensionratingscale-description"></a>The `DimensionRatingScale` property type specifies Property description not available. for an [AWS::BedrockAgentCore::Evaluator](aws-resource-bedrockagentcore-evaluator.md).

## Syntax
<a name="aws-properties-bedrockagentcore-evaluator-dimensionratingscale-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-evaluator-dimensionratingscale-syntax.json"></a>

```
{
  "[Categorical](#cfn-bedrockagentcore-evaluator-dimensionratingscale-categorical)" : {{[ CategoricalScaleDefinition, ... ]}},
  "[Numerical](#cfn-bedrockagentcore-evaluator-dimensionratingscale-numerical)" : {{[ NumericalScaleDefinition, ... ]}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-evaluator-dimensionratingscale-syntax.yaml"></a>

```
  [Categorical](#cfn-bedrockagentcore-evaluator-dimensionratingscale-categorical): {{
    - CategoricalScaleDefinition}}
  [Numerical](#cfn-bedrockagentcore-evaluator-dimensionratingscale-numerical): {{
    - NumericalScaleDefinition}}
```

## Properties
<a name="aws-properties-bedrockagentcore-evaluator-dimensionratingscale-properties"></a>

`Categorical`  <a name="cfn-bedrockagentcore-evaluator-dimensionratingscale-categorical"></a>
Property description not available.
*Required*: No
*Type*: Array of [CategoricalScaleDefinition](aws-properties-bedrockagentcore-evaluator-categoricalscaledefinition.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Numerical`  <a name="cfn-bedrockagentcore-evaluator-dimensionratingscale-numerical"></a>
Property description not available.
*Required*: No
*Type*: Array of [NumericalScaleDefinition](aws-properties-bedrockagentcore-evaluator-numericalscaledefinition.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
