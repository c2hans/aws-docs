---
source_url: https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/single-producer-single-consumer.html
---

# Enabling deduplication for a single-producer/consumer system in Amazon SQS
<a name="single-producer-single-consumer"></a>

If you have a single producer and a single consumer, and messages are unique because they include an application-specific message ID in the body, follow these best practices:
+ Enable content-based deduplication for the queue (each of your messages has a unique body). The producer can omit the message deduplication ID.
+ When content-based deduplication is enabled for an Amazon SQS FIFO queue, and a message is sent with a deduplication ID, the [`SendMessage`](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_SendMessage.html) deduplication ID overrides the generated content-based deduplication ID.
+ Although the consumer isn't required to provide a receive request attempt ID for each request, it's a best practice because it allows fail-retry sequences to execute faster.
+ You can retry send or receive requests because they don't interfere with the ordering of messages in FIFO queues.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Queue Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSSimpleQueueService` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
