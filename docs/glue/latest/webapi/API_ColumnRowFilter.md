---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_ColumnRowFilter.html
---

# ColumnRowFilter
<a name="API_ColumnRowFilter"></a>

A filter that uses both column-level and row-level filtering.

## Contents
<a name="API_ColumnRowFilter_Contents"></a>

 ** ColumnName **   <a name="Glue-Type-ColumnRowFilter-ColumnName"></a>
A string containing the name of the column.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** RowFilterExpression **   <a name="Glue-Type-ColumnRowFilter-RowFilterExpression"></a>
A string containing the row-level filter expression.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

## See Also
<a name="API_ColumnRowFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/ColumnRowFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/ColumnRowFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/ColumnRowFilter)
