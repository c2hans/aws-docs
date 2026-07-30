---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudwatch-anomalydetector-metric.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudWatch::AnomalyDetector Metric
<a name="aws-properties-cloudwatch-anomalydetector-metric"></a>

Represents a specific metric.

## Syntax
<a name="aws-properties-cloudwatch-anomalydetector-metric-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudwatch-anomalydetector-metric-syntax.json"></a>

```
{
  "[Dimensions](#cfn-cloudwatch-anomalydetector-metric-dimensions)" : {{[ Dimension, ... ]}},
  "[MetricName](#cfn-cloudwatch-anomalydetector-metric-metricname)" : {{String}},
  "[Namespace](#cfn-cloudwatch-anomalydetector-metric-namespace)" : {{String}}
}
```

### YAML
<a name="aws-properties-cloudwatch-anomalydetector-metric-syntax.yaml"></a>

```
  [Dimensions](#cfn-cloudwatch-anomalydetector-metric-dimensions): {{
    - Dimension}}
  [MetricName](#cfn-cloudwatch-anomalydetector-metric-metricname): {{String}}
  [Namespace](#cfn-cloudwatch-anomalydetector-metric-namespace): {{String}}
```

## Properties
<a name="aws-properties-cloudwatch-anomalydetector-metric-properties"></a>

`Dimensions`  <a name="cfn-cloudwatch-anomalydetector-metric-dimensions"></a>
The dimensions for the metric.
*Required*: No
*Type*: Array of [Dimension](aws-properties-cloudwatch-anomalydetector-dimension.md)
*Maximum*: `30`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MetricName`  <a name="cfn-cloudwatch-anomalydetector-metric-metricname"></a>
The name of the metric. This is a required field.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Namespace`  <a name="cfn-cloudwatch-anomalydetector-metric-namespace"></a>
The namespace of the metric.
*Required*: Yes
*Type*: String
*Pattern*: `[^:].*`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
