---
source_url: https://docs.aws.amazon.com/firehose/latest/APIReference/API_SplunkDestinationDescription.html
---

# SplunkDestinationDescription
<a name="API_SplunkDestinationDescription"></a>

Describes a destination in Splunk.

## Contents
<a name="API_SplunkDestinationDescription_Contents"></a>

 ** BufferingHints **   <a name="Firehose-Type-SplunkDestinationDescription-BufferingHints"></a>
The buffering options. If no value is specified, the default values for Splunk are used.
Type: [SplunkBufferingHints](API_SplunkBufferingHints.md) object
Required: No

 ** CloudWatchLoggingOptions **   <a name="Firehose-Type-SplunkDestinationDescription-CloudWatchLoggingOptions"></a>
The Amazon CloudWatch logging options for your Firehose stream.
Type: [CloudWatchLoggingOptions](API_CloudWatchLoggingOptions.md) object
Required: No

 ** HECAcknowledgmentTimeoutInSeconds **   <a name="Firehose-Type-SplunkDestinationDescription-HECAcknowledgmentTimeoutInSeconds"></a>
The amount of time that Firehose waits to receive an acknowledgment from Splunk after it sends it data. At the end of the timeout period, Firehose either tries to send the data again or considers it an error, based on your retry settings.
Type: Integer
Valid Range: Minimum value of 180. Maximum value of 600.
Required: No

 ** HECEndpoint **   <a name="Firehose-Type-SplunkDestinationDescription-HECEndpoint"></a>
The HTTP Event Collector (HEC) endpoint to which Firehose sends your data.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `.*`
Required: No

 ** HECEndpointType **   <a name="Firehose-Type-SplunkDestinationDescription-HECEndpointType"></a>
This type can be either "Raw" or "Event."
Type: String
Valid Values: `Raw | Event`
Required: No

 ** HECToken **   <a name="Firehose-Type-SplunkDestinationDescription-HECToken"></a>
A GUID you obtain from your Splunk cluster when you create a new HEC endpoint.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `.*`
Required: No

 ** ProcessingConfiguration **   <a name="Firehose-Type-SplunkDestinationDescription-ProcessingConfiguration"></a>
The data processing configuration.
Type: [ProcessingConfiguration](API_ProcessingConfiguration.md) object
Required: No

 ** RetryOptions **   <a name="Firehose-Type-SplunkDestinationDescription-RetryOptions"></a>
The retry behavior in case Firehose is unable to deliver data to Splunk or if it doesn't receive an acknowledgment of receipt from Splunk.
Type: [SplunkRetryOptions](API_SplunkRetryOptions.md) object
Required: No

 ** S3BackupMode **   <a name="Firehose-Type-SplunkDestinationDescription-S3BackupMode"></a>
Defines how documents should be delivered to Amazon S3. When set to `FailedDocumentsOnly`, Firehose writes any data that could not be indexed to the configured Amazon S3 destination. When set to `AllDocuments`, Firehose delivers all incoming records to Amazon S3, and also writes failed documents to Amazon S3. Default value is `FailedDocumentsOnly`.
Type: String
Valid Values: `FailedEventsOnly | AllEvents`
Required: No

 ** S3DestinationDescription **   <a name="Firehose-Type-SplunkDestinationDescription-S3DestinationDescription"></a>
The Amazon S3 destination.>
Type: [S3DestinationDescription](API_S3DestinationDescription.md) object
Required: No

 ** SecretsManagerConfiguration **   <a name="Firehose-Type-SplunkDestinationDescription-SecretsManagerConfiguration"></a>
 The configuration that defines how you access secrets for Splunk.
Type: [SecretsManagerConfiguration](API_SecretsManagerConfiguration.md) object
Required: No

## See Also
<a name="API_SplunkDestinationDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/firehose-2015-08-04/SplunkDestinationDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/firehose-2015-08-04/SplunkDestinationDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/firehose-2015-08-04/SplunkDestinationDescription)
