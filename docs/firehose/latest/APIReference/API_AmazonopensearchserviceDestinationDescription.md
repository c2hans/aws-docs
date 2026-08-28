---
source_url: https://docs.aws.amazon.com/firehose/latest/APIReference/API_AmazonopensearchserviceDestinationDescription.html
---

# AmazonopensearchserviceDestinationDescription
<a name="API_AmazonopensearchserviceDestinationDescription"></a>

The destination description in Amazon OpenSearch Service.

## Contents
<a name="API_AmazonopensearchserviceDestinationDescription_Contents"></a>

 ** BufferingHints **   <a name="Firehose-Type-AmazonopensearchserviceDestinationDescription-BufferingHints"></a>
The buffering options.
Type: [AmazonopensearchserviceBufferingHints](API_AmazonopensearchserviceBufferingHints.md) object
Required: No

 ** CloudWatchLoggingOptions **   <a name="Firehose-Type-AmazonopensearchserviceDestinationDescription-CloudWatchLoggingOptions"></a>
Describes the Amazon CloudWatch logging options for your Firehose stream.
Type: [CloudWatchLoggingOptions](API_CloudWatchLoggingOptions.md) object
Required: No

 ** ClusterEndpoint **   <a name="Firehose-Type-AmazonopensearchserviceDestinationDescription-ClusterEndpoint"></a>
The endpoint to use when communicating with the cluster. Firehose uses either this ClusterEndpoint or the DomainARN field to send data to Amazon OpenSearch Service.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `https:.*`
Required: No

 ** DocumentIdOptions **   <a name="Firehose-Type-AmazonopensearchserviceDestinationDescription-DocumentIdOptions"></a>
Indicates the method for setting up document ID. The supported methods are Firehose generated document ID and OpenSearch Service generated document ID.
Type: [DocumentIdOptions](API_DocumentIdOptions.md) object
Required: No

 ** DomainARN **   <a name="Firehose-Type-AmazonopensearchserviceDestinationDescription-DomainARN"></a>
The ARN of the Amazon OpenSearch Service domain.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `arn:.*:es:[a-zA-Z0-9\-]+:\d{12}:domain/[a-z][-0-9a-z]{2,27}`
Required: No

 ** IndexName **   <a name="Firehose-Type-AmazonopensearchserviceDestinationDescription-IndexName"></a>
The Amazon OpenSearch Service index name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 80.
Pattern: `.*`
Required: No

 ** IndexRotationPeriod **   <a name="Firehose-Type-AmazonopensearchserviceDestinationDescription-IndexRotationPeriod"></a>
The Amazon OpenSearch Service index rotation period
Type: String
Valid Values: `NoRotation | OneHour | OneDay | OneWeek | OneMonth`
Required: No

 ** ProcessingConfiguration **   <a name="Firehose-Type-AmazonopensearchserviceDestinationDescription-ProcessingConfiguration"></a>
Describes a data processing configuration.
Type: [ProcessingConfiguration](API_ProcessingConfiguration.md) object
Required: No

 ** RetryOptions **   <a name="Firehose-Type-AmazonopensearchserviceDestinationDescription-RetryOptions"></a>
The Amazon OpenSearch Service retry options.
Type: [AmazonopensearchserviceRetryOptions](API_AmazonopensearchserviceRetryOptions.md) object
Required: No

 ** RoleARN **   <a name="Firehose-Type-AmazonopensearchserviceDestinationDescription-RoleARN"></a>
The Amazon Resource Name (ARN) of the AWS credentials.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `arn:.*:iam::\d{12}:role/[a-zA-Z_0-9+=,.@\-_/]+`
Required: No

 ** S3BackupMode **   <a name="Firehose-Type-AmazonopensearchserviceDestinationDescription-S3BackupMode"></a>
The Amazon S3 backup mode.
Type: String
Valid Values: `FailedDocumentsOnly | AllDocuments`
Required: No

 ** S3DestinationDescription **   <a name="Firehose-Type-AmazonopensearchserviceDestinationDescription-S3DestinationDescription"></a>
Describes a destination in Amazon S3.
Type: [S3DestinationDescription](API_S3DestinationDescription.md) object
Required: No

 ** TypeName **   <a name="Firehose-Type-AmazonopensearchserviceDestinationDescription-TypeName"></a>
The Amazon OpenSearch Service type name. This applies to Elasticsearch 6.x and lower versions. For Elasticsearch 7.x and OpenSearch Service 1.x, there's no value for TypeName.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Pattern: `.*`
Required: No

 ** VpcConfigurationDescription **   <a name="Firehose-Type-AmazonopensearchserviceDestinationDescription-VpcConfigurationDescription"></a>
The details of the VPC of the Amazon OpenSearch Service destination.
Type: [VpcConfigurationDescription](API_VpcConfigurationDescription.md) object
Required: No

## See Also
<a name="API_AmazonopensearchserviceDestinationDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/firehose-2015-08-04/AmazonopensearchserviceDestinationDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/firehose-2015-08-04/AmazonopensearchserviceDestinationDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/firehose-2015-08-04/AmazonopensearchserviceDestinationDescription)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Data Firehose. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query firehose` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
