---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_FieldLevelEncryptionProfileConfig.html
---

# FieldLevelEncryptionProfileConfig
<a name="API_FieldLevelEncryptionProfileConfig"></a>

A complex data type of profiles for the field-level encryption.

## Contents
<a name="API_FieldLevelEncryptionProfileConfig_Contents"></a>

 ** CallerReference **   <a name="cloudfront-Type-FieldLevelEncryptionProfileConfig-CallerReference"></a>
A unique number that ensures that the request can't be replayed.
Type: String
Required: Yes

 ** EncryptionEntities **   <a name="cloudfront-Type-FieldLevelEncryptionProfileConfig-EncryptionEntities"></a>
A complex data type of encryption entities for the field-level encryption profile that include the public key ID, provider, and field patterns for specifying which fields to encrypt with this key.
Type: [EncryptionEntities](API_EncryptionEntities.md) object
Required: Yes

 ** Name **   <a name="cloudfront-Type-FieldLevelEncryptionProfileConfig-Name"></a>
Profile name for the field-level encryption profile.
Type: String
Required: Yes

 ** Comment **   <a name="cloudfront-Type-FieldLevelEncryptionProfileConfig-Comment"></a>
An optional comment for the field-level encryption profile. The comment cannot be longer than 128 characters.
Type: String
Required: No

## See Also
<a name="API_FieldLevelEncryptionProfileConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/FieldLevelEncryptionProfileConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/FieldLevelEncryptionProfileConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/FieldLevelEncryptionProfileConfig)
