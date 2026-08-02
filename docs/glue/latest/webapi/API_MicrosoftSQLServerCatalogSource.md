---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_MicrosoftSQLServerCatalogSource.html
---

# MicrosoftSQLServerCatalogSource
<a name="API_MicrosoftSQLServerCatalogSource"></a>

Specifies a Microsoft SQL server data source in the AWS Glue Data Catalog.

## Contents
<a name="API_MicrosoftSQLServerCatalogSource_Contents"></a>

 ** Database **   <a name="Glue-Type-MicrosoftSQLServerCatalogSource-Database"></a>
The name of the database to read from.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: Yes

 ** Name **   <a name="Glue-Type-MicrosoftSQLServerCatalogSource-Name"></a>
The name of the data source.
Type: String
Pattern: `([^\r\n])*`
Required: Yes

 ** Table **   <a name="Glue-Type-MicrosoftSQLServerCatalogSource-Table"></a>
The name of the table in the database to read from.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: Yes

## See Also
<a name="API_MicrosoftSQLServerCatalogSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/MicrosoftSQLServerCatalogSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/MicrosoftSQLServerCatalogSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/MicrosoftSQLServerCatalogSource)
