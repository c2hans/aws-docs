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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
