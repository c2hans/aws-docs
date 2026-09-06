---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_KinesisFirehoseOutputUpdate.html
---

# KinesisFirehoseOutputUpdate
<a name="API_KinesisFirehoseOutputUpdate"></a>

For a SQL-based Kinesis Data Analytics application, when updating an output configuration using the [UpdateApplication](API_UpdateApplication.md) operation, provides information about a Kinesis Data Firehose delivery stream that is configured as the destination.

## Contents
<a name="API_KinesisFirehoseOutputUpdate_Contents"></a>

 ** ResourceARNUpdate **   <a name="APIReference-Type-KinesisFirehoseOutputUpdate-ResourceARNUpdate"></a>
The Amazon Resource Name (ARN) of the delivery stream to write to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:.*`
Required: Yes

## See Also
<a name="API_KinesisFirehoseOutputUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/KinesisFirehoseOutputUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/KinesisFirehoseOutputUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/KinesisFirehoseOutputUpdate)
