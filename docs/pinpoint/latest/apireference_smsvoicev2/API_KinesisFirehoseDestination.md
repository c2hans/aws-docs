---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_KinesisFirehoseDestination.html
---

# KinesisFirehoseDestination
<a name="API_KinesisFirehoseDestination"></a>

Contains the delivery stream Amazon Resource Name (ARN), and the ARN of the AWS Identity and Access Management (IAM) role associated with a Firehose event destination.

Event destinations, such as Firehose, are associated with configuration sets, which enable you to publish message sending events.

## Contents
<a name="API_KinesisFirehoseDestination_Contents"></a>

 ** DeliveryStreamArn **   <a name="pinpoint-Type-KinesisFirehoseDestination-DeliveryStreamArn"></a>
The Amazon Resource Name (ARN) of the delivery stream.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:\S+`
Required: Yes

 ** IamRoleArn **   <a name="pinpoint-Type-KinesisFirehoseDestination-IamRoleArn"></a>
The ARN of an AWS Identity and Access Management role that is able to write event data to an Amazon Data Firehose destination.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:\S+`
Required: Yes

## See Also
<a name="API_KinesisFirehoseDestination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/KinesisFirehoseDestination)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/KinesisFirehoseDestination)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/KinesisFirehoseDestination)
