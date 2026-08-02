---
source_url: https://docs.aws.amazon.com/autoscaling/application/APIReference/API_TargetTrackingScalingPolicyConfiguration.html
---

# TargetTrackingScalingPolicyConfiguration
<a name="API_TargetTrackingScalingPolicyConfiguration"></a>

Represents a target tracking scaling policy configuration to use with Application Auto Scaling.

For more information, see [Target tracking scaling policies](https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-target-tracking.html) in the *Application Auto Scaling User Guide*.

## Contents
<a name="API_TargetTrackingScalingPolicyConfiguration_Contents"></a>

 ** TargetValue **   <a name="autoscaling-Type-TargetTrackingScalingPolicyConfiguration-TargetValue"></a>
The target value for the metric. Although this property accepts numbers of type Double, it won't accept values that are either too small or too large. Values must be in the range of -2^360 to 2^360. The value must be a valid number based on the choice of metric. For example, if the metric is CPU utilization, then the target value is a percent value that represents how much of the CPU can be used before scaling out.
If the scaling policy specifies the `ALBRequestCountPerTarget` predefined metric, specify the target utilization as the optimal average request count per target during any one-minute interval.
Type: Double
Required: Yes

 ** CustomizedMetricSpecification **   <a name="autoscaling-Type-TargetTrackingScalingPolicyConfiguration-CustomizedMetricSpecification"></a>
A customized metric. You can specify either a predefined metric or a customized metric.
Type: [CustomizedMetricSpecification](API_CustomizedMetricSpecification.md) object
Required: No

 ** DisableScaleIn **   <a name="autoscaling-Type-TargetTrackingScalingPolicyConfiguration-DisableScaleIn"></a>
Indicates whether scale in by the target tracking scaling policy is disabled. If the value is `true`, scale in is disabled and the target tracking scaling policy won't remove capacity from the scalable target. Otherwise, scale in is enabled and the target tracking scaling policy can remove capacity from the scalable target. The default value is `false`.
Type: Boolean
Required: No

 ** PredefinedMetricSpecification **   <a name="autoscaling-Type-TargetTrackingScalingPolicyConfiguration-PredefinedMetricSpecification"></a>
A predefined metric. You can specify either a predefined metric or a customized metric.
Type: [PredefinedMetricSpecification](API_PredefinedMetricSpecification.md) object
Required: No

 ** ScaleInCooldown **   <a name="autoscaling-Type-TargetTrackingScalingPolicyConfiguration-ScaleInCooldown"></a>
The amount of time, in seconds, after a scale-in activity completes before another scale-in activity can start. For more information and for default values, see [Define cooldown periods](https://docs.aws.amazon.com/autoscaling/application/userguide/target-tracking-scaling-policy-overview.html#target-tracking-cooldown) in the *Application Auto Scaling User Guide*.
Type: Integer
Required: No

 ** ScaleOutCooldown **   <a name="autoscaling-Type-TargetTrackingScalingPolicyConfiguration-ScaleOutCooldown"></a>
The amount of time, in seconds, to wait for a previous scale-out activity to take effect. For more information and for default values, see [Define cooldown periods](https://docs.aws.amazon.com/autoscaling/application/userguide/target-tracking-scaling-policy-overview.html#target-tracking-cooldown) in the *Application Auto Scaling User Guide*.
Type: Integer
Required: No

## See Also
<a name="API_TargetTrackingScalingPolicyConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-autoscaling-2016-02-06/TargetTrackingScalingPolicyConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-autoscaling-2016-02-06/TargetTrackingScalingPolicyConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-autoscaling-2016-02-06/TargetTrackingScalingPolicyConfiguration)
