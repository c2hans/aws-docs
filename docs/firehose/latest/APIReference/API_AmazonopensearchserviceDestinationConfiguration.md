---
source_url: https://docs.aws.amazon.com/firehose/latest/APIReference/API_AmazonopensearchserviceDestinationConfiguration.html
---

# AmazonopensearchserviceDestinationConfiguration
<a name="API_AmazonopensearchserviceDestinationConfiguration"></a>

Describes the configuration of a destination in Amazon OpenSearch Service

## Contents
<a name="API_AmazonopensearchserviceDestinationConfiguration_Contents"></a>

 ** IndexName **   <a name="Firehose-Type-AmazonopensearchserviceDestinationConfiguration-IndexName"></a>
The ElasticsearAmazon OpenSearch Service index name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 80.
Pattern: `.*`
Required: Yes

 ** RoleARN **   <a name="Firehose-Type-AmazonopensearchserviceDestinationConfiguration-RoleARN"></a>
The Amazon Resource Name (ARN) of the IAM role to be assumed by Firehose for calling the Amazon OpenSearch Service Configuration API and for indexing documents.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `arn:.*:iam::\d{12}:role/[a-zA-Z_0-9+=,.@\-_/]+`
Required: Yes

 ** S3Configuration **   <a name="Firehose-Type-AmazonopensearchserviceDestinationConfiguration-S3Configuration"></a>
Describes the configuration of a destination in Amazon S3.
Type: [S3DestinationConfiguration](API_S3DestinationConfiguration.md) object
Required: Yes

 ** BufferingHints **   <a name="Firehose-Type-AmazonopensearchserviceDestinationConfiguration-BufferingHints"></a>
The buffering options. If no value is specified, the default values for AmazonopensearchserviceBufferingHints are used.
Type: [AmazonopensearchserviceBufferingHints](API_AmazonopensearchserviceBufferingHints.md) object
Required: No

 ** CloudWatchLoggingOptions **   <a name="Firehose-Type-AmazonopensearchserviceDestinationConfiguration-CloudWatchLoggingOptions"></a>
Describes the Amazon CloudWatch logging options for your Firehose stream.
Type: [CloudWatchLoggingOptions](API_CloudWatchLoggingOptions.md) object
Required: No

 ** ClusterEndpoint **   <a name="Firehose-Type-AmazonopensearchserviceDestinationConfiguration-ClusterEndpoint"></a>
The endpoint to use when communicating with the cluster. Specify either this ClusterEndpoint or the DomainARN field.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `https:.*`
Required: No

 ** DocumentIdOptions **   <a name="Firehose-Type-AmazonopensearchserviceDestinationConfiguration-DocumentIdOptions"></a>
Indicates the method for setting up document ID. The supported methods are Firehose generated document ID and OpenSearch Service generated document ID.
Type: [DocumentIdOptions](API_DocumentIdOptions.md) object
Required: No

 ** DomainARN **   <a name="Firehose-Type-AmazonopensearchserviceDestinationConfiguration-DomainARN"></a>
The ARN of the Amazon OpenSearch Service domain. The IAM role must have permissions for DescribeElasticsearchDomain, DescribeElasticsearchDomains, and DescribeElasticsearchDomainConfig after assuming the role specified in RoleARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `arn:.*:es:[a-zA-Z0-9\-]+:\d{12}:domain/[a-z][-0-9a-z]{2,27}`
Required: No

 ** IndexRotationPeriod **   <a name="Firehose-Type-AmazonopensearchserviceDestinationConfiguration-IndexRotationPeriod"></a>
The Amazon OpenSearch Service index rotation period. Index rotation appends a timestamp to the IndexName to facilitate the expiration of old data.
Type: String
Valid Values: `NoRotation | OneHour | OneDay | OneWeek | OneMonth`
Required: No

 ** ProcessingConfiguration **   <a name="Firehose-Type-AmazonopensearchserviceDestinationConfiguration-ProcessingConfiguration"></a>
Describes a data processing configuration.
Type: [ProcessingConfiguration](API_ProcessingConfiguration.md) object
Required: No

 ** RetryOptions **   <a name="Firehose-Type-AmazonopensearchserviceDestinationConfiguration-RetryOptions"></a>
The retry behavior in case Firehose is unable to deliver documents to Amazon OpenSearch Service. The default value is 300 (5 minutes).
Type: [AmazonopensearchserviceRetryOptions](API_AmazonopensearchserviceRetryOptions.md) object
Required: No

 ** S3BackupMode **   <a name="Firehose-Type-AmazonopensearchserviceDestinationConfiguration-S3BackupMode"></a>
Defines how documents should be delivered to Amazon S3. When it is set to FailedDocumentsOnly, Firehose writes any documents that could not be indexed to the configured Amazon S3 destination, with AmazonOpenSearchService-failed/ appended to the key prefix. When set to AllDocuments, Firehose delivers all incoming records to Amazon S3, and also writes failed documents with AmazonOpenSearchService-failed/ appended to the prefix.
Type: String
Valid Values: `FailedDocumentsOnly | AllDocuments`
Required: No

 ** TypeName **   <a name="Firehose-Type-AmazonopensearchserviceDestinationConfiguration-TypeName"></a>
The Amazon OpenSearch Service type name. For Elasticsearch 6.x, there can be only one type per index. If you try to specify a new type for an existing index that already has another type, Firehose returns an error during run time.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Pattern: `.*`
Required: No

 ** VpcConfiguration **   <a name="Firehose-Type-AmazonopensearchserviceDestinationConfiguration-VpcConfiguration"></a>
The details of the VPC of the Amazon OpenSearch or Amazon OpenSearch Serverless destination.
Type: [VpcConfiguration](API_VpcConfiguration.md) object
Required: No

## See Also
<a name="API_AmazonopensearchserviceDestinationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/firehose-2015-08-04/AmazonopensearchserviceDestinationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/firehose-2015-08-04/AmazonopensearchserviceDestinationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/firehose-2015-08-04/AmazonopensearchserviceDestinationConfiguration)
