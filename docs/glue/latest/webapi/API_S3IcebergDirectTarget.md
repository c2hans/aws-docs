---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_S3IcebergDirectTarget.html
---

# S3IcebergDirectTarget
<a name="API_S3IcebergDirectTarget"></a>

Specifies a target that writes to an Iceberg data source in Amazon S3.

## Contents
<a name="API_S3IcebergDirectTarget_Contents"></a>

 ** Compression **   <a name="Glue-Type-S3IcebergDirectTarget-Compression"></a>
Specifies the compression codec used for Iceberg table files in S3.
Type: String
Valid Values: `gzip | lzo | uncompressed | snappy`
Required: Yes

 ** Format **   <a name="Glue-Type-S3IcebergDirectTarget-Format"></a>
Specifies the file format used for storing Iceberg table data (e.g., Parquet, ORC).
Type: String
Valid Values: `json | csv | avro | orc | parquet | hudi | delta | iceberg | hyper | xml`
Required: Yes

 ** Inputs **   <a name="Glue-Type-S3IcebergDirectTarget-Inputs"></a>
Defines the single input source that provides data to this Iceberg target.
Type: Array of strings
Array Members: Fixed number of 1 item.
Pattern: `[A-Za-z0-9_-]*`
Required: Yes

 ** Name **   <a name="Glue-Type-S3IcebergDirectTarget-Name"></a>
Specifies the unique identifier for the Iceberg target node in your data pipeline.
Type: String
Pattern: `([^\r\n])*`
Required: Yes

 ** Path **   <a name="Glue-Type-S3IcebergDirectTarget-Path"></a>
Defines the S3 location where the Iceberg table data will be stored.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: Yes

 ** AdditionalOptions **   <a name="Glue-Type-S3IcebergDirectTarget-AdditionalOptions"></a>
Provides additional configuration options for customizing the Iceberg table behavior.
Type: String to string map
Key Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Value Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

 ** AutoDataQuality **   <a name="Glue-Type-S3IcebergDirectTarget-AutoDataQuality"></a>
Specifies configuration options for automatic data quality evaluation in AWS Glue jobs. This structure enables automated data quality checks and monitoring during ETL operations, helping to ensure data integrity and reliability without manual intervention.
Type: [AutoDataQuality](API_AutoDataQuality.md) object
Required: No

 ** NumberTargetPartitions **   <a name="Glue-Type-S3IcebergDirectTarget-NumberTargetPartitions"></a>
Sets the number of target partitions for distributing Iceberg table files across S3.
Type: String
Required: No

 ** OutputSchemas **   <a name="Glue-Type-S3IcebergDirectTarget-OutputSchemas"></a>
Specifies the data schema for the S3 Iceberg direct target.
Type: Array of [GlueSchema](API_GlueSchema.md) objects
Required: No

 ** PartitionKeys **   <a name="Glue-Type-S3IcebergDirectTarget-PartitionKeys"></a>
Specifies the columns used to partition the Iceberg table data in S3.
Type: Array of arrays of strings
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

 ** SchemaChangePolicy **   <a name="Glue-Type-S3IcebergDirectTarget-SchemaChangePolicy"></a>
Defines how schema changes are handled when writing data to the Iceberg table.
Type: [DirectSchemaChangePolicy](API_DirectSchemaChangePolicy.md) object
Required: No

## See Also
<a name="API_S3IcebergDirectTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/S3IcebergDirectTarget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/S3IcebergDirectTarget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/S3IcebergDirectTarget)
