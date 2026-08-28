---
source_url: https://docs.aws.amazon.com/firehose/latest/APIReference/API_IcebergDestinationUpdate.html
---

# IcebergDestinationUpdate
<a name="API_IcebergDestinationUpdate"></a>

 Describes an update for a destination in Apache Iceberg Tables.

## Contents
<a name="API_IcebergDestinationUpdate_Contents"></a>

 ** AppendOnly **   <a name="Firehose-Type-IcebergDestinationUpdate-AppendOnly"></a>
 Describes whether all incoming data for this delivery stream will be append only (inserts only and not for updates and deletes) for Iceberg delivery. This feature is only applicable for Apache Iceberg Tables.
The default value is false. If you set this value to true, Firehose automatically increases the throughput limit of a stream based on the throttling levels of the stream. If you set this parameter to true for a stream with updates and deletes, you will see out of order delivery.
Type: Boolean
Required: No

 ** BufferingHints **   <a name="Firehose-Type-IcebergDestinationUpdate-BufferingHints"></a>
Describes hints for the buffering to perform before delivering data to the destination. These options are treated as hints, and therefore Firehose might choose to use different values when it is optimal. The `SizeInMBs` and `IntervalInSeconds` parameters are optional. However, if specify a value for one of them, you must also provide a value for the other.
Type: [BufferingHints](API_BufferingHints.md) object
Required: No

 ** CatalogConfiguration **   <a name="Firehose-Type-IcebergDestinationUpdate-CatalogConfiguration"></a>
 Configuration describing where the destination Iceberg tables are persisted.
Type: [CatalogConfiguration](API_CatalogConfiguration.md) object
Required: No

 ** CloudWatchLoggingOptions **   <a name="Firehose-Type-IcebergDestinationUpdate-CloudWatchLoggingOptions"></a>
Describes the Amazon CloudWatch logging options for your Firehose stream.
Type: [CloudWatchLoggingOptions](API_CloudWatchLoggingOptions.md) object
Required: No

 ** DestinationTableConfigurationList **   <a name="Firehose-Type-IcebergDestinationUpdate-DestinationTableConfigurationList"></a>
 Provides a list of `DestinationTableConfigurations` which Firehose uses to deliver data to Apache Iceberg Tables. Firehose will write data with insert if table specific configuration is not provided here.
Type: Array of [DestinationTableConfiguration](API_DestinationTableConfiguration.md) objects
Required: No

 ** ProcessingConfiguration **   <a name="Firehose-Type-IcebergDestinationUpdate-ProcessingConfiguration"></a>
Describes a data processing configuration.
Type: [ProcessingConfiguration](API_ProcessingConfiguration.md) object
Required: No

 ** RetryOptions **   <a name="Firehose-Type-IcebergDestinationUpdate-RetryOptions"></a>
 The retry behavior in case Firehose is unable to deliver data to a destination.
Type: [RetryOptions](API_RetryOptions.md) object
Required: No

 ** RoleARN **   <a name="Firehose-Type-IcebergDestinationUpdate-RoleARN"></a>
 The Amazon Resource Name (ARN) of the IAM role to be assumed by Firehose for calling Apache Iceberg Tables.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `arn:.*:iam::\d{12}:role/[a-zA-Z_0-9+=,.@\-_/]+`
Required: No

 ** S3BackupMode **   <a name="Firehose-Type-IcebergDestinationUpdate-S3BackupMode"></a>
 Describes how Firehose will backup records. Currently,Firehose only supports `FailedDataOnly`.
Type: String
Valid Values: `FailedDataOnly | AllData`
Required: No

 ** S3Configuration **   <a name="Firehose-Type-IcebergDestinationUpdate-S3Configuration"></a>
Describes the configuration of a destination in Amazon S3.
Type: [S3DestinationConfiguration](API_S3DestinationConfiguration.md) object
Required: No

 ** SchemaEvolutionConfiguration **   <a name="Firehose-Type-IcebergDestinationUpdate-SchemaEvolutionConfiguration"></a>
 The configuration to enable automatic schema evolution.
Amazon Data Firehose is in preview release and is subject to change.
Type: [SchemaEvolutionConfiguration](API_SchemaEvolutionConfiguration.md) object
Required: No

 ** TableCreationConfiguration **   <a name="Firehose-Type-IcebergDestinationUpdate-TableCreationConfiguration"></a>
 The configuration to enable automatic table creation.
Amazon Data Firehose is in preview release and is subject to change.
Type: [TableCreationConfiguration](API_TableCreationConfiguration.md) object
Required: No

## See Also
<a name="API_IcebergDestinationUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/firehose-2015-08-04/IcebergDestinationUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/firehose-2015-08-04/IcebergDestinationUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/firehose-2015-08-04/IcebergDestinationUpdate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Data Firehose. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query firehose` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
