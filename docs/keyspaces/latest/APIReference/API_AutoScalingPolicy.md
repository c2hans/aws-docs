---
source_url: https://docs.aws.amazon.com/keyspaces/latest/APIReference/API_AutoScalingPolicy.html
---

# AutoScalingPolicy
<a name="API_AutoScalingPolicy"></a>

Amazon Keyspaces supports the `target tracking` auto scaling policy. With this policy, Amazon Keyspaces auto scaling ensures that the table's ratio of consumed to provisioned capacity stays at or near the target value that you specify. You define the target value as a percentage between 20 and 90.

## Contents
<a name="API_AutoScalingPolicy_Contents"></a>

 ** targetTrackingScalingPolicyConfiguration **   <a name="keyspaces-Type-AutoScalingPolicy-targetTrackingScalingPolicyConfiguration"></a>
Auto scaling scales up capacity automatically when traffic exceeds this target utilization rate, and then back down when it falls below the target. A `double` between 20 and 90.
Type: [TargetTrackingScalingPolicyConfiguration](API_TargetTrackingScalingPolicyConfiguration.md) object
Required: No

## See Also
<a name="API_AutoScalingPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/keyspaces-2022-02-10/AutoScalingPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/keyspaces-2022-02-10/AutoScalingPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/keyspaces-2022-02-10/AutoScalingPolicy)
