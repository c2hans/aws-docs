---
source_url: https://docs.aws.amazon.com/kinesis/latest/APIReference/API_CreateQueue.html
---

# CreateQueue

Creates a queue on the specified data stream. A queue delivers records from the stream to a queue consumer, tracks the delivery state of each record, and redelivers any record that is not acknowledged before its visibility timeout expires.

A queue does not extend how long the stream keeps a record. When a record reaches the end of the data stream's retention period, the queue stops delivering it.

Your queue consumer calls [ReceiveQueueRecords](API_ReceiveQueueRecords.md) to receive up to 10 records at a time. After it processes records, it calls [AcknowledgeQueueRecords](API_AcknowledgeQueueRecords.md) so the queue does not deliver them again.

Queues are supported only on data streams in on-demand capacity mode.

Creating a queue does not change how producers write to the stream, and it does not change how existing stream consumers read from it. A queue counts as a registered consumer on the stream and shares the stream's registered consumer limit with enhanced fan-out consumers: 20 on On-demand Standard and 50 on On-demand Advantage.

Use `StartingPosition` to set the position in the stream where delivery begins. The default is `LATEST`.

 `CreateQueue` is an asynchronous operation. Upon receiving a `CreateQueue` request, Amazon Kinesis Data Streams immediately returns a queue description with a `QueueStatus` of `CREATING`. After the queue is created, Kinesis Data Streams sets the `QueueStatus` to `ACTIVE`. You can begin receiving records after the queue is `ACTIVE`. Use [DescribeQueue](API_DescribeQueue.md) to check the status of the queue.

Each queue has built-in dead-letter handling. When a record has been received `MaxReceiveCount` times without being acknowledged, it becomes a dead-letter record, and [ReceiveQueueRecords](API_ReceiveQueueRecords.md) no longer returns it. You work with dead-letter records through a separate set of operations that use the same queue ARN: [ReceiveDeadLetterQueueRecords](API_ReceiveDeadLetterQueueRecords.md), [AcknowledgeDeadLetterQueueRecords](API_AcknowledgeDeadLetterQueueRecords.md), [UpdateDeadLetterQueueRecordsVisibility](API_UpdateDeadLetterQueueRecordsVisibility.md), and [RestoreDeadLetterQueueRecords](API_RestoreDeadLetterQueueRecords.md).

Dead-letter handling is enabled by default, with a `MaxReceiveCount` of 6. To use a different value, or to turn dead-letter handling off, specify `DeadLetterConfiguration` in `QueueAttributes`.

## Request Syntax
<a name="API_CreateQueue_RequestSyntax"></a>

```
{
   "QueueAttributes": {
      "DeadLetterConfiguration": {
         "MaxReceiveCount": {{number}},
         "TargetType": "{{string}}"
      },
      "VisibilityTimeoutSeconds": {{number}}
   },
   "QueueName": "{{string}}",
   "StreamConfigurationList": [
      {
         "StartingPosition": {
            "Timestamp": {{number}},
            "Type": "{{string}}"
         },
         "StreamARN": "{{string}}"
      }
   ],
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## Request Parameters
<a name="API_CreateQueue_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [QueueAttributes](#API_CreateQueue_RequestSyntax) **   <a name="Streams-CreateQueue-request-QueueAttributes"></a>
The configuration attributes for the queue, including its visibility timeout and its dead-letter handling configuration.
Type: [QueueAttributes](API_QueueAttributes.md) object
Required: No

 ** [QueueName](#API_CreateQueue_RequestSyntax) **   <a name="Streams-CreateQueue-request-QueueName"></a>
A name for the queue. The name is scoped to the AWS account and Region used by the request, so two queues in different accounts, or in the same account and different Regions, can have the same name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** [StreamConfigurationList](#API_CreateQueue_RequestSyntax) **   <a name="Streams-CreateQueue-request-StreamConfigurationList"></a>
The data stream the queue delivers records from, and the position in that stream where delivery begins. The list must contain exactly one entry, because a queue delivers records from a single data stream.
Type: Array of [QueueStreamConfiguration](API_QueueStreamConfiguration.md) objects
Array Members: Fixed number of 1 item.
Required: Yes

 ** [Tags](#API_CreateQueue_RequestSyntax) **   <a name="Streams-CreateQueue-request-Tags"></a>
A set of up to 50 key-value pairs to apply to the queue. You can also add, change, and remove tags after the queue is created with [TagResource](API_TagResource.md) and [UntagResource](API_UntagResource.md).
Type: String to string map
Map Entries: Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateQueue_ResponseSyntax"></a>

```
{
   "QueueDescription": {
      "QueueARN": "string",
      "QueueAttributes": {
         "DeadLetterConfiguration": {
            "MaxReceiveCount": number,
            "TargetType": "string"
         },
         "VisibilityTimeoutSeconds": number
      },
      "QueueCreationTimestamp": number,
      "QueueName": "string",
      "QueueStatus": "string",
      "StreamConfigurationList": [
         {
            "StartingPosition": {
               "Timestamp": number,
               "Type": "string"
            },
            "StreamARN": "string"
         }
      ]
   }
}
```

## Response Elements
<a name="API_CreateQueue_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [QueueDescription](#API_CreateQueue_ResponseSyntax) **   <a name="Streams-CreateQueue-response-QueueDescription"></a>
A description of the queue that was created.
Type: [QueueDescription](API_QueueDescription.md) object

## Errors
<a name="API_CreateQueue_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Specifies that you do not have the permissions required to perform this operation.
HTTP Status Code: 400

 ** InternalFailureException **
The processing of the request failed because of an unknown error, exception, or failure.
HTTP Status Code: 500

 ** InvalidArgumentException **
A specified parameter exceeds its restrictions, is not supported, or can't be used. For more information, see the returned message.
 ** message **
A message that provides information about the error.
HTTP Status Code: 400

 ** LimitExceededException **
The requested resource exceeds the maximum number allowed, or the number of concurrent stream requests exceeds the maximum number allowed.
 ** message **
A message that provides information about the error.
HTTP Status Code: 400

 ** ResourceInUseException **
The resource is not available for this operation. For successful operation, the resource must be in the `ACTIVE` state.
 ** message **
A message that provides information about the error.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The requested resource could not be found. The stream might not be specified correctly.
 ** message **
A message that provides information about the error.
HTTP Status Code: 400

 ** ValidationException **
The request failed validation. For example, a parameter value is not valid, a combination of parameters is not supported, or the operation is not supported for the stream's capacity mode. The error message describes the specific reason.
HTTP Status Code: 400

## See Also
<a name="API_CreateQueue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kinesis-2013-12-02/CreateQueue)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kinesis-2013-12-02/CreateQueue)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesis-2013-12-02/CreateQueue)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kinesis-2013-12-02/CreateQueue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesis-2013-12-02/CreateQueue)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kinesis-2013-12-02/CreateQueue)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kinesis-2013-12-02/CreateQueue)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kinesis-2013-12-02/CreateQueue)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/kinesis-2013-12-02/CreateQueue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesis-2013-12-02/CreateQueue)
