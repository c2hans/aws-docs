---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_WarmPoolConfiguration.html
---

# WarmPoolConfiguration
<a name="API_WarmPoolConfiguration"></a>

Describes a warm pool configuration.

## Contents
<a name="API_WarmPoolConfiguration_Contents"></a>

 ** InstanceReusePolicy **
The instance reuse policy.
Type: [InstanceReusePolicy](API_InstanceReusePolicy.md) object
Required: No

 ** MaxGroupPreparedCapacity **
The maximum number of instances that are allowed to be in the warm pool or in any state except `Terminated` for the Auto Scaling group.
Type: Integer
Valid Range: Minimum value of -1.
Required: No

 ** MinSize **
The minimum number of instances to maintain in the warm pool.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** PoolState **
The instance state to transition to after the lifecycle actions are complete.
Type: String
Valid Values: `Stopped | Running | Hibernated`
Required: No

 ** Status **
The status of a warm pool that is marked for deletion.
Type: String
Valid Values: `PendingDelete`
Required: No

## See Also
<a name="API_WarmPoolConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/WarmPoolConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/WarmPoolConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/WarmPoolConfiguration)
