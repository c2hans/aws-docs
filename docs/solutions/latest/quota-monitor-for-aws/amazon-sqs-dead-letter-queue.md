---
source_url: https://docs.aws.amazon.com/solutions/latest/quota-monitor-for-aws/amazon-sqs-dead-letter-queue.html
---

# Amazon SQS dead-letter queue
<a name="amazon-sqs-dead-letter-queue"></a>

The Quota Monitor for AWS solution deploys an Amazon SQS [dead-letter queue](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html). The `Summarizer` Lambda function, and other Lambda functions in the spoke accounts, attempt to process messages three times. If it cannot process the message after three attempts, it sends the message to the dead-letter queue where you can debug.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Quota Monitor for AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
