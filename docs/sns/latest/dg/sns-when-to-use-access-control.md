---
source_url: https://docs.aws.amazon.com/sns/latest/dg/sns-when-to-use-access-control.html
---

# Amazon SNS access control use cases
<a name="sns-when-to-use-access-control"></a>

You have a great deal of flexibility in how you grant or deny access to a resource. However, the typical use cases are fairly simple:
+ You want to grant another AWS account a particular type of topic action (for example, Publish). For more information, see [Grant AWS account access to a topic](sns-access-policy-use-cases.md#sns-grant-aws-account-access-to-topic).
+ You want to limit subscriptions to your topic to only the HTTPS protocol. For more information, see [Limit subscriptions to HTTPS](sns-access-policy-use-cases.md#sns-limit-subscriptions-to-https).
+ You want to allow Amazon SNS to publish messages to your Amazon SQS queue. For more information, see [Publish messages to an Amazon SQS queue](sns-access-policy-use-cases.md#sns-publish-messages-to-sqs-queue).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Notification Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sns` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
