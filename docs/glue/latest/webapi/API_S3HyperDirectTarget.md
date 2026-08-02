---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_S3HyperDirectTarget.html
---

# S3HyperDirectTarget
<a name="API_S3HyperDirectTarget"></a>

Specifies a HyperDirect data target that writes to Amazon S3.

## Contents
<a name="API_S3HyperDirectTarget_Contents"></a>

 ** Inputs **   <a name="Glue-Type-S3HyperDirectTarget-Inputs"></a>
Specifies the input source for the HyperDirect target.
Type: Array of strings
Array Members: Fixed number of 1 item.
Pattern: `[A-Za-z0-9_-]*`
Required: Yes

 ** Name **   <a name="Glue-Type-S3HyperDirectTarget-Name"></a>
The unique identifier for the HyperDirect target node.
Type: String
Pattern: `([^\r\n])*`
Required: Yes

 ** Path **   <a name="Glue-Type-S3HyperDirectTarget-Path"></a>
The S3 location where the output data will be written.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: Yes

 ** AutoDataQuality **   <a name="Glue-Type-S3HyperDirectTarget-AutoDataQuality"></a>
Specifies whether to automatically enable data quality evaluation for the S3 Hyper direct target. When set to `true`, data quality checks are performed automatically during the write operation.
Type: [AutoDataQuality](API_AutoDataQuality.md) object
Required: No

 ** Compression **   <a name="Glue-Type-S3HyperDirectTarget-Compression"></a>
The compression type to apply to the output data.
Type: String
Valid Values: `uncompressed`
Required: No

 ** Format **   <a name="Glue-Type-S3HyperDirectTarget-Format"></a>
Specifies the data output format for the HyperDirect target.
Type: String
Valid Values: `json | csv | avro | orc | parquet | hudi | delta | iceberg | hyper | xml`
Required: No

 ** OutputSchemas **   <a name="Glue-Type-S3HyperDirectTarget-OutputSchemas"></a>
Specifies the data schema for the S3 Hyper direct target.
Type: Array of [GlueSchema](API_GlueSchema.md) objects
Required: No

 ** PartitionKeys **   <a name="Glue-Type-S3HyperDirectTarget-PartitionKeys"></a>
Defines the partitioning strategy for the output data.
Type: Array of arrays of strings
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

 ** SchemaChangePolicy **   <a name="Glue-Type-S3HyperDirectTarget-SchemaChangePolicy"></a>
Defines how schema changes are handled during write operations.
Type: [DirectSchemaChangePolicy](API_DirectSchemaChangePolicy.md) object
Required: No

## See Also
<a name="API_S3HyperDirectTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/S3HyperDirectTarget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/S3HyperDirectTarget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/S3HyperDirectTarget)
