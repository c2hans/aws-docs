---
source_url: https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/providing-message-deduplication-id.html
---

# When to provide a message deduplication ID in Amazon SQS
<a name="providing-message-deduplication-id"></a>

A producer should specify a message deduplication ID in the following scenarios:
+ When sending identical message bodies that must be treated as unique.
+ When sending messages with the same content but different message attributes, ensuring each message is processed separately.
+ When sending messages with different content (for example, a retry counter in the message body) but requiring Amazon SQS to recognize them as duplicates.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Queue Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSSimpleQueueService` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
