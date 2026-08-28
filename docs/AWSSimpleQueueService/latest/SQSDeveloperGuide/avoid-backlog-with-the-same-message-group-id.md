---
source_url: https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/avoid-backlog-with-the-same-message-group-id.html
---

# Avoid large message backlogs with the same message group ID in Amazon SQS
<a name="avoid-backlog-with-the-same-message-group-id"></a>

FIFO queues support a maximum of 120,000 in-flight messages (messages received by a consumer but not yet deleted). If this limit is reached, Amazon SQS does not return an error, but processing may be impacted. You can request an increase beyond this limit by contacting [AWS Support](https://docs.aws.amazon.com/awssupport/latest/user/create-service-quota-increase.html).

FIFO queues scan the first 120,000 messages to determine available message groups. If a large backlog builds up in a single message group, messages from other groups sent later will remain blocked until the backlog is processed.

**Note**
A message backlog can occur when a consumer repeatedly fails to process a message. This could be due to message content issues or consumer-side failures. To prevent message processing delays, configure a [dead-letter queue](sqs-dead-letter-queues.md) to move unprocessed messages after multiple failed attempts. This ensures that other messages in the same message group can be processed, preventing system bottlenecks.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Queue Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSSimpleQueueService` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
