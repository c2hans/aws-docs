---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_S3CatalogTarget.html
---

# S3CatalogTarget
<a name="API_S3CatalogTarget"></a>

Specifies a data target that writes to Amazon S3 using the AWS Glue Data Catalog.

## Contents
<a name="API_S3CatalogTarget_Contents"></a>

 ** Database **   <a name="Glue-Type-S3CatalogTarget-Database"></a>
The name of the database to write to.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: Yes

 ** Inputs **   <a name="Glue-Type-S3CatalogTarget-Inputs"></a>
The nodes that are inputs to the data target.
Type: Array of strings
Array Members: Fixed number of 1 item.
Pattern: `[A-Za-z0-9_-]*`
Required: Yes

 ** Name **   <a name="Glue-Type-S3CatalogTarget-Name"></a>
The name of the data target.
Type: String
Pattern: `([^\r\n])*`
Required: Yes

 ** Table **   <a name="Glue-Type-S3CatalogTarget-Table"></a>
The name of the table in the database to write to.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: Yes

 ** AutoDataQuality **   <a name="Glue-Type-S3CatalogTarget-AutoDataQuality"></a>
Specifies whether to automatically enable data quality evaluation for the S3 catalog target. When set to `true`, data quality checks are performed automatically during the write operation.
Type: [AutoDataQuality](API_AutoDataQuality.md) object
Required: No

 ** PartitionKeys **   <a name="Glue-Type-S3CatalogTarget-PartitionKeys"></a>
Specifies native partitioning using a sequence of keys.
Type: Array of arrays of strings
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

 ** SchemaChangePolicy **   <a name="Glue-Type-S3CatalogTarget-SchemaChangePolicy"></a>
A policy that specifies update behavior for the crawler.
Type: [CatalogSchemaChangePolicy](API_CatalogSchemaChangePolicy.md) object
Required: No

## See Also
<a name="API_S3CatalogTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/S3CatalogTarget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/S3CatalogTarget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/S3CatalogTarget)
