---
source_url: https://docs.aws.amazon.com/kinesis/latest/APIReference/API_S3TablesConfiguration.html
---

# S3TablesConfiguration
<a name="API_S3TablesConfiguration"></a>

Specifies a destination streaming table on Apache Iceberg.

## Contents
<a name="API_S3TablesConfiguration_Contents"></a>

 ** CompressionType **   <a name="Streams-Type-S3TablesConfiguration-CompressionType"></a>
The compression applied to Parquet data files. Valid values:
+  `NONE` - No compression.
+  `ZSTD` - Zstandard compression.
+  `SNAPPY` - Snappy compression.
Type: String
Valid Values: `NONE | ZSTD | SNAPPY`
Required: Yes

 ** Namespace **   <a name="Streams-Type-S3TablesConfiguration-Namespace"></a>
The namespace (database) of the destination table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[0-9a-z_]+`
Required: Yes

 ** TableBucketARN **   <a name="Streams-Type-S3TablesConfiguration-TableBucketARN"></a>
The Amazon Resource Name (ARN) of the Amazon S3 table bucket.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws[-a-z0-9]*:s3tables:[-a-z0-9]+:\d{12}:bucket/[a-z0-9_-]{3,63}`
Required: Yes

 ** TableName **   <a name="Streams-Type-S3TablesConfiguration-TableName"></a>
The name of the destination table. Amazon Kinesis Data Streams creates this table in the specified table bucket.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[0-9a-z_]+`
Required: Yes

 ** PartitionSpec **   <a name="Streams-Type-S3TablesConfiguration-PartitionSpec"></a>
The partitioning specification for the destination table.
Type: [PartitionSpec](API_PartitionSpec.md) object
Required: No

## See Also
<a name="API_S3TablesConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesis-2013-12-02/S3TablesConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesis-2013-12-02/S3TablesConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesis-2013-12-02/S3TablesConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kinesis Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kinesis` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
