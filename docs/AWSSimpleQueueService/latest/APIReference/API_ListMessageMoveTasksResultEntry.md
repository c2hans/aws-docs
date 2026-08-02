---
source_url: https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ListMessageMoveTasksResultEntry.html
---

# ListMessageMoveTasksResultEntry
<a name="API_ListMessageMoveTasksResultEntry"></a>

Contains the details of a message movement task.

## Contents
<a name="API_ListMessageMoveTasksResultEntry_Contents"></a>

 ** ApproximateNumberOfMessagesMoved **   <a name="SQS-Type-ListMessageMoveTasksResultEntry-ApproximateNumberOfMessagesMoved"></a>
The approximate number of messages already moved to the destination queue.
Type: Long
Required: No

 ** ApproximateNumberOfMessagesToMove **   <a name="SQS-Type-ListMessageMoveTasksResultEntry-ApproximateNumberOfMessagesToMove"></a>
The number of messages to be moved from the source queue. This number is obtained at the time of starting the message movement task and is only included after the message movement task is selected to start.
Type: Long
Required: No

 ** DestinationArn **   <a name="SQS-Type-ListMessageMoveTasksResultEntry-DestinationArn"></a>
The ARN of the destination queue if it has been specified in the `StartMessageMoveTask` request. If a `DestinationArn` has not been specified in the `StartMessageMoveTask` request, this field value will be NULL.
Type: String
Required: No

 ** FailureReason **   <a name="SQS-Type-ListMessageMoveTasksResultEntry-FailureReason"></a>
The task failure reason (only included if the task status is FAILED).
Type: String
Required: No

 ** MaxNumberOfMessagesPerSecond **   <a name="SQS-Type-ListMessageMoveTasksResultEntry-MaxNumberOfMessagesPerSecond"></a>
The number of messages to be moved per second (the message movement rate), if it has been specified in the `StartMessageMoveTask` request. If a `MaxNumberOfMessagesPerSecond` has not been specified in the `StartMessageMoveTask` request, this field value will be NULL.
Type: Integer
Required: No

 ** SourceArn **   <a name="SQS-Type-ListMessageMoveTasksResultEntry-SourceArn"></a>
The ARN of the queue that contains the messages to be moved to another queue.
Type: String
Required: No

 ** StartedTimestamp **   <a name="SQS-Type-ListMessageMoveTasksResultEntry-StartedTimestamp"></a>
The timestamp of starting the message movement task.
Type: Long
Required: No

 ** Status **   <a name="SQS-Type-ListMessageMoveTasksResultEntry-Status"></a>
The status of the message movement task. Possible values are: RUNNING, COMPLETED, CANCELLING, CANCELLED, and FAILED.
Type: String
Required: No

 ** TaskHandle **   <a name="SQS-Type-ListMessageMoveTasksResultEntry-TaskHandle"></a>
An identifier associated with a message movement task. When this field is returned in the response of the `ListMessageMoveTasks` action, it is only populated for tasks that are in RUNNING status.
Type: String
Required: No

## See Also
<a name="API_ListMessageMoveTasksResultEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sqs-2012-11-05/ListMessageMoveTasksResultEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sqs-2012-11-05/ListMessageMoveTasksResultEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sqs-2012-11-05/ListMessageMoveTasksResultEntry)
