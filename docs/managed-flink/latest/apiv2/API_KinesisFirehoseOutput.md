---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_KinesisFirehoseOutput.html
---

# KinesisFirehoseOutput
<a name="API_KinesisFirehoseOutput"></a>

For a SQL-based Kinesis Data Analytics application, when configuring application output, identifies a Kinesis Data Firehose delivery stream as the destination. You provide the stream Amazon Resource Name (ARN) of the delivery stream.

## Contents
<a name="API_KinesisFirehoseOutput_Contents"></a>

 ** ResourceARN **   <a name="APIReference-Type-KinesisFirehoseOutput-ResourceARN"></a>
The ARN of the destination delivery stream to write to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:.*`
Required: Yes

## See Also
<a name="API_KinesisFirehoseOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/KinesisFirehoseOutput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/KinesisFirehoseOutput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/KinesisFirehoseOutput)
