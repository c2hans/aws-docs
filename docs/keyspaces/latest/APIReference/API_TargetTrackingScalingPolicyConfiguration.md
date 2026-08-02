---
source_url: https://docs.aws.amazon.com/keyspaces/latest/APIReference/API_TargetTrackingScalingPolicyConfiguration.html
---

# TargetTrackingScalingPolicyConfiguration
<a name="API_TargetTrackingScalingPolicyConfiguration"></a>

The auto scaling policy that scales a table based on the ratio of consumed to provisioned capacity.

## Contents
<a name="API_TargetTrackingScalingPolicyConfiguration_Contents"></a>

 ** targetValue **   <a name="keyspaces-Type-TargetTrackingScalingPolicyConfiguration-targetValue"></a>
Specifies the target value for the target tracking auto scaling policy.
Amazon Keyspaces auto scaling scales up capacity automatically when traffic exceeds this target utilization rate, and then back down when it falls below the target. This ensures that the ratio of consumed capacity to provisioned capacity stays at or near this value. You define `targetValue` as a percentage. A `double` between 20 and 90.
Type: Double
Required: Yes

 ** disableScaleIn **   <a name="keyspaces-Type-TargetTrackingScalingPolicyConfiguration-disableScaleIn"></a>
Specifies if `scale-in` is enabled.
When auto scaling automatically decreases capacity for a table, the table *scales in*. When scaling policies are set, they can't scale in the table lower than its minimum capacity.
Type: Boolean
Required: No

 ** scaleInCooldown **   <a name="keyspaces-Type-TargetTrackingScalingPolicyConfiguration-scaleInCooldown"></a>
Specifies a `scale-in` cool down period.
A cooldown period in seconds between scaling activities that lets the table stabilize before another scaling activity starts.
Type: Integer
Required: No

 ** scaleOutCooldown **   <a name="keyspaces-Type-TargetTrackingScalingPolicyConfiguration-scaleOutCooldown"></a>
Specifies a scale out cool down period.
A cooldown period in seconds between scaling activities that lets the table stabilize before another scaling activity starts.
Type: Integer
Required: No

## See Also
<a name="API_TargetTrackingScalingPolicyConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/keyspaces-2022-02-10/TargetTrackingScalingPolicyConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/keyspaces-2022-02-10/TargetTrackingScalingPolicyConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/keyspaces-2022-02-10/TargetTrackingScalingPolicyConfiguration)
