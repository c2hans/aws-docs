---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_KinesisFirehoseInput.html
---

# KinesisFirehoseInput
<a name="API_KinesisFirehoseInput"></a>

For a SQL-based Kinesis Data Analytics application, identifies a Kinesis Data Firehose delivery stream as the streaming source. You provide the delivery stream's Amazon Resource Name (ARN).

## Contents
<a name="API_KinesisFirehoseInput_Contents"></a>

 ** ResourceARN **   <a name="APIReference-Type-KinesisFirehoseInput-ResourceARN"></a>
The Amazon Resource Name (ARN) of the delivery stream.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:.*`
Required: Yes

## See Also
<a name="API_KinesisFirehoseInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/KinesisFirehoseInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/KinesisFirehoseInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/KinesisFirehoseInput)
