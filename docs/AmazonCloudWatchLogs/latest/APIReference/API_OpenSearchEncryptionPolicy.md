---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_OpenSearchEncryptionPolicy.html
---

# OpenSearchEncryptionPolicy
<a name="API_OpenSearchEncryptionPolicy"></a>

This structure contains information about the OpenSearch Service encryption policy used for this integration. The encryption policy was created automatically when you created the integration. For more information, see [Encryption policies](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-encryption.html#serverless-encryption-policies) in the OpenSearch Service Developer Guide.

## Contents
<a name="API_OpenSearchEncryptionPolicy_Contents"></a>

 ** policyName **   <a name="CWL-Type-OpenSearchEncryptionPolicy-policyName"></a>
The name of the encryption policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\.\-_/#A-Za-z0-9]+`
Required: No

 ** status **   <a name="CWL-Type-OpenSearchEncryptionPolicy-status"></a>
This structure contains information about the status of this OpenSearch Service resource.
Type: [OpenSearchResourceStatus](API_OpenSearchResourceStatus.md) object
Required: No

## See Also
<a name="API_OpenSearchEncryptionPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/OpenSearchEncryptionPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/OpenSearchEncryptionPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/OpenSearchEncryptionPolicy)
