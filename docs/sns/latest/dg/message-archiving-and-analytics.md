---
source_url: https://docs.aws.amazon.com/sns/latest/dg/message-archiving-and-analytics.html
---

# Amazon SNS message archiving, replay, and analytics
<a name="message-archiving-and-analytics"></a>

Amazon SNS standard topics support message archiving through . You can fan out notifications to Firehose delivery streams, which allows you to send notifications to storage and analytics destinations that Firehose supports, including Amazon Simple Storage Service (Amazon S3), Amazon Redshift, and more.

Amazon SNS FIFO topics support an in-place, no-code, message archive that lets topic owners store (or *archive*) messages published to a topic for up to 365 days. For topics with an active `ArchivePolicy`, subscribers can then create a `ReplayPolicy` to retrieve (or *replay*) the archived messages back to a subscribed endpoint. To learn more about this feature, see [Amazon SNS message archiving and replay for FIFO topics](fifo-message-archiving-replay.md).

| Features | Standard Topics | FIFO Topics |
| --- | --- | --- |
| Message archiving | [Fanout to Firehose delivery streams](sns-firehose-as-subscriber.md) | [Amazon SNS message archiving for FIFO topic owners](message-archiving-and-replay-topic-owner.md) |
| Message replay | Replay for standard topics is not a built in feature. Many customers build their own based on their message archive. | [Amazon SNS message replay for FIFO topic subscribers](message-archiving-and-replay-subscriber.md) |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Notification Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sns` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
