---
source_url: https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ChangeMessageVisibility.html
---

# ChangeMessageVisibility
<a name="API_ChangeMessageVisibility"></a>

Changes the visibility timeout of a specified message in a queue to a new value. The default visibility timeout for a message is 30 seconds. The minimum is 0 seconds. The maximum is 12 hours. For more information, see [Visibility Timeout](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-visibility-timeout.html) in the *Amazon SQS Developer Guide*.

For example, if the default timeout for a queue is 60 seconds, 15 seconds have elapsed since you received the message, and you send a ChangeMessageVisibility call with `VisibilityTimeout` set to 10 seconds, the 10 seconds begin to count from the time that you make the `ChangeMessageVisibility` call. Thus, any attempt to change the visibility timeout or to delete that message 10 seconds after you initially change the visibility timeout (a total of 25 seconds) might result in an error.

An Amazon SQS message has three basic states:

1. Sent to a queue by a producer.

1. Received from the queue by a consumer.

1. Deleted from the queue.

A message is considered to be *stored* after it is sent to a queue by a producer, but not yet received from the queue by a consumer (that is, between states 1 and 2). There is no limit to the number of stored messages. A message is considered to be *in flight* after it is received from a queue by a consumer, but not yet deleted from the queue (that is, between states 2 and 3). There is a limit to the number of in flight messages.

Limits that apply to in flight messages are unrelated to the *unlimited* number of stored messages.

For most standard queues (depending on queue traffic and message backlog), there can be a maximum of approximately 120,000 in flight messages (received from a queue by a consumer, but not yet deleted from the queue). If you reach this limit, Amazon SQS returns the `OverLimit` error message. To avoid reaching the limit, you should delete messages from the queue after they're processed. You can also increase the number of queues you use to process your messages. To request a limit increase, [file a support request](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase&limitType=service-code-sqs).

For FIFO queues, there can be a maximum of 120,000 in flight messages (received from a queue by a consumer, but not yet deleted from the queue). If you reach this limit, Amazon SQS returns no error messages.

**Important**
If you attempt to set the `VisibilityTimeout` to a value greater than the maximum time left, Amazon SQS returns an error. Amazon SQS doesn't automatically recalculate and increase the timeout to the maximum remaining time.
Unlike with a queue, when you change the visibility timeout for a specific message the timeout value is applied immediately but isn't saved in memory for that message. If you don't delete a message after it is received, the visibility timeout for the message reverts to the original timeout value (not to the value you set using the `ChangeMessageVisibility` action) the next time the message is received.

## Request Syntax
<a name="API_ChangeMessageVisibility_RequestSyntax"></a>

```
{
   "QueueUrl": "{{string}}",
   "ReceiptHandle": "{{string}}",
   "VisibilityTimeout": {{number}}
}
```

## Request Parameters
<a name="API_ChangeMessageVisibility_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [QueueUrl](#API_ChangeMessageVisibility_RequestSyntax) **   <a name="SQS-ChangeMessageVisibility-request-QueueUrl"></a>
The URL of the Amazon SQS queue whose message's visibility is changed.
Queue URLs and names are case-sensitive.
Type: String
Required: Yes

 ** [ReceiptHandle](#API_ChangeMessageVisibility_RequestSyntax) **   <a name="SQS-ChangeMessageVisibility-request-ReceiptHandle"></a>
The receipt handle associated with the message, whose visibility timeout is changed. This parameter is returned by the ` ReceiveMessage ` action.
Type: String
Required: Yes

 ** [VisibilityTimeout](#API_ChangeMessageVisibility_RequestSyntax) **   <a name="SQS-ChangeMessageVisibility-request-VisibilityTimeout"></a>
The new value for the message's visibility timeout (in seconds). Values range: `0` to `43200`. Maximum: 12 hours.
Type: Integer
Required: Yes

## Response Elements
<a name="API_ChangeMessageVisibility_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_ChangeMessageVisibility_Errors"></a>

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md).

 ** InvalidAddress **
The specified ID is invalid.
HTTP Status Code: 400

 ** InvalidSecurity **
The request was not made over HTTPS or did not use SigV4 for signing.
HTTP Status Code: 400

 ** MessageNotInflight **
The specified message isn't in flight.
HTTP Status Code: 400

 ** QueueDoesNotExist **
Ensure that the `QueueUrl` is correct and that the queue has not been deleted.
HTTP Status Code: 400

 ** ReceiptHandleIsInvalid **
The specified receipt handle isn't valid.
HTTP Status Code: 400

 ** RequestThrottled **
The request was denied due to request throttling.
+ Exceeds the permitted request rate for the queue or for the recipient of the request.
+ Ensure that the request rate is within the Amazon SQS limits for sending messages. For more information, see [Amazon SQS quotas](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-quotas.html#quotas-requests) in the *Amazon SQS Developer Guide*.
HTTP Status Code: 400

 ** UnsupportedOperation **
Error code 400. Unsupported operation.
HTTP Status Code: 400

## Examples
<a name="API_ChangeMessageVisibility_Examples"></a>

The following example queries request changes the visibility timeout for a message to 60 seconds. The structure of `AUTHPARAMS` depends on the signature of the API request. For more information, see [ Examples of Signed Signature Version 4 Requests](https://docs.aws.amazon.com/general/latest/gr/sigv4-signed-request-examples.html) in the * AWS General Reference*.

### Example
<a name="API_ChangeMessageVisibility_Example_1"></a>

 **Using AWS JSON protocol (Default)**

#### Sample Request
<a name="API_ChangeMessageVisibility_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: sqs.us-east-1.amazonaws.com
X-Amz-Target: AmazonSQS.ChangeMessageVisibility
X-Amz-Date: <Date>
Content-Type: application/x-amz-json-1.0
Authorization: <AuthParams>
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
{
    "QueueUrl": "https://sqs.us-east-1.amazonaws.com/177715257436/MyQueue/",
    "ReceiptHandle": "AQEBaZ+j5qUoOAoxlmrCQPkBm9njMWXqemmIG6shMHCO6fV20JrQYg/AiZ8JELwLwOu5U61W+aIX5Qzu7GGofxJuvzymr4Ph53RiR0mudj4InLSgpSspYeTRDteBye5tV/txbZDdNZxsi+qqZA9xPnmMscKQqF6pGhnGIKrnkYGl45Nl6GPIZv62LrIRb6mSqOn1fn0yqrvmWuuY3w2UzQbaYunJWGxpzZze21EOBtywknU3Je/g7G9is+c6K9hGniddzhLkK1tHzZKjejOU4jokaiB4nmi0dF3JqLzDsQuPF0Gi8qffhEvw56nl8QCbluSJScFhJYvoagGnDbwOnd9z50L239qtFIgETdpKyirlWwl/NGjWJ45dqWpiW3d2Ws7q",
    "VisibilityTimeout": 60
}
```

#### Sample Response
<a name="API_ChangeMessageVisibility_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <requestId>
Content-Length: 0
Date: <Date>
Content-Type: application/x-amz-json-1.0
```

### Example
<a name="API_ChangeMessageVisibility_Example_2"></a>

 **Using AWS query protocol**

#### Sample Request
<a name="API_ChangeMessageVisibility_Example_2_Request"></a>

```
POST /177715257436/MyQueue HTTP/1.1
Host: sqs.us-east-1.amazonaws.com
X-Amz-Date: <Date>
Content-Type: application/x-www-form-urlencoded
Authorization: <AuthParams>
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
Action=ChangeMessageVisibility
&VisibilityTimeout=60
&ReceiptHandle=AQEBwPTK2fT2gy97H1iyU5in9umgT+Y4IOxyKGOzpZa8iemEqoR5/aPn0xAodmiVTzyrW7S4e8XwcWbB04XK92jIQzUpiGwRFA4Dl7r3GOw84Qzq/0OBQe/JaKxJw6iilafYA5fo1SJQo5Wg8xXbJHTVlJqgvTXd/UtlByLMhWMi0JMra1UUjYiPsGtYUpLVnOaRkYSPvzRnFFYUbcqCW9lm2BijQKK6KNOZyCCfIh8TooE5i4P2L9N3o9yUHwMdv6p0nb5lKaGurQ2sJwwsyhXf38ZHnVN6pWwsqQnWKYuEXpxPofxd2lcLdgUurMpydS22DzCrkAaf6gmrdxbmCAoeQxE0sFf8alwX9yQmcOjny9aLGe7ro4Vl5o5KMr5hHM4vHEyhwi4wHeKM6MGX0vATA==
```

#### Sample Response
<a name="API_ChangeMessageVisibility_Example_2_Response"></a>

```
HTTP/1.1 200 OK
<?xml version="1.0"?>
<ChangeMessageVisibilityResponse xmlns="http://queue.amazonaws.com/doc/2012-11-05/">
    <ResponseMetadata>
        <RequestId>6a7a282a-d013-4a59-aba9-335b0fa48bed</RequestId>
    </ResponseMetadata>
</ChangeMessageVisibilityResponse>
```

## See Also
<a name="API_ChangeMessageVisibility_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sqs-2012-11-05/ChangeMessageVisibility)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sqs-2012-11-05/ChangeMessageVisibility)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sqs-2012-11-05/ChangeMessageVisibility)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sqs-2012-11-05/ChangeMessageVisibility)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sqs-2012-11-05/ChangeMessageVisibility)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sqs-2012-11-05/ChangeMessageVisibility)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sqs-2012-11-05/ChangeMessageVisibility)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sqs-2012-11-05/ChangeMessageVisibility)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sqs-2012-11-05/ChangeMessageVisibility)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sqs-2012-11-05/ChangeMessageVisibility)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Queue Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSSimpleQueueService` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
