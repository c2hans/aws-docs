---
source_url: https://docs.aws.amazon.com/eks/latest/APIReference/API_KubeControllerManagerConfigRequest.html
---

# KubeControllerManagerConfigRequest
<a name="API_KubeControllerManagerConfigRequest"></a>

The configuration for the Kubernetes controller manager on an Amazon EKS cluster.

## Contents
<a name="API_KubeControllerManagerConfigRequest_Contents"></a>

 ** horizontalPodAutoscalerControllerConfig **   <a name="AmazonEKS-Type-KubeControllerManagerConfigRequest-horizontalPodAutoscalerControllerConfig"></a>
The horizontal pod autoscaler controller configuration.
Type: [HorizontalPodAutoscalerControllerConfigRequest](API_HorizontalPodAutoscalerControllerConfigRequest.md) object
Required: No

 ** podGcControllerConfig **   <a name="AmazonEKS-Type-KubeControllerManagerConfigRequest-podGcControllerConfig"></a>
The pod garbage collection controller configuration.
Type: [PodGcControllerConfigRequest](API_PodGcControllerConfigRequest.md) object
Required: No

## See Also
<a name="API_KubeControllerManagerConfigRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/KubeControllerManagerConfigRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/KubeControllerManagerConfigRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/KubeControllerManagerConfigRequest)
