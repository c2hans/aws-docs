---
source_url: https://docs.aws.amazon.com/athena/latest/APIReference/API_Column.html
---

# Column
<a name="API_Column"></a>

Contains metadata for a column in a table.

## Contents
<a name="API_Column_Contents"></a>

 ** Name **   <a name="athena-Type-Column-Name"></a>
The name of the column.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** Comment **   <a name="athena-Type-Column-Comment"></a>
Optional information about the column.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** Type **   <a name="athena-Type-Column-Type"></a>
The data type of the column.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

## See Also
<a name="API_Column_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/athena-2017-05-18/Column)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/athena-2017-05-18/Column)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/athena-2017-05-18/Column)
