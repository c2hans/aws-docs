---
source_url: https://docs.aws.amazon.com/solutions/latest/quota-monitor-for-aws/amazon-sqs-dead-letter-queue.html
---

# Amazon SQS dead-letter queue
<a name="amazon-sqs-dead-letter-queue"></a>

The Quota Monitor for AWS solution deploys an Amazon SQS [dead-letter queue](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html). The `Summarizer` Lambda function, and other Lambda functions in the spoke accounts, attempt to process messages three times. If it cannot process the message after three attempts, it sends the message to the dead-letter queue where you can debug.
