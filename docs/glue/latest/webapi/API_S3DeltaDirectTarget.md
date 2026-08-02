---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_S3DeltaDirectTarget.html
---

# S3DeltaDirectTarget
<a name="API_S3DeltaDirectTarget"></a>

Specifies a target that writes to a Delta Lake data source in Amazon S3.

## Contents
<a name="API_S3DeltaDirectTarget_Contents"></a>

 ** Compression **   <a name="Glue-Type-S3DeltaDirectTarget-Compression"></a>
Specifies how the data is compressed. This is generally not necessary if the data has a standard file extension. Possible values are `"gzip"` and `"bzip"`).
Type: String
Valid Values: `uncompressed | snappy`
Required: Yes

 ** Format **   <a name="Glue-Type-S3DeltaDirectTarget-Format"></a>
Specifies the data output format for the target.
Type: String
Valid Values: `json | csv | avro | orc | parquet | hudi | delta | iceberg | hyper | xml`
Required: Yes

 ** Inputs **   <a name="Glue-Type-S3DeltaDirectTarget-Inputs"></a>
The nodes that are inputs to the data target.
Type: Array of strings
Array Members: Fixed number of 1 item.
Pattern: `[A-Za-z0-9_-]*`
Required: Yes

 ** Name **   <a name="Glue-Type-S3DeltaDirectTarget-Name"></a>
The name of the data target.
Type: String
Pattern: `([^\r\n])*`
Required: Yes

 ** Path **   <a name="Glue-Type-S3DeltaDirectTarget-Path"></a>
The Amazon S3 path of your Delta Lake data source to write to.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: Yes

 ** AdditionalOptions **   <a name="Glue-Type-S3DeltaDirectTarget-AdditionalOptions"></a>
Specifies additional connection options for the connector.
Type: String to string map
Key Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Value Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

 ** AutoDataQuality **   <a name="Glue-Type-S3DeltaDirectTarget-AutoDataQuality"></a>
Specifies whether to automatically enable data quality evaluation for the S3 Delta direct target. When set to `true`, data quality checks are performed automatically during the write operation.
Type: [AutoDataQuality](API_AutoDataQuality.md) object
Required: No

 ** NumberTargetPartitions **   <a name="Glue-Type-S3DeltaDirectTarget-NumberTargetPartitions"></a>
Specifies the number of target partitions for distributing Delta Lake dataset files across Amazon S3.
Type: String
Required: No

 ** PartitionKeys **   <a name="Glue-Type-S3DeltaDirectTarget-PartitionKeys"></a>
Specifies native partitioning using a sequence of keys.
Type: Array of arrays of strings
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

 ** SchemaChangePolicy **   <a name="Glue-Type-S3DeltaDirectTarget-SchemaChangePolicy"></a>
A policy that specifies update behavior for the crawler.
Type: [DirectSchemaChangePolicy](API_DirectSchemaChangePolicy.md) object
Required: No

## See Also
<a name="API_S3DeltaDirectTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/S3DeltaDirectTarget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/S3DeltaDirectTarget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/S3DeltaDirectTarget)
