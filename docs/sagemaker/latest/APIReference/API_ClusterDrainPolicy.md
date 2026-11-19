---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ClusterDrainPolicy.html
---

# ClusterDrainPolicy

Specifies how pods are evicted from an instance before it is patched with the `DrainFirst` strategy. By default, evictions respect Kubernetes Pod Disruption Budgets.

## Contents
<a name="API_ClusterDrainPolicy_Contents"></a>

 ** DrainTimeoutInSeconds **   <a name="sagemaker-Type-ClusterDrainPolicy-DrainTimeoutInSeconds"></a>
The maximum time, in seconds, to wait for the pods on an instance to drain. Valid values are from 0 to 5400 (90 minutes). The default is 3600 (1 hour).
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 5400.
Required: No

 ** OnDrainTimeout **   <a name="sagemaker-Type-ClusterDrainPolicy-OnDrainTimeout"></a>
The action to take if the pods on an instance don't drain within `DrainTimeoutInSeconds`. The default is `Skip`.
+  `Skip`: Doesn't patch the instance. The instance is uncordoned and remains on the previous AMI version. This can leave the instance group partially patched. You can then use UpdateClusterSoftware with the desired ImageReleaseVersion to manually update the remaining instances.
+  `Force`: Deletes the remaining pods without respecting Pod Disruption Budgets, and then patches the instance.
Type: String
Valid Values: `Force | Skip`
Required: No

## See Also
<a name="API_ClusterDrainPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ClusterDrainPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ClusterDrainPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ClusterDrainPolicy)
