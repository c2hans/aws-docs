---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-applicationautoscaling-scalingpolicy-stepadjustment.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ApplicationAutoScaling::ScalingPolicy StepAdjustment
<a name="aws-properties-applicationautoscaling-scalingpolicy-stepadjustment"></a>

`StepAdjustment` specifies a step adjustment for the `StepAdjustments` property of the [AWS::ApplicationAutoScaling::ScalingPolicy StepScalingPolicyConfiguration](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration.html) property type.

For the following examples, suppose that you have an alarm with a breach threshold of 50:
+ To trigger a step adjustment when the metric is greater than or equal to 50 and less than 60, specify a lower bound of 0 and an upper bound of 10.
+ To trigger a step adjustment when the metric is greater than 40 and less than or equal to 50, specify a lower bound of -10 and an upper bound of 0.

For more information, see [Step adjustments](https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-step-scaling-policies.html#as-scaling-steps) in the *Application Auto Scaling User Guide*.

You can find a sample template snippet in the [Examples](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html#aws-resource-applicationautoscaling-scalingpolicy--examples) section of the `AWS::ApplicationAutoScaling::ScalingPolicy` documentation.

## Syntax
<a name="aws-properties-applicationautoscaling-scalingpolicy-stepadjustment-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-applicationautoscaling-scalingpolicy-stepadjustment-syntax.json"></a>

```
{
  "[MetricIntervalLowerBound](#cfn-applicationautoscaling-scalingpolicy-stepadjustment-metricintervallowerbound)" : {{Number}},
  "[MetricIntervalUpperBound](#cfn-applicationautoscaling-scalingpolicy-stepadjustment-metricintervalupperbound)" : {{Number}},
  "[ScalingAdjustment](#cfn-applicationautoscaling-scalingpolicy-stepadjustment-scalingadjustment)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-applicationautoscaling-scalingpolicy-stepadjustment-syntax.yaml"></a>

```
  [MetricIntervalLowerBound](#cfn-applicationautoscaling-scalingpolicy-stepadjustment-metricintervallowerbound): {{Number}}
  [MetricIntervalUpperBound](#cfn-applicationautoscaling-scalingpolicy-stepadjustment-metricintervalupperbound): {{Number}}
  [ScalingAdjustment](#cfn-applicationautoscaling-scalingpolicy-stepadjustment-scalingadjustment): {{Integer}}
```

## Properties
<a name="aws-properties-applicationautoscaling-scalingpolicy-stepadjustment-properties"></a>

`MetricIntervalLowerBound`  <a name="cfn-applicationautoscaling-scalingpolicy-stepadjustment-metricintervallowerbound"></a>
The lower bound for the difference between the alarm threshold and the CloudWatch metric. If the metric value is above the breach threshold, the lower bound is inclusive (the metric must be greater than or equal to the threshold plus the lower bound). Otherwise, it is exclusive (the metric must be greater than the threshold plus the lower bound). A null value indicates negative infinity.
You must specify at least one upper or lower bound.
*Required*: Conditional
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MetricIntervalUpperBound`  <a name="cfn-applicationautoscaling-scalingpolicy-stepadjustment-metricintervalupperbound"></a>
The upper bound for the difference between the alarm threshold and the CloudWatch metric. If the metric value is above the breach threshold, the upper bound is exclusive (the metric must be less than the threshold plus the upper bound). Otherwise, it is inclusive (the metric must be less than or equal to the threshold plus the upper bound). A null value indicates positive infinity.
You must specify at least one upper or lower bound.
*Required*: Conditional
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScalingAdjustment`  <a name="cfn-applicationautoscaling-scalingpolicy-stepadjustment-scalingadjustment"></a>
The amount by which to scale. The adjustment is based on the value that you specified in the `AdjustmentType` property (either an absolute number or a percentage). A positive value adds to the current capacity and a negative number subtracts from the current capacity.
*Required*: Yes
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-applicationautoscaling-scalingpolicy-stepadjustment--seealso"></a>
+  [Configure Application Auto Scaling resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/quickref-application-auto-scaling.html)
+ [Getting started](https://docs.aws.amazon.com/autoscaling/application/userguide/getting-started.html) in the *Application Auto Scaling User Guide*
