---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference/API_BounceAction.html
---

# BounceAction
<a name="API_BounceAction"></a>

When included in a receipt rule, this action rejects the received email by returning a bounce response to the sender and, optionally, publishes a notification to Amazon Simple Notification Service (Amazon SNS).

For information about sending a bounce message in response to a received email, see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/dg/receiving-email-action-bounce.html).

## Contents
<a name="API_BounceAction_Contents"></a>

 ** Message **
Human-readable text to include in the bounce message.
Type: String
Required: Yes

 ** Sender **
The email address of the sender of the bounced email. This is the address from which the bounce message is sent.
Type: String
Required: Yes

 ** SmtpReplyCode **
The SMTP reply code, as defined by [RFC 5321](https://tools.ietf.org/html/rfc5321).
Type: String
Required: Yes

 ** StatusCode **
The SMTP enhanced status code, as defined by [RFC 3463](https://tools.ietf.org/html/rfc3463).
Type: String
Required: No

 ** TopicArn **
The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the bounce action is taken. You can find the ARN of a topic by using the [ListTopics](https://docs.aws.amazon.com/sns/latest/api/API_ListTopics.html) operation in Amazon SNS.
For more information about Amazon SNS topics, see the [Amazon SNS Developer Guide](https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html).
Type: String
Required: No

## See Also
<a name="API_BounceAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/email-2010-12-01/BounceAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/email-2010-12-01/BounceAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/email-2010-12-01/BounceAction)
