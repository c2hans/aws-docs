---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_ScalingPolicy.html
---

# ScalingPolicy
<a name="API_ScalingPolicy"></a>

Describes a scaling policy.

## Contents
<a name="API_ScalingPolicy_Contents"></a>

 ** AdjustmentType **
Specifies how the scaling adjustment is interpreted (for example, an absolute number or a percentage). The valid values are `ChangeInCapacity`, `ExactCapacity`, and `PercentChangeInCapacity`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** Alarms.member.N **
The CloudWatch alarms related to the policy.
Type: Array of [Alarm](API_Alarm.md) objects
Required: No

 ** AutoScalingGroupName **
The name of the Auto Scaling group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** Cooldown **
The duration of the policy's cooldown period, in seconds.
Type: Integer
Required: No

 ** Enabled **
Indicates whether the policy is enabled (`true`) or disabled (`false`).
Type: Boolean
Required: No

 ** EstimatedInstanceWarmup **
The estimated time, in seconds, until a newly launched instance can contribute to the CloudWatch metrics.
Type: Integer
Required: No

 ** MetricAggregationType **
The aggregation type for the CloudWatch metrics. The valid values are `Minimum`, `Maximum`, and `Average`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** MinAdjustmentMagnitude **
The minimum value to scale by when the adjustment type is `PercentChangeInCapacity`.
Type: Integer
Required: No

 ** MinAdjustmentStep **
 *This member has been deprecated.*
Available for backward compatibility. Use `MinAdjustmentMagnitude` instead.
Type: Integer
Required: No

 ** PolicyARN **
The Amazon Resource Name (ARN) of the policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** PolicyName **
The name of the scaling policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** PolicyType **
One of the following policy types:
+  `TargetTrackingScaling`
+  `StepScaling`
+  `SimpleScaling` (default)
+  `PredictiveScaling`
For more information, see [Target tracking scaling policies](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-target-tracking.html) and [Step and simple scaling policies](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-simple-step.html) in the *Amazon EC2 Auto Scaling User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** PredictiveScalingConfiguration **
A predictive scaling policy.
Type: [PredictiveScalingConfiguration](API_PredictiveScalingConfiguration.md) object
Required: No

 ** ScalingAdjustment **
The amount by which to scale, based on the specified adjustment type. A positive value adds to the current capacity while a negative number removes from the current capacity.
Type: Integer
Required: No

 ** StepAdjustments.member.N **
A set of adjustments that enable you to scale based on the size of the alarm breach.
Type: Array of [StepAdjustment](API_StepAdjustment.md) objects
Required: No

 ** TargetTrackingConfiguration **
A target tracking scaling policy.
Type: [TargetTrackingConfiguration](API_TargetTrackingConfiguration.md) object
Required: No

## See Also
<a name="API_ScalingPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/ScalingPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/ScalingPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/ScalingPolicy)
