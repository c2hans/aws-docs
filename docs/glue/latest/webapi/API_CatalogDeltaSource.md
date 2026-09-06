---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_CatalogDeltaSource.html
---

# CatalogDeltaSource
<a name="API_CatalogDeltaSource"></a>

Specifies a Delta Lake data source that is registered in the AWS Glue Data Catalog.

## Contents
<a name="API_CatalogDeltaSource_Contents"></a>

 ** Database **   <a name="Glue-Type-CatalogDeltaSource-Database"></a>
The name of the database to read from.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: Yes

 ** Name **   <a name="Glue-Type-CatalogDeltaSource-Name"></a>
The name of the Delta Lake data source.
Type: String
Pattern: `([^\r\n])*`
Required: Yes

 ** Table **   <a name="Glue-Type-CatalogDeltaSource-Table"></a>
The name of the table in the database to read from.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: Yes

 ** AdditionalDeltaOptions **   <a name="Glue-Type-CatalogDeltaSource-AdditionalDeltaOptions"></a>
Specifies additional connection options.
Type: String to string map
Key Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Value Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

 ** OutputSchemas **   <a name="Glue-Type-CatalogDeltaSource-OutputSchemas"></a>
Specifies the data schema for the Delta Lake source.
Type: Array of [GlueSchema](API_GlueSchema.md) objects
Required: No

## See Also
<a name="API_CatalogDeltaSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/CatalogDeltaSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/CatalogDeltaSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/CatalogDeltaSource)
