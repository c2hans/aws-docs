---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_Column.html
---

# Column
<a name="API_Column"></a>

A column within a schema relation, derived from the underlying table.

## Contents
<a name="API_Column_Contents"></a>

 ** name **   <a name="API-Type-Column-name"></a>
The name of the column.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `[a-z0-9_](([a-z0-9_ ]+-)*([a-z0-9_ ]+))?`
Required: Yes

 ** type **   <a name="API-Type-Column-type"></a>
The type of the column.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t]*`
Required: Yes

## See Also
<a name="API_Column_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/Column)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/Column)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/Column)
