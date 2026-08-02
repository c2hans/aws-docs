---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_EffectiveLifecyclePolicyDetail.html
---

# EffectiveLifecyclePolicyDetail
<a name="API_EffectiveLifecyclePolicyDetail"></a>

Error information for an OpenSearch Serverless request.

## Contents
<a name="API_EffectiveLifecyclePolicyDetail_Contents"></a>

 ** noMinRetentionPeriod **   <a name="opensearchserverless-Type-EffectiveLifecyclePolicyDetail-noMinRetentionPeriod"></a>
The minimum number of index retention days set. That is an optional param that will return as `true` if the minimum number of days or hours is not set to a index resource.
Type: Boolean
Required: No

 ** policyName **   <a name="opensearchserverless-Type-EffectiveLifecyclePolicyDetail-policyName"></a>
The name of the lifecycle policy.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 32.
Pattern: `[a-z][a-z0-9-]+`
Required: No

 ** resource **   <a name="opensearchserverless-Type-EffectiveLifecyclePolicyDetail-resource"></a>
The name of the OpenSearch Serverless index resource.
Type: String
Required: No

 ** resourceType **   <a name="opensearchserverless-Type-EffectiveLifecyclePolicyDetail-resourceType"></a>
The type of OpenSearch Serverless resource. Currently, the only supported resource is `index`.
Type: String
Valid Values: `index`
Required: No

 ** retentionPeriod **   <a name="opensearchserverless-Type-EffectiveLifecyclePolicyDetail-retentionPeriod"></a>
The minimum number of index retention in days or hours. This is an optional parameter that will return only if it’s set.
Type: String
Required: No

 ** type **   <a name="opensearchserverless-Type-EffectiveLifecyclePolicyDetail-type"></a>
The type of lifecycle policy.
Type: String
Valid Values: `retention`
Required: No

## See Also
<a name="API_EffectiveLifecyclePolicyDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchserverless-2021-11-01/EffectiveLifecyclePolicyDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchserverless-2021-11-01/EffectiveLifecyclePolicyDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchserverless-2021-11-01/EffectiveLifecyclePolicyDetail)
