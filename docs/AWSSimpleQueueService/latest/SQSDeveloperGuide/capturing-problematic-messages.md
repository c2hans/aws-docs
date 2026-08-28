---
source_url: https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/capturing-problematic-messages.html
---

# Capturing problematic messages in Amazon SQS
<a name="capturing-problematic-messages"></a>

To capture all messages that can't be processed, and to collect accurate CloudWatch metrics, configure a [dead-letter queue](sqs-dead-letter-queues.md).
+ The redrive policy redirects messages to a dead-letter queue after the source queue fails to process a message a specified number of times.
+ Using a dead-letter queue decreases the number of messages and reduces the possibility of exposing you to *poison pill* messages (messages that are received but can't be processed).
+ Including a poison pill message in a queue can distort the [`ApproximateAgeOfOldestMessage`](sqs-available-cloudwatch-metrics.md) CloudWatch metric by giving an incorrect age of the poison pill message. Configuring a dead-letter queue helps avoid false alarms when using this metric.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Queue Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSSimpleQueueService` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
