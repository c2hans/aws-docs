---
source_url: https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/avoding-processing-duplicates-in-multiple-producer-consumer-system.html
---

# Preventing duplicate processing in a multiple-producer/consumer system in Amazon SQS
<a name="avoding-processing-duplicates-in-multiple-producer-consumer-system"></a>

In a high-throughput, low-latency system where message ordering is not a priority, producers can assign a unique [`MessageGroupId`](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_SendMessage.html) to each message. This ensures that Amazon SQS FIFO queues eliminate duplicates, even in a multiple-producer/multiple-consumer setup. While this approach prevents duplicate messages, it does not guarantee message ordering since each message is treated as its own independent group.

In any system with multiple producers and consumers, there is always a risk of duplicate delivery. If a consumer fails to process a message before the visibility timeout expires, Amazon SQS makes the message available again, potentially allowing another consumer to pick it up. To mitigate this, ensure proper message acknowledgment and visibility timeout settings based on processing time.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Queue Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSSimpleQueueService` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
