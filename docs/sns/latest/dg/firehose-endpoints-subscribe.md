---
source_url: https://docs.aws.amazon.com/sns/latest/dg/firehose-endpoints-subscribe.html
---

# Subscribing a Firehose delivery stream to an Amazon SNS topic
<a name="firehose-endpoints-subscribe"></a>

To deliver Amazon SNS notifications to [ delivery streams](sns-firehose-as-subscriber.md), first make sure that you've addressed all the [prerequisites](prereqs-kinesis-data-firehose.md). For a list of supported endpoints, see [ endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/fh.html) in the *Amazon Web Services General Reference*.

**To subscribe a Firehose delivery stream to a topic**

1. Sign in to the [Amazon SNS console](https://console.aws.amazon.com/sns/home).

1. In the navigation pane, choose **Subscriptions**.

1. On the **Subscriptions** page, choose **Create subscription**.

1. On the **Create subscription** page, in the **Details** section, do the following:

   1. For **Topic ARN**, choose the Amazon Resource Name (ARN) of a standard topic.

   1. For **Protocol**, choose **Firehose**.

   1. For **Endpoint**, choose the ARN of a Firehose delivery stream that can receive notifications from Amazon SNS.

   1. For **Subscription role ARN**, specify the ARN of the AWS Identity and Access Management (IAM) role that you created for writing to Firehose delivery streams. For more information, see [Prerequisites for subscribing Firehose delivery streams to Amazon SNS topics](prereqs-kinesis-data-firehose.md).

   1. (Optional) To remove any Amazon SNS metadata from published messages, choose **Enable raw message delivery**. For more information, see [Amazon SNS raw message delivery](sns-large-payload-raw-message-delivery.md).

1. (Optional) To configure a filter policy, expand the **Subscription filter policy** section. For more information, see [Amazon SNS subscription filter policies](sns-subscription-filter-policies.md).

1. (Optional) To configure a dead-letter queue for the subscription, expand the **Redrive policy (dead-letter queue)** section. For more information, see [Amazon SNS dead-letter queues](sns-dead-letter-queues.md).

1. Choose **Create subscription**.

The console creates the subscription and opens the subscription's **Details** page.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Notification Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sns` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
