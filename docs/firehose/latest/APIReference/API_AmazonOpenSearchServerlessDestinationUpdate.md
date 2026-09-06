---
source_url: https://docs.aws.amazon.com/firehose/latest/APIReference/API_AmazonOpenSearchServerlessDestinationUpdate.html
---

# AmazonOpenSearchServerlessDestinationUpdate
<a name="API_AmazonOpenSearchServerlessDestinationUpdate"></a>

Describes an update for a destination in the Serverless offering for Amazon OpenSearch Service.

## Contents
<a name="API_AmazonOpenSearchServerlessDestinationUpdate_Contents"></a>

 ** BufferingHints **   <a name="Firehose-Type-AmazonOpenSearchServerlessDestinationUpdate-BufferingHints"></a>
The buffering options. If no value is specified, AmazonopensearchBufferingHints object default values are used.
Type: [AmazonOpenSearchServerlessBufferingHints](API_AmazonOpenSearchServerlessBufferingHints.md) object
Required: No

 ** CloudWatchLoggingOptions **   <a name="Firehose-Type-AmazonOpenSearchServerlessDestinationUpdate-CloudWatchLoggingOptions"></a>
Describes the Amazon CloudWatch logging options for your Firehose stream.
Type: [CloudWatchLoggingOptions](API_CloudWatchLoggingOptions.md) object
Required: No

 ** CollectionEndpoint **   <a name="Firehose-Type-AmazonOpenSearchServerlessDestinationUpdate-CollectionEndpoint"></a>
The endpoint to use when communicating with the collection in the Serverless offering for Amazon OpenSearch Service.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `https:.*`
Required: No

 ** IndexName **   <a name="Firehose-Type-AmazonOpenSearchServerlessDestinationUpdate-IndexName"></a>
The Serverless offering for Amazon OpenSearch Service index name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 80.
Pattern: `.*`
Required: No

 ** ProcessingConfiguration **   <a name="Firehose-Type-AmazonOpenSearchServerlessDestinationUpdate-ProcessingConfiguration"></a>
Describes a data processing configuration.
Type: [ProcessingConfiguration](API_ProcessingConfiguration.md) object
Required: No

 ** RetryOptions **   <a name="Firehose-Type-AmazonOpenSearchServerlessDestinationUpdate-RetryOptions"></a>
The retry behavior in case Firehose is unable to deliver documents to the Serverless offering for Amazon OpenSearch Service. The default value is 300 (5 minutes).
Type: [AmazonOpenSearchServerlessRetryOptions](API_AmazonOpenSearchServerlessRetryOptions.md) object
Required: No

 ** RoleARN **   <a name="Firehose-Type-AmazonOpenSearchServerlessDestinationUpdate-RoleARN"></a>
The Amazon Resource Name (ARN) of the IAM role to be assumed by Firehose for calling the Serverless offering for Amazon OpenSearch Service Configuration API and for indexing documents.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `arn:.*:iam::\d{12}:role/[a-zA-Z_0-9+=,.@\-_/]+`
Required: No

 ** S3Update **   <a name="Firehose-Type-AmazonOpenSearchServerlessDestinationUpdate-S3Update"></a>
Describes an update for a destination in Amazon S3.
Type: [S3DestinationUpdate](API_S3DestinationUpdate.md) object
Required: No

## See Also
<a name="API_AmazonOpenSearchServerlessDestinationUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/firehose-2015-08-04/AmazonOpenSearchServerlessDestinationUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/firehose-2015-08-04/AmazonOpenSearchServerlessDestinationUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/firehose-2015-08-04/AmazonOpenSearchServerlessDestinationUpdate)
