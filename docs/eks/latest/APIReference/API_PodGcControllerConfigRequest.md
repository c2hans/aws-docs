---
source_url: https://docs.aws.amazon.com/eks/latest/APIReference/API_PodGcControllerConfigRequest.html
---

# PodGcControllerConfigRequest
<a name="API_PodGcControllerConfigRequest"></a>

The pod garbage collection controller configuration for the Kubernetes controller manager.

## Contents
<a name="API_PodGcControllerConfigRequest_Contents"></a>

 ** terminatedPodGcThreshold **   <a name="AmazonEKS-Type-PodGcControllerConfigRequest-terminatedPodGcThreshold"></a>
The number of terminated pods that can exist before the garbage collector starts deleting them.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000000.
Required: No

## See Also
<a name="API_PodGcControllerConfigRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/PodGcControllerConfigRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/PodGcControllerConfigRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/PodGcControllerConfigRequest)
