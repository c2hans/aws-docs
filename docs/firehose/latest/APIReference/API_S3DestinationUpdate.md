---
source_url: https://docs.aws.amazon.com/firehose/latest/APIReference/API_S3DestinationUpdate.html
---

# S3DestinationUpdate
<a name="API_S3DestinationUpdate"></a>

Describes an update for a destination in Amazon S3.

## Contents
<a name="API_S3DestinationUpdate_Contents"></a>

 ** BucketARN **   <a name="Firehose-Type-S3DestinationUpdate-BucketARN"></a>
The ARN of the S3 bucket. For more information, see [Amazon Resource Names (ARNs) and AWS Service Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:.*:s3:::[\w\.\-]{1,255}`
Required: No

 ** BufferingHints **   <a name="Firehose-Type-S3DestinationUpdate-BufferingHints"></a>
The buffering option. If no value is specified, `BufferingHints` object default values are used.
Type: [BufferingHints](API_BufferingHints.md) object
Required: No

 ** CloudWatchLoggingOptions **   <a name="Firehose-Type-S3DestinationUpdate-CloudWatchLoggingOptions"></a>
The CloudWatch logging options for your Firehose stream.
Type: [CloudWatchLoggingOptions](API_CloudWatchLoggingOptions.md) object
Required: No

 ** CompressionFormat **   <a name="Firehose-Type-S3DestinationUpdate-CompressionFormat"></a>
The compression format. If no value is specified, the default is `UNCOMPRESSED`.
The compression formats `SNAPPY` or `ZIP` cannot be specified for Amazon Redshift destinations because they are not supported by the Amazon Redshift `COPY` operation that reads from the S3 bucket.
Type: String
Valid Values: `UNCOMPRESSED | GZIP | ZIP | Snappy | HADOOP_SNAPPY`
Required: No

 ** EncryptionConfiguration **   <a name="Firehose-Type-S3DestinationUpdate-EncryptionConfiguration"></a>
The encryption configuration. If no value is specified, the default is no encryption.
Type: [EncryptionConfiguration](API_EncryptionConfiguration.md) object
Required: No

 ** ErrorOutputPrefix **   <a name="Firehose-Type-S3DestinationUpdate-ErrorOutputPrefix"></a>
A prefix that Firehose evaluates and adds to failed records before writing them to S3. This prefix appears immediately following the bucket name. For information about how to specify this prefix, see [Custom Prefixes for Amazon S3 Objects](https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*`
Required: No

 ** Prefix **   <a name="Firehose-Type-S3DestinationUpdate-Prefix"></a>
The "YYYY/MM/DD/HH" time format prefix is automatically used for delivered Amazon S3 files. You can also specify a custom prefix, as described in [Custom Prefixes for Amazon S3 Objects](https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*`
Required: No

 ** RoleARN **   <a name="Firehose-Type-S3DestinationUpdate-RoleARN"></a>
The Amazon Resource Name (ARN) of the AWS credentials. For more information, see [Amazon Resource Names (ARNs) and AWS Service Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `arn:.*:iam::\d{12}:role/[a-zA-Z_0-9+=,.@\-_/]+`
Required: No

## See Also
<a name="API_S3DestinationUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/firehose-2015-08-04/S3DestinationUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/firehose-2015-08-04/S3DestinationUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/firehose-2015-08-04/S3DestinationUpdate)
