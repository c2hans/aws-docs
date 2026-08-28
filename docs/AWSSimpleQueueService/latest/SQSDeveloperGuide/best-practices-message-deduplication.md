---
source_url: https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/best-practices-message-deduplication.html
---

# Amazon SQS message deduplication and grouping
<a name="best-practices-message-deduplication"></a>

This topic provides best practices for ensuring consistent message processing in Amazon SQS. It explains how to use:
+ [`MessageDeduplicationId`](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_SendMessage.html#API_SendMessage_RequestSyntax) to prevent duplicate messages in FIFO queues.
+ [`MessageGroupId`](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_SendMessage.html) to manage message ordering within distinct message groups.

****Topics****
+ [Avoiding inconsistent message processing in Amazon SQS](avoiding-inconsistent-message-processing.md)
+ [Using the message deduplication ID](using-messagededuplicationid-property.md)
+ [Using the message group ID](using-messagegroupid-property.md)
+ [Using the receive request attempt ID](using-receiverequestattemptid-request-parameter.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Queue Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSSimpleQueueService` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
