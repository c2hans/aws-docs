---
source_url: https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-resources-required-process-messages.html
---

# Resources required to process Amazon SQS messages
<a name="sqs-resources-required-process-messages"></a>

Amazon SQS provides estimates of the approximate number of delayed, visible, and not visible messages in a queue to help you assess the resources needed for processing. For more information about visibility, see [Amazon SQS visibility timeout](sqs-visibility-timeout.md).

**Note**
For some metrics, the result is approximate because of the distributed architecture of Amazon SQS. In most cases, the count should be close to the actual number of messages in the queue.

The following table lists the attribute name to use with the `[GetQueueAttributes](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_GetQueueAttributes.html)` action:

| Task | Attribute name |
| --- | --- |
| Get the approximate number of messages available for retrieval from the queue. | ApproximateNumberOfMessagesVisible |
| Get the approximate number of messages in the queue that are delayed and not available for reading immediately. This can happen when the queue is configured as a delay queue or when a message has been sent with a delay parameter.  | ApproximateNumberOfMessagesDelayed |
| Get the approximate number of messages that are in flight. Messages are considered to be in flight if they have been sent to a client but have not yet been deleted or have not yet reached the end of their visibility window. | ApproximateNumberOfMessagesNotVisible |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Queue Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSSimpleQueueService` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
