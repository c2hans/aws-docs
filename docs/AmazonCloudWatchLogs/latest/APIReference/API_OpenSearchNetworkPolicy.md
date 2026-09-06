---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_OpenSearchNetworkPolicy.html
---

# OpenSearchNetworkPolicy
<a name="API_OpenSearchNetworkPolicy"></a>

This structure contains information about the OpenSearch Service network policy used for this integration. The network policy assigns network access settings to collections. For more information, see [Network policies](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-network.html#serverless-network-policies) in the OpenSearch Service Developer Guide.

## Contents
<a name="API_OpenSearchNetworkPolicy_Contents"></a>

 ** policyName **   <a name="CWL-Type-OpenSearchNetworkPolicy-policyName"></a>
The name of the network policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\.\-_/#A-Za-z0-9]+`
Required: No

 ** status **   <a name="CWL-Type-OpenSearchNetworkPolicy-status"></a>
This structure contains information about the status of this OpenSearch Service resource.
Type: [OpenSearchResourceStatus](API_OpenSearchResourceStatus.md) object
Required: No

## See Also
<a name="API_OpenSearchNetworkPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/OpenSearchNetworkPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/OpenSearchNetworkPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/OpenSearchNetworkPolicy)
