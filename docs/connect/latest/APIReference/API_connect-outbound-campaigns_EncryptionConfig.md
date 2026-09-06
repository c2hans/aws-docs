---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-outbound-campaigns_EncryptionConfig.html
---

# EncryptionConfig
<a name="API_connect-outbound-campaigns_EncryptionConfig"></a>

Contains encryption configuration for an Connect Customer instance.

## Contents
<a name="API_connect-outbound-campaigns_EncryptionConfig_Contents"></a>

 ** enabled **   <a name="connect-Type-connect-outbound-campaigns_EncryptionConfig-enabled"></a>
The status of whether encryption is done using a customer managed key or AWS owned key.
Type: Boolean
Required: Yes

 ** encryptionType **   <a name="connect-Type-connect-outbound-campaigns_EncryptionConfig-encryptionType"></a>
The type of encryption.
Type: String
Valid Values: `KMS`
Required: No

 ** keyArn **   <a name="connect-Type-connect-outbound-campaigns_EncryptionConfig-keyArn"></a>
The Amazon Resource Name (ARN) of the customer managed key or AWS owned key.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: No

## See Also
<a name="API_connect-outbound-campaigns_EncryptionConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcampaigns-2021-01-30/EncryptionConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcampaigns-2021-01-30/EncryptionConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcampaigns-2021-01-30/EncryptionConfig)
