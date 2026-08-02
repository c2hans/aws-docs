---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_EncryptionConfig.html
---

# EncryptionConfig
<a name="API_EncryptionConfig"></a>

The encryption configuration.

## Contents
<a name="API_EncryptionConfig_Contents"></a>

 ** EncryptionType **   <a name="connect-Type-EncryptionConfig-EncryptionType"></a>
The type of encryption.
Type: String
Valid Values: `KMS`
Required: Yes

 ** KeyId **   <a name="connect-Type-EncryptionConfig-KeyId"></a>
The full ARN of the encryption key.
Be sure to provide the full ARN of the encryption key, not just the ID.
Connect Customer supports only KMS keys with the default key spec of [https://docs.aws.amazon.com/kms/latest/developerguide/asymmetric-key-specs.html#key-spec-symmetric-default](https://docs.aws.amazon.com/kms/latest/developerguide/asymmetric-key-specs.html#key-spec-symmetric-default).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

## See Also
<a name="API_EncryptionConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/EncryptionConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/EncryptionConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/EncryptionConfig)
