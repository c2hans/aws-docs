---
source_url: https://docs.aws.amazon.com/eks/latest/APIReference/API_ArgoCdNetworkAccessConfigResponse.html
---

# ArgoCdNetworkAccessConfigResponse
<a name="API_ArgoCdNetworkAccessConfigResponse"></a>

The response object containing network access configuration for the Argo CD capability's managed API server endpoint. If VPC endpoint IDs are present, public access is blocked and the Argo CD server is only accessible through the specified VPC endpoints.

## Contents
<a name="API_ArgoCdNetworkAccessConfigResponse_Contents"></a>

 ** vpceIds **   <a name="AmazonEKS-Type-ArgoCdNetworkAccessConfigResponse-vpceIds"></a>
The list of VPC endpoint IDs associated with the managed Argo CD API server endpoint. Each VPC endpoint provides private connectivity from a specific VPC to the Argo CD server.
Type: Array of strings
Required: No

## See Also
<a name="API_ArgoCdNetworkAccessConfigResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/ArgoCdNetworkAccessConfigResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/ArgoCdNetworkAccessConfigResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/ArgoCdNetworkAccessConfigResponse)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EKS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
