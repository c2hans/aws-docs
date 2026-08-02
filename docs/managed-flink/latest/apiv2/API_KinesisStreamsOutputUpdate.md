---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_KinesisStreamsOutputUpdate.html
---

# KinesisStreamsOutputUpdate
<a name="API_KinesisStreamsOutputUpdate"></a>

When you update a SQL-based Kinesis Data Analytics application's output configuration using the [UpdateApplication](API_UpdateApplication.md) operation, provides information about a Kinesis data stream that is configured as the destination.

## Contents
<a name="API_KinesisStreamsOutputUpdate_Contents"></a>

 ** ResourceARNUpdate **   <a name="APIReference-Type-KinesisStreamsOutputUpdate-ResourceARNUpdate"></a>
The Amazon Resource Name (ARN) of the Kinesis data stream where you want to write the output.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:.*`
Required: Yes

## See Also
<a name="API_KinesisStreamsOutputUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/KinesisStreamsOutputUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/KinesisStreamsOutputUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/KinesisStreamsOutputUpdate)
