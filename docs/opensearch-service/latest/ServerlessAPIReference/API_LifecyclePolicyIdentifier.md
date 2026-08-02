---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_LifecyclePolicyIdentifier.html
---

# LifecyclePolicyIdentifier
<a name="API_LifecyclePolicyIdentifier"></a>

The unique identifiers of policy types and policy names.

## Contents
<a name="API_LifecyclePolicyIdentifier_Contents"></a>

 ** name **   <a name="opensearchserverless-Type-LifecyclePolicyIdentifier-name"></a>
The name of the lifecycle policy.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 32.
Pattern: `[a-z][a-z0-9-]+`
Required: Yes

 ** type **   <a name="opensearchserverless-Type-LifecyclePolicyIdentifier-type"></a>
The type of lifecycle policy.
Type: String
Valid Values: `retention`
Required: Yes

## See Also
<a name="API_LifecyclePolicyIdentifier_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchserverless-2021-11-01/LifecyclePolicyIdentifier)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchserverless-2021-11-01/LifecyclePolicyIdentifier)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchserverless-2021-11-01/LifecyclePolicyIdentifier)
