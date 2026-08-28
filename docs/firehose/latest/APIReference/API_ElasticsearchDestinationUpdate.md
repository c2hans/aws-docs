---
source_url: https://docs.aws.amazon.com/firehose/latest/APIReference/API_ElasticsearchDestinationUpdate.html
---

# ElasticsearchDestinationUpdate
<a name="API_ElasticsearchDestinationUpdate"></a>

Describes an update for a destination in Amazon OpenSearch Service.

## Contents
<a name="API_ElasticsearchDestinationUpdate_Contents"></a>

 ** BufferingHints **   <a name="Firehose-Type-ElasticsearchDestinationUpdate-BufferingHints"></a>
The buffering options. If no value is specified, `ElasticsearchBufferingHints` object default values are used.
Type: [ElasticsearchBufferingHints](API_ElasticsearchBufferingHints.md) object
Required: No

 ** CloudWatchLoggingOptions **   <a name="Firehose-Type-ElasticsearchDestinationUpdate-CloudWatchLoggingOptions"></a>
The CloudWatch logging options for your Firehose stream.
Type: [CloudWatchLoggingOptions](API_CloudWatchLoggingOptions.md) object
Required: No

 ** ClusterEndpoint **   <a name="Firehose-Type-ElasticsearchDestinationUpdate-ClusterEndpoint"></a>
The endpoint to use when communicating with the cluster. Specify either this `ClusterEndpoint` or the `DomainARN` field.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `https:.*`
Required: No

 ** DocumentIdOptions **   <a name="Firehose-Type-ElasticsearchDestinationUpdate-DocumentIdOptions"></a>
Indicates the method for setting up document ID. The supported methods are Firehose generated document ID and OpenSearch Service generated document ID.
Type: [DocumentIdOptions](API_DocumentIdOptions.md) object
Required: No

 ** DomainARN **   <a name="Firehose-Type-ElasticsearchDestinationUpdate-DomainARN"></a>
The ARN of the Amazon OpenSearch Service domain. The IAM role must have permissions for `DescribeDomain`, `DescribeDomains`, and `DescribeDomainConfig` after assuming the IAM role specified in `RoleARN`. For more information, see [Amazon Resource Names (ARNs) and AWS Service Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html).
Specify either `ClusterEndpoint` or `DomainARN`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `arn:.*:es:[a-zA-Z0-9\-]+:\d{12}:domain/[a-z][-0-9a-z]{2,27}`
Required: No

 ** IndexName **   <a name="Firehose-Type-ElasticsearchDestinationUpdate-IndexName"></a>
The Elasticsearch index name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 80.
Pattern: `.*`
Required: No

 ** IndexRotationPeriod **   <a name="Firehose-Type-ElasticsearchDestinationUpdate-IndexRotationPeriod"></a>
The Elasticsearch index rotation period. Index rotation appends a timestamp to `IndexName` to facilitate the expiration of old data. For more information, see [Index Rotation for the Amazon OpenSearch Service Destination](https://docs.aws.amazon.com/firehose/latest/dev/basic-deliver.html#es-index-rotation). Default value is `OneDay`.
Type: String
Valid Values: `NoRotation | OneHour | OneDay | OneWeek | OneMonth`
Required: No

 ** ProcessingConfiguration **   <a name="Firehose-Type-ElasticsearchDestinationUpdate-ProcessingConfiguration"></a>
The data processing configuration.
Type: [ProcessingConfiguration](API_ProcessingConfiguration.md) object
Required: No

 ** RetryOptions **   <a name="Firehose-Type-ElasticsearchDestinationUpdate-RetryOptions"></a>
The retry behavior in case Firehose is unable to deliver documents to Amazon OpenSearch Service. The default value is 300 (5 minutes).
Type: [ElasticsearchRetryOptions](API_ElasticsearchRetryOptions.md) object
Required: No

 ** RoleARN **   <a name="Firehose-Type-ElasticsearchDestinationUpdate-RoleARN"></a>
The Amazon Resource Name (ARN) of the IAM role to be assumed by Firehose for calling the Amazon OpenSearch Service Configuration API and for indexing documents. For more information, see [Grant Firehose Access to an Amazon S3 Destination](https://docs.aws.amazon.com/firehose/latest/dev/controlling-access.html#using-iam-s3) and [Amazon Resource Names (ARNs) and AWS Service Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `arn:.*:iam::\d{12}:role/[a-zA-Z_0-9+=,.@\-_/]+`
Required: No

 ** S3Update **   <a name="Firehose-Type-ElasticsearchDestinationUpdate-S3Update"></a>
The Amazon S3 destination.
Type: [S3DestinationUpdate](API_S3DestinationUpdate.md) object
Required: No

 ** TypeName **   <a name="Firehose-Type-ElasticsearchDestinationUpdate-TypeName"></a>
The Elasticsearch type name. For Elasticsearch 6.x, there can be only one type per index. If you try to specify a new type for an existing index that already has another type, Firehose returns an error during runtime.
If you upgrade Elasticsearch from 6.x to 7.x and don’t update your Firehose stream, Firehose still delivers data to Elasticsearch with the old index name and type name. If you want to update your Firehose stream with a new index name, provide an empty string for `TypeName`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Pattern: `.*`
Required: No

## See Also
<a name="API_ElasticsearchDestinationUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/firehose-2015-08-04/ElasticsearchDestinationUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/firehose-2015-08-04/ElasticsearchDestinationUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/firehose-2015-08-04/ElasticsearchDestinationUpdate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Data Firehose. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query firehose` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
