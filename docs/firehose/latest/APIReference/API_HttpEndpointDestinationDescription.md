---
source_url: https://docs.aws.amazon.com/firehose/latest/APIReference/API_HttpEndpointDestinationDescription.html
---

# HttpEndpointDestinationDescription
<a name="API_HttpEndpointDestinationDescription"></a>

Describes the HTTP endpoint destination.

## Contents
<a name="API_HttpEndpointDestinationDescription_Contents"></a>

 ** BufferingHints **   <a name="Firehose-Type-HttpEndpointDestinationDescription-BufferingHints"></a>
Describes buffering options that can be applied to the data before it is delivered to the HTTPS endpoint destination. Firehose teats these options as hints, and it might choose to use more optimal values. The `SizeInMBs` and `IntervalInSeconds` parameters are optional. However, if specify a value for one of them, you must also provide a value for the other.
Type: [HttpEndpointBufferingHints](API_HttpEndpointBufferingHints.md) object
Required: No

 ** CloudWatchLoggingOptions **   <a name="Firehose-Type-HttpEndpointDestinationDescription-CloudWatchLoggingOptions"></a>
Describes the Amazon CloudWatch logging options for your Firehose stream.
Type: [CloudWatchLoggingOptions](API_CloudWatchLoggingOptions.md) object
Required: No

 ** EndpointConfiguration **   <a name="Firehose-Type-HttpEndpointDestinationDescription-EndpointConfiguration"></a>
The configuration of the specified HTTP endpoint destination.
Type: [HttpEndpointDescription](API_HttpEndpointDescription.md) object
Required: No

 ** ProcessingConfiguration **   <a name="Firehose-Type-HttpEndpointDestinationDescription-ProcessingConfiguration"></a>
Describes a data processing configuration.
Type: [ProcessingConfiguration](API_ProcessingConfiguration.md) object
Required: No

 ** RequestConfiguration **   <a name="Firehose-Type-HttpEndpointDestinationDescription-RequestConfiguration"></a>
The configuration of request sent to the HTTP endpoint specified as the destination.
Type: [HttpEndpointRequestConfiguration](API_HttpEndpointRequestConfiguration.md) object
Required: No

 ** RetryOptions **   <a name="Firehose-Type-HttpEndpointDestinationDescription-RetryOptions"></a>
Describes the retry behavior in case Firehose is unable to deliver data to the specified HTTP endpoint destination, or if it doesn't receive a valid acknowledgment of receipt from the specified HTTP endpoint destination.
Type: [HttpEndpointRetryOptions](API_HttpEndpointRetryOptions.md) object
Required: No

 ** RoleARN **   <a name="Firehose-Type-HttpEndpointDestinationDescription-RoleARN"></a>
Firehose uses this IAM role for all the permissions that the delivery stream needs.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `arn:.*:iam::\d{12}:role/[a-zA-Z_0-9+=,.@\-_/]+`
Required: No

 ** S3BackupMode **   <a name="Firehose-Type-HttpEndpointDestinationDescription-S3BackupMode"></a>
Describes the S3 bucket backup options for the data that Kinesis Firehose delivers to the HTTP endpoint destination. You can back up all documents (`AllData`) or only the documents that Firehose could not deliver to the specified HTTP endpoint destination (`FailedDataOnly`).
Type: String
Valid Values: `FailedDataOnly | AllData`
Required: No

 ** S3DestinationDescription **   <a name="Firehose-Type-HttpEndpointDestinationDescription-S3DestinationDescription"></a>
Describes a destination in Amazon S3.
Type: [S3DestinationDescription](API_S3DestinationDescription.md) object
Required: No

 ** SecretsManagerConfiguration **   <a name="Firehose-Type-HttpEndpointDestinationDescription-SecretsManagerConfiguration"></a>
 The configuration that defines how you access secrets for HTTP Endpoint destination.
Type: [SecretsManagerConfiguration](API_SecretsManagerConfiguration.md) object
Required: No

## See Also
<a name="API_HttpEndpointDestinationDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/firehose-2015-08-04/HttpEndpointDestinationDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/firehose-2015-08-04/HttpEndpointDestinationDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/firehose-2015-08-04/HttpEndpointDestinationDescription)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Data Firehose. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query firehose` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
