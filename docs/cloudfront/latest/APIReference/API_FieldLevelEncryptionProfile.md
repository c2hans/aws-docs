---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_FieldLevelEncryptionProfile.html
---

# FieldLevelEncryptionProfile
<a name="API_FieldLevelEncryptionProfile"></a>

A complex data type for field-level encryption profiles.

## Contents
<a name="API_FieldLevelEncryptionProfile_Contents"></a>

 ** FieldLevelEncryptionProfileConfig **   <a name="cloudfront-Type-FieldLevelEncryptionProfile-FieldLevelEncryptionProfileConfig"></a>
A complex data type that includes the profile name and the encryption entities for the field-level encryption profile.
Type: [FieldLevelEncryptionProfileConfig](API_FieldLevelEncryptionProfileConfig.md) object
Required: Yes

 ** Id **   <a name="cloudfront-Type-FieldLevelEncryptionProfile-Id"></a>
The ID for a field-level encryption profile configuration which includes a set of profiles that specify certain selected data fields to be encrypted by specific public keys.
Type: String
Required: Yes

 ** LastModifiedTime **   <a name="cloudfront-Type-FieldLevelEncryptionProfile-LastModifiedTime"></a>
The last time the field-level encryption profile was updated.
Type: Timestamp
Required: Yes

## See Also
<a name="API_FieldLevelEncryptionProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/FieldLevelEncryptionProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/FieldLevelEncryptionProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/FieldLevelEncryptionProfile)
