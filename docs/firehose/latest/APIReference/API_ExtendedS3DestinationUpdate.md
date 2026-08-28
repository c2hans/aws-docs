---
source_url: https://docs.aws.amazon.com/firehose/latest/APIReference/API_ExtendedS3DestinationUpdate.html
---

# ExtendedS3DestinationUpdate
<a name="API_ExtendedS3DestinationUpdate"></a>

Describes an update for a destination in Amazon S3.

## Contents
<a name="API_ExtendedS3DestinationUpdate_Contents"></a>

 ** BucketARN **   <a name="Firehose-Type-ExtendedS3DestinationUpdate-BucketARN"></a>
The ARN of the S3 bucket. For more information, see [Amazon Resource Names (ARNs) and AWS Service Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:.*:s3:::[\w\.\-]{1,255}`
Required: No

 ** BufferingHints **   <a name="Firehose-Type-ExtendedS3DestinationUpdate-BufferingHints"></a>
The buffering option.
Type: [BufferingHints](API_BufferingHints.md) object
Required: No

 ** CloudWatchLoggingOptions **   <a name="Firehose-Type-ExtendedS3DestinationUpdate-CloudWatchLoggingOptions"></a>
The Amazon CloudWatch logging options for your Firehose stream.
Type: [CloudWatchLoggingOptions](API_CloudWatchLoggingOptions.md) object
Required: No

 ** CompressionFormat **   <a name="Firehose-Type-ExtendedS3DestinationUpdate-CompressionFormat"></a>
The compression format. If no value is specified, the default is `UNCOMPRESSED`.
Type: String
Valid Values: `UNCOMPRESSED | GZIP | ZIP | Snappy | HADOOP_SNAPPY`
Required: No

 ** CustomTimeZone **   <a name="Firehose-Type-ExtendedS3DestinationUpdate-CustomTimeZone"></a>
The time zone you prefer. UTC is the default.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `^$|[a-zA-Z/_]+`
Required: No

 ** DataFormatConversionConfiguration **   <a name="Firehose-Type-ExtendedS3DestinationUpdate-DataFormatConversionConfiguration"></a>
The serializer, deserializer, and schema for converting data from the JSON format to the Parquet or ORC format before writing it to Amazon S3.
Type: [DataFormatConversionConfiguration](API_DataFormatConversionConfiguration.md) object
Required: No

 ** DynamicPartitioningConfiguration **   <a name="Firehose-Type-ExtendedS3DestinationUpdate-DynamicPartitioningConfiguration"></a>
The configuration of the dynamic partitioning mechanism that creates smaller data sets from the streaming data by partitioning it based on partition keys. Currently, dynamic partitioning is only supported for Amazon S3 destinations.
Type: [DynamicPartitioningConfiguration](API_DynamicPartitioningConfiguration.md) object
Required: No

 ** EncryptionConfiguration **   <a name="Firehose-Type-ExtendedS3DestinationUpdate-EncryptionConfiguration"></a>
The encryption configuration. If no value is specified, the default is no encryption.
Type: [EncryptionConfiguration](API_EncryptionConfiguration.md) object
Required: No

 ** ErrorOutputPrefix **   <a name="Firehose-Type-ExtendedS3DestinationUpdate-ErrorOutputPrefix"></a>
A prefix that Firehose evaluates and adds to failed records before writing them to S3. This prefix appears immediately following the bucket name. For information about how to specify this prefix, see [Custom Prefixes for Amazon S3 Objects](https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*`
Required: No

 ** FileExtension **   <a name="Firehose-Type-ExtendedS3DestinationUpdate-FileExtension"></a>
Specify a file extension. It will override the default file extension
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `^$|\.[0-9a-z!\-_.*'()]+`
Required: No

 ** Prefix **   <a name="Firehose-Type-ExtendedS3DestinationUpdate-Prefix"></a>
The "YYYY/MM/DD/HH" time format prefix is automatically used for delivered Amazon S3 files. You can also specify a custom prefix, as described in [Custom Prefixes for Amazon S3 Objects](https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*`
Required: No

 ** ProcessingConfiguration **   <a name="Firehose-Type-ExtendedS3DestinationUpdate-ProcessingConfiguration"></a>
The data processing configuration.
Type: [ProcessingConfiguration](API_ProcessingConfiguration.md) object
Required: No

 ** RoleARN **   <a name="Firehose-Type-ExtendedS3DestinationUpdate-RoleARN"></a>
The Amazon Resource Name (ARN) of the AWS credentials. For more information, see [Amazon Resource Names (ARNs) and AWS Service Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `arn:.*:iam::\d{12}:role/[a-zA-Z_0-9+=,.@\-_/]+`
Required: No

 ** S3BackupMode **   <a name="Firehose-Type-ExtendedS3DestinationUpdate-S3BackupMode"></a>
You can update a Firehose stream to enable Amazon S3 backup if it is disabled. If backup is enabled, you can't update the Firehose stream to disable it.
Type: String
Valid Values: `Disabled | Enabled`
Required: No

 ** S3BackupUpdate **   <a name="Firehose-Type-ExtendedS3DestinationUpdate-S3BackupUpdate"></a>
The Amazon S3 destination for backup.
Type: [S3DestinationUpdate](API_S3DestinationUpdate.md) object
Required: No

## See Also
<a name="API_ExtendedS3DestinationUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/firehose-2015-08-04/ExtendedS3DestinationUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/firehose-2015-08-04/ExtendedS3DestinationUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/firehose-2015-08-04/ExtendedS3DestinationUpdate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Data Firehose. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query firehose` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
