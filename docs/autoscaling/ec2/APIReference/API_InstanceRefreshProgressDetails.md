---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_InstanceRefreshProgressDetails.html
---

# InstanceRefreshProgressDetails
<a name="API_InstanceRefreshProgressDetails"></a>

Reports progress on replacing instances in an Auto Scaling group that has a warm pool. This includes separate details for instances in the warm pool and instances in the Auto Scaling group (the live pool).

## Contents
<a name="API_InstanceRefreshProgressDetails_Contents"></a>

 ** LivePoolProgress **
Reports progress on replacing instances that are in the Auto Scaling group.
Type: [InstanceRefreshLivePoolProgress](API_InstanceRefreshLivePoolProgress.md) object
Required: No

 ** WarmPoolProgress **
Reports progress on replacing instances that are in the warm pool.
Type: [InstanceRefreshWarmPoolProgress](API_InstanceRefreshWarmPoolProgress.md) object
Required: No

## See Also
<a name="API_InstanceRefreshProgressDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/InstanceRefreshProgressDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/InstanceRefreshProgressDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/InstanceRefreshProgressDetails)
