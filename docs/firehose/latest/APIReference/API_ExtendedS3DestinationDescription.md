---
source_url: https://docs.aws.amazon.com/firehose/latest/APIReference/API_ExtendedS3DestinationDescription.html
---

# ExtendedS3DestinationDescription
<a name="API_ExtendedS3DestinationDescription"></a>

Describes a destination in Amazon S3.

## Contents
<a name="API_ExtendedS3DestinationDescription_Contents"></a>

 ** BucketARN **   <a name="Firehose-Type-ExtendedS3DestinationDescription-BucketARN"></a>
The ARN of the S3 bucket. For more information, see [Amazon Resource Names (ARNs) and AWS Service Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:.*:s3:::[\w\.\-]{1,255}`
Required: Yes

 ** BufferingHints **   <a name="Firehose-Type-ExtendedS3DestinationDescription-BufferingHints"></a>
The buffering option.
Type: [BufferingHints](API_BufferingHints.md) object
Required: Yes

 ** CompressionFormat **   <a name="Firehose-Type-ExtendedS3DestinationDescription-CompressionFormat"></a>
The compression format. If no value is specified, the default is `UNCOMPRESSED`.
Type: String
Valid Values: `UNCOMPRESSED | GZIP | ZIP | Snappy | HADOOP_SNAPPY`
Required: Yes

 ** EncryptionConfiguration **   <a name="Firehose-Type-ExtendedS3DestinationDescription-EncryptionConfiguration"></a>
The encryption configuration. If no value is specified, the default is no encryption.
Type: [EncryptionConfiguration](API_EncryptionConfiguration.md) object
Required: Yes

 ** RoleARN **   <a name="Firehose-Type-ExtendedS3DestinationDescription-RoleARN"></a>
The Amazon Resource Name (ARN) of the AWS credentials. For more information, see [Amazon Resource Names (ARNs) and AWS Service Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `arn:.*:iam::\d{12}:role/[a-zA-Z_0-9+=,.@\-_/]+`
Required: Yes

 ** CloudWatchLoggingOptions **   <a name="Firehose-Type-ExtendedS3DestinationDescription-CloudWatchLoggingOptions"></a>
The Amazon CloudWatch logging options for your Firehose stream.
Type: [CloudWatchLoggingOptions](API_CloudWatchLoggingOptions.md) object
Required: No

 ** CustomTimeZone **   <a name="Firehose-Type-ExtendedS3DestinationDescription-CustomTimeZone"></a>
The time zone you prefer. UTC is the default.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `^$|[a-zA-Z/_]+`
Required: No

 ** DataFormatConversionConfiguration **   <a name="Firehose-Type-ExtendedS3DestinationDescription-DataFormatConversionConfiguration"></a>
The serializer, deserializer, and schema for converting data from the JSON format to the Parquet or ORC format before writing it to Amazon S3.
Type: [DataFormatConversionConfiguration](API_DataFormatConversionConfiguration.md) object
Required: No

 ** DynamicPartitioningConfiguration **   <a name="Firehose-Type-ExtendedS3DestinationDescription-DynamicPartitioningConfiguration"></a>
The configuration of the dynamic partitioning mechanism that creates smaller data sets from the streaming data by partitioning it based on partition keys. Currently, dynamic partitioning is only supported for Amazon S3 destinations.
Type: [DynamicPartitioningConfiguration](API_DynamicPartitioningConfiguration.md) object
Required: No

 ** ErrorOutputPrefix **   <a name="Firehose-Type-ExtendedS3DestinationDescription-ErrorOutputPrefix"></a>
A prefix that Firehose evaluates and adds to failed records before writing them to S3. This prefix appears immediately following the bucket name. For information about how to specify this prefix, see [Custom Prefixes for Amazon S3 Objects](https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*`
Required: No

 ** FileExtension **   <a name="Firehose-Type-ExtendedS3DestinationDescription-FileExtension"></a>
Specify a file extension. It will override the default file extension
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `^$|\.[0-9a-z!\-_.*'()]+`
Required: No

 ** Prefix **   <a name="Firehose-Type-ExtendedS3DestinationDescription-Prefix"></a>
The "YYYY/MM/DD/HH" time format prefix is automatically used for delivered Amazon S3 files. You can also specify a custom prefix, as described in [Custom Prefixes for Amazon S3 Objects](https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*`
Required: No

 ** ProcessingConfiguration **   <a name="Firehose-Type-ExtendedS3DestinationDescription-ProcessingConfiguration"></a>
The data processing configuration.
Type: [ProcessingConfiguration](API_ProcessingConfiguration.md) object
Required: No

 ** S3BackupDescription **   <a name="Firehose-Type-ExtendedS3DestinationDescription-S3BackupDescription"></a>
The configuration for backup in Amazon S3.
Type: [S3DestinationDescription](API_S3DestinationDescription.md) object
Required: No

 ** S3BackupMode **   <a name="Firehose-Type-ExtendedS3DestinationDescription-S3BackupMode"></a>
The Amazon S3 backup mode.
Type: String
Valid Values: `Disabled | Enabled`
Required: No

## See Also
<a name="API_ExtendedS3DestinationDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/firehose-2015-08-04/ExtendedS3DestinationDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/firehose-2015-08-04/ExtendedS3DestinationDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/firehose-2015-08-04/ExtendedS3DestinationDescription)
