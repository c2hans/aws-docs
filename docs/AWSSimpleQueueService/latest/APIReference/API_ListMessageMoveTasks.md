---
source_url: https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ListMessageMoveTasks.html
---

# ListMessageMoveTasks
<a name="API_ListMessageMoveTasks"></a>

Gets the most recent message movement tasks (up to 10) under a specific source queue.

**Note**
This action is currently limited to supporting message redrive from [dead-letter queues (DLQs)](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html) only. In this context, the source queue is the dead-letter queue (DLQ), while the destination queue can be the original source queue (from which the messages were driven to the dead-letter-queue), or a custom destination queue.
Only one active message movement task is supported per queue at any given time.

## Request Syntax
<a name="API_ListMessageMoveTasks_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "SourceArn": "{{string}}"
}
```

## Request Parameters
<a name="API_ListMessageMoveTasks_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListMessageMoveTasks_RequestSyntax) **   <a name="SQS-ListMessageMoveTasks-request-MaxResults"></a>
The maximum number of results to include in the response. The default is 1, which provides the most recent message movement task. The upper limit is 10.
Type: Integer
Required: No

 ** [SourceArn](#API_ListMessageMoveTasks_RequestSyntax) **   <a name="SQS-ListMessageMoveTasks-request-SourceArn"></a>
The ARN of the queue whose message movement tasks are to be listed.
Type: String
Required: Yes

## Response Syntax
<a name="API_ListMessageMoveTasks_ResponseSyntax"></a>

```
{
   "Results": [
      {
         "ApproximateNumberOfMessagesMoved": number,
         "ApproximateNumberOfMessagesToMove": number,
         "DestinationArn": "string",
         "FailureReason": "string",
         "MaxNumberOfMessagesPerSecond": number,
         "SourceArn": "string",
         "StartedTimestamp": number,
         "Status": "string",
         "TaskHandle": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListMessageMoveTasks_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Results](#API_ListMessageMoveTasks_ResponseSyntax) **   <a name="SQS-ListMessageMoveTasks-response-Results"></a>
A list of message movement tasks and their attributes.
Type: Array of [ListMessageMoveTasksResultEntry](API_ListMessageMoveTasksResultEntry.md) objects

## Errors
<a name="API_ListMessageMoveTasks_Errors"></a>

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
<a name="API_ListMessageMoveTasks_Examples"></a>

### Example
<a name="API_ListMessageMoveTasks_Example_1"></a>

 **Using AWS query protocol**

The following example query lists the five most recent message movement tasks on `MyDeadLetterQueue`, which has only two tasks since it was created. The structure of `AUTHPARAMS` depends on the signature of the API request. For more information, see [ Examples of Signed Signature Version 4 Requests](https://docs.aws.amazon.com/general/latest/gr/sigv4-signed-request-examples.html) in the * AWS General Reference*.

#### Sample Request
<a name="API_ListMessageMoveTasks_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: sqs.us-east-1.amazonaws.com
X-Amz-Date: <Date>
Content-Type: application/x-www-form-urlencoded
Authorization: <AuthParams>
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
Action=ListMessageMoveTasks
&SourceArn=arn:aws:sqs:us-east-1:555555555555:MyDeadLetterQueue
&MaxResults=5
```

#### Sample Response
<a name="API_ListMessageMoveTasks_Example_1_Response"></a>

```
HTTP/1.1 200 OK
<?xml version="1.0"?>
<ListMessageMoveTasksResponse xmlns="http://queue.amazonaws.com/doc/2012-11-05/">
    <ListMessageMoveTasksResult>
        <Result>
            <ApproximateNumberOfMessagesMoved>50</ApproximateNumberOfMessagesMoved>
            <ApproximateNumberOfMessagesToMove>0</ApproximateNumberOfMessagesToMove>
            <DestinationArn>arn:aws:sqs:us-east-1:555555555555:MySourceQueue</DestinationArn>
            <MaxNumberOfMessagesPerSecond>20</MaxNumberOfMessagesPerSecond>
            <SourceArn>arn:aws:sqs:us-east-1:555555555555:MyDeadLetterQueue</SourceArn>
            <StartedTimestamp>1684429053010</StartedTimestamp>
            <Status>COMPLETED</Status>
        </Result>
        <Result>
            <ApproximateNumberOfMessagesMoved>50</ApproximateNumberOfMessagesMoved>
            <ApproximateNumberOfMessagesToMove>100</ApproximateNumberOfMessagesToMove>
            <DestinationArn>arn:aws:sqs:us-east-1:555555555555:MySourceQueue</DestinationArn>
            <MaxNumberOfMessagesPerSecond>10</MaxNumberOfMessagesPerSecond>
            <SourceArn>arn:aws:sqs:us-east-1:555555555555:MyDeadLetterQueue</SourceArn>
            <StartedTimestamp>1684429993999</StartedTimestamp>
            <Status>RUNNING</Status>
            <TaskHandle>eyJ0YXNrSWQiOiJkYzE2OWUwNC0wZTU1LTQ0ZDItYWE5MC1jMDgwY2ExZjM2ZjciLCJzb3VyY2VBcm4iOiJhcm46YXdzOnNxczp1cy1lYXN0LTE6MTc3NzE1MjU3NDM2Ok15RGVhZExldHRlclF1ZXVlIn0=</TaskHandle>
        </Result>
        <ResponseMetadata>
            <RequestId>9b20926c-8b35-5d8e-9559-ce1c22e754dc</RequestId>
        </ResponseMetadata>
    </ListMessageMoveTasksResult>
</ListMessageMoveTasksResponse>
```

## See Also
<a name="API_ListMessageMoveTasks_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sqs-2012-11-05/ListMessageMoveTasks)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sqs-2012-11-05/ListMessageMoveTasks)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sqs-2012-11-05/ListMessageMoveTasks)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sqs-2012-11-05/ListMessageMoveTasks)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sqs-2012-11-05/ListMessageMoveTasks)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sqs-2012-11-05/ListMessageMoveTasks)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sqs-2012-11-05/ListMessageMoveTasks)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sqs-2012-11-05/ListMessageMoveTasks)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sqs-2012-11-05/ListMessageMoveTasks)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sqs-2012-11-05/ListMessageMoveTasks)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Queue Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSSimpleQueueService` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
