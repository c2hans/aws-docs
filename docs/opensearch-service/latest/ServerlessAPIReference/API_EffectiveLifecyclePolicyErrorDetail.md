---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_EffectiveLifecyclePolicyErrorDetail.html
---

# EffectiveLifecyclePolicyErrorDetail
<a name="API_EffectiveLifecyclePolicyErrorDetail"></a>

Error information for an OpenSearch Serverless request.

## Contents
<a name="API_EffectiveLifecyclePolicyErrorDetail_Contents"></a>

 ** errorCode **   <a name="opensearchserverless-Type-EffectiveLifecyclePolicyErrorDetail-errorCode"></a>
The error code for the request.
Type: String
Required: No

 ** errorMessage **   <a name="opensearchserverless-Type-EffectiveLifecyclePolicyErrorDetail-errorMessage"></a>
A description of the error. For example, `The specified Index resource is not found`.
Type: String
Required: No

 ** resource **   <a name="opensearchserverless-Type-EffectiveLifecyclePolicyErrorDetail-resource"></a>
The name of OpenSearch Serverless index resource.
Type: String
Required: No

 ** type **   <a name="opensearchserverless-Type-EffectiveLifecyclePolicyErrorDetail-type"></a>
The type of lifecycle policy.
Type: String
Valid Values: `retention`
Required: No

## See Also
<a name="API_EffectiveLifecyclePolicyErrorDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchserverless-2021-11-01/EffectiveLifecyclePolicyErrorDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchserverless-2021-11-01/EffectiveLifecyclePolicyErrorDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchserverless-2021-11-01/EffectiveLifecyclePolicyErrorDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Serverless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
