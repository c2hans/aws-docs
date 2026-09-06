---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/lambda-event-filtering-partial-batch-responses-for-sqs/best-practices-partial-batch-responses.html
---

# Best practices for implementing partial batch responses
<a name="best-practices-partial-batch-responses"></a>

This section provides best practices for configuring partial batch responses for Amazon SQS event sources.
+ Configure a [dead-letter queue](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html) to avoid creating a snowball anti-pattern in your serverless application's architecture. For more information, see the **Avoiding snowball anti-patterns** section.
+ Configure your Lambda function event source mapping to make only failed messages visible. To do this, add **ReportBatchItemFailures** to the **FunctionResponseTypes** list when you configure event source mapping. Your Lambda function, when invoked by SQS, should implement partial batch responses. Consider using the Powertools for AWS Lambda Batch Processing utility, which processes SQS messages with built-in partial-batch support.

## Batch processing
<a name="batch-processing.39aa8cb2-a0de-583e-8fc3-f952d282ee9b"></a>
+ Implement partial batch responses in your Lambda function being invoked by SQS. Consider using the Powertools for AWS Lambda Batch Processing utility. This utility handles SQS message processing with built-in partial batch response support. For more information, see [Reporting batch item failures for Lambda functions with an Amazon SQS trigger](https://docs.aws.amazon.com/lambda/latest/dg/example_serverless_SQS_Lambda_batch_item_failures_section.html) in the *AWS Lambda Developer Guide*.

**Powertools for AWS Lambda Batch Processing Utility**
+ [Powertools for AWS Lambda Batch Processing Utility (Python)](https://docs.aws.amazon.com/powertools/python/latest/utilities/batch/)
+ [Powertools for AWS Lambda Batch Processing Utility (Java)](https://docs.aws.amazon.com/powertools/java/latest/utilities/batch/)
+ [Powertools for AWS Lambda Batch Processing Utility (.Net)](https://docs.aws.amazon.com/powertools/dotnet/utilities/batch-processing/)
+ [Powertools for AWS Lambda Batch Processing Utility (TypeScript)](https://docs.aws.amazon.com/powertools/typescript/latest/features/batch/)

## Idempotency
<a name="idempotency.f5a720a5-edf6-5499-ad24-4b330500346f"></a>
+ Define the number of times that you want a message delivered to the source queue before it's moved to the dead-letter queue. Ensure that the value you define fits your application's use case by identifying the most likely causes of failure and their estimated recovery times. To define the number of retries, configure the **maxReceiveCount** value on the source queue's **RedrivePolicy**. For more information, see [SetQueueAttributes](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_SetQueueAttributes.html) in the *Amazon SQS API Reference*. Also, see [Introducing Amazon Simple Queue Service dead-letter queue redrive to source queues](https://aws.amazon.com/blogs/compute/introducing-amazon-simple-queue-service-dead-letter-queue-redrive-to-source-queues/).
+ Ensure that your Lambda code is idempotent and can handle messages multiple times. To implement idempotency, consider using the Powertools for AWS Lambda Idempotency Utility, which prepares a function's code to support individual jobs inside an Amazon SQS batch. Start by incorporating **ReportBatchItemFailures** in your event source mapping. For more information, see [Implementing partial batch responses](https://docs.aws.amazon.com/lambda/latest/dg/services-sqs-errorhandling.html#services-sqs-batchfailurereporting) in the *AWS Lambda Developer Guide* and [How can I prevent an Amazon SQS message from invoking my Lambda function more than once?](https://aws.amazon.com/premiumsupport/knowledge-center/lambda-function-process-sqs-messages/)

**Powertools for AWS Lambda Idempotency Utility**
+ [Powertools for AWS Lambda Idempotency Utility (Python)](https://docs.aws.amazon.com/powertools/python/latest/utilities/idempotency/)
+ [Powertools for AWS Lambda Idempotency Utility (Java)](https://docs.aws.amazon.com/powertools/java/latest/utilities/idempotency/)
+ [Powertools for AWS Lambda Idempotency Utility (.Net)](https://docs.aws.amazon.com/powertools/dotnet/utilities/idempotency/)
+ [Powertools for AWS Lambda Idempotency Utility (Typescript)](https://docs.aws.amazon.com/powertools/typescript/latest/features/idempotency/)

## Metrics
<a name="metrics.49767344-bfcf-5b9d-851b-97c9cf492614"></a>
+ To incorporate business metrics in your function to track job details and failed jobs, consider using **aws-embedded-metrics** or the Powertools for AWS Lambda Metrics Utility, which emits operational and business metrics while processing SQS events in [embedded metric format](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Embedded_Metric_Format_Libraries.html).

**Powertools for AWS Lambda Metrics Utility**
+ [Powertools for AWS Lambda Metrics Utility (Python)](https://docs.aws.amazon.com/powertools/python/latest/core/metrics/)
+ [Powertools for AWS Lambda Metrics Utility (Java)](https://docs.aws.amazon.com/powertools/java/latest/core/metrics/)
+ [Powertools for AWS Lambda Metrics Utility (.Net)](https://docs.aws.amazon.com/powertools/dotnet/core/metrics/)
+ [Powertools for AWS Lambda Metrics Utility (Typescript)](https://docs.aws.amazon.com/powertools/typescript/latest/features/metrics/)
+ If you use a [First-In-First-Out (FIFO) queue](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-fifo-queues.html), your function should stop processing messages after the first failure and return all failed and unprocessed messages in **batchItemFailures**. This helps preserve the message order of your queue.

**Note**
To track the overall performance of an application that uses partial-batch processing, code-level performance tracking is required. After batch processing is configured, Lambda function invocations usually succeed regardless of the processing result.

### Avoiding snowball anti-patterns
<a name="avoiding-snowball-anti-patterns"></a>

Lambda and Amazon SQS can't control the messages that upstream microservices write to an SQS queue. If there are messages that can't be processed, Lambda returns those unprocessed messages to the source SQS queue unless a separate dead-letter queue is configured. Unprocessed messages are then retried by the Lambda function. If no dead-letter queue exists, the number of unprocessed messages returned to the Amazon SQS queue eventually outnumbers the queue's valid messages.

This type of snowball anti-pattern—where each successive Lambda invocation worsens the problem—can cause the following issues:
+ **Poor user experience** because the jobs don't process or take longer than usual to process
+ **Increased cost** proportional to the exponentially increasing number of messages in the Amazon SQS queue and message retries
+ Reduced Lambda computing capacity for the application or AWS account [if the function doesn't have a limit on its invocation requests](https://docs.aws.amazon.com/lambda/latest/operatorguide/throttling.html)

To avoid creating a snowball anti-pattern when configuring partial batch responses, it's best to also create a dead-letter queue. This separate queue can store messages that aren't processed successfully and help you better manage the lifecycle of your application's unprocessed messages.

For more information, see [Configure a dead-letter queue using the Amazon SQS console](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-configure-dead-letter-queue.html) in the *Amazon SQS Developer Guide*.
