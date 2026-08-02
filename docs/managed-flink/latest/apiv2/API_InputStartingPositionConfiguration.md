---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_InputStartingPositionConfiguration.html
---

# InputStartingPositionConfiguration
<a name="API_InputStartingPositionConfiguration"></a>

Describes the point at which the application reads from the streaming source.

## Contents
<a name="API_InputStartingPositionConfiguration_Contents"></a>

 ** InputStartingPosition **   <a name="APIReference-Type-InputStartingPositionConfiguration-InputStartingPosition"></a>
The starting position on the stream.
+  `NOW` - Start reading just after the most recent record in the stream, and start at the request timestamp that the customer issued.
+  `TRIM_HORIZON` - Start reading at the last untrimmed record in the stream, which is the oldest record available in the stream. This option is not available for an Amazon Kinesis Data Firehose delivery stream.
+  `LAST_STOPPED_POINT` - Resume reading from where the application last stopped reading.
Type: String
Valid Values: `NOW | TRIM_HORIZON | LAST_STOPPED_POINT`
Required: No

## See Also
<a name="API_InputStartingPositionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/InputStartingPositionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/InputStartingPositionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/InputStartingPositionConfiguration)
