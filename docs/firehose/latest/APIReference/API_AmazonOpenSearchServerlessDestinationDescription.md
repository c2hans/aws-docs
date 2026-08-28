---
source_url: https://docs.aws.amazon.com/firehose/latest/APIReference/API_AmazonOpenSearchServerlessDestinationDescription.html
---

# AmazonOpenSearchServerlessDestinationDescription
<a name="API_AmazonOpenSearchServerlessDestinationDescription"></a>

The destination description in the Serverless offering for Amazon OpenSearch Service.

## Contents
<a name="API_AmazonOpenSearchServerlessDestinationDescription_Contents"></a>

 ** BufferingHints **   <a name="Firehose-Type-AmazonOpenSearchServerlessDestinationDescription-BufferingHints"></a>
The buffering options.
Type: [AmazonOpenSearchServerlessBufferingHints](API_AmazonOpenSearchServerlessBufferingHints.md) object
Required: No

 ** CloudWatchLoggingOptions **   <a name="Firehose-Type-AmazonOpenSearchServerlessDestinationDescription-CloudWatchLoggingOptions"></a>
Describes the Amazon CloudWatch logging options for your Firehose stream.
Type: [CloudWatchLoggingOptions](API_CloudWatchLoggingOptions.md) object
Required: No

 ** CollectionEndpoint **   <a name="Firehose-Type-AmazonOpenSearchServerlessDestinationDescription-CollectionEndpoint"></a>
The endpoint to use when communicating with the collection in the Serverless offering for Amazon OpenSearch Service.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `https:.*`
Required: No

 ** IndexName **   <a name="Firehose-Type-AmazonOpenSearchServerlessDestinationDescription-IndexName"></a>
The Serverless offering for Amazon OpenSearch Service index name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 80.
Pattern: `.*`
Required: No

 ** ProcessingConfiguration **   <a name="Firehose-Type-AmazonOpenSearchServerlessDestinationDescription-ProcessingConfiguration"></a>
Describes a data processing configuration.
Type: [ProcessingConfiguration](API_ProcessingConfiguration.md) object
Required: No

 ** RetryOptions **   <a name="Firehose-Type-AmazonOpenSearchServerlessDestinationDescription-RetryOptions"></a>
The Serverless offering for Amazon OpenSearch Service retry options.
Type: [AmazonOpenSearchServerlessRetryOptions](API_AmazonOpenSearchServerlessRetryOptions.md) object
Required: No

 ** RoleARN **   <a name="Firehose-Type-AmazonOpenSearchServerlessDestinationDescription-RoleARN"></a>
The Amazon Resource Name (ARN) of the AWS credentials.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `arn:.*:iam::\d{12}:role/[a-zA-Z_0-9+=,.@\-_/]+`
Required: No

 ** S3BackupMode **   <a name="Firehose-Type-AmazonOpenSearchServerlessDestinationDescription-S3BackupMode"></a>
The Amazon S3 backup mode.
Type: String
Valid Values: `FailedDocumentsOnly | AllDocuments`
Required: No

 ** S3DestinationDescription **   <a name="Firehose-Type-AmazonOpenSearchServerlessDestinationDescription-S3DestinationDescription"></a>
Describes a destination in Amazon S3.
Type: [S3DestinationDescription](API_S3DestinationDescription.md) object
Required: No

 ** VpcConfigurationDescription **   <a name="Firehose-Type-AmazonOpenSearchServerlessDestinationDescription-VpcConfigurationDescription"></a>
The details of the VPC of the Amazon OpenSearch Service destination.
Type: [VpcConfigurationDescription](API_VpcConfigurationDescription.md) object
Required: No

## See Also
<a name="API_AmazonOpenSearchServerlessDestinationDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/firehose-2015-08-04/AmazonOpenSearchServerlessDestinationDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/firehose-2015-08-04/AmazonOpenSearchServerlessDestinationDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/firehose-2015-08-04/AmazonOpenSearchServerlessDestinationDescription)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Data Firehose. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query firehose` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
