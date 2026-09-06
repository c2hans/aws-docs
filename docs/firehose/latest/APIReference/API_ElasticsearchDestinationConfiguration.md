---
source_url: https://docs.aws.amazon.com/firehose/latest/APIReference/API_ElasticsearchDestinationConfiguration.html
---

# ElasticsearchDestinationConfiguration
<a name="API_ElasticsearchDestinationConfiguration"></a>

Describes the configuration of a destination in Amazon OpenSearch Service.

## Contents
<a name="API_ElasticsearchDestinationConfiguration_Contents"></a>

 ** IndexName **   <a name="Firehose-Type-ElasticsearchDestinationConfiguration-IndexName"></a>
The Elasticsearch index name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 80.
Pattern: `.*`
Required: Yes

 ** RoleARN **   <a name="Firehose-Type-ElasticsearchDestinationConfiguration-RoleARN"></a>
The Amazon Resource Name (ARN) of the IAM role to be assumed by Firehose for calling the Amazon OpenSearch Service Configuration API and for indexing documents. For more information, see [Grant Firehose Access to an Amazon S3 Destination](https://docs.aws.amazon.com/firehose/latest/dev/controlling-access.html#using-iam-s3) and [Amazon Resource Names (ARNs) and AWS Service Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `arn:.*:iam::\d{12}:role/[a-zA-Z_0-9+=,.@\-_/]+`
Required: Yes

 ** S3Configuration **   <a name="Firehose-Type-ElasticsearchDestinationConfiguration-S3Configuration"></a>
The configuration for the backup Amazon S3 location.
Type: [S3DestinationConfiguration](API_S3DestinationConfiguration.md) object
Required: Yes

 ** BufferingHints **   <a name="Firehose-Type-ElasticsearchDestinationConfiguration-BufferingHints"></a>
The buffering options. If no value is specified, the default values for `ElasticsearchBufferingHints` are used.
Type: [ElasticsearchBufferingHints](API_ElasticsearchBufferingHints.md) object
Required: No

 ** CloudWatchLoggingOptions **   <a name="Firehose-Type-ElasticsearchDestinationConfiguration-CloudWatchLoggingOptions"></a>
The Amazon CloudWatch logging options for your Firehose stream.
Type: [CloudWatchLoggingOptions](API_CloudWatchLoggingOptions.md) object
Required: No

 ** ClusterEndpoint **   <a name="Firehose-Type-ElasticsearchDestinationConfiguration-ClusterEndpoint"></a>
The endpoint to use when communicating with the cluster. Specify either this `ClusterEndpoint` or the `DomainARN` field.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `https:.*`
Required: No

 ** DocumentIdOptions **   <a name="Firehose-Type-ElasticsearchDestinationConfiguration-DocumentIdOptions"></a>
Indicates the method for setting up document ID. The supported methods are Firehose generated document ID and OpenSearch Service generated document ID.
Type: [DocumentIdOptions](API_DocumentIdOptions.md) object
Required: No

 ** DomainARN **   <a name="Firehose-Type-ElasticsearchDestinationConfiguration-DomainARN"></a>
The ARN of the Amazon OpenSearch Service domain. The IAM role must have permissions for `DescribeDomain`, `DescribeDomains`, and `DescribeDomainConfig` after assuming the role specified in **RoleARN**. For more information, see [Amazon Resource Names (ARNs) and AWS Service Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html).
Specify either `ClusterEndpoint` or `DomainARN`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `arn:.*:es:[a-zA-Z0-9\-]+:\d{12}:domain/[a-z][-0-9a-z]{2,27}`
Required: No

 ** IndexRotationPeriod **   <a name="Firehose-Type-ElasticsearchDestinationConfiguration-IndexRotationPeriod"></a>
The Elasticsearch index rotation period. Index rotation appends a timestamp to the `IndexName` to facilitate the expiration of old data. For more information, see [Index Rotation for the Amazon OpenSearch Service Destination](https://docs.aws.amazon.com/firehose/latest/dev/basic-deliver.html#es-index-rotation). The default value is `OneDay`.
Type: String
Valid Values: `NoRotation | OneHour | OneDay | OneWeek | OneMonth`
Required: No

 ** ProcessingConfiguration **   <a name="Firehose-Type-ElasticsearchDestinationConfiguration-ProcessingConfiguration"></a>
The data processing configuration.
Type: [ProcessingConfiguration](API_ProcessingConfiguration.md) object
Required: No

 ** RetryOptions **   <a name="Firehose-Type-ElasticsearchDestinationConfiguration-RetryOptions"></a>
The retry behavior in case Firehose is unable to deliver documents to Amazon OpenSearch Service. The default value is 300 (5 minutes).
Type: [ElasticsearchRetryOptions](API_ElasticsearchRetryOptions.md) object
Required: No

 ** S3BackupMode **   <a name="Firehose-Type-ElasticsearchDestinationConfiguration-S3BackupMode"></a>
Defines how documents should be delivered to Amazon S3. When it is set to `FailedDocumentsOnly`, Firehose writes any documents that could not be indexed to the configured Amazon S3 destination, with `AmazonOpenSearchService-failed/` appended to the key prefix. When set to `AllDocuments`, Firehose delivers all incoming records to Amazon S3, and also writes failed documents with `AmazonOpenSearchService-failed/` appended to the prefix. For more information, see [Amazon S3 Backup for the Amazon OpenSearch Service Destination](https://docs.aws.amazon.com/firehose/latest/dev/basic-deliver.html#es-s3-backup). Default value is `FailedDocumentsOnly`.
You can't change this backup mode after you create the Firehose stream.
Type: String
Valid Values: `FailedDocumentsOnly | AllDocuments`
Required: No

 ** TypeName **   <a name="Firehose-Type-ElasticsearchDestinationConfiguration-TypeName"></a>
The Elasticsearch type name. For Elasticsearch 6.x, there can be only one type per index. If you try to specify a new type for an existing index that already has another type, Firehose returns an error during run time.
For Elasticsearch 7.x, don't specify a `TypeName`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Pattern: `.*`
Required: No

 ** VpcConfiguration **   <a name="Firehose-Type-ElasticsearchDestinationConfiguration-VpcConfiguration"></a>
The details of the VPC of the Amazon destination.
Type: [VpcConfiguration](API_VpcConfiguration.md) object
Required: No

## See Also
<a name="API_ElasticsearchDestinationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/firehose-2015-08-04/ElasticsearchDestinationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/firehose-2015-08-04/ElasticsearchDestinationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/firehose-2015-08-04/ElasticsearchDestinationConfiguration)
