---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_RecordTag.html
---

# RecordTag
<a name="API_RecordTag"></a>

Information about a tag, which is a key-value pair.

## Contents
<a name="API_RecordTag_Contents"></a>

 ** Key **   <a name="servicecatalog-Type-RecordTag-Key"></a>
The key for this tag.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-%@]*)$`
Required: No

 ** Value **   <a name="servicecatalog-Type-RecordTag-Value"></a>
The value for this tag.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-%@]*)$`
Required: No

## See Also
<a name="API_RecordTag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/RecordTag)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/RecordTag)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/RecordTag)
