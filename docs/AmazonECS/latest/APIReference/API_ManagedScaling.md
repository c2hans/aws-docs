---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ManagedScaling.html
---

# ManagedScaling
<a name="API_ManagedScaling"></a>

The managed scaling settings for the Auto Scaling group capacity provider.

When managed scaling is turned on, Amazon ECS manages the scale-in and scale-out actions of the Auto Scaling group. Amazon ECS manages a target tracking scaling policy using an Amazon ECS managed CloudWatch metric with the specified `targetCapacity` value as the target value for the metric. For more information, see [Using managed scaling](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/asg-capacity-providers.html#asg-capacity-providers-managed-scaling) in the *Amazon Elastic Container Service Developer Guide*.

If managed scaling is off, the user must manage the scaling of the Auto Scaling group.

## Contents
<a name="API_ManagedScaling_Contents"></a>

 ** instanceWarmupPeriod **   <a name="ECS-Type-ManagedScaling-instanceWarmupPeriod"></a>
The period of time, in seconds, after a newly launched Amazon EC2 instance can contribute to CloudWatch metrics for Auto Scaling group. If this parameter is omitted, the default value of `300` seconds is used.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 10000.
Required: No

 ** maximumScalingStepSize **   <a name="ECS-Type-ManagedScaling-maximumScalingStepSize"></a>
The maximum number of Amazon EC2 instances that Amazon ECS will scale out at one time. If this parameter is omitted, the default value of `10000` is used.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 10000.
Required: No

 ** minimumScalingStepSize **   <a name="ECS-Type-ManagedScaling-minimumScalingStepSize"></a>
The minimum number of Amazon EC2 instances that Amazon ECS will scale out at one time. The scale in process is not affected by this parameter If this parameter is omitted, the default value of `1` is used.
When additional capacity is required, Amazon ECS will scale up the minimum scaling step size even if the actual demand is less than the minimum scaling step size.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 10000.
Required: No

 ** status **   <a name="ECS-Type-ManagedScaling-status"></a>
Determines whether to use managed scaling for the capacity provider.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** targetCapacity **   <a name="ECS-Type-ManagedScaling-targetCapacity"></a>
The target capacity utilization as a percentage for the capacity provider. The specified value must be greater than `0` and less than or equal to `100`. For example, if you want the capacity provider to maintain 10% spare capacity, then that means the utilization is 90%, so use a `targetCapacity` of `90`. The default value of `100` percent results in the Amazon EC2 instances in your Auto Scaling group being completely used.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

## See Also
<a name="API_ManagedScaling_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/ManagedScaling)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/ManagedScaling)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/ManagedScaling)
