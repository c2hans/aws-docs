---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-applicationautoscaling-scalingpolicy-targettrackingmetric.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ApplicationAutoScaling::ScalingPolicy TargetTrackingMetric
<a name="aws-properties-applicationautoscaling-scalingpolicy-targettrackingmetric"></a>

Represents a specific metric for a target tracking scaling policy for Application Auto Scaling.

Metric is a property of the [AWS::ApplicationAutoScaling::ScalingPolicy TargetTrackingMetricStat](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingmetricstat.html) property type.

## Syntax
<a name="aws-properties-applicationautoscaling-scalingpolicy-targettrackingmetric-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-applicationautoscaling-scalingpolicy-targettrackingmetric-syntax.json"></a>

```
{
  "[Dimensions](#cfn-applicationautoscaling-scalingpolicy-targettrackingmetric-dimensions)" : {{[ TargetTrackingMetricDimension, ... ]}},
  "[MetricName](#cfn-applicationautoscaling-scalingpolicy-targettrackingmetric-metricname)" : {{String}},
  "[Namespace](#cfn-applicationautoscaling-scalingpolicy-targettrackingmetric-namespace)" : {{String}}
}
```

### YAML
<a name="aws-properties-applicationautoscaling-scalingpolicy-targettrackingmetric-syntax.yaml"></a>

```
  [Dimensions](#cfn-applicationautoscaling-scalingpolicy-targettrackingmetric-dimensions): {{
    - TargetTrackingMetricDimension}}
  [MetricName](#cfn-applicationautoscaling-scalingpolicy-targettrackingmetric-metricname): {{String}}
  [Namespace](#cfn-applicationautoscaling-scalingpolicy-targettrackingmetric-namespace): {{String}}
```

## Properties
<a name="aws-properties-applicationautoscaling-scalingpolicy-targettrackingmetric-properties"></a>

`Dimensions`  <a name="cfn-applicationautoscaling-scalingpolicy-targettrackingmetric-dimensions"></a>
The dimensions for the metric. For the list of available dimensions, see the AWS documentation available from the table in [AWS services that publish CloudWatch metrics ](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/aws-services-cloudwatch-metrics.html) in the *Amazon CloudWatch User Guide*.
Conditional: If you published your metric with dimensions, you must specify the same dimensions in your scaling policy.
*Required*: No
*Type*: Array of [TargetTrackingMetricDimension](aws-properties-applicationautoscaling-scalingpolicy-targettrackingmetricdimension.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MetricName`  <a name="cfn-applicationautoscaling-scalingpolicy-targettrackingmetric-metricname"></a>
The name of the metric.
*Required*: No
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Namespace`  <a name="cfn-applicationautoscaling-scalingpolicy-targettrackingmetric-namespace"></a>
The namespace of the metric. For more information, see the table in [AWS services that publish CloudWatch metrics ](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/aws-services-cloudwatch-metrics.html) in the *Amazon CloudWatch User Guide*.
*Required*: No
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
