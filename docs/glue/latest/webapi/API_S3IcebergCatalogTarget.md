---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_S3IcebergCatalogTarget.html
---

# S3IcebergCatalogTarget
<a name="API_S3IcebergCatalogTarget"></a>

Specifies an Apache Iceberg catalog target that writes data to Amazon S3 and registers the table in the AWS Glue Data Catalog.

## Contents
<a name="API_S3IcebergCatalogTarget_Contents"></a>

 ** Database **   <a name="Glue-Type-S3IcebergCatalogTarget-Database"></a>
The name of the database to write to.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: Yes

 ** Inputs **   <a name="Glue-Type-S3IcebergCatalogTarget-Inputs"></a>
The input connection for the Iceberg catalog target.
Type: Array of strings
Array Members: Fixed number of 1 item.
Pattern: `[A-Za-z0-9_-]*`
Required: Yes

 ** Name **   <a name="Glue-Type-S3IcebergCatalogTarget-Name"></a>
The name of the Iceberg catalog target.
Type: String
Pattern: `([^\r\n])*`
Required: Yes

 ** Table **   <a name="Glue-Type-S3IcebergCatalogTarget-Table"></a>
The name of the table to write to in the catalog.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: Yes

 ** AdditionalOptions **   <a name="Glue-Type-S3IcebergCatalogTarget-AdditionalOptions"></a>
Specifies additional connection options for the Iceberg catalog target.
Type: String to string map
Key Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Value Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

 ** AutoDataQuality **   <a name="Glue-Type-S3IcebergCatalogTarget-AutoDataQuality"></a>
Specifies whether to automatically enable data quality evaluation for the S3 Iceberg catalog target. When set to `true`, data quality checks are performed automatically during the write operation.
Type: [AutoDataQuality](API_AutoDataQuality.md) object
Required: No

 ** PartitionKeys **   <a name="Glue-Type-S3IcebergCatalogTarget-PartitionKeys"></a>
A list of partition keys for the Iceberg table.
Type: Array of arrays of strings
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

 ** SchemaChangePolicy **   <a name="Glue-Type-S3IcebergCatalogTarget-SchemaChangePolicy"></a>
The policy for handling schema changes in the catalog target.
Type: [CatalogSchemaChangePolicy](API_CatalogSchemaChangePolicy.md) object
Required: No

## See Also
<a name="API_S3IcebergCatalogTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/S3IcebergCatalogTarget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/S3IcebergCatalogTarget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/S3IcebergCatalogTarget)
