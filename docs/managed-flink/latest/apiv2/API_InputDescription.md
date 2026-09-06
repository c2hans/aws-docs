---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_InputDescription.html
---

# InputDescription
<a name="API_InputDescription"></a>

Describes the application input configuration for a SQL-based Kinesis Data Analytics application.

## Contents
<a name="API_InputDescription_Contents"></a>

 ** InAppStreamNames **   <a name="APIReference-Type-InputDescription-InAppStreamNames"></a>
Returns the in-application stream names that are mapped to the stream source.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[^-\s<>&]*`
Required: No

 ** InputId **   <a name="APIReference-Type-InputDescription-InputId"></a>
The input ID that is associated with the application input. This is the ID that Kinesis Data Analytics assigns to each input configuration that you add to your application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `[a-zA-Z0-9_.-]+`
Required: No

 ** InputParallelism **   <a name="APIReference-Type-InputDescription-InputParallelism"></a>
Describes the configured parallelism (number of in-application streams mapped to the streaming source).
Type: [InputParallelism](API_InputParallelism.md) object
Required: No

 ** InputProcessingConfigurationDescription **   <a name="APIReference-Type-InputDescription-InputProcessingConfigurationDescription"></a>
The description of the preprocessor that executes on records in this input before the application's code is run.
Type: [InputProcessingConfigurationDescription](API_InputProcessingConfigurationDescription.md) object
Required: No

 ** InputSchema **   <a name="APIReference-Type-InputDescription-InputSchema"></a>
Describes the format of the data in the streaming source, and how each data element maps to corresponding columns in the in-application stream that is being created.
Type: [SourceSchema](API_SourceSchema.md) object
Required: No

 ** InputStartingPositionConfiguration **   <a name="APIReference-Type-InputDescription-InputStartingPositionConfiguration"></a>
The point at which the application is configured to read from the input stream.
Type: [InputStartingPositionConfiguration](API_InputStartingPositionConfiguration.md) object
Required: No

 ** KinesisFirehoseInputDescription **   <a name="APIReference-Type-InputDescription-KinesisFirehoseInputDescription"></a>
If a Kinesis Data Firehose delivery stream is configured as a streaming source, provides the delivery stream's ARN.
Type: [KinesisFirehoseInputDescription](API_KinesisFirehoseInputDescription.md) object
Required: No

 ** KinesisStreamsInputDescription **   <a name="APIReference-Type-InputDescription-KinesisStreamsInputDescription"></a>
If a Kinesis data stream is configured as a streaming source, provides the Kinesis data stream's Amazon Resource Name (ARN).
Type: [KinesisStreamsInputDescription](API_KinesisStreamsInputDescription.md) object
Required: No

 ** NamePrefix **   <a name="APIReference-Type-InputDescription-NamePrefix"></a>
The in-application name prefix.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[^-\s<>&]*`
Required: No

## See Also
<a name="API_InputDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/InputDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/InputDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/InputDescription)
