---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_FieldLevelEncryptionProfileList.html
---

# FieldLevelEncryptionProfileList
<a name="API_FieldLevelEncryptionProfileList"></a>

List of field-level encryption profiles.

## Contents
<a name="API_FieldLevelEncryptionProfileList_Contents"></a>

 ** MaxItems **   <a name="cloudfront-Type-FieldLevelEncryptionProfileList-MaxItems"></a>
The maximum number of field-level encryption profiles you want in the response body.
Type: Integer
Required: Yes

 ** Quantity **   <a name="cloudfront-Type-FieldLevelEncryptionProfileList-Quantity"></a>
The number of field-level encryption profiles.
Type: Integer
Required: Yes

 ** Items **   <a name="cloudfront-Type-FieldLevelEncryptionProfileList-Items"></a>
The field-level encryption profile items.
Type: Array of [FieldLevelEncryptionProfileSummary](API_FieldLevelEncryptionProfileSummary.md) objects
Required: No

 ** NextMarker **   <a name="cloudfront-Type-FieldLevelEncryptionProfileList-NextMarker"></a>
If there are more elements to be listed, this element is present and contains the value that you can use for the `Marker` request parameter to continue listing your profiles where you left off.
Type: String
Required: No

## See Also
<a name="API_FieldLevelEncryptionProfileList_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/FieldLevelEncryptionProfileList)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/FieldLevelEncryptionProfileList)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/FieldLevelEncryptionProfileList)
