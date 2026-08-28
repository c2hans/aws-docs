---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/lambda-event-filtering-partial-batch-responses-for-sqs/best-practices-event-filtering.html
---

# Best practices for implementing Lambda event filtering
<a name="best-practices-event-filtering"></a>

The following are best practices for configuring [Lambda event filtering for Amazon SQS event sources](https://aws.amazon.com/about-aws/whats-new/2021/11/aws-lambda-event-filtering-amazon-sqs-dynamodb-kinesis-sources/):
+ Familiarize yourself with the [Lambda service's filter rule syntax](https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventfiltering.html#filtering-syntax)—specifically [the filter rule syntax Lambda uses for Amazon SQS](https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventfiltering.html#filtering-sqs). Then, design an event filter according to your business logic. The effectiveness of any event filter depends on its ability to invoke a Lambda function only when it should. To accomplish this, you must apply the correct syntax to your filter rules so that the rules reflect the needs of your application's business logic.
+ In situations where the application's business logic demands a more complex series of filter conditions, make sure that you use multi-level filtering.** **For more information and example data objects, see [Multi-level filtering](https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventfiltering.html#multi-level-filtering) in the *AWS Lambda Developer Guide*.
+ Limit how long you want Amazon SQS to retain unprocessed messages for by defining the **MessageRetentionPeriod** value in your Amazon SQS request parameters. Make sure that the value you define fits your application's use case by identifying how long it typically takes a valid message to process. For more information, see [SetQueueAttributes](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_SetQueueAttributes.html) in the *Amazon SQS API Reference*. Also, see the **Avoiding non-matching message accumulation** section of this guide.
+ Configure an Amazon SQS [dead-letter queue](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html) in situations where Lambda function unavailability could make it impossible to process valid messages. This extra Amazon SQS queue helps avoid creating a snowball anti-pattern in your serverless application's architecture. For more information, see **Avoiding snowball anti-patterns** in the **Best practices for implementing partial batch responses** section of this guide.
+ Make sure that you activate the event filter feature on the Lambda service. The feature must be activated when you initially create your Lambda function. For instructions, see [Attaching filter criteria to an event source mapping (console)](https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventfiltering.html#filtering-console) or [Attaching filter criteria to an event source mapping (AWS CLI)](https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventfiltering.html#filtering-cli) in the *AWS Lambda Developer Guide*.

## Avoiding non-matching message accumulation
<a name="avoiding-non-matching-message-accumulation"></a>

If an event filter isn't designed appropriately, a high volume of irrelevant messages can quickly overwhelm a Lambda function's Amazon SQS queue. In this scenario, a Lambda function processes all of the messages in an initial message batch, even if few of those messages are relevant. While the function takes longer to process the additional, irrelevant messages, more irrelevant messages are added to the Amazon SQS queue. These new messages cause the function to take even longer to process the next message batch, unless a **MessageRetentionPeriod** parameter is configured. Over time, the number of irrelevant messages in the source queue outnumber the valid messages.

The **MessageRetentionPeriod** parameter limits how long an Amazon SQS queue retains unprocessed messages for in seconds. For example, a **MessageRetentionPeriod** value of 3,600 seconds would remove all of the unprocessed messages from a queue after one hour.

For instructions, see [SetQueueAttributes](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_SetQueueAttributes.html) in the *Amazon SQS API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
