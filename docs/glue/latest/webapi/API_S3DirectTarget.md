---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_S3DirectTarget.html
---

# S3DirectTarget
<a name="API_S3DirectTarget"></a>

Specifies a data target that writes to Amazon S3.

## Contents
<a name="API_S3DirectTarget_Contents"></a>

 ** Format **   <a name="Glue-Type-S3DirectTarget-Format"></a>
Specifies the data output format for the target.
Type: String
Valid Values: `json | csv | avro | orc | parquet | hudi | delta | iceberg | hyper | xml`
Required: Yes

 ** Inputs **   <a name="Glue-Type-S3DirectTarget-Inputs"></a>
The nodes that are inputs to the data target.
Type: Array of strings
Array Members: Fixed number of 1 item.
Pattern: `[A-Za-z0-9_-]*`
Required: Yes

 ** Name **   <a name="Glue-Type-S3DirectTarget-Name"></a>
The name of the data target.
Type: String
Pattern: `([^\r\n])*`
Required: Yes

 ** Path **   <a name="Glue-Type-S3DirectTarget-Path"></a>
A single Amazon S3 path to write to.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: Yes

 ** AutoDataQuality **   <a name="Glue-Type-S3DirectTarget-AutoDataQuality"></a>
Specifies whether to automatically enable data quality evaluation for the S3 direct target. When set to `true`, data quality checks are performed automatically during the write operation.
Type: [AutoDataQuality](API_AutoDataQuality.md) object
Required: No

 ** Compression **   <a name="Glue-Type-S3DirectTarget-Compression"></a>
Specifies how the data is compressed. This is generally not necessary if the data has a standard file extension. Possible values are `"gzip"` and `"bzip"`).
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

 ** NumberTargetPartitions **   <a name="Glue-Type-S3DirectTarget-NumberTargetPartitions"></a>
Specifies the number of target partitions when writing data directly to Amazon S3.
Type: String
Required: No

 ** OutputSchemas **   <a name="Glue-Type-S3DirectTarget-OutputSchemas"></a>
Specifies the data schema for the S3 direct target.
Type: Array of [GlueSchema](API_GlueSchema.md) objects
Required: No

 ** PartitionKeys **   <a name="Glue-Type-S3DirectTarget-PartitionKeys"></a>
Specifies native partitioning using a sequence of keys.
Type: Array of arrays of strings
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

 ** SchemaChangePolicy **   <a name="Glue-Type-S3DirectTarget-SchemaChangePolicy"></a>
A policy that specifies update behavior for the crawler.
Type: [DirectSchemaChangePolicy](API_DirectSchemaChangePolicy.md) object
Required: No

## See Also
<a name="API_S3DirectTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/S3DirectTarget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/S3DirectTarget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/S3DirectTarget)
