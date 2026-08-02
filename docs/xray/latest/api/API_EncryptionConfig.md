---
source_url: https://docs.aws.amazon.com/xray/latest/api/API_EncryptionConfig.html
---

# EncryptionConfig
<a name="API_EncryptionConfig"></a>

A configuration document that specifies encryption configuration settings.

## Contents
<a name="API_EncryptionConfig_Contents"></a>

 ** KeyId **   <a name="xray-Type-EncryptionConfig-KeyId"></a>
The ID of the KMS key used for encryption, if applicable.
Type: String
Required: No

 ** Status **   <a name="xray-Type-EncryptionConfig-Status"></a>
The encryption status. While the status is `UPDATING`, X-Ray may encrypt data with a combination of the new and old settings.
Type: String
Valid Values: `UPDATING | ACTIVE`
Required: No

 ** Type **   <a name="xray-Type-EncryptionConfig-Type"></a>
The type of encryption. Set to `KMS` for encryption with KMS keys. Set to `NONE` for default encryption.
Type: String
Valid Values: `NONE | KMS`
Required: No

## See Also
<a name="API_EncryptionConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/xray-2016-04-12/EncryptionConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/xray-2016-04-12/EncryptionConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/xray-2016-04-12/EncryptionConfig)
