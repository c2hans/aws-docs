---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_EncryptionConfig.html
---

# EncryptionConfig
<a name="API_EncryptionConfig"></a>

Encryption settings for a collection.

## Contents
<a name="API_EncryptionConfig_Contents"></a>

 ** aWSOwnedKey **   <a name="opensearchserverless-Type-EncryptionConfig-aWSOwnedKey"></a>
Indicates whether to use an AWS-owned key for encryption.
Type: Boolean
Required: No

 ** kmsKeyArn **   <a name="opensearchserverless-Type-EncryptionConfig-kmsKeyArn"></a>
The ARN of the AWS Key Management Service key used to encrypt the collection.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 100.
Pattern: `arn:(aws|aws-us-gov|aws-cn|aws-iso|aws-iso-b):kms:[a-z0-9-]+:[0-9]{12}:key/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: No

## See Also
<a name="API_EncryptionConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchserverless-2021-11-01/EncryptionConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchserverless-2021-11-01/EncryptionConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchserverless-2021-11-01/EncryptionConfig)
