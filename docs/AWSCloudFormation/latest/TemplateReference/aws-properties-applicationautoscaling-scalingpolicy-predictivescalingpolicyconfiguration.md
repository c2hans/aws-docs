---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-applicationautoscaling-scalingpolicy-predictivescalingpolicyconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ApplicationAutoScaling::ScalingPolicy PredictiveScalingPolicyConfiguration
<a name="aws-properties-applicationautoscaling-scalingpolicy-predictivescalingpolicyconfiguration"></a>

 Represents a predictive scaling policy configuration. Predictive scaling is supported on Amazon ECS services.

## Syntax
<a name="aws-properties-applicationautoscaling-scalingpolicy-predictivescalingpolicyconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-applicationautoscaling-scalingpolicy-predictivescalingpolicyconfiguration-syntax.json"></a>

```
{
  "[MaxCapacityBreachBehavior](#cfn-applicationautoscaling-scalingpolicy-predictivescalingpolicyconfiguration-maxcapacitybreachbehavior)" : {{String}},
  "[MaxCapacityBuffer](#cfn-applicationautoscaling-scalingpolicy-predictivescalingpolicyconfiguration-maxcapacitybuffer)" : {{Integer}},
  "[MetricSpecifications](#cfn-applicationautoscaling-scalingpolicy-predictivescalingpolicyconfiguration-metricspecifications)" : {{[ PredictiveScalingMetricSpecification, ... ]}},
  "[Mode](#cfn-applicationautoscaling-scalingpolicy-predictivescalingpolicyconfiguration-mode)" : {{String}},
  "[SchedulingBufferTime](#cfn-applicationautoscaling-scalingpolicy-predictivescalingpolicyconfiguration-schedulingbuffertime)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-applicationautoscaling-scalingpolicy-predictivescalingpolicyconfiguration-syntax.yaml"></a>

```
  [MaxCapacityBreachBehavior](#cfn-applicationautoscaling-scalingpolicy-predictivescalingpolicyconfiguration-maxcapacitybreachbehavior): {{String}}
  [MaxCapacityBuffer](#cfn-applicationautoscaling-scalingpolicy-predictivescalingpolicyconfiguration-maxcapacitybuffer): {{Integer}}
  [MetricSpecifications](#cfn-applicationautoscaling-scalingpolicy-predictivescalingpolicyconfiguration-metricspecifications): {{
    - PredictiveScalingMetricSpecification}}
  [Mode](#cfn-applicationautoscaling-scalingpolicy-predictivescalingpolicyconfiguration-mode): {{String}}
  [SchedulingBufferTime](#cfn-applicationautoscaling-scalingpolicy-predictivescalingpolicyconfiguration-schedulingbuffertime): {{Integer}}
```

## Properties
<a name="aws-properties-applicationautoscaling-scalingpolicy-predictivescalingpolicyconfiguration-properties"></a>

`MaxCapacityBreachBehavior`  <a name="cfn-applicationautoscaling-scalingpolicy-predictivescalingpolicyconfiguration-maxcapacitybreachbehavior"></a>
 Defines the behavior that should be applied if the forecast capacity approaches or exceeds the maximum capacity. Defaults to `HonorMaxCapacity` if not specified.
*Required*: No
*Type*: String
*Allowed values*: `HonorMaxCapacity | IncreaseMaxCapacity`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaxCapacityBuffer`  <a name="cfn-applicationautoscaling-scalingpolicy-predictivescalingpolicyconfiguration-maxcapacitybuffer"></a>
 The size of the capacity buffer to use when the forecast capacity is close to or exceeds the maximum capacity. The value is specified as a percentage relative to the forecast capacity. For example, if the buffer is 10, this means a 10 percent buffer, such that if the forecast capacity is 50, and the maximum capacity is 40, then the effective maximum capacity is 55.
Required if the `MaxCapacityBreachBehavior` property is set to `IncreaseMaxCapacity`, and cannot be used otherwise.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MetricSpecifications`  <a name="cfn-applicationautoscaling-scalingpolicy-predictivescalingpolicyconfiguration-metricspecifications"></a>
 This structure includes the metrics and target utilization to use for predictive scaling.
This is an array, but we currently only support a single metric specification. That is, you can specify a target value and a single metric pair, or a target value and one scaling metric and one load metric.
*Required*: Yes
*Type*: Array of [PredictiveScalingMetricSpecification](aws-properties-applicationautoscaling-scalingpolicy-predictivescalingmetricspecification.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Mode`  <a name="cfn-applicationautoscaling-scalingpolicy-predictivescalingpolicyconfiguration-mode"></a>
 The predictive scaling mode. Defaults to `ForecastOnly` if not specified.
*Required*: No
*Type*: String
*Allowed values*: `ForecastOnly | ForecastAndScale`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SchedulingBufferTime`  <a name="cfn-applicationautoscaling-scalingpolicy-predictivescalingpolicyconfiguration-schedulingbuffertime"></a>
 The amount of time, in seconds, that the start time can be advanced.
The value must be less than the forecast interval duration of 3600 seconds (60 minutes). Defaults to 300 seconds if not specified.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `3600`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
