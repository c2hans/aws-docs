---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_Output.html
---

# Output
<a name="API_Output"></a>

 Describes a SQL-based Kinesis Data Analytics application's output configuration, in which you identify an in-application stream and a destination where you want the in-application stream data to be written. The destination can be a Kinesis data stream or a Kinesis Data Firehose delivery stream.

## Contents
<a name="API_Output_Contents"></a>

 ** DestinationSchema **   <a name="APIReference-Type-Output-DestinationSchema"></a>
Describes the data format when records are written to the destination.
Type: [DestinationSchema](API_DestinationSchema.md) object
Required: Yes

 ** Name **   <a name="APIReference-Type-Output-Name"></a>
The name of the in-application stream.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[^-\s<>&]*`
Required: Yes

 ** KinesisFirehoseOutput **   <a name="APIReference-Type-Output-KinesisFirehoseOutput"></a>
Identifies a Kinesis Data Firehose delivery stream as the destination.
Type: [KinesisFirehoseOutput](API_KinesisFirehoseOutput.md) object
Required: No

 ** KinesisStreamsOutput **   <a name="APIReference-Type-Output-KinesisStreamsOutput"></a>
Identifies a Kinesis data stream as the destination.
Type: [KinesisStreamsOutput](API_KinesisStreamsOutput.md) object
Required: No

 ** LambdaOutput **   <a name="APIReference-Type-Output-LambdaOutput"></a>
Identifies an Amazon Lambda function as the destination.
Type: [LambdaOutput](API_LambdaOutput.md) object
Required: No

## See Also
<a name="API_Output_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/Output)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/Output)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/Output)
