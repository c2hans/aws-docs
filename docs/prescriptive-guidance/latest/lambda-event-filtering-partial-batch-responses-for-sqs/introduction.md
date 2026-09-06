---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/lambda-event-filtering-partial-batch-responses-for-sqs/introduction.html
---

# Improve performance using AWS Lambda event filtering and partial batch responses for Amazon SQS
<a name="introduction"></a>

*Alan Oberto Jimenez and Connor Kirkpatrick, Amazon Web Services*

This guide covers best practices for configuring [AWS Lambda event filtering](https://aws.amazon.com/about-aws/whats-new/2021/11/aws-lambda-event-filtering-amazon-sqs-dynamodb-kinesis-sources/) and [partial batch responses](https://aws.amazon.com/about-aws/whats-new/2021/11/aws-lambda-partial-batch-response-sqs-event-source/) for Amazon Simple Queue Service (Amazon SQS) event sources. These controls address two common performance pitfalls associated with Lambda's default message batch processing behavior:
+ **Poison-pill messages** that cause a Lambda function to retry entire Amazon SQS message batches multiple times
+ **Irrelevant Amazon SQS events** that cause a Lambda function to invoke unnecessarily

By setting up these controls, you can configure your Lambda functions to process Amazon SQS message batches more efficiently and improve your serverless application's performance.

## Targeted business outcomes
<a name="business-outcomes"></a>

This guide helps you do the following:
+ Improve your serverless application's user experience by reducing the time it takes for your Lambda functions to process Amazon SQS message batches.
+ Improve your serverless architecture's operational capabilities and overall stability by isolating Amazon SQS messages that your Lambda functions can't process.
+ Reduce the operational cost of your serverless application by lowering the number of unnecessary Lambda function invocations.
+ Simplify your Lambda functions' code to improve their performance when processing Amazon SQS message batches.
