---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ClusterMetadata.html
---

# ClusterMetadata
<a name="API_ClusterMetadata"></a>

Metadata information about a HyperPod cluster showing information about the cluster level operations, such as creating, updating, and deleting.

## Contents
<a name="API_ClusterMetadata_Contents"></a>

 ** EksRoleAccessEntries **   <a name="sagemaker-Type-ClusterMetadata-EksRoleAccessEntries"></a>
A list of Amazon EKS IAM role ARNs associated with the cluster. This is created by HyperPod on your behalf and only applies for EKS orchestrated clusters.
Type: Array of strings
Required: No

 ** FailureMessage **   <a name="sagemaker-Type-ClusterMetadata-FailureMessage"></a>
An error message describing why the cluster level operation (such as creating, updating, or deleting) failed.
Type: String
Required: No

 ** SlrAccessEntry **   <a name="sagemaker-Type-ClusterMetadata-SlrAccessEntry"></a>
The Service-Linked Role (SLR) associated with the cluster. This is created by HyperPod on your behalf and only applies for EKS orchestrated clusters.
Type: String
Required: No

## See Also
<a name="API_ClusterMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ClusterMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ClusterMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ClusterMetadata)
