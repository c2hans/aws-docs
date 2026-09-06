---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_Column.html
---

# Column
<a name="API_Column"></a>

A column in a `Table`.

## Contents
<a name="API_Column_Contents"></a>

 ** Name **   <a name="Glue-Type-Column-Name"></a>
The name of the `Column`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** Comment **   <a name="Glue-Type-Column-Comment"></a>
A free-form text comment.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** Parameters **   <a name="Glue-Type-Column-Parameters"></a>
These key-value pairs define properties associated with the column.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Key Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Value Length Constraints: Maximum length of 512000.
Required: No

 ** Type **   <a name="Glue-Type-Column-Type"></a>
The data type of the `Column`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 131072.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

## See Also
<a name="API_Column_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/Column)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/Column)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/Column)
