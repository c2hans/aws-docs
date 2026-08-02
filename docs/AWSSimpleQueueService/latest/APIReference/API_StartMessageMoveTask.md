---
source_url: https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_StartMessageMoveTask.html
---

# StartMessageMoveTask
<a name="API_StartMessageMoveTask"></a>

Starts an asynchronous task to move messages from a specified source queue to a specified destination queue.

**Note**
This action is currently limited to supporting message redrive from queues that are configured as [dead-letter queues (DLQs)](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html) of other Amazon SQS queues only. Non-SQS queue sources of dead-letter queues, such as AWS Lambda or Amazon SNS topics, are currently not supported.
In dead-letter queues redrive context, the `StartMessageMoveTask` the source queue is the DLQ, while the destination queue can be the original source queue (from which the messages were driven to the dead-letter-queue), or a custom destination queue.
Only one active message movement task is supported per queue at any given time.

## Request Syntax
<a name="API_StartMessageMoveTask_RequestSyntax"></a>

```
{
   "DestinationArn": "{{string}}",
   "MaxNumberOfMessagesPerSecond": {{number}},
   "SourceArn": "{{string}}"
}
```

## Request Parameters
<a name="API_StartMessageMoveTask_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DestinationArn](#API_StartMessageMoveTask_RequestSyntax) **   <a name="SQS-StartMessageMoveTask-request-DestinationArn"></a>
The ARN of the queue that receives the moved messages. You can use this field to specify the destination queue where you would like to redrive messages. If this field is left blank, the messages will be redriven back to their respective original source queues.
Type: String
Required: No

 ** [MaxNumberOfMessagesPerSecond](#API_StartMessageMoveTask_RequestSyntax) **   <a name="SQS-StartMessageMoveTask-request-MaxNumberOfMessagesPerSecond"></a>
The number of messages to be moved per second (the message movement rate). You can use this field to define a fixed message movement rate. The maximum value for messages per second is 500. If this field is left blank, the system will optimize the rate based on the queue message backlog size, which may vary throughout the duration of the message movement task.
Type: Integer
Required: No

 ** [SourceArn](#API_StartMessageMoveTask_RequestSyntax) **   <a name="SQS-StartMessageMoveTask-request-SourceArn"></a>
The ARN of the queue that contains the messages to be moved to another queue. Currently, only ARNs of dead-letter queues (DLQs) whose sources are other Amazon SQS queues are accepted. DLQs whose sources are non-SQS queues, such as AWS Lambda or Amazon SNS topics, are not currently supported.
Type: String
Required: Yes

## Response Syntax
<a name="API_StartMessageMoveTask_ResponseSyntax"></a>

```
{
   "TaskHandle": "string"
}
```

## Response Elements
<a name="API_StartMessageMoveTask_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [TaskHandle](#API_StartMessageMoveTask_ResponseSyntax) **   <a name="SQS-StartMessageMoveTask-response-TaskHandle"></a>
An identifier associated with a message movement task. You can use this identifier to cancel a specified message movement task using the `CancelMessageMoveTask` action.
Type: String

## Errors
<a name="API_StartMessageMoveTask_Errors"></a>

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
<a name="API_StartMessageMoveTask_Examples"></a>

### Example
<a name="API_StartMessageMoveTask_Example_1"></a>

 **Using AWS query protocol**

The following example query starts a message move task on a dead-letter queue `MyDeadLetterQueue` to its source queue, with a limit of 10 messages per second. The structure of `AUTHPARAMS` depends on the signature of the API request. For more information, see [ Examples of Signed Signature Version 4 Requests](https://docs.aws.amazon.com/general/latest/gr/sigv4-signed-request-examples.html) in the * AWS General Reference*.

#### Sample Request
<a name="API_StartMessageMoveTask_Example_1_Request"></a>

```
POST /  HTTP/1.1
Host: sqs.us-east-1.amazonaws.com
X-Amz-Date: <Date>
Content-Type: application/x-www-form-urlencoded
Authorization: <AuthParams>
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
Action=StartMessageMoveTask
&SourceArn=arn:aws:sqs:us-east-1:555555555555:MyDeadLetterQueue
&MaxNumberOfMessagesPerSecond=10
```

#### Sample Response
<a name="API_StartMessageMoveTask_Example_1_Response"></a>

```
HTTP/1.1 200 OK
<?xml version="1.0"?>
<StartMessageMoveTaskResponse xmlns="http://queue.amazonaws.com/doc/2012-11-05/">
    <StartMessageMoveTaskResult>
        <TaskHandle>eyJ0YXNrSWQiOiJkYzE2OWUwNC0wZTU1LTQ0ZDItYWE5MC1jMDgwY2ExZjM2ZjciLCJzb3VyY2VBcm4iOiJhcm46YXdzOnNxczp1cy1lYXN0LTE6MTc3NzE1MjU3NDM2Ok15RGVhZExldHRlclF1ZXVlIn0=</TaskHandle>
    </StartMessageMoveTaskResult>
    <ResponseMetadata>
        <RequestId>9b20926c-8b35-5d8e-9559-ce1c22e754dc</RequestId>
    </ResponseMetadata>
</StartMessageMoveTaskResponse>
```

## See Also
<a name="API_StartMessageMoveTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sqs-2012-11-05/StartMessageMoveTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sqs-2012-11-05/StartMessageMoveTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sqs-2012-11-05/StartMessageMoveTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sqs-2012-11-05/StartMessageMoveTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sqs-2012-11-05/StartMessageMoveTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sqs-2012-11-05/StartMessageMoveTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sqs-2012-11-05/StartMessageMoveTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sqs-2012-11-05/StartMessageMoveTask)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sqs-2012-11-05/StartMessageMoveTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sqs-2012-11-05/StartMessageMoveTask)
