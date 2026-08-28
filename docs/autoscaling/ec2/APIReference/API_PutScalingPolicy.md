---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_PutScalingPolicy.html
---

# PutScalingPolicy
<a name="API_PutScalingPolicy"></a>

Creates or updates a scaling policy for an Auto Scaling group. Scaling policies are used to scale an Auto Scaling group based on configurable metrics. If no policies are defined, the dynamic scaling and predictive scaling features are not used.

For more information about using dynamic scaling, see [Target tracking scaling policies](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-target-tracking.html) and [Step and simple scaling policies](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-simple-step.html) in the *Amazon EC2 Auto Scaling User Guide*.

For more information about using predictive scaling, see [Predictive scaling for Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-predictive-scaling.html) in the *Amazon EC2 Auto Scaling User Guide*.

You can view the scaling policies for an Auto Scaling group using the [DescribePolicies](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribePolicies.html) API call. If you are no longer using a scaling policy, you can delete it by calling the [DeletePolicy](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DeletePolicy.html) API.

## Request Parameters
<a name="API_PutScalingPolicy_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** AdjustmentType **
Specifies how the scaling adjustment is interpreted (for example, an absolute number or a percentage). The valid values are `ChangeInCapacity`, `ExactCapacity`, and `PercentChangeInCapacity`.
Required if the policy type is `StepScaling` or `SimpleScaling`. For more information, see [Scaling adjustment types](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-simple-step.html#as-scaling-adjustment) in the *Amazon EC2 Auto Scaling User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** AutoScalingGroupName **
The name of the Auto Scaling group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: Yes

 ** Cooldown **
A cooldown period, in seconds, that applies to a specific simple scaling policy. When a cooldown period is specified here, it overrides the default cooldown.
Valid only if the policy type is `SimpleScaling`. For more information, see [Scaling cooldowns for Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-scaling-cooldowns.html) in the *Amazon EC2 Auto Scaling User Guide*.
Default: None
Type: Integer
Required: No

 ** Enabled **
Indicates whether the scaling policy is enabled or disabled. The default is enabled. For more information, see [Disable a scaling policy for an Auto Scaling group](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-enable-disable-scaling-policy.html) in the *Amazon EC2 Auto Scaling User Guide*.
Type: Boolean
Required: No

 ** EstimatedInstanceWarmup **
 *Not needed if the default instance warmup is defined for the group.*
The estimated time, in seconds, until a newly launched instance can contribute to the CloudWatch metrics. This warm-up period applies to instances launched due to a specific target tracking or step scaling policy. When a warm-up period is specified here, it overrides the default instance warmup.
Valid only if the policy type is `TargetTrackingScaling` or `StepScaling`.
The default is to use the value for the default instance warmup defined for the group. If default instance warmup is null, then `EstimatedInstanceWarmup` falls back to the value of default cooldown.
Type: Integer
Required: No

 ** MetricAggregationType **
The aggregation type for the CloudWatch metrics. The valid values are `Minimum`, `Maximum`, and `Average`. If the aggregation type is null, the value is treated as `Average`.
Valid only if the policy type is `StepScaling`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** MinAdjustmentMagnitude **
The minimum value to scale by when the adjustment type is `PercentChangeInCapacity`. For example, suppose that you create a step scaling policy to scale out an Auto Scaling group by 25 percent and you specify a `MinAdjustmentMagnitude` of 2. If the group has 4 instances and the scaling policy is performed, 25 percent of 4 is 1. However, because you specified a `MinAdjustmentMagnitude` of 2, Amazon EC2 Auto Scaling scales out the group by 2 instances.
Valid only if the policy type is `StepScaling` or `SimpleScaling`. For more information, see [Scaling adjustment types](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-simple-step.html#as-scaling-adjustment) in the *Amazon EC2 Auto Scaling User Guide*.
Some Auto Scaling groups use instance weights. In this case, set the `MinAdjustmentMagnitude` to a value that is at least as large as your largest instance weight.
Type: Integer
Required: No

 ** MinAdjustmentStep **
 *This parameter has been deprecated.*
Available for backward compatibility. Use `MinAdjustmentMagnitude` instead.
Type: Integer
Required: No

 ** PolicyName **
The name of the policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: Yes

 ** PolicyType **
One of the following policy types:
+  `TargetTrackingScaling`
+  `StepScaling`
+  `SimpleScaling` (default)
+  `PredictiveScaling`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** PredictiveScalingConfiguration **
A predictive scaling policy. Provides support for predefined and custom metrics.
Predefined metrics include CPU utilization, network in/out, and the Application Load Balancer request count.
Required if the policy type is `PredictiveScaling`.
Type: [PredictiveScalingConfiguration](API_PredictiveScalingConfiguration.md) object
Required: No

 ** ScalingAdjustment **
The amount by which to scale, based on the specified adjustment type. A positive value adds to the current capacity while a negative number removes from the current capacity. For exact capacity, you must specify a non-negative value.
Required if the policy type is `SimpleScaling`. (Not used with any other policy type.)
Type: Integer
Required: No

 **StepAdjustments.member.N**
A set of adjustments that enable you to scale based on the size of the alarm breach.
Required if the policy type is `StepScaling`. (Not used with any other policy type.)
Type: Array of [StepAdjustment](API_StepAdjustment.md) objects
Required: No

 ** TargetTrackingConfiguration **
A target tracking scaling policy. Provides support for predefined or custom metrics.
The following predefined metrics are available:
+  `ASGAverageCPUUtilization`
+  `ASGAverageNetworkIn`
+  `ASGAverageNetworkOut`
+  `ALBRequestCountPerTarget`
If you specify `ALBRequestCountPerTarget` for the metric, you must specify the `ResourceLabel` property with the `PredefinedMetricSpecification`.
Required if the policy type is `TargetTrackingScaling`.
Type: [TargetTrackingConfiguration](API_TargetTrackingConfiguration.md) object
Required: No

## Response Elements
<a name="API_PutScalingPolicy_ResponseElements"></a>

The following elements are returned by the service.

 **Alarms.member.N**
The CloudWatch alarms created for the target tracking scaling policy.
Type: Array of [Alarm](API_Alarm.md) objects

 ** PolicyARN **
The Amazon Resource Name (ARN) of the policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`

## Errors
<a name="API_PutScalingPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** LimitExceeded **
You have already reached a limit for your Amazon EC2 Auto Scaling resources (for example, Auto Scaling groups, launch configurations, or lifecycle hooks). For more information, see [DescribeAccountLimits](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeAccountLimits.html).
 ** message **

HTTP Status Code: 400

 ** ResourceContention **
You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).
 ** message **

HTTP Status Code: 500

 ** ServiceLinkedRoleFailure **
The service-linked role is not yet ready for use.
HTTP Status Code: 500

## Examples
<a name="API_PutScalingPolicy_Examples"></a>

### Example
<a name="API_PutScalingPolicy_Example_1"></a>

This example illustrates one usage of PutScalingPolicy.

#### Sample Request
<a name="API_PutScalingPolicy_Example_1_Request"></a>

```
https://autoscaling.amazonaws.com/?Action=PutScalingPolicy
&AutoScalingGroupName=my-asg
&PolicyName=alb1000-target-tracking-scaling-policy
&PolicyType=TargetTrackingScaling
&TargetTrackingConfiguration.TargetValue=1000.0
&TargetTrackingConfiguration.PredefinedMetricSpecification.PredefinedMetricType=ALBRequestCountPerTarget
&TargetTrackingConfiguration.PredefinedMetricSpecification.ResourceLabel=app%2Fmy-alb%2F778d41231b141a0f%2Ftargetgroup%2Fmy-alb-target-group%2F943f017f100becff
&Version=2011-01-01
&AUTHPARAMS
```

#### Sample Response
<a name="API_PutScalingPolicy_Example_1_Response"></a>

```
<PutScalingPolicyResponse xmlns="https://autoscaling.amazonaws.com/doc/2011-01-01/">
  <PutScalingPolicyResult>
    <PolicyARN>arn:aws:autoscaling:us-east-1:123456789012:scalingPolicy:228f02c2-c665-4bfd-aaac-8b04080bea3c:autoScalingGroupName/my-asg:policyName/alb1000-target-tracking-scaling-policy</PolicyARN>
    <Alarms>
      <member>
        <AlarmName>TargetTracking-my-asg-AlarmHigh-fc0e4183-23ac-497e-9992-691c9980c38e</AlarmName>
        <AlarmARN>arn:aws:cloudwatch:us-east-1:123456789012:alarm:TargetTracking-my-asg-AlarmHigh-fc0e4183-23ac-497e-9992-691c9980c38e</AlarmARN>
      </member>
      <member>
        <AlarmName>TargetTracking-my-asg-AlarmLow-61a39305-ed0c-47af-bd9e-471a352ee1a2</AlarmName>
        <AlarmARN>arn:aws:cloudwatch:us-east-1:123456789012:alarm:TargetTracking-my-asg-AlarmLow-61a39305-ed0c-47af-bd9e-471a352ee1a2</AlarmARN>
      </member>
    </Alarms>
  </PutScalingPolicyResult>
  <ResponseMetadata>
    <RequestId>7c6e177f-f082-11e1-ac58-3714bEXAMPLE</RequestId>
  </ResponseMetadata>
</PutScalingPolicyResponse>
```

## See Also
<a name="API_PutScalingPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/autoscaling-2011-01-01/PutScalingPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/autoscaling-2011-01-01/PutScalingPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/PutScalingPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/autoscaling-2011-01-01/PutScalingPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/PutScalingPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/autoscaling-2011-01-01/PutScalingPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/autoscaling-2011-01-01/PutScalingPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/autoscaling-2011-01-01/PutScalingPolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/autoscaling-2011-01-01/PutScalingPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/PutScalingPolicy)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
