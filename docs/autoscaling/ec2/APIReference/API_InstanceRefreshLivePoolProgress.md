---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_InstanceRefreshLivePoolProgress.html
---

# InstanceRefreshLivePoolProgress
<a name="API_InstanceRefreshLivePoolProgress"></a>

Reports progress on replacing instances that are in the Auto Scaling group.

## Contents
<a name="API_InstanceRefreshLivePoolProgress_Contents"></a>

 ** InstancesToUpdate **
The number of instances remaining to update.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** PercentageComplete **
The percentage of instances in the Auto Scaling group that have been replaced. For each instance replacement, Amazon EC2 Auto Scaling tracks the instance's health status and warm-up time. When the instance's health status changes to healthy and the specified warm-up time passes, the instance is considered updated and is added to the percentage complete.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

## See Also
<a name="API_InstanceRefreshLivePoolProgress_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/InstanceRefreshLivePoolProgress)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/InstanceRefreshLivePoolProgress)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/InstanceRefreshLivePoolProgress)
