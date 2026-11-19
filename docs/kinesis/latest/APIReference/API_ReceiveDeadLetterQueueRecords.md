---
source_url: https://docs.aws.amazon.com/kinesis/latest/APIReference/API_ReceiveDeadLetterQueueRecords.html
---

# ReceiveDeadLetterQueueRecords

Receives up to 10 dead-letter records from the specified queue. Each queue has built-in dead-letter handling: when a record has been received `MaxReceiveCount` times without being acknowledged, it becomes a dead-letter record, which usually means your queue consumer could not process it. The dead-letter record stays in the same queue, and [ReceiveQueueRecords](API_ReceiveQueueRecords.md) no longer returns it.

Dead-letter records carry the same data and partition key as when they were first delivered, and are returned with a receipt handle. Use the receipt handle to acknowledge the record with [AcknowledgeDeadLetterQueueRecords](API_AcknowledgeDeadLetterQueueRecords.md), which discards it, to change its visibility with [UpdateDeadLetterQueueRecordsVisibility](API_UpdateDeadLetterQueueRecordsVisibility.md), or to restore it with [RestoreDeadLetterQueueRecords](API_RestoreDeadLetterQueueRecords.md), which returns it to the normal receive path so that [ReceiveQueueRecords](API_ReceiveQueueRecords.md) can return it again.

Use this operation to inspect the records your queue consumer could not process, so you can correct the cause and then either acknowledge or restore them.

A queue delivers dead-letter records while it is in the `ACTIVE` state.

## Request Syntax
<a name="API_ReceiveDeadLetterQueueRecords_RequestSyntax"></a>

```
{
   "Limit": {{number}},
   "QueueARN": "{{string}}",
   "VisibilityTimeoutSeconds": {{number}},
   "WaitTimeSeconds": {{number}}
}
```

## Request Parameters
<a name="API_ReceiveDeadLetterQueueRecords_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [Limit](#API_ReceiveDeadLetterQueueRecords_RequestSyntax) **   <a name="Streams-ReceiveDeadLetterQueueRecords-request-Limit"></a>
The maximum number of records to return. The queue never returns more dead-letter records than this value, and might return fewer. The default is 10.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 10.
Required: No

 ** [QueueARN](#API_ReceiveDeadLetterQueueRecords_RequestSyntax) **   <a name="Streams-ReceiveDeadLetterQueueRecords-request-QueueARN"></a>
The ARN of the queue whose dead-letter records are received.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws.*:kinesis:.*:\d{12}:queue/\S+`
Required: Yes

 ** [VisibilityTimeoutSeconds](#API_ReceiveDeadLetterQueueRecords_RequestSyntax) **   <a name="Streams-ReceiveDeadLetterQueueRecords-request-VisibilityTimeoutSeconds"></a>
The duration, in seconds, that the records returned by this request are in flight and not visible to any consumer instance. If you do not specify this value, the queue's visibility timeout is used.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 43200.
Required: No

 ** [WaitTimeSeconds](#API_ReceiveDeadLetterQueueRecords_RequestSyntax) **   <a name="Streams-ReceiveDeadLetterQueueRecords-request-WaitTimeSeconds"></a>
The duration, in seconds, that the call waits for a record to become visible before returning. The default is 9.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 20.
Required: No

## Response Syntax
<a name="API_ReceiveDeadLetterQueueRecords_ResponseSyntax"></a>

```
{
   "QueueRecords": [
      {
         "ApproximateArrivalTimestamp": number,
         "Data": blob,
         "FirstReceiveTimestamp": number,
         "PartitionKey": "string",
         "ReceiptHandle": "string",
         "ReceiveCount": number,
         "RecordId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ReceiveDeadLetterQueueRecords_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [QueueRecords](#API_ReceiveDeadLetterQueueRecords_ResponseSyntax) **   <a name="Streams-ReceiveDeadLetterQueueRecords-response-QueueRecords"></a>
The dead-letter records received from the queue. This list is empty when no dead-letter records are visible.
Type: Array of [QueueRecord](API_QueueRecord.md) objects

## Errors
<a name="API_ReceiveDeadLetterQueueRecords_Errors"></a>

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

 ** KMSAccessDeniedException **
The ciphertext references a key that doesn't exist or that you don't have access to.
 ** message **
A message that provides information about the error.
HTTP Status Code: 400

 ** KMSDisabledException **
The request was rejected because the specified KMS key isn't enabled.
 ** message **
A message that provides information about the error.
HTTP Status Code: 400

 ** KMSInvalidStateException **
The request was rejected because the state of the specified resource isn't valid for this request. For more information, see [How Key State Affects Use of a Customer Master Key](https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html) in the * AWS Key Management Service Developer Guide*.
 ** message **
A message that provides information about the error.
HTTP Status Code: 400

 ** KMSNotFoundException **
The request was rejected because the specified entity or resource can't be found.
 ** message **
A message that provides information about the error.
HTTP Status Code: 400

 ** KMSOptInRequired **
The AWS access key ID needs a subscription for the service.
 ** message **
A message that provides information about the error.
HTTP Status Code: 400

 ** KMSThrottlingException **
The request was denied due to request throttling. For more information about throttling, see [Limits](https://docs.aws.amazon.com/kms/latest/developerguide/limits.html#requests-per-second) in the * AWS Key Management Service Developer Guide*.
 ** message **
A message that provides information about the error.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The requested resource could not be found. The stream might not be specified correctly.
 ** message **
A message that provides information about the error.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied because the request rate is too high. Reduce the frequency of your requests, and retry them with exponential backoff.
 ** message **
A message that provides information about the error.
HTTP Status Code: 400

## See Also
<a name="API_ReceiveDeadLetterQueueRecords_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kinesis-2013-12-02/ReceiveDeadLetterQueueRecords)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kinesis-2013-12-02/ReceiveDeadLetterQueueRecords)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesis-2013-12-02/ReceiveDeadLetterQueueRecords)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kinesis-2013-12-02/ReceiveDeadLetterQueueRecords)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesis-2013-12-02/ReceiveDeadLetterQueueRecords)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kinesis-2013-12-02/ReceiveDeadLetterQueueRecords)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kinesis-2013-12-02/ReceiveDeadLetterQueueRecords)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kinesis-2013-12-02/ReceiveDeadLetterQueueRecords)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/kinesis-2013-12-02/ReceiveDeadLetterQueueRecords)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesis-2013-12-02/ReceiveDeadLetterQueueRecords)
