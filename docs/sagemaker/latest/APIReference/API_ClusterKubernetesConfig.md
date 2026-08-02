---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ClusterKubernetesConfig.html
---

# ClusterKubernetesConfig
<a name="API_ClusterKubernetesConfig"></a>

Kubernetes configuration that specifies labels and taints to be applied to cluster nodes in an instance group.

## Contents
<a name="API_ClusterKubernetesConfig_Contents"></a>

 ** Labels **   <a name="sagemaker-Type-ClusterKubernetesConfig-Labels"></a>
Key-value pairs of labels to be applied to cluster nodes.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 317.
Key Pattern: `([a-z0-9]([-a-z0-9]*[a-z0-9])?(\.[a-z0-9]([-a-z0-9]*[a-z0-9])?)*/)?[A-Za-z0-9]([-A-Za-z0-9_.]*[A-Za-z0-9])?`
Value Length Constraints: Minimum length of 1. Maximum length of 63.
Value Pattern: `(([A-Za-z0-9][-A-Za-z0-9_.]*)?[A-Za-z0-9])?`
Required: No

 ** Taints **   <a name="sagemaker-Type-ClusterKubernetesConfig-Taints"></a>
List of taints to be applied to cluster nodes.
Type: Array of [ClusterKubernetesTaint](API_ClusterKubernetesTaint.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## See Also
<a name="API_ClusterKubernetesConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ClusterKubernetesConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ClusterKubernetesConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ClusterKubernetesConfig)
