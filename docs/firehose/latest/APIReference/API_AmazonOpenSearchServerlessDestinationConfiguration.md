---
source_url: https://docs.aws.amazon.com/firehose/latest/APIReference/API_AmazonOpenSearchServerlessDestinationConfiguration.html
---

# AmazonOpenSearchServerlessDestinationConfiguration
<a name="API_AmazonOpenSearchServerlessDestinationConfiguration"></a>

Describes the configuration of a destination in the Serverless offering for Amazon OpenSearch Service.

## Contents
<a name="API_AmazonOpenSearchServerlessDestinationConfiguration_Contents"></a>

 ** IndexName **   <a name="Firehose-Type-AmazonOpenSearchServerlessDestinationConfiguration-IndexName"></a>
The Serverless offering for Amazon OpenSearch Service index name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 80.
Pattern: `.*`
Required: Yes

 ** RoleARN **   <a name="Firehose-Type-AmazonOpenSearchServerlessDestinationConfiguration-RoleARN"></a>
The Amazon Resource Name (ARN) of the IAM role to be assumed by Firehose for calling the Serverless offering for Amazon OpenSearch Service Configuration API and for indexing documents.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `arn:.*:iam::\d{12}:role/[a-zA-Z_0-9+=,.@\-_/]+`
Required: Yes

 ** S3Configuration **   <a name="Firehose-Type-AmazonOpenSearchServerlessDestinationConfiguration-S3Configuration"></a>
Describes the configuration of a destination in Amazon S3.
Type: [S3DestinationConfiguration](API_S3DestinationConfiguration.md) object
Required: Yes

 ** BufferingHints **   <a name="Firehose-Type-AmazonOpenSearchServerlessDestinationConfiguration-BufferingHints"></a>
The buffering options. If no value is specified, the default values for AmazonopensearchserviceBufferingHints are used.
Type: [AmazonOpenSearchServerlessBufferingHints](API_AmazonOpenSearchServerlessBufferingHints.md) object
Required: No

 ** CloudWatchLoggingOptions **   <a name="Firehose-Type-AmazonOpenSearchServerlessDestinationConfiguration-CloudWatchLoggingOptions"></a>
Describes the Amazon CloudWatch logging options for your Firehose stream.
Type: [CloudWatchLoggingOptions](API_CloudWatchLoggingOptions.md) object
Required: No

 ** CollectionEndpoint **   <a name="Firehose-Type-AmazonOpenSearchServerlessDestinationConfiguration-CollectionEndpoint"></a>
The endpoint to use when communicating with the collection in the Serverless offering for Amazon OpenSearch Service.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `https:.*`
Required: No

 ** ProcessingConfiguration **   <a name="Firehose-Type-AmazonOpenSearchServerlessDestinationConfiguration-ProcessingConfiguration"></a>
Describes a data processing configuration.
Type: [ProcessingConfiguration](API_ProcessingConfiguration.md) object
Required: No

 ** RetryOptions **   <a name="Firehose-Type-AmazonOpenSearchServerlessDestinationConfiguration-RetryOptions"></a>
The retry behavior in case Firehose is unable to deliver documents to the Serverless offering for Amazon OpenSearch Service. The default value is 300 (5 minutes).
Type: [AmazonOpenSearchServerlessRetryOptions](API_AmazonOpenSearchServerlessRetryOptions.md) object
Required: No

 ** S3BackupMode **   <a name="Firehose-Type-AmazonOpenSearchServerlessDestinationConfiguration-S3BackupMode"></a>
Defines how documents should be delivered to Amazon S3. When it is set to FailedDocumentsOnly, Firehose writes any documents that could not be indexed to the configured Amazon S3 destination, with AmazonOpenSearchService-failed/ appended to the key prefix. When set to AllDocuments, Firehose delivers all incoming records to Amazon S3, and also writes failed documents with AmazonOpenSearchService-failed/ appended to the prefix.
Type: String
Valid Values: `FailedDocumentsOnly | AllDocuments`
Required: No

 ** VpcConfiguration **   <a name="Firehose-Type-AmazonOpenSearchServerlessDestinationConfiguration-VpcConfiguration"></a>
The details of the VPC of the Amazon OpenSearch or Amazon OpenSearch Serverless destination.
Type: [VpcConfiguration](API_VpcConfiguration.md) object
Required: No

## See Also
<a name="API_AmazonOpenSearchServerlessDestinationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/firehose-2015-08-04/AmazonOpenSearchServerlessDestinationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/firehose-2015-08-04/AmazonOpenSearchServerlessDestinationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/firehose-2015-08-04/AmazonOpenSearchServerlessDestinationConfiguration)
