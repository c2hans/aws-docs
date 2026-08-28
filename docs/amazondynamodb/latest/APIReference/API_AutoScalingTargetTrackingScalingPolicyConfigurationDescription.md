---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_AutoScalingTargetTrackingScalingPolicyConfigurationDescription.html
---

# AutoScalingTargetTrackingScalingPolicyConfigurationDescription
<a name="API_AutoScalingTargetTrackingScalingPolicyConfigurationDescription"></a>

Represents the properties of a target tracking scaling policy.

## Contents
<a name="API_AutoScalingTargetTrackingScalingPolicyConfigurationDescription_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** TargetValue **   <a name="DDB-Type-AutoScalingTargetTrackingScalingPolicyConfigurationDescription-TargetValue"></a>
The target value for the metric. The range is 8.515920e-109 to 1.174271e\+108 (Base 10) or 2e-360 to 2e360 (Base 2).
Type: Double
Required: Yes

 ** DisableScaleIn **   <a name="DDB-Type-AutoScalingTargetTrackingScalingPolicyConfigurationDescription-DisableScaleIn"></a>
Indicates whether scale in by the target tracking policy is disabled. If the value is true, scale in is disabled and the target tracking policy won't remove capacity from the scalable resource. Otherwise, scale in is enabled and the target tracking policy can remove capacity from the scalable resource. The default value is false.
Type: Boolean
Required: No

 ** ScaleInCooldown **   <a name="DDB-Type-AutoScalingTargetTrackingScalingPolicyConfigurationDescription-ScaleInCooldown"></a>
The amount of time, in seconds, after a scale in activity completes before another scale in activity can start. The cooldown period is used to block subsequent scale in requests until it has expired. You should scale in conservatively to protect your application's availability. However, if another alarm triggers a scale out policy during the cooldown period after a scale-in, application auto scaling scales out your scalable target immediately.
Type: Integer
Required: No

 ** ScaleOutCooldown **   <a name="DDB-Type-AutoScalingTargetTrackingScalingPolicyConfigurationDescription-ScaleOutCooldown"></a>
The amount of time, in seconds, after a scale out activity completes before another scale out activity can start. While the cooldown period is in effect, the capacity that has been added by the previous scale out event that initiated the cooldown is calculated as part of the desired capacity for the next scale out. You should continuously (but not excessively) scale out.
Type: Integer
Required: No

## See Also
<a name="API_AutoScalingTargetTrackingScalingPolicyConfigurationDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/AutoScalingTargetTrackingScalingPolicyConfigurationDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/AutoScalingTargetTrackingScalingPolicyConfigurationDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/AutoScalingTargetTrackingScalingPolicyConfigurationDescription)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DynamoDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazondynamodb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
