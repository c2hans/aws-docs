---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-personalize-solution-algorithmhyperparameterranges.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Personalize::Solution AlgorithmHyperParameterRanges
<a name="aws-properties-personalize-solution-algorithmhyperparameterranges"></a>

Specifies the hyperparameters and their ranges. Hyperparameters can be categorical, continuous, or integer-valued.

## Syntax
<a name="aws-properties-personalize-solution-algorithmhyperparameterranges-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-personalize-solution-algorithmhyperparameterranges-syntax.json"></a>

```
{
  "[CategoricalHyperParameterRanges](#cfn-personalize-solution-algorithmhyperparameterranges-categoricalhyperparameterranges)" : {{[ CategoricalHyperParameterRange, ... ]}},
  "[ContinuousHyperParameterRanges](#cfn-personalize-solution-algorithmhyperparameterranges-continuoushyperparameterranges)" : {{[ ContinuousHyperParameterRange, ... ]}},
  "[IntegerHyperParameterRanges](#cfn-personalize-solution-algorithmhyperparameterranges-integerhyperparameterranges)" : {{[ IntegerHyperParameterRange, ... ]}}
}
```

### YAML
<a name="aws-properties-personalize-solution-algorithmhyperparameterranges-syntax.yaml"></a>

```
  [CategoricalHyperParameterRanges](#cfn-personalize-solution-algorithmhyperparameterranges-categoricalhyperparameterranges): {{
    - CategoricalHyperParameterRange}}
  [ContinuousHyperParameterRanges](#cfn-personalize-solution-algorithmhyperparameterranges-continuoushyperparameterranges): {{
    - ContinuousHyperParameterRange}}
  [IntegerHyperParameterRanges](#cfn-personalize-solution-algorithmhyperparameterranges-integerhyperparameterranges): {{
    - IntegerHyperParameterRange}}
```

## Properties
<a name="aws-properties-personalize-solution-algorithmhyperparameterranges-properties"></a>

`CategoricalHyperParameterRanges`  <a name="cfn-personalize-solution-algorithmhyperparameterranges-categoricalhyperparameterranges"></a>
Provides the name and range of a categorical hyperparameter.
*Required*: No
*Type*: Array of [CategoricalHyperParameterRange](aws-properties-personalize-solution-categoricalhyperparameterrange.md)
*Maximum*: `100`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ContinuousHyperParameterRanges`  <a name="cfn-personalize-solution-algorithmhyperparameterranges-continuoushyperparameterranges"></a>
Provides the name and range of a continuous hyperparameter.
*Required*: No
*Type*: Array of [ContinuousHyperParameterRange](aws-properties-personalize-solution-continuoushyperparameterrange.md)
*Maximum*: `100`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`IntegerHyperParameterRanges`  <a name="cfn-personalize-solution-algorithmhyperparameterranges-integerhyperparameterranges"></a>
Provides the name and range of an integer-valued hyperparameter.
*Required*: No
*Type*: Array of [IntegerHyperParameterRange](aws-properties-personalize-solution-integerhyperparameterrange.md)
*Maximum*: `100`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
