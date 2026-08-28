---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-personalize-solution-hpoobjective.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Personalize::Solution HpoObjective
<a name="aws-properties-personalize-solution-hpoobjective"></a>

The metric to optimize during hyperparameter optimization (HPO).

**Note**
Amazon Personalize doesn't support configuring the `hpoObjective` at this time.

## Syntax
<a name="aws-properties-personalize-solution-hpoobjective-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-personalize-solution-hpoobjective-syntax.json"></a>

```
{
  "[MetricName](#cfn-personalize-solution-hpoobjective-metricname)" : {{String}},
  "[MetricRegex](#cfn-personalize-solution-hpoobjective-metricregex)" : {{String}},
  "[Type](#cfn-personalize-solution-hpoobjective-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-personalize-solution-hpoobjective-syntax.yaml"></a>

```
  [MetricName](#cfn-personalize-solution-hpoobjective-metricname): {{String}}
  [MetricRegex](#cfn-personalize-solution-hpoobjective-metricregex): {{String}}
  [Type](#cfn-personalize-solution-hpoobjective-type): {{String}}
```

## Properties
<a name="aws-properties-personalize-solution-hpoobjective-properties"></a>

`MetricName`  <a name="cfn-personalize-solution-hpoobjective-metricname"></a>
The name of the metric.
*Required*: No
*Type*: String
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MetricRegex`  <a name="cfn-personalize-solution-hpoobjective-metricregex"></a>
A regular expression for finding the metric in the training job logs.
*Required*: No
*Type*: String
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Type`  <a name="cfn-personalize-solution-hpoobjective-type"></a>
The type of the metric. Valid values are `Maximize` and `Minimize`.
*Required*: No
*Type*: String
*Allowed values*: `Maximize | Minimize`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
