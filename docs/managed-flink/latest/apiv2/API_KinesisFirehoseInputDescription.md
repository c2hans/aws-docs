---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_KinesisFirehoseInputDescription.html
---

# KinesisFirehoseInputDescription
<a name="API_KinesisFirehoseInputDescription"></a>

Describes the Amazon Kinesis Data Firehose delivery stream that is configured as the streaming source in the application input configuration.

## Contents
<a name="API_KinesisFirehoseInputDescription_Contents"></a>

 ** ResourceARN **   <a name="APIReference-Type-KinesisFirehoseInputDescription-ResourceARN"></a>
The Amazon Resource Name (ARN) of the delivery stream.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:.*`
Required: Yes

 ** RoleARN **   <a name="APIReference-Type-KinesisFirehoseInputDescription-RoleARN"></a>
The ARN of the IAM role that Kinesis Data Analytics assumes to access the stream.
Provided for backward compatibility. Applications that are created with the current API version have an application-level service execution role rather than a resource-level role.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:.*`
Required: No

## See Also
<a name="API_KinesisFirehoseInputDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/KinesisFirehoseInputDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/KinesisFirehoseInputDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/KinesisFirehoseInputDescription)
