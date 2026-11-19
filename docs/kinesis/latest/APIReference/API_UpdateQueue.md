---
source_url: https://docs.aws.amazon.com/kinesis/latest/APIReference/API_UpdateQueue.html
---

# UpdateQueue

Updates the configuration attributes of the specified queue. You can change the queue's visibility timeout, its dead-letter handling configuration, or both.

A new visibility timeout applies to records received after the update completes. Records that are already in flight keep the visibility timeout they were received with. To change the visibility timeout of a record that is already in flight, use [UpdateQueueRecordsVisibility](API_UpdateQueueRecordsVisibility.md).

 `UpdateQueue` is an asynchronous operation. Upon receiving an `UpdateQueue` request, Amazon Kinesis Data Streams sets the `QueueStatus` to `UPDATING`, and sets it back to `ACTIVE` when the update is complete. You can continue to receive and acknowledge records while the queue is `UPDATING`.

You can't change the data stream or the starting position of a queue after you create it. To read from a different stream or position, create a new queue.

## Request Syntax
<a name="API_UpdateQueue_RequestSyntax"></a>

```
{
   "QueueARN": "{{string}}",
   "QueueAttributes": {
      "DeadLetterConfiguration": {
         "MaxReceiveCount": {{number}},
         "TargetType": "{{string}}"
      },
      "VisibilityTimeoutSeconds": {{number}}
   }
}
```

## Request Parameters
<a name="API_UpdateQueue_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [QueueARN](#API_UpdateQueue_RequestSyntax) **   <a name="Streams-UpdateQueue-request-QueueARN"></a>
The ARN of the queue to update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws.*:kinesis:.*:\d{12}:queue/\S+`
Required: Yes

 ** [QueueAttributes](#API_UpdateQueue_RequestSyntax) **   <a name="Streams-UpdateQueue-request-QueueAttributes"></a>
The configuration attributes to apply to the queue. Attributes you do not specify are left unchanged.
Type: [QueueAttributes](API_QueueAttributes.md) object
Required: Yes

## Response Syntax
<a name="API_UpdateQueue_ResponseSyntax"></a>

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
<a name="API_UpdateQueue_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [QueueDescription](#API_UpdateQueue_ResponseSyntax) **   <a name="Streams-UpdateQueue-response-QueueDescription"></a>
A description of the queue, including the updated attributes.
Type: [QueueDescription](API_QueueDescription.md) object

## Errors
<a name="API_UpdateQueue_Errors"></a>

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
<a name="API_UpdateQueue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kinesis-2013-12-02/UpdateQueue)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kinesis-2013-12-02/UpdateQueue)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesis-2013-12-02/UpdateQueue)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kinesis-2013-12-02/UpdateQueue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesis-2013-12-02/UpdateQueue)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kinesis-2013-12-02/UpdateQueue)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kinesis-2013-12-02/UpdateQueue)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kinesis-2013-12-02/UpdateQueue)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/kinesis-2013-12-02/UpdateQueue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesis-2013-12-02/UpdateQueue)
