---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference/API_SNSDestination.html
---

# SNSDestination
<a name="API_SNSDestination"></a>

Contains the topic ARN associated with an Amazon Simple Notification Service (Amazon SNS) event destination.

Event destinations, such as Amazon SNS, are associated with configuration sets, which enable you to publish email sending events. For information about using configuration sets, see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/dg/monitor-sending-activity.html).

## Contents
<a name="API_SNSDestination_Contents"></a>

 ** TopicARN **
The ARN of the Amazon SNS topic for email sending events. You can find the ARN of a topic by using the [ListTopics](https://docs.aws.amazon.com/sns/latest/api/API_ListTopics.html) Amazon SNS operation.
For more information about Amazon SNS topics, see the [Amazon SNS Developer Guide](https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html).
Type: String
Required: Yes

## See Also
<a name="API_SNSDestination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/email-2010-12-01/SNSDestination)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/email-2010-12-01/SNSDestination)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/email-2010-12-01/SNSDestination)
