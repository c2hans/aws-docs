---
source_url: https://docs.aws.amazon.com/firehose/latest/APIReference/API_IcebergDestinationConfiguration.html
---

# IcebergDestinationConfiguration
<a name="API_IcebergDestinationConfiguration"></a>

 Specifies the destination configure settings for Apache Iceberg Table.

## Contents
<a name="API_IcebergDestinationConfiguration_Contents"></a>

 ** CatalogConfiguration **   <a name="Firehose-Type-IcebergDestinationConfiguration-CatalogConfiguration"></a>
 Configuration describing where the destination Apache Iceberg Tables are persisted.
Type: [CatalogConfiguration](API_CatalogConfiguration.md) object
Required: Yes

 ** RoleARN **   <a name="Firehose-Type-IcebergDestinationConfiguration-RoleARN"></a>
 The Amazon Resource Name (ARN) of the IAM role to be assumed by Firehose for calling Apache Iceberg Tables.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `arn:.*:iam::\d{12}:role/[a-zA-Z_0-9+=,.@\-_/]+`
Required: Yes

 ** S3Configuration **   <a name="Firehose-Type-IcebergDestinationConfiguration-S3Configuration"></a>
Describes the configuration of a destination in Amazon S3.
Type: [S3DestinationConfiguration](API_S3DestinationConfiguration.md) object
Required: Yes

 ** AppendOnly **   <a name="Firehose-Type-IcebergDestinationConfiguration-AppendOnly"></a>
 Describes whether all incoming data for this delivery stream will be append only (inserts only and not for updates and deletes) for Iceberg delivery. This feature is only applicable for Apache Iceberg Tables.
The default value is false. If you set this value to true, Firehose automatically increases the throughput limit of a stream based on the throttling levels of the stream. If you set this parameter to true for a stream with updates and deletes, you will see out of order delivery.
Type: Boolean
Required: No

 ** BufferingHints **   <a name="Firehose-Type-IcebergDestinationConfiguration-BufferingHints"></a>
Describes hints for the buffering to perform before delivering data to the destination. These options are treated as hints, and therefore Firehose might choose to use different values when it is optimal. The `SizeInMBs` and `IntervalInSeconds` parameters are optional. However, if specify a value for one of them, you must also provide a value for the other.
Type: [BufferingHints](API_BufferingHints.md) object
Required: No

 ** CloudWatchLoggingOptions **   <a name="Firehose-Type-IcebergDestinationConfiguration-CloudWatchLoggingOptions"></a>
Describes the Amazon CloudWatch logging options for your Firehose stream.
Type: [CloudWatchLoggingOptions](API_CloudWatchLoggingOptions.md) object
Required: No

 ** DestinationTableConfigurationList **   <a name="Firehose-Type-IcebergDestinationConfiguration-DestinationTableConfigurationList"></a>
 Provides a list of `DestinationTableConfigurations` which Firehose uses to deliver data to Apache Iceberg Tables. Firehose will write data with insert if table specific configuration is not provided here.
Type: Array of [DestinationTableConfiguration](API_DestinationTableConfiguration.md) objects
Required: No

 ** ProcessingConfiguration **   <a name="Firehose-Type-IcebergDestinationConfiguration-ProcessingConfiguration"></a>
Describes a data processing configuration.
Type: [ProcessingConfiguration](API_ProcessingConfiguration.md) object
Required: No

 ** RetryOptions **   <a name="Firehose-Type-IcebergDestinationConfiguration-RetryOptions"></a>
 The retry behavior in case Firehose is unable to deliver data to a destination.
Type: [RetryOptions](API_RetryOptions.md) object
Required: No

 ** S3BackupMode **   <a name="Firehose-Type-IcebergDestinationConfiguration-S3BackupMode"></a>
 Describes how Firehose will backup records. Currently,S3 backup only supports `FailedDataOnly`.
Type: String
Valid Values: `FailedDataOnly | AllData`
Required: No

 ** SchemaEvolutionConfiguration **   <a name="Firehose-Type-IcebergDestinationConfiguration-SchemaEvolutionConfiguration"></a>
The configuration to enable automatic schema evolution.
Amazon Data Firehose is in preview release and is subject to change.
Type: [SchemaEvolutionConfiguration](API_SchemaEvolutionConfiguration.md) object
Required: No

 ** TableCreationConfiguration **   <a name="Firehose-Type-IcebergDestinationConfiguration-TableCreationConfiguration"></a>
The configuration to enable automatic table creation.
Amazon Data Firehose is in preview release and is subject to change.
Type: [TableCreationConfiguration](API_TableCreationConfiguration.md) object
Required: No

## See Also
<a name="API_IcebergDestinationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/firehose-2015-08-04/IcebergDestinationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/firehose-2015-08-04/IcebergDestinationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/firehose-2015-08-04/IcebergDestinationConfiguration)
