---
source_url: https://docs.aws.amazon.com/eks/latest/APIReference/API_KubeApiServerConfigRequest.html
---

# KubeApiServerConfigRequest
<a name="API_KubeApiServerConfigRequest"></a>

The configuration for the Kubernetes API server on an Amazon EKS cluster.

## Contents
<a name="API_KubeApiServerConfigRequest_Contents"></a>

 ** eventTtl **   <a name="AmazonEKS-Type-KubeApiServerConfigRequest-eventTtl"></a>
The duration that Kubernetes events are retained. Valid values are single-unit durations such as `30m` or `1h`.
Type: String
Required: No

 ** serviceNodePortRange **   <a name="AmazonEKS-Type-KubeApiServerConfigRequest-serviceNodePortRange"></a>
The port range for NodePort services.
Type: [ServiceNodePortRange](API_ServiceNodePortRange.md) object
Required: No

## See Also
<a name="API_KubeApiServerConfigRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/KubeApiServerConfigRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/KubeApiServerConfigRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/KubeApiServerConfigRequest)
