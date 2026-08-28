---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-evaluator-ratingscale.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Evaluator RatingScale
<a name="aws-properties-bedrockagentcore-evaluator-ratingscale"></a>

 The rating scale that defines how the evaluator should score agent performance, either numerical or categorical.

## Syntax
<a name="aws-properties-bedrockagentcore-evaluator-ratingscale-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-evaluator-ratingscale-syntax.json"></a>

```
{
  "[Categorical](#cfn-bedrockagentcore-evaluator-ratingscale-categorical)" : {{[ CategoricalScaleDefinition, ... ]}},
  "[Numerical](#cfn-bedrockagentcore-evaluator-ratingscale-numerical)" : {{[ NumericalScaleDefinition, ... ]}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-evaluator-ratingscale-syntax.yaml"></a>

```
  [Categorical](#cfn-bedrockagentcore-evaluator-ratingscale-categorical): {{
    - CategoricalScaleDefinition}}
  [Numerical](#cfn-bedrockagentcore-evaluator-ratingscale-numerical): {{
    - NumericalScaleDefinition}}
```

## Properties
<a name="aws-properties-bedrockagentcore-evaluator-ratingscale-properties"></a>

`Categorical`  <a name="cfn-bedrockagentcore-evaluator-ratingscale-categorical"></a>
 The categorical rating scale with named categories and definitions for qualitative evaluation.
*Required*: No
*Type*: Array of [CategoricalScaleDefinition](aws-properties-bedrockagentcore-evaluator-categoricalscaledefinition.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Numerical`  <a name="cfn-bedrockagentcore-evaluator-ratingscale-numerical"></a>
 The numerical rating scale with defined score values and descriptions for quantitative evaluation.
*Required*: No
*Type*: Array of [NumericalScaleDefinition](aws-properties-bedrockagentcore-evaluator-numericalscaledefinition.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
