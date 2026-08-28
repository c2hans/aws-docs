---
source_url: https://docs.aws.amazon.com/scheduler/latest/APIReference/API_Target.html
---

# Target
<a name="API_Target"></a>

The schedule's target. EventBridge Scheduler supports templated target that invoke common API operations, as well as universal targets that you can customize to invoke over 6,000 API operations across more than 270 services. You can only specify one templated or universal target for a schedule.

## Contents
<a name="API_Target_Contents"></a>

 ** Arn **   <a name="scheduler-Type-Target-Arn"></a>
The Amazon Resource Name (ARN) of the target.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Required: Yes

 ** RoleArn **   <a name="scheduler-Type-Target-RoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role that EventBridge Scheduler will use for this target when the schedule is invoked.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `arn:aws(-[a-z]+)?:iam::\d{12}:role\/[\w+=,.@\/-]+`
Required: Yes

 ** DeadLetterConfig **   <a name="scheduler-Type-Target-DeadLetterConfig"></a>
An object that contains information about an Amazon SQS queue that EventBridge Scheduler uses as a dead-letter queue for your schedule. If specified, EventBridge Scheduler delivers failed events that could not be successfully delivered to a target to the queue.
Type: [DeadLetterConfig](API_DeadLetterConfig.md) object
Required: No

 ** EcsParameters **   <a name="scheduler-Type-Target-EcsParameters"></a>
The templated target type for the Amazon ECS [`RunTask`](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_RunTask.html) API operation.
Type: [EcsParameters](API_EcsParameters.md) object
Required: No

 ** EventBridgeParameters **   <a name="scheduler-Type-Target-EventBridgeParameters"></a>
The templated target type for the EventBridge [`PutEvents`](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_PutEvents.html) API operation.
Type: [EventBridgeParameters](API_EventBridgeParameters.md) object
Required: No

 ** Input **   <a name="scheduler-Type-Target-Input"></a>
The text, or well-formed JSON, passed to the target. If you are configuring a templated Lambda, AWS Step Functions, or Amazon EventBridge target, the input must be a well-formed JSON. For all other target types, a JSON is not required. If you do not specify anything for this field, EventBridge Scheduler delivers a default notification to the target. The maximum size of the `Input` field is 256 KB.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** KinesisParameters **   <a name="scheduler-Type-Target-KinesisParameters"></a>
The templated target type for the Amazon Kinesis [`PutRecord`](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_PutRecord.html) API operation.
Type: [KinesisParameters](API_KinesisParameters.md) object
Required: No

 ** RetryPolicy **   <a name="scheduler-Type-Target-RetryPolicy"></a>
A `RetryPolicy` object that includes information about the retry policy settings, including the maximum age of an event, and the maximum number of times EventBridge Scheduler will try to deliver the event to a target.
Type: [RetryPolicy](API_RetryPolicy.md) object
Required: No

 ** SageMakerPipelineParameters **   <a name="scheduler-Type-Target-SageMakerPipelineParameters"></a>
The templated target type for the Amazon SageMaker [`StartPipelineExecution`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_StartPipelineExecution.html) API operation.
Type: [SageMakerPipelineParameters](API_SageMakerPipelineParameters.md) object
Required: No

 ** SqsParameters **   <a name="scheduler-Type-Target-SqsParameters"></a>
The templated target type for the Amazon SQS [`SendMessage`](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_SendMessage.html) API operation. Contains the message group ID to use when the target is a FIFO queue. If you specify an Amazon SQS FIFO queue as a target, the queue must have content-based deduplication enabled. For more information, see [Using the Amazon SQS message deduplication ID](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/using-messagededuplicationid-property.html) in the *Amazon SQS Developer Guide*.
Type: [SqsParameters](API_SqsParameters.md) object
Required: No

## See Also
<a name="API_Target_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/scheduler-2021-06-30/Target)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/scheduler-2021-06-30/Target)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/scheduler-2021-06-30/Target)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for EventBridge Scheduler. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query scheduler` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
