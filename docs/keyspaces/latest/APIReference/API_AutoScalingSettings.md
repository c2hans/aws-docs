---
source_url: https://docs.aws.amazon.com/keyspaces/latest/APIReference/API_AutoScalingSettings.html
---

# AutoScalingSettings
<a name="API_AutoScalingSettings"></a>

The optional auto scaling settings for a table with provisioned throughput capacity.

To turn on auto scaling for a table in `throughputMode:PROVISIONED`, you must specify the following parameters.

Configure the minimum and maximum capacity units. The auto scaling policy ensures that capacity never goes below the minimum or above the maximum range.
+  `minimumUnits`: The minimum level of throughput the table should always be ready to support. The value must be between 1 and the max throughput per second quota for your account (40,000 by default).
+  `maximumUnits`: The maximum level of throughput the table should always be ready to support. The value must be between 1 and the max throughput per second quota for your account (40,000 by default).
+  `scalingPolicy`: Amazon Keyspaces supports the `target tracking` scaling policy. The auto scaling target is the provisioned capacity of the table.
  +  `targetTrackingScalingPolicyConfiguration`: To define the target tracking policy, you must define the target value.
    +  `targetValue`: The target utilization rate of the table. Amazon Keyspaces auto scaling ensures that the ratio of consumed capacity to provisioned capacity stays at or near this value. You define `targetValue` as a percentage. A `double` between 20 and 90. (Required)
    +  `disableScaleIn`: A `boolean` that specifies if `scale-in` is disabled or enabled for the table. This parameter is disabled by default. To turn on `scale-in`, set the `boolean` value to `FALSE`. This means that capacity for a table can be automatically scaled down on your behalf. (Optional)
    +  `scaleInCooldown`: A cooldown period in seconds between scaling activities that lets the table stabilize before another scale in activity starts. If no value is provided, the default is 0. (Optional)
    +  `scaleOutCooldown`: A cooldown period in seconds between scaling activities that lets the table stabilize before another scale out activity starts. If no value is provided, the default is 0. (Optional)

For more information, see [Managing throughput capacity automatically with Amazon Keyspaces auto scaling](https://docs.aws.amazon.com/keyspaces/latest/devguide/autoscaling.html) in the *Amazon Keyspaces Developer Guide*.

## Contents
<a name="API_AutoScalingSettings_Contents"></a>

 ** autoScalingDisabled **   <a name="keyspaces-Type-AutoScalingSettings-autoScalingDisabled"></a>
This optional parameter enables auto scaling for the table if set to `false`.
Type: Boolean
Required: No

 ** maximumUnits **   <a name="keyspaces-Type-AutoScalingSettings-maximumUnits"></a>
Manage costs by specifying the maximum amount of throughput to provision. The value must be between 1 and the max throughput per second quota for your account (40,000 by default).
Type: Long
Valid Range: Minimum value of 1.
Required: No

 ** minimumUnits **   <a name="keyspaces-Type-AutoScalingSettings-minimumUnits"></a>
The minimum level of throughput the table should always be ready to support. The value must be between 1 and the max throughput per second quota for your account (40,000 by default).
Type: Long
Valid Range: Minimum value of 1.
Required: No

 ** scalingPolicy **   <a name="keyspaces-Type-AutoScalingSettings-scalingPolicy"></a>
Amazon Keyspaces supports the `target tracking` auto scaling policy. With this policy, Amazon Keyspaces auto scaling ensures that the table's ratio of consumed to provisioned capacity stays at or near the target value that you specify. You define the target value as a percentage between 20 and 90.
Type: [AutoScalingPolicy](API_AutoScalingPolicy.md) object
Required: No

## See Also
<a name="API_AutoScalingSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/keyspaces-2022-02-10/AutoScalingSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/keyspaces-2022-02-10/AutoScalingSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/keyspaces-2022-02-10/AutoScalingSettings)
