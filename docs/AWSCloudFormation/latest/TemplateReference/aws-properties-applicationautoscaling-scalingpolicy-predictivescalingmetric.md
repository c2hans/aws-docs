---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-applicationautoscaling-scalingpolicy-predictivescalingmetric.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ApplicationAutoScaling::ScalingPolicy PredictiveScalingMetric
<a name="aws-properties-applicationautoscaling-scalingpolicy-predictivescalingmetric"></a>

 Describes the scaling metric.

## Syntax
<a name="aws-properties-applicationautoscaling-scalingpolicy-predictivescalingmetric-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-applicationautoscaling-scalingpolicy-predictivescalingmetric-syntax.json"></a>

```
{
  "[Dimensions](#cfn-applicationautoscaling-scalingpolicy-predictivescalingmetric-dimensions)" : {{[ PredictiveScalingMetricDimension, ... ]}},
  "[MetricName](#cfn-applicationautoscaling-scalingpolicy-predictivescalingmetric-metricname)" : {{String}},
  "[Namespace](#cfn-applicationautoscaling-scalingpolicy-predictivescalingmetric-namespace)" : {{String}}
}
```

### YAML
<a name="aws-properties-applicationautoscaling-scalingpolicy-predictivescalingmetric-syntax.yaml"></a>

```
  [Dimensions](#cfn-applicationautoscaling-scalingpolicy-predictivescalingmetric-dimensions): {{
    - PredictiveScalingMetricDimension}}
  [MetricName](#cfn-applicationautoscaling-scalingpolicy-predictivescalingmetric-metricname): {{String}}
  [Namespace](#cfn-applicationautoscaling-scalingpolicy-predictivescalingmetric-namespace): {{String}}
```

## Properties
<a name="aws-properties-applicationautoscaling-scalingpolicy-predictivescalingmetric-properties"></a>

`Dimensions`  <a name="cfn-applicationautoscaling-scalingpolicy-predictivescalingmetric-dimensions"></a>
 Describes the dimensions of the metric.
*Required*: No
*Type*: Array of [PredictiveScalingMetricDimension](aws-properties-applicationautoscaling-scalingpolicy-predictivescalingmetricdimension.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MetricName`  <a name="cfn-applicationautoscaling-scalingpolicy-predictivescalingmetric-metricname"></a>
 The name of the metric.
*Required*: No
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Namespace`  <a name="cfn-applicationautoscaling-scalingpolicy-predictivescalingmetric-namespace"></a>
 The namespace of the metric.
*Required*: No
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
