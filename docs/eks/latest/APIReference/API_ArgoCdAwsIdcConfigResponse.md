---
source_url: https://docs.aws.amazon.com/eks/latest/APIReference/API_ArgoCdAwsIdcConfigResponse.html
---

# ArgoCdAwsIdcConfigResponse
<a name="API_ArgoCdAwsIdcConfigResponse"></a>

The response object containing IAM Identity CenterIAM; Identity Center configuration details for an Argo CD capability.

## Contents
<a name="API_ArgoCdAwsIdcConfigResponse_Contents"></a>

 ** idcInstanceArn **   <a name="AmazonEKS-Type-ArgoCdAwsIdcConfigResponse-idcInstanceArn"></a>
The Amazon Resource Name (ARN) of the IAM Identity CenterIAM; Identity Center instance used for authentication.
Type: String
Required: No

 ** idcManagedApplicationArn **   <a name="AmazonEKS-Type-ArgoCdAwsIdcConfigResponse-idcManagedApplicationArn"></a>
The Amazon Resource Name (ARN) of the managed application created in IAM Identity CenterIAM; Identity Center for this Argo CD capability. This application is automatically created and managed by Amazon EKS.
Type: String
Required: No

 ** idcRegion **   <a name="AmazonEKS-Type-ArgoCdAwsIdcConfigResponse-idcRegion"></a>
The Region where the IAM Identity CenterIAM; Identity Center instance is located.
Type: String
Required: No

## See Also
<a name="API_ArgoCdAwsIdcConfigResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/ArgoCdAwsIdcConfigResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/ArgoCdAwsIdcConfigResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/ArgoCdAwsIdcConfigResponse)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EKS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
