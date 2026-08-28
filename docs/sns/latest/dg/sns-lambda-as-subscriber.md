---
source_url: https://docs.aws.amazon.com/sns/latest/dg/sns-lambda-as-subscriber.html
---

# Fanout Amazon SNS notifications to Lambda functions for automated processing
<a name="sns-lambda-as-subscriber"></a>

Amazon SNS integrates with AWS Lambda, allowing you to trigger Lambda functions in response to Amazon SNS notifications. When a message is published to an Amazon SNS topic that has a Lambda function subscribed to it, the Lambda function is invoked with the payload of the published message. The Lambda function receives the message payload as an input parameter and can manipulate the information in the message, publish the message to other Amazon SNS topics, or send the message to other AWS services.

Amazon SNS also supports message delivery status attributes for message notifications sent to Lambda endpoints. For more information, see [Amazon SNS message delivery status](sns-topic-attributes.md).

**Topics**
+ [Prerequisites](lambda-prereq.md)
+ [Subscribing a function to a topic](lambda-console.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Notification Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sns` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
