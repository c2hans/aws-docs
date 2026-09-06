---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_ApplicationEncryptionConfigurationDescription.html
---

# ApplicationEncryptionConfigurationDescription
<a name="API_ApplicationEncryptionConfigurationDescription"></a>

Describes the encryption at rest configuration.

## Contents
<a name="API_ApplicationEncryptionConfigurationDescription_Contents"></a>

 ** KeyType **   <a name="APIReference-Type-ApplicationEncryptionConfigurationDescription-KeyType"></a>
Specifies the type of key used for encryption at rest.
Type: String
Valid Values: `AWS_OWNED_KEY | CUSTOMER_MANAGED_KEY`
Required: Yes

 ** KeyId **   <a name="APIReference-Type-ApplicationEncryptionConfigurationDescription-KeyId"></a>
The key ARN, key ID, alias ARN, or alias name of the KMS key used for encryption at rest.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## See Also
<a name="API_ApplicationEncryptionConfigurationDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/ApplicationEncryptionConfigurationDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/ApplicationEncryptionConfigurationDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/ApplicationEncryptionConfigurationDescription)
