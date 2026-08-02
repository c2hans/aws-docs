---
source_url: https://docs.aws.amazon.com/eks/latest/APIReference/API_ArgoCdNetworkAccessConfigRequest.html
---

# ArgoCdNetworkAccessConfigRequest
<a name="API_ArgoCdNetworkAccessConfigRequest"></a>

Configuration for network access to the Argo CD capability's managed API server endpoint. When VPC endpoint IDs are specified, public access is blocked and the Argo CD server is only accessible through the specified VPC endpoints.

## Contents
<a name="API_ArgoCdNetworkAccessConfigRequest_Contents"></a>

 ** vpceIds **   <a name="AmazonEKS-Type-ArgoCdNetworkAccessConfigRequest-vpceIds"></a>
A list of VPC endpoint IDs to associate with the managed Argo CD API server endpoint. Each VPC endpoint provides private connectivity from a specific VPC to the Argo CD server. You can specify multiple VPC endpoint IDs to enable access from multiple VPCs.
Type: Array of strings
Required: No

## See Also
<a name="API_ArgoCdNetworkAccessConfigRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/ArgoCdNetworkAccessConfigRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/ArgoCdNetworkAccessConfigRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/ArgoCdNetworkAccessConfigRequest)
