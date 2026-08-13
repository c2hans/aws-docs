---
source_url: https://docs.aws.amazon.com/eks/latest/APIReference/API_KubeApiServerConfigResponse.html
---

# KubeApiServerConfigResponse
<a name="API_KubeApiServerConfigResponse"></a>

The Kubernetes API server configuration for an Amazon EKS cluster.

## Contents
<a name="API_KubeApiServerConfigResponse_Contents"></a>

 ** eventTtl **   <a name="AmazonEKS-Type-KubeApiServerConfigResponse-eventTtl"></a>
The duration that Kubernetes events are retained.
Type: String
Required: No

 ** serviceNodePortRange **   <a name="AmazonEKS-Type-KubeApiServerConfigResponse-serviceNodePortRange"></a>
The port range for NodePort services.
Type: [ServiceNodePortRange](API_ServiceNodePortRange.md) object
Required: No

## See Also
<a name="API_KubeApiServerConfigResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/KubeApiServerConfigResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/KubeApiServerConfigResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/KubeApiServerConfigResponse)
