---
source_url: https://docs.aws.amazon.com/arc-region-switch/latest/api/API_KubernetesScalingResource.html
---

# KubernetesScalingResource
<a name="API_KubernetesScalingResource"></a>

Defines a Kubernetes resource to scale in an Amazon EKS cluster.

## Contents
<a name="API_KubernetesScalingResource_Contents"></a>

 ** name **   <a name="regionswitch-Type-KubernetesScalingResource-name"></a>
The name for the Kubernetes resource.
Type: String
Required: Yes

 ** namespace **   <a name="regionswitch-Type-KubernetesScalingResource-namespace"></a>
The namespace for the Kubernetes resource.
Type: String
Pattern: `[a-z0-9][a-z0-9-]{0,61}[a-z0-9]`
Required: Yes

 ** hpaName **   <a name="regionswitch-Type-KubernetesScalingResource-hpaName"></a>
The hpaname for the Kubernetes resource.
Type: String
Required: No

## See Also
<a name="API_KubernetesScalingResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/arc-region-switch-2022-07-26/KubernetesScalingResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/arc-region-switch-2022-07-26/KubernetesScalingResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/arc-region-switch-2022-07-26/KubernetesScalingResource)
