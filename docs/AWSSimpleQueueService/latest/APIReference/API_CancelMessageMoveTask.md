---
source_url: https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_CancelMessageMoveTask.html
---

# CancelMessageMoveTask
<a name="API_CancelMessageMoveTask"></a>

Cancels a specified message movement task. A message movement can only be cancelled when the current status is RUNNING. Cancelling a message movement task does not revert the messages that have already been moved. It can only stop the messages that have not been moved yet.

**Note**
This action is currently limited to supporting message redrive from [dead-letter queues (DLQs)](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html) only. In this context, the source queue is the dead-letter queue (DLQ), while the destination queue can be the original source queue (from which the messages were driven to the dead-letter-queue), or a custom destination queue.
Only one active message movement task is supported per queue at any given time.

## Request Syntax
<a name="API_CancelMessageMoveTask_RequestSyntax"></a>

```
{
   "TaskHandle": "{{string}}"
}
```

## Request Parameters
<a name="API_CancelMessageMoveTask_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [TaskHandle](#API_CancelMessageMoveTask_RequestSyntax) **   <a name="SQS-CancelMessageMoveTask-request-TaskHandle"></a>
An identifier associated with a message movement task.
Type: String
Required: Yes

## Response Syntax
<a name="API_CancelMessageMoveTask_ResponseSyntax"></a>

```
{
   "ApproximateNumberOfMessagesMoved": number
}
```

## Response Elements
<a name="API_CancelMessageMoveTask_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ApproximateNumberOfMessagesMoved](#API_CancelMessageMoveTask_ResponseSyntax) **   <a name="SQS-CancelMessageMoveTask-response-ApproximateNumberOfMessagesMoved"></a>
The approximate number of messages already moved to the destination queue.
Type: Long

## Errors
<a name="API_CancelMessageMoveTask_Errors"></a>

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md).

 ** InvalidAddress **
The specified ID is invalid.
HTTP Status Code: 400

 ** InvalidSecurity **
The request was not made over HTTPS or did not use SigV4 for signing.
HTTP Status Code: 400

 ** RequestThrottled **
The request was denied due to request throttling.
+ Exceeds the permitted request rate for the queue or for the recipient of the request.
+ Ensure that the request rate is within the Amazon SQS limits for sending messages. For more information, see [Amazon SQS quotas](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-quotas.html#quotas-requests) in the *Amazon SQS Developer Guide*.
HTTP Status Code: 400

 ** ResourceNotFoundException **
One or more specified resources don't exist.
HTTP Status Code: 400

 ** UnsupportedOperation **
Error code 400. Unsupported operation.
HTTP Status Code: 400

## Examples
<a name="API_CancelMessageMoveTask_Examples"></a>

### Example
<a name="API_CancelMessageMoveTask_Example_1"></a>

 **Using AWS query protocol**

The following example query cancels an existing running message move task. The structure of `AUTHPARAMS` depends on the signature of the API request. For more information, see [ Examples of Signed Signature Version 4 Requests](https://docs.aws.amazon.com/general/latest/gr/sigv4-signed-request-examples.html) in the * AWS General Reference*.

#### Sample Request
<a name="API_CancelMessageMoveTask_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: sqs.us-east-1.amazonaws.com
X-Amz-Date: <Date>
Content-Type: application/x-www-form-urlencoded
Authorization: <AuthParams>
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
Action=CancelMessageMoveTask
&TaskHandle=eyJ0YXNrSWQiOiJkYzE2OWUwNC0wZTU1LTQ0ZDItYWE5MC1jMDgwY2ExZjM2ZjciLCJzb3VyY2VBcm4iOiJhcm46YXdzOnNxczp1cy1lYXN0LTE6MTc3NzE1MjU3NDM2Ok15RGVhZExldHRlclF1ZXVlIn0=
```

#### Sample Response
<a name="API_CancelMessageMoveTask_Example_1_Response"></a>

```
HTTP/1.1 200 OK
<?xml version="1.0"?>
<CancelMessageMoveTaskResponse xmlns="http://queue.amazonaws.com/doc/2012-11-05/">
    <CancelMessageMoveTaskResult>
        <ApproximateNumberOfMessagesMoved>300</ApproximateNumberOfMessagesMoved>
    </CancelMessageMoveTaskResult>
    <ResponseMetadata>
        <RequestId>9b20926c-8b35-5d8e-9559-ce1c22e754dc</RequestId>
    </ResponseMetadata>
</CancelMessageMoveTaskResponse>
```

## See Also
<a name="API_CancelMessageMoveTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sqs-2012-11-05/CancelMessageMoveTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sqs-2012-11-05/CancelMessageMoveTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sqs-2012-11-05/CancelMessageMoveTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sqs-2012-11-05/CancelMessageMoveTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sqs-2012-11-05/CancelMessageMoveTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sqs-2012-11-05/CancelMessageMoveTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sqs-2012-11-05/CancelMessageMoveTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sqs-2012-11-05/CancelMessageMoveTask)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sqs-2012-11-05/CancelMessageMoveTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sqs-2012-11-05/CancelMessageMoveTask)
