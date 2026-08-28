---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference/API_KinesisFirehoseDestination.html
---

# KinesisFirehoseDestination
<a name="API_KinesisFirehoseDestination"></a>

Contains the delivery stream ARN and the IAM role ARN associated with an Amazon Kinesis Firehose event destination.

Event destinations, such as Amazon Kinesis Firehose, are associated with configuration sets, which enable you to publish email sending events. For information about using configuration sets, see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/dg/monitor-sending-activity.html).

## Contents
<a name="API_KinesisFirehoseDestination_Contents"></a>

 ** DeliveryStreamARN **
The ARN of the Amazon Kinesis Firehose stream that email sending events should be published to.
Type: String
Required: Yes

 ** IAMRoleARN **
The ARN of the IAM role under which Amazon SES publishes email sending events to the Amazon Kinesis Firehose stream.
Type: String
Required: Yes

## See Also
<a name="API_KinesisFirehoseDestination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/email-2010-12-01/KinesisFirehoseDestination)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/email-2010-12-01/KinesisFirehoseDestination)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/email-2010-12-01/KinesisFirehoseDestination)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ses` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
