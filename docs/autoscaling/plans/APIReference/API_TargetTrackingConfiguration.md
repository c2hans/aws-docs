---
source_url: https://docs.aws.amazon.com/autoscaling/plans/APIReference/API_TargetTrackingConfiguration.html
---

# TargetTrackingConfiguration
<a name="API_TargetTrackingConfiguration"></a>

Describes a target tracking configuration for a scalable resource. Used with [ScalingInstruction](API_ScalingInstruction.md) and [ScalingPolicy](API_ScalingPolicy.md).

## Contents
<a name="API_TargetTrackingConfiguration_Contents"></a>

 ** TargetValue **   <a name="autoscaling-Type-TargetTrackingConfiguration-TargetValue"></a>
The target value for the metric. Although this property accepts numbers of type Double, it won't accept values that are either too small or too large. Values must be in the range of -2^360 to 2^360.
Type: Double
Required: Yes

 ** CustomizedScalingMetricSpecification **   <a name="autoscaling-Type-TargetTrackingConfiguration-CustomizedScalingMetricSpecification"></a>
A customized metric. You can specify either a predefined metric or a customized metric.
Type: [CustomizedScalingMetricSpecification](API_CustomizedScalingMetricSpecification.md) object
Required: No

 ** DisableScaleIn **   <a name="autoscaling-Type-TargetTrackingConfiguration-DisableScaleIn"></a>
Indicates whether scale in by the target tracking scaling policy is disabled. If the value is `true`, scale in is disabled and the target tracking scaling policy doesn't remove capacity from the scalable resource. Otherwise, scale in is enabled and the target tracking scaling policy can remove capacity from the scalable resource.
The default value is `false`.
Type: Boolean
Required: No

 ** EstimatedInstanceWarmup **   <a name="autoscaling-Type-TargetTrackingConfiguration-EstimatedInstanceWarmup"></a>
The estimated time, in seconds, until a newly launched instance can contribute to the CloudWatch metrics. This value is used only if the resource is an Auto Scaling group.
Type: Integer
Required: No

 ** PredefinedScalingMetricSpecification **   <a name="autoscaling-Type-TargetTrackingConfiguration-PredefinedScalingMetricSpecification"></a>
A predefined metric. You can specify either a predefined metric or a customized metric.
Type: [PredefinedScalingMetricSpecification](API_PredefinedScalingMetricSpecification.md) object
Required: No

 ** ScaleInCooldown **   <a name="autoscaling-Type-TargetTrackingConfiguration-ScaleInCooldown"></a>
The amount of time, in seconds, after a scale-in activity completes before another scale-in activity can start. This property is not used if the scalable resource is an Auto Scaling group.
With the *scale-in cooldown period*, the intention is to scale in conservatively to protect your application’s availability, so scale-in activities are blocked until the cooldown period has expired. However, if another alarm triggers a scale-out activity during the scale-in cooldown period, Auto Scaling scales out the target immediately. In this case, the scale-in cooldown period stops and doesn't complete.
Type: Integer
Required: No

 ** ScaleOutCooldown **   <a name="autoscaling-Type-TargetTrackingConfiguration-ScaleOutCooldown"></a>
The amount of time, in seconds, to wait for a previous scale-out activity to take effect. This property is not used if the scalable resource is an Auto Scaling group.
With the *scale-out cooldown period*, the intention is to continuously (but not excessively) scale out. After Auto Scaling successfully scales out using a target tracking scaling policy, it starts to calculate the cooldown time. The scaling policy won't increase the desired capacity again unless either a larger scale out is triggered or the cooldown period ends.
Type: Integer
Required: No

## See Also
<a name="API_TargetTrackingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-plans-2018-01-06/TargetTrackingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-plans-2018-01-06/TargetTrackingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-plans-2018-01-06/TargetTrackingConfiguration)
