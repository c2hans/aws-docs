---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_LifecyclePolicyResourceIdentifier.html
---

# LifecyclePolicyResourceIdentifier
<a name="API_LifecyclePolicyResourceIdentifier"></a>

The unique identifiers of policy types and resource names.

## Contents
<a name="API_LifecyclePolicyResourceIdentifier_Contents"></a>

 ** resource **   <a name="opensearchserverless-Type-LifecyclePolicyResourceIdentifier-resource"></a>
The name of the OpenSearch Serverless ilndex resource.
Type: String
Pattern: `index/[a-z][a-z0-9-]{3,63}/([a-z;0-9&$%][+.~=\-_a-z;0-9&$%]*)`
Required: Yes

 ** type **   <a name="opensearchserverless-Type-LifecyclePolicyResourceIdentifier-type"></a>
The type of lifecycle policy.
Type: String
Valid Values: `retention`
Required: Yes

## See Also
<a name="API_LifecyclePolicyResourceIdentifier_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchserverless-2021-11-01/LifecyclePolicyResourceIdentifier)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchserverless-2021-11-01/LifecyclePolicyResourceIdentifier)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchserverless-2021-11-01/LifecyclePolicyResourceIdentifier)
