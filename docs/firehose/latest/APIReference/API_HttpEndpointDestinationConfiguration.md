---
source_url: https://docs.aws.amazon.com/firehose/latest/APIReference/API_HttpEndpointDestinationConfiguration.html
---

# HttpEndpointDestinationConfiguration
<a name="API_HttpEndpointDestinationConfiguration"></a>

Describes the configuration of the HTTP endpoint destination.

## Contents
<a name="API_HttpEndpointDestinationConfiguration_Contents"></a>

 ** EndpointConfiguration **   <a name="Firehose-Type-HttpEndpointDestinationConfiguration-EndpointConfiguration"></a>
The configuration of the HTTP endpoint selected as the destination.
Type: [HttpEndpointConfiguration](API_HttpEndpointConfiguration.md) object
Required: Yes

 ** S3Configuration **   <a name="Firehose-Type-HttpEndpointDestinationConfiguration-S3Configuration"></a>
Describes the configuration of a destination in Amazon S3.
Type: [S3DestinationConfiguration](API_S3DestinationConfiguration.md) object
Required: Yes

 ** BufferingHints **   <a name="Firehose-Type-HttpEndpointDestinationConfiguration-BufferingHints"></a>
The buffering options that can be used before data is delivered to the specified destination. Firehose treats these options as hints, and it might choose to use more optimal values. The `SizeInMBs` and `IntervalInSeconds` parameters are optional. However, if you specify a value for one of them, you must also provide a value for the other.
Type: [HttpEndpointBufferingHints](API_HttpEndpointBufferingHints.md) object
Required: No

 ** CloudWatchLoggingOptions **   <a name="Firehose-Type-HttpEndpointDestinationConfiguration-CloudWatchLoggingOptions"></a>
Describes the Amazon CloudWatch logging options for your Firehose stream.
Type: [CloudWatchLoggingOptions](API_CloudWatchLoggingOptions.md) object
Required: No

 ** ProcessingConfiguration **   <a name="Firehose-Type-HttpEndpointDestinationConfiguration-ProcessingConfiguration"></a>
Describes a data processing configuration.
Type: [ProcessingConfiguration](API_ProcessingConfiguration.md) object
Required: No

 ** RequestConfiguration **   <a name="Firehose-Type-HttpEndpointDestinationConfiguration-RequestConfiguration"></a>
The configuration of the request sent to the HTTP endpoint that is specified as the destination.
Type: [HttpEndpointRequestConfiguration](API_HttpEndpointRequestConfiguration.md) object
Required: No

 ** RetryOptions **   <a name="Firehose-Type-HttpEndpointDestinationConfiguration-RetryOptions"></a>
Describes the retry behavior in case Firehose is unable to deliver data to the specified HTTP endpoint destination, or if it doesn't receive a valid acknowledgment of receipt from the specified HTTP endpoint destination.
Type: [HttpEndpointRetryOptions](API_HttpEndpointRetryOptions.md) object
Required: No

 ** RoleARN **   <a name="Firehose-Type-HttpEndpointDestinationConfiguration-RoleARN"></a>
Firehose uses this IAM role for all the permissions that the delivery stream needs.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `arn:.*:iam::\d{12}:role/[a-zA-Z_0-9+=,.@\-_/]+`
Required: No

 ** S3BackupMode **   <a name="Firehose-Type-HttpEndpointDestinationConfiguration-S3BackupMode"></a>
Describes the S3 bucket backup options for the data that Firehose delivers to the HTTP endpoint destination. You can back up all documents (`AllData`) or only the documents that Firehose could not deliver to the specified HTTP endpoint destination (`FailedDataOnly`).
Type: String
Valid Values: `FailedDataOnly | AllData`
Required: No

 ** SecretsManagerConfiguration **   <a name="Firehose-Type-HttpEndpointDestinationConfiguration-SecretsManagerConfiguration"></a>
 The configuration that defines how you access secrets for HTTP Endpoint destination.
Type: [SecretsManagerConfiguration](API_SecretsManagerConfiguration.md) object
Required: No

## See Also
<a name="API_HttpEndpointDestinationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/firehose-2015-08-04/HttpEndpointDestinationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/firehose-2015-08-04/HttpEndpointDestinationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/firehose-2015-08-04/HttpEndpointDestinationConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Data Firehose. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query firehose` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
