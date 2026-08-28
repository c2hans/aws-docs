---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-personalize-solution-automlconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Personalize::Solution AutoMLConfig
<a name="aws-properties-personalize-solution-automlconfig"></a>

When the solution performs AutoML (`performAutoML` is true in [CreateSolution](https://docs.aws.amazon.com/personalize/latest/dg/API_CreateSolution.html)), Amazon Personalize determines which recipe, from the specified list, optimizes the given metric. Amazon Personalize then uses that recipe for the solution.

## Syntax
<a name="aws-properties-personalize-solution-automlconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-personalize-solution-automlconfig-syntax.json"></a>

```
{
  "[MetricName](#cfn-personalize-solution-automlconfig-metricname)" : {{String}},
  "[RecipeList](#cfn-personalize-solution-automlconfig-recipelist)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-personalize-solution-automlconfig-syntax.yaml"></a>

```
  [MetricName](#cfn-personalize-solution-automlconfig-metricname): {{String}}
  [RecipeList](#cfn-personalize-solution-automlconfig-recipelist): {{
    - String}}
```

## Properties
<a name="aws-properties-personalize-solution-automlconfig-properties"></a>

`MetricName`  <a name="cfn-personalize-solution-automlconfig-metricname"></a>
The metric to optimize.
*Required*: No
*Type*: String
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RecipeList`  <a name="cfn-personalize-solution-automlconfig-recipelist"></a>
The list of candidate recipes.
*Required*: No
*Type*: Array of String
*Maximum*: `256 | 100`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
