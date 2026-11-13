---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_EncryptionConfigurationDescription.html
---

# EncryptionConfigurationDescription
<a name="API_EncryptionConfigurationDescription"></a>

Describes the encryption configuration of snapshot data for a snapshot operation.

## Contents
<a name="API_EncryptionConfigurationDescription_Contents"></a>

 ** KeyType **   <a name="APIReference-Type-EncryptionConfigurationDescription-KeyType"></a>
Specifies the type of key used for encryption.
Type: String
Valid Values: `AWS_OWNED_KEY | CUSTOMER_MANAGED_KEY`
Required: Yes

 ** KeyId **   <a name="APIReference-Type-EncryptionConfigurationDescription-KeyId"></a>
The KMS key used for encryption.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## See Also
<a name="API_EncryptionConfigurationDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/EncryptionConfigurationDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/EncryptionConfigurationDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/EncryptionConfigurationDescription)
