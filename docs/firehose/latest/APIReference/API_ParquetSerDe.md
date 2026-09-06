---
source_url: https://docs.aws.amazon.com/firehose/latest/APIReference/API_ParquetSerDe.html
---

# ParquetSerDe
<a name="API_ParquetSerDe"></a>

A serializer to use for converting data to the Parquet format before storing it in Amazon S3. For more information, see [Apache Parquet](https://parquet.apache.org/docs/).

## Contents
<a name="API_ParquetSerDe_Contents"></a>

 ** BlockSizeBytes **   <a name="Firehose-Type-ParquetSerDe-BlockSizeBytes"></a>
The Hadoop Distributed File System (HDFS) block size. This is useful if you intend to copy the data from Amazon S3 to HDFS before querying. The default is 256 MiB and the minimum is 64 MiB. Firehose uses this value for padding calculations.
Type: Integer
Valid Range: Minimum value of 67108864.
Required: No

 ** Compression **   <a name="Firehose-Type-ParquetSerDe-Compression"></a>
The compression code to use over data blocks. The possible values are `UNCOMPRESSED`, `SNAPPY`, and `GZIP`, with the default being `SNAPPY`. Use `SNAPPY` for higher decompression speed. Use `GZIP` if the compression ratio is more important than speed.
Type: String
Valid Values: `UNCOMPRESSED | GZIP | SNAPPY`
Required: No

 ** EnableDictionaryCompression **   <a name="Firehose-Type-ParquetSerDe-EnableDictionaryCompression"></a>
Indicates whether to enable dictionary compression.
Type: Boolean
Required: No

 ** MaxPaddingBytes **   <a name="Firehose-Type-ParquetSerDe-MaxPaddingBytes"></a>
The maximum amount of padding to apply. This is useful if you intend to copy the data from Amazon S3 to HDFS before querying. The default is 0.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** PageSizeBytes **   <a name="Firehose-Type-ParquetSerDe-PageSizeBytes"></a>
The Parquet page size. Column chunks are divided into pages. A page is conceptually an indivisible unit (in terms of compression and encoding). The minimum value is 64 KiB and the default is 1 MiB.
Type: Integer
Valid Range: Minimum value of 65536.
Required: No

 ** WriterVersion **   <a name="Firehose-Type-ParquetSerDe-WriterVersion"></a>
Indicates the version of row format to output. The possible values are `V1` and `V2`. The default is `V1`.
Type: String
Valid Values: `V1 | V2`
Required: No

## See Also
<a name="API_ParquetSerDe_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/firehose-2015-08-04/ParquetSerDe)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/firehose-2015-08-04/ParquetSerDe)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/firehose-2015-08-04/ParquetSerDe)
