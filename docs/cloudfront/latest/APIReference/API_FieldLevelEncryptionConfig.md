---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_FieldLevelEncryptionConfig.html
---

# FieldLevelEncryptionConfig
<a name="API_FieldLevelEncryptionConfig"></a>

A complex data type that includes the profile configurations specified for field-level encryption.

## Contents
<a name="API_FieldLevelEncryptionConfig_Contents"></a>

 ** CallerReference **   <a name="cloudfront-Type-FieldLevelEncryptionConfig-CallerReference"></a>
A unique number that ensures the request can't be replayed.
Type: String
Required: Yes

 ** Comment **   <a name="cloudfront-Type-FieldLevelEncryptionConfig-Comment"></a>
An optional comment about the configuration. The comment cannot be longer than 128 characters.
Type: String
Required: No

 ** ContentTypeProfileConfig **   <a name="cloudfront-Type-FieldLevelEncryptionConfig-ContentTypeProfileConfig"></a>
A complex data type that specifies when to forward content if a content type isn't recognized and profiles to use as by default in a request if a query argument doesn't specify a profile to use.
Type: [ContentTypeProfileConfig](API_ContentTypeProfileConfig.md) object
Required: No

 ** QueryArgProfileConfig **   <a name="cloudfront-Type-FieldLevelEncryptionConfig-QueryArgProfileConfig"></a>
A complex data type that specifies when to forward content if a profile isn't found and the profile that can be provided as a query argument in a request.
Type: [QueryArgProfileConfig](API_QueryArgProfileConfig.md) object
Required: No

## See Also
<a name="API_FieldLevelEncryptionConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/FieldLevelEncryptionConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/FieldLevelEncryptionConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/FieldLevelEncryptionConfig)
