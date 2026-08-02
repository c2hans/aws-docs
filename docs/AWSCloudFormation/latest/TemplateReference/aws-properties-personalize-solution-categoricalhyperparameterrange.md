---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-personalize-solution-categoricalhyperparameterrange.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Personalize::Solution CategoricalHyperParameterRange
<a name="aws-properties-personalize-solution-categoricalhyperparameterrange"></a>

Provides the name and range of a categorical hyperparameter.

## Syntax
<a name="aws-properties-personalize-solution-categoricalhyperparameterrange-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-personalize-solution-categoricalhyperparameterrange-syntax.json"></a>

```
{
  "[Name](#cfn-personalize-solution-categoricalhyperparameterrange-name)" : {{String}},
  "[Values](#cfn-personalize-solution-categoricalhyperparameterrange-values)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-personalize-solution-categoricalhyperparameterrange-syntax.yaml"></a>

```
  [Name](#cfn-personalize-solution-categoricalhyperparameterrange-name): {{String}}
  [Values](#cfn-personalize-solution-categoricalhyperparameterrange-values): {{
    - String}}
```

## Properties
<a name="aws-properties-personalize-solution-categoricalhyperparameterrange-properties"></a>

`Name`  <a name="cfn-personalize-solution-categoricalhyperparameterrange-name"></a>
The name of the hyperparameter.
*Required*: No
*Type*: String
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Values`  <a name="cfn-personalize-solution-categoricalhyperparameterrange-values"></a>
A list of the categories for the hyperparameter.
*Required*: No
*Type*: Array of String
*Maximum*: `1000 | 100`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
