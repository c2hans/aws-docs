---
source_url: https://docs.aws.amazon.com/kinesis/latest/APIReference/API_DeleteQueue.html
---

# DeleteQueue

Deletes the specified queue. Records that are in flight when you delete the queue are not delivered again, and receipt handles issued by the queue stop being valid.

Deleting a queue does not delete the data stream the queue was created on, and does not delete any records in that stream. Those records remain available to stream consumers and to other queues on the same stream for the rest of their retention period.

 `DeleteQueue` is an asynchronous operation. Upon receiving a `DeleteQueue` request, Amazon Kinesis Data Streams sets the `QueueStatus` to `DELETING`. The queue is deleted when the operation completes. A queue in the `DELETING` state does not deliver records.

You must delete every queue on a data stream before you can delete the stream, or switch it from on-demand to provisioned capacity mode.

## Request Syntax
<a name="API_DeleteQueue_RequestSyntax"></a>

```
{
   "QueueARN": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteQueue_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [QueueARN](#API_DeleteQueue_RequestSyntax) **   <a name="Streams-DeleteQueue-request-QueueARN"></a>
The ARN of the queue to delete.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws.*:kinesis:.*:\d{12}:queue/\S+`
Required: Yes

## Response Elements
<a name="API_DeleteQueue_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteQueue_Errors"></a>

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

 ** ResourceNotFoundException **
The requested resource could not be found. The stream might not be specified correctly.
 ** message **
A message that provides information about the error.
HTTP Status Code: 400

 ** ValidationException **
The request failed validation. For example, a parameter value is not valid, a combination of parameters is not supported, or the operation is not supported for the stream's capacity mode. The error message describes the specific reason.
HTTP Status Code: 400

## See Also
<a name="API_DeleteQueue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kinesis-2013-12-02/DeleteQueue)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kinesis-2013-12-02/DeleteQueue)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesis-2013-12-02/DeleteQueue)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kinesis-2013-12-02/DeleteQueue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesis-2013-12-02/DeleteQueue)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kinesis-2013-12-02/DeleteQueue)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kinesis-2013-12-02/DeleteQueue)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kinesis-2013-12-02/DeleteQueue)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/kinesis-2013-12-02/DeleteQueue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesis-2013-12-02/DeleteQueue)
