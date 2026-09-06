---
source_url: https://docs.aws.amazon.com/autoscaling/application/APIReference/API_StepScalingPolicyConfiguration.html
---

# StepScalingPolicyConfiguration
<a name="API_StepScalingPolicyConfiguration"></a>

Represents a step scaling policy configuration to use with Application Auto Scaling.

For more information, see [Step scaling policies](https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-step-scaling-policies.html) in the *Application Auto Scaling User Guide*.

## Contents
<a name="API_StepScalingPolicyConfiguration_Contents"></a>

 ** AdjustmentType **   <a name="autoscaling-Type-StepScalingPolicyConfiguration-AdjustmentType"></a>
Specifies how the `ScalingAdjustment` value in a [StepAdjustment](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_StepAdjustment.html) is interpreted (for example, an absolute number or a percentage). The valid values are `ChangeInCapacity`, `ExactCapacity`, and `PercentChangeInCapacity`.
 `AdjustmentType` is required if you are adding a new step scaling policy configuration.
Type: String
Valid Values: `ChangeInCapacity | PercentChangeInCapacity | ExactCapacity`
Required: No

 ** Cooldown **   <a name="autoscaling-Type-StepScalingPolicyConfiguration-Cooldown"></a>
The amount of time, in seconds, to wait for a previous scaling activity to take effect. If not specified, the default value is 300. For more information, see [Cooldown period](https://docs.aws.amazon.com/autoscaling/application/userguide/step-scaling-policy-overview.html#step-scaling-cooldown) in the *Application Auto Scaling User Guide*.
Type: Integer
Required: No

 ** MetricAggregationType **   <a name="autoscaling-Type-StepScalingPolicyConfiguration-MetricAggregationType"></a>
The aggregation type for the CloudWatch metrics. Valid values are `Minimum`, `Maximum`, and `Average`. If the aggregation type is null, the value is treated as `Average`.
Type: String
Valid Values: `Average | Minimum | Maximum`
Required: No

 ** MinAdjustmentMagnitude **   <a name="autoscaling-Type-StepScalingPolicyConfiguration-MinAdjustmentMagnitude"></a>
The minimum value to scale by when the adjustment type is `PercentChangeInCapacity`. For example, suppose that you create a step scaling policy to scale out an Amazon ECS service by 25 percent and you specify a `MinAdjustmentMagnitude` of 2. If the service has 4 tasks and the scaling policy is performed, 25 percent of 4 is 1. However, because you specified a `MinAdjustmentMagnitude` of 2, Application Auto Scaling scales out the service by 2 tasks.
Type: Integer
Required: No

 ** StepAdjustments **   <a name="autoscaling-Type-StepScalingPolicyConfiguration-StepAdjustments"></a>
A set of adjustments that enable you to scale based on the size of the alarm breach.
At least one step adjustment is required if you are adding a new step scaling policy configuration.
Type: Array of [StepAdjustment](API_StepAdjustment.md) objects
Required: No

## See Also
<a name="API_StepScalingPolicyConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-autoscaling-2016-02-06/StepScalingPolicyConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-autoscaling-2016-02-06/StepScalingPolicyConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-autoscaling-2016-02-06/StepScalingPolicyConfiguration)
