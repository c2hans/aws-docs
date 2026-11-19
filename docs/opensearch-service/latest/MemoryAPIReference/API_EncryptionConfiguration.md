---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_EncryptionConfiguration.html
---

# EncryptionConfiguration

Encryption settings for a space.

## Contents
<a name="API_EncryptionConfiguration_Contents"></a>

 ** kmsKeyArn **   <a name="opensearchmemory-Type-EncryptionConfiguration-kmsKeyArn"></a>
The ARN of a customer managed AWS KMS key that encrypts the space's data. The key must be an enabled symmetric encryption key in the space's Region, and you need permission to create grants on it (`kms:CreateGrant`). Otherwise, the request fails with `ValidationException` or `AccessDeniedException`.
Type: String
Required: No

## See Also
<a name="API_EncryptionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchmemory-2026-08-24/EncryptionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchmemory-2026-08-24/EncryptionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchmemory-2026-08-24/EncryptionConfiguration)
