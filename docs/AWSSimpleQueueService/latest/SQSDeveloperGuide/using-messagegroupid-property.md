---
source_url: https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/using-messagegroupid-property.html
---

# Using the message group ID with Amazon SQS FIFO Queues
<a name="using-messagegroupid-property"></a>

In FIFO (First-In-First-Out) queues, [`MessageGroupId`](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_SendMessage.html) is an attribute that organizes messages into distinct groups. Messages within the same message group are always processed one at a time, in strict order, ensuring that no two messages from the same group are processed simultaneously. In standard queues, using `MessageGroupId` enables [fair queues](sqs-fair-queues.md). If strict ordering is required, use a FIFO queue.

**Topics**
+ [Interleaving multiple ordered message groups in Amazon SQS](interleaving-multiple-ordered-message-groups.md)
+ [Preventing duplicate processing in a multiple-producer/consumer system in Amazon SQS](avoding-processing-duplicates-in-multiple-producer-consumer-system.md)
+ [Avoid large message backlogs with the same message group ID in Amazon SQS](avoid-backlog-with-the-same-message-group-id.md)
+ [Avoid reusing the same message group ID with virtual queues in Amazon SQS](avoiding-reusing-message-group-id-with-virtual-queues.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Queue Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSSimpleQueueService` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
