---
source_url: https://docs.aws.amazon.com/eks/latest/APIReference/API_KubeControllerManagerVersionConfig.html
---

# KubeControllerManagerVersionConfig
<a name="API_KubeControllerManagerVersionConfig"></a>

The Kubernetes controller manager version-specific configuration defaults and constraints.

## Contents
<a name="API_KubeControllerManagerVersionConfig_Contents"></a>

 ** horizontalPodAutoscalerControllerConfig **   <a name="AmazonEKS-Type-KubeControllerManagerVersionConfig-horizontalPodAutoscalerControllerConfig"></a>
The horizontal pod autoscaler controller configuration with default value and constraints.
Type: [HorizontalPodAutoscalerControllerVersionConfig](API_HorizontalPodAutoscalerControllerVersionConfig.md) object
Required: No

 ** podGcControllerConfig **   <a name="AmazonEKS-Type-KubeControllerManagerVersionConfig-podGcControllerConfig"></a>
The pod garbage collection controller configuration with default value and constraints.
Type: [PodGcControllerVersionConfig](API_PodGcControllerVersionConfig.md) object
Required: No

## See Also
<a name="API_KubeControllerManagerVersionConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/KubeControllerManagerVersionConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/KubeControllerManagerVersionConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/KubeControllerManagerVersionConfig)
