---
source_url: https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/using-messagededuplicationid-property.html
---

# Using the message deduplication ID in Amazon SQS
<a name="using-messagededuplicationid-property"></a>

[`MessageDeduplicationId`](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_SendMessage.html) is a token used only in Amazon SQS FIFO queues to prevent duplicate message delivery. It ensures that within a 5-minute deduplication window, only one instance of a message with the same deduplication ID is processed and delivered.

If Amazon SQS has already accepted a message with a specific deduplication ID, any subsequent messages with the same ID will be acknowledged but not delivered to consumers.

**Note**
Amazon SQS continues tracking the deduplication ID even after the message has been received and deleted.

**Topics**
+ [When to provide a message deduplication ID in Amazon SQS](providing-message-deduplication-id.md)
+ [Enabling deduplication for a single-producer/consumer system in Amazon SQS](single-producer-single-consumer.md)
+ [Outage recovery scenarios in Amazon SQS](designing-for-outage-recovery-scenarios.md)
+ [Configuring visibility timeouts in Amazon SQS](working-with-visibility-timeouts.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Queue Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSSimpleQueueService` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
