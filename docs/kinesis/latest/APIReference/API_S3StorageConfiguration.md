---
source_url: https://docs.aws.amazon.com/kinesis/latest/APIReference/API_S3StorageConfiguration.html
---

# S3StorageConfiguration
<a name="API_S3StorageConfiguration"></a>

The Amazon S3 storage settings for a general purpose Amazon S3 destination.

## Contents
<a name="API_S3StorageConfiguration_Contents"></a>

 ** BucketARN **   <a name="Streams-Type-S3StorageConfiguration-BucketARN"></a>
The Amazon Resource Name (ARN) of the destination Amazon S3 bucket.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws[-a-z0-9]*:s3:::[a-z0-9._-]{3,63}`
Required: Yes

 ** CompressionType **   <a name="Streams-Type-S3StorageConfiguration-CompressionType"></a>
The compression applied to delivered objects. Valid values:
+  `NONE` - No compression.
+  `GZIP` - gzip compression.
+  `ZSTD` - Zstandard compression.
Type: String
Valid Values: `NONE | GZIP | ZSTD`
Required: Yes

 ** ExpectedBucketOwner **   <a name="Streams-Type-S3StorageConfiguration-ExpectedBucketOwner"></a>
The AWS account ID of the expected owner of the destination bucket. This value helps prevent delivery to an unintended bucket if ownership changes.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: Yes

 ** OutputKeyTemplate **   <a name="Streams-Type-S3StorageConfiguration-OutputKeyTemplate"></a>
The template used to construct the Amazon S3 object key for delivered objects. If not specified, a default template is used.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[0-9A-Za-z!\-_'.*()\/=:{}]+`
Required: No

 ** StorageClass **   <a name="Streams-Type-S3StorageConfiguration-StorageClass"></a>
The Amazon S3 storage class for delivered objects. Valid values:
+  `STANDARD` - The default storage class, for frequently accessed data.
+  `INTELLIGENT_TIERING` - Automatically moves objects to the most cost-effective access tier based on usage patterns.
+  `GLACIER_IR` - Low-cost storage for rarely accessed data that requires millisecond retrieval.
Type: String
Valid Values: `STANDARD | INTELLIGENT_TIERING | GLACIER_IR`
Required: No

## See Also
<a name="API_S3StorageConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesis-2013-12-02/S3StorageConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesis-2013-12-02/S3StorageConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesis-2013-12-02/S3StorageConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kinesis Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kinesis` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
