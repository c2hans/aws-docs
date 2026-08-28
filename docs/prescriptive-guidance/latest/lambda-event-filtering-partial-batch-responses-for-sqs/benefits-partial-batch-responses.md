---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/lambda-event-filtering-partial-batch-responses-for-sqs/benefits-partial-batch-responses.html
---

# Benefits of using partial batch responses for Amazon SQS event sources
<a name="benefits-partial-batch-responses"></a>

Configuring partial batch responses gives your Lambda functions the ability to process partial Amazon SQS message batches and retry only failed messages. This removes the need for repetitive data transfer and increases throughput.

By default, if a Lambda function fails to process one message in an Amazon SQS message batch, then the entire batch returns to the queue. After the [visibility timeout](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-visibility-timeout.html) occurs, the Lambda function then receives the message batch again. If the function fails to process valid messages multiple times, then Amazon SQS sends the messages to your [dead-letter queue](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html), if you've configured one.

Because of this default batch processing behavior, a single failed (*poison-pill*) message can cause a Lambda function to retry a message batch multiple times. These message batch retries can decrease an application's performance—even if your function code is [idempotent](https://aws.amazon.com/premiumsupport/knowledge-center/lambda-function-idempotent/) and capable of handling messages multiple times.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
