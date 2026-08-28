---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference/API_EventDestination.html
---

# EventDestination
<a name="API_EventDestination"></a>

Contains information about an event destination.

**Note**
When you create or update an event destination, you must provide one, and only one, destination. The destination can be Amazon CloudWatch, Amazon Kinesis Firehose or Amazon Simple Notification Service (Amazon SNS).

Event destinations are associated with configuration sets, which enable you to publish email sending events to Amazon CloudWatch, Amazon Kinesis Firehose, or Amazon Simple Notification Service (Amazon SNS). For information about using configuration sets, see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/dg/monitor-sending-activity.html).

## Contents
<a name="API_EventDestination_Contents"></a>

 ** MatchingEventTypes.member.N **
The type of email sending events to publish to the event destination.
+  `send` - The call was successful and Amazon SES is attempting to deliver the email.
+  `reject` - Amazon SES determined that the email contained a virus and rejected it.
+  `bounce` - The recipient's mail server permanently rejected the email. This corresponds to a hard bounce.
+  `complaint` - The recipient marked the email as spam.
+  `delivery` - Amazon SES successfully delivered the email to the recipient's mail server.
+  `open` - The recipient received the email and opened it in their email client.
+  `click` - The recipient clicked one or more links in the email.
+  `renderingFailure` - Amazon SES did not send the email because of a template rendering issue.
Type: Array of strings
Valid Values: `send | reject | bounce | complaint | delivery | open | click | renderingFailure`
Required: Yes

 ** Name **
The name of the event destination. The name must meet the following requirements:
+ Contain only ASCII letters (a-z, A-Z), numbers (0-9), underscores (\_), or dashes (-).
+ Contain 64 characters or fewer.
Type: String
Required: Yes

 ** CloudWatchDestination **
An object that contains the names, default values, and sources of the dimensions associated with an Amazon CloudWatch event destination.
Type: [CloudWatchDestination](API_CloudWatchDestination.md) object
Required: No

 ** Enabled **
Sets whether Amazon SES publishes events to this destination when you send an email with the associated configuration set. Set to `true` to enable publishing to this destination; set to `false` to prevent publishing to this destination. The default value is `false`.
Type: Boolean
Required: No

 ** KinesisFirehoseDestination **
An object that contains the delivery stream ARN and the IAM role ARN associated with an Amazon Kinesis Firehose event destination.
Type: [KinesisFirehoseDestination](API_KinesisFirehoseDestination.md) object
Required: No

 ** SNSDestination **
An object that contains the topic ARN associated with an Amazon Simple Notification Service (Amazon SNS) event destination.
Type: [SNSDestination](API_SNSDestination.md) object
Required: No

## See Also
<a name="API_EventDestination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/email-2010-12-01/EventDestination)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/email-2010-12-01/EventDestination)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/email-2010-12-01/EventDestination)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ses` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
