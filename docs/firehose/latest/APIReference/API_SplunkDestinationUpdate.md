---
source_url: https://docs.aws.amazon.com/firehose/latest/APIReference/API_SplunkDestinationUpdate.html
---

# SplunkDestinationUpdate
<a name="API_SplunkDestinationUpdate"></a>

Describes an update for a destination in Splunk.

## Contents
<a name="API_SplunkDestinationUpdate_Contents"></a>

 ** BufferingHints **   <a name="Firehose-Type-SplunkDestinationUpdate-BufferingHints"></a>
The buffering options. If no value is specified, the default values for Splunk are used.
Type: [SplunkBufferingHints](API_SplunkBufferingHints.md) object
Required: No

 ** CloudWatchLoggingOptions **   <a name="Firehose-Type-SplunkDestinationUpdate-CloudWatchLoggingOptions"></a>
The Amazon CloudWatch logging options for your Firehose stream.
Type: [CloudWatchLoggingOptions](API_CloudWatchLoggingOptions.md) object
Required: No

 ** HECAcknowledgmentTimeoutInSeconds **   <a name="Firehose-Type-SplunkDestinationUpdate-HECAcknowledgmentTimeoutInSeconds"></a>
The amount of time that Firehose waits to receive an acknowledgment from Splunk after it sends data. At the end of the timeout period, Firehose either tries to send the data again or considers it an error, based on your retry settings.
Type: Integer
Valid Range: Minimum value of 180. Maximum value of 600.
Required: No

 ** HECEndpoint **   <a name="Firehose-Type-SplunkDestinationUpdate-HECEndpoint"></a>
The HTTP Event Collector (HEC) endpoint to which Firehose sends your data.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `.*`
Required: No

 ** HECEndpointType **   <a name="Firehose-Type-SplunkDestinationUpdate-HECEndpointType"></a>
This type can be either "Raw" or "Event."
Type: String
Valid Values: `Raw | Event`
Required: No

 ** HECToken **   <a name="Firehose-Type-SplunkDestinationUpdate-HECToken"></a>
A GUID that you obtain from your Splunk cluster when you create a new HEC endpoint.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `.*`
Required: No

 ** ProcessingConfiguration **   <a name="Firehose-Type-SplunkDestinationUpdate-ProcessingConfiguration"></a>
The data processing configuration.
Type: [ProcessingConfiguration](API_ProcessingConfiguration.md) object
Required: No

 ** RetryOptions **   <a name="Firehose-Type-SplunkDestinationUpdate-RetryOptions"></a>
The retry behavior in case Firehose is unable to deliver data to Splunk or if it doesn't receive an acknowledgment of receipt from Splunk.
Type: [SplunkRetryOptions](API_SplunkRetryOptions.md) object
Required: No

 ** S3BackupMode **   <a name="Firehose-Type-SplunkDestinationUpdate-S3BackupMode"></a>
Specifies how you want Firehose to back up documents to Amazon S3. When set to `FailedDocumentsOnly`, Firehose writes any data that could not be indexed to the configured Amazon S3 destination. When set to `AllEvents`, Firehose delivers all incoming records to Amazon S3, and also writes failed documents to Amazon S3. The default value is `FailedEventsOnly`.
You can update this backup mode from `FailedEventsOnly` to `AllEvents`. You can't update it from `AllEvents` to `FailedEventsOnly`.
Type: String
Valid Values: `FailedEventsOnly | AllEvents`
Required: No

 ** S3Update **   <a name="Firehose-Type-SplunkDestinationUpdate-S3Update"></a>
Your update to the configuration of the backup Amazon S3 location.
Type: [S3DestinationUpdate](API_S3DestinationUpdate.md) object
Required: No

 ** SecretsManagerConfiguration **   <a name="Firehose-Type-SplunkDestinationUpdate-SecretsManagerConfiguration"></a>
 The configuration that defines how you access secrets for Splunk.
Type: [SecretsManagerConfiguration](API_SecretsManagerConfiguration.md) object
Required: No

## See Also
<a name="API_SplunkDestinationUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/firehose-2015-08-04/SplunkDestinationUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/firehose-2015-08-04/SplunkDestinationUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/firehose-2015-08-04/SplunkDestinationUpdate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Data Firehose. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query firehose` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
