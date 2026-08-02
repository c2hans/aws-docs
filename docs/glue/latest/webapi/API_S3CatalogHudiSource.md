---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_S3CatalogHudiSource.html
---

# S3CatalogHudiSource
<a name="API_S3CatalogHudiSource"></a>

Specifies a Hudi data source that is registered in the AWS Glue Data Catalog. The Hudi data source must be stored in Amazon S3.

## Contents
<a name="API_S3CatalogHudiSource_Contents"></a>

 ** Database **   <a name="Glue-Type-S3CatalogHudiSource-Database"></a>
The name of the database to read from.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: Yes

 ** Name **   <a name="Glue-Type-S3CatalogHudiSource-Name"></a>
The name of the Hudi data source.
Type: String
Pattern: `([^\r\n])*`
Required: Yes

 ** Table **   <a name="Glue-Type-S3CatalogHudiSource-Table"></a>
The name of the table in the database to read from.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: Yes

 ** AdditionalHudiOptions **   <a name="Glue-Type-S3CatalogHudiSource-AdditionalHudiOptions"></a>
Specifies additional connection options.
Type: String to string map
Key Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Value Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

 ** OutputSchemas **   <a name="Glue-Type-S3CatalogHudiSource-OutputSchemas"></a>
Specifies the data schema for the Hudi source.
Type: Array of [GlueSchema](API_GlueSchema.md) objects
Required: No

## See Also
<a name="API_S3CatalogHudiSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/S3CatalogHudiSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/S3CatalogHudiSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/S3CatalogHudiSource)
