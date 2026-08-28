---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudwatch-alarm-metric.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudWatch::Alarm Metric
<a name="aws-properties-cloudwatch-alarm-metric"></a>

The `Metric` property type represents a specific metric. `Metric` is a property of the [MetricStat](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-metricstat.html) property type.

## Syntax
<a name="aws-properties-cloudwatch-alarm-metric-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudwatch-alarm-metric-syntax.json"></a>

```
{
  "[Dimensions](#cfn-cloudwatch-alarm-metric-dimensions)" : {{[ Dimension, ... ]}},
  "[MetricName](#cfn-cloudwatch-alarm-metric-metricname)" : {{String}},
  "[Namespace](#cfn-cloudwatch-alarm-metric-namespace)" : {{String}}
}
```

### YAML
<a name="aws-properties-cloudwatch-alarm-metric-syntax.yaml"></a>

```
  [Dimensions](#cfn-cloudwatch-alarm-metric-dimensions): {{
    - Dimension}}
  [MetricName](#cfn-cloudwatch-alarm-metric-metricname): {{String}}
  [Namespace](#cfn-cloudwatch-alarm-metric-namespace): {{String}}
```

## Properties
<a name="aws-properties-cloudwatch-alarm-metric-properties"></a>

`Dimensions`  <a name="cfn-cloudwatch-alarm-metric-dimensions"></a>
The metric dimensions that you want to be used for the metric that the alarm will watch.
*Required*: No
*Type*: Array of [Dimension](aws-properties-cloudwatch-alarm-dimension.md)
*Maximum*: `30`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MetricName`  <a name="cfn-cloudwatch-alarm-metric-metricname"></a>
The name of the metric that you want the alarm to watch. This is a required field.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Namespace`  <a name="cfn-cloudwatch-alarm-metric-namespace"></a>
The namespace of the metric that the alarm will watch.
*Required*: No
*Type*: String
*Pattern*: `[^:].*`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
