---
source_url: https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/dead-letter-queues-alarms-cloudwatch.html
---

# Creating alarms for dead-letter queues using Amazon CloudWatch
<a name="dead-letter-queues-alarms-cloudwatch"></a>

Set up a CloudWatch alarm to monitor messages in a dead-letter queue using the [`ApproximateNumberOfMessagesVisible`](sqs-available-cloudwatch-metrics.md) metric. For detailed instructions, see [Creating CloudWatch alarms for Amazon SQS metrics](set-cloudwatch-alarms-for-metrics.md). When the alarm triggers, indicating messages have been moved to the dead-letter queue, you can [poll](sqs-short-and-long-polling.md) the queue to review and retrieve them.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Queue Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSSimpleQueueService` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
