---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_MigrationTableProperties.html
---

# MigrationTableProperties
<a name="API_s3Buckets_MigrationTableProperties"></a>

The properties of the data files that a migration writes. The migration also sets the compression codec and dictionary encoding as the destination table's write properties, so they remain the table's defaults after you complete the migration.

## Contents
<a name="API_s3Buckets_MigrationTableProperties_Contents"></a>

 ** compressionCodec **   <a name="AmazonS3-Type-s3Buckets_MigrationTableProperties-compressionCodec"></a>
The compression codec of the data files. The default is `zstd`.
Type: String
Valid Values: `zstd | snappy | gzip | uncompressed`
Required: No

 ** dictionaryEncoding **   <a name="AmazonS3-Type-s3Buckets_MigrationTableProperties-dictionaryEncoding"></a>
Specifies whether the data files use dictionary encoding. The default is `true`.
Type: Boolean
Required: No

 ** icebergFormatVersion **   <a name="AmazonS3-Type-s3Buckets_MigrationTableProperties-icebergFormatVersion"></a>
The Iceberg format version of the destination table. Valid values are `2` and `3`. The default is `2`.
Type: Integer
Required: No

 ** writeFormat **   <a name="AmazonS3-Type-s3Buckets_MigrationTableProperties-writeFormat"></a>
The file format of the data files. The only supported format is `parquet`, the default.
Type: String
Valid Values: `parquet`
Required: No

## See Also
<a name="API_s3Buckets_MigrationTableProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/MigrationTableProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/MigrationTableProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/MigrationTableProperties)
