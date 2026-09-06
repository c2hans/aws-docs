---
source_url: https://docs.aws.amazon.com/firehose/latest/APIReference/API_EncryptionConfiguration.html
---

# EncryptionConfiguration
<a name="API_EncryptionConfiguration"></a>

Describes the encryption for a destination in Amazon S3.

## Contents
<a name="API_EncryptionConfiguration_Contents"></a>

 ** KMSEncryptionConfig **   <a name="Firehose-Type-EncryptionConfiguration-KMSEncryptionConfig"></a>
The encryption key.
Type: [KMSEncryptionConfig](API_KMSEncryptionConfig.md) object
Required: No

 ** NoEncryptionConfig **   <a name="Firehose-Type-EncryptionConfiguration-NoEncryptionConfig"></a>
Specifically override existing encryption information to ensure that no encryption is used.
Type: String
Valid Values: `NoEncryption`
Required: No

## See Also
<a name="API_EncryptionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/firehose-2015-08-04/EncryptionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/firehose-2015-08-04/EncryptionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/firehose-2015-08-04/EncryptionConfiguration)
