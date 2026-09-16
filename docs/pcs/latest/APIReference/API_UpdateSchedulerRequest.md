---
source_url: https://docs.aws.amazon.com/pcs/latest/APIReference/API_UpdateSchedulerRequest.html
---

# UpdateSchedulerRequest
<a name="API_UpdateSchedulerRequest"></a>

The scheduler configuration for updating a cluster. Use this to specify the scheduler version to update to.

## Contents
<a name="API_UpdateSchedulerRequest_Contents"></a>

 ** version **   <a name="PCS-Type-UpdateSchedulerRequest-version"></a>
The scheduler version to update the cluster to. You can only update to a newer version. For more information about supported versions and update paths, see [Updating the scheduler version on a cluster](https://docs.aws.amazon.com/pcs/latest/userguide/working-with_clusters_version_update.html) in the * AWS PCS User Guide*.
Valid Values: `24.05 | 24.11 | 25.05 | 25.11 | 26.05`
Type: String
Required: Yes

## See Also
<a name="API_UpdateSchedulerRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pcs-2023-02-10/UpdateSchedulerRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pcs-2023-02-10/UpdateSchedulerRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pcs-2023-02-10/UpdateSchedulerRequest)
