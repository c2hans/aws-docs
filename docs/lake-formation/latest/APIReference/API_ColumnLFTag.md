---
source_url: https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_ColumnLFTag.html
---

# ColumnLFTag
<a name="API_ColumnLFTag"></a>

A structure containing the name of a column resource and the LF-tags attached to it.

## Contents
<a name="API_ColumnLFTag_Contents"></a>

 ** LFTags **   <a name="lakeformation-Type-ColumnLFTag-LFTags"></a>
The LF-tags attached to a column resource.
Type: Array of [LFTagPair](API_LFTagPair.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: No

 ** Name **   <a name="lakeformation-Type-ColumnLFTag-Name"></a>
The name of a column resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

## See Also
<a name="API_ColumnLFTag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lakeformation-2017-03-31/ColumnLFTag)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lakeformation-2017-03-31/ColumnLFTag)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lakeformation-2017-03-31/ColumnLFTag)
