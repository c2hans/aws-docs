---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_FieldLevelEncryptionProfileSummary.html
---

# FieldLevelEncryptionProfileSummary
<a name="API_FieldLevelEncryptionProfileSummary"></a>

The field-level encryption profile summary.

## Contents
<a name="API_FieldLevelEncryptionProfileSummary_Contents"></a>

 ** EncryptionEntities **   <a name="cloudfront-Type-FieldLevelEncryptionProfileSummary-EncryptionEntities"></a>
A complex data type of encryption entities for the field-level encryption profile that include the public key ID, provider, and field patterns for specifying which fields to encrypt with this key.
Type: [EncryptionEntities](API_EncryptionEntities.md) object
Required: Yes

 ** Id **   <a name="cloudfront-Type-FieldLevelEncryptionProfileSummary-Id"></a>
ID for the field-level encryption profile summary.
Type: String
Required: Yes

 ** LastModifiedTime **   <a name="cloudfront-Type-FieldLevelEncryptionProfileSummary-LastModifiedTime"></a>
The time when the field-level encryption profile summary was last updated.
Type: Timestamp
Required: Yes

 ** Name **   <a name="cloudfront-Type-FieldLevelEncryptionProfileSummary-Name"></a>
Name for the field-level encryption profile summary.
Type: String
Required: Yes

 ** Comment **   <a name="cloudfront-Type-FieldLevelEncryptionProfileSummary-Comment"></a>
An optional comment for the field-level encryption profile summary. The comment cannot be longer than 128 characters.
Type: String
Required: No

## See Also
<a name="API_FieldLevelEncryptionProfileSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/FieldLevelEncryptionProfileSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/FieldLevelEncryptionProfileSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/FieldLevelEncryptionProfileSummary)
