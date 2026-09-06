---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_FieldLevelEncryption.html
---

# FieldLevelEncryption
<a name="API_FieldLevelEncryption"></a>

A complex data type that includes the profile configurations and other options specified for field-level encryption.

## Contents
<a name="API_FieldLevelEncryption_Contents"></a>

 ** FieldLevelEncryptionConfig **   <a name="cloudfront-Type-FieldLevelEncryption-FieldLevelEncryptionConfig"></a>
A complex data type that includes the profile configurations specified for field-level encryption.
Type: [FieldLevelEncryptionConfig](API_FieldLevelEncryptionConfig.md) object
Required: Yes

 ** Id **   <a name="cloudfront-Type-FieldLevelEncryption-Id"></a>
The configuration ID for a field-level encryption configuration which includes a set of profiles that specify certain selected data fields to be encrypted by specific public keys.
Type: String
Required: Yes

 ** LastModifiedTime **   <a name="cloudfront-Type-FieldLevelEncryption-LastModifiedTime"></a>
The last time the field-level encryption configuration was changed.
Type: Timestamp
Required: Yes

## See Also
<a name="API_FieldLevelEncryption_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/FieldLevelEncryption)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/FieldLevelEncryption)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/FieldLevelEncryption)
