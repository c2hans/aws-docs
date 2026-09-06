---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_LifecyclePolicyDetail.html
---

# LifecyclePolicyDetail
<a name="API_LifecyclePolicyDetail"></a>

Details about an OpenSearch Serverless lifecycle policy.

## Contents
<a name="API_LifecyclePolicyDetail_Contents"></a>

 ** createdDate **   <a name="opensearchserverless-Type-LifecyclePolicyDetail-createdDate"></a>
The date the lifecycle policy was created.
Type: Long
Required: No

 ** description **   <a name="opensearchserverless-Type-LifecyclePolicyDetail-description"></a>
The description of the lifecycle policy.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Required: No

 ** lastModifiedDate **   <a name="opensearchserverless-Type-LifecyclePolicyDetail-lastModifiedDate"></a>
The timestamp of when the lifecycle policy was last modified.
Type: Long
Required: No

 ** name **   <a name="opensearchserverless-Type-LifecyclePolicyDetail-name"></a>
The name of the lifecycle policy.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 32.
Pattern: `[a-z][a-z0-9-]+`
Required: No

 ** policy **   <a name="opensearchserverless-Type-LifecyclePolicyDetail-policy"></a>
The JSON policy document without any whitespaces.
Type: JSON value
Required: No

 ** policyVersion **   <a name="opensearchserverless-Type-LifecyclePolicyDetail-policyVersion"></a>
The version of the lifecycle policy.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 36.
Pattern: `([0-9a-zA-Z+/]{4})*(([0-9a-zA-Z+/]{2}==)|([0-9a-zA-Z+/]{3}=))?`
Required: No

 ** type **   <a name="opensearchserverless-Type-LifecyclePolicyDetail-type"></a>
The type of lifecycle policy.
Type: String
Valid Values: `retention`
Required: No

## See Also
<a name="API_LifecyclePolicyDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchserverless-2021-11-01/LifecyclePolicyDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchserverless-2021-11-01/LifecyclePolicyDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchserverless-2021-11-01/LifecyclePolicyDetail)
