---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_FieldLevelEncryptionList.html
---

# FieldLevelEncryptionList
<a name="API_FieldLevelEncryptionList"></a>

List of field-level encryption configurations.

## Contents
<a name="API_FieldLevelEncryptionList_Contents"></a>

 ** MaxItems **   <a name="cloudfront-Type-FieldLevelEncryptionList-MaxItems"></a>
The maximum number of elements you want in the response body.
Type: Integer
Required: Yes

 ** Quantity **   <a name="cloudfront-Type-FieldLevelEncryptionList-Quantity"></a>
The number of field-level encryption items.
Type: Integer
Required: Yes

 ** Items **   <a name="cloudfront-Type-FieldLevelEncryptionList-Items"></a>
An array of field-level encryption items.
Type: Array of [FieldLevelEncryptionSummary](API_FieldLevelEncryptionSummary.md) objects
Required: No

 ** NextMarker **   <a name="cloudfront-Type-FieldLevelEncryptionList-NextMarker"></a>
If there are more elements to be listed, this element is present and contains the value that you can use for the `Marker` request parameter to continue listing your configurations where you left off.
Type: String
Required: No

## See Also
<a name="API_FieldLevelEncryptionList_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/FieldLevelEncryptionList)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/FieldLevelEncryptionList)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/FieldLevelEncryptionList)
