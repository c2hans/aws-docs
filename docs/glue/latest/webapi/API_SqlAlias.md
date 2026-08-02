---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_SqlAlias.html
---

# SqlAlias
<a name="API_SqlAlias"></a>

Represents a single entry in the list of values for `SqlAliases`.

## Contents
<a name="API_SqlAlias_Contents"></a>

 ** Alias **   <a name="Glue-Type-SqlAlias-Alias"></a>
A temporary name given to a table, or a column in a table.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: Yes

 ** From **   <a name="Glue-Type-SqlAlias-From"></a>
A table, or a column in a table.
Type: String
Pattern: `[A-Za-z0-9_-]*`
Required: Yes

## See Also
<a name="API_SqlAlias_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/SqlAlias)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/SqlAlias)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/SqlAlias)
