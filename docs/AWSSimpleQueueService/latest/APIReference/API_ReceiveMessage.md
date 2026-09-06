---
source_url: https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ReceiveMessage.html
---

# ReceiveMessage
<a name="API_ReceiveMessage"></a>

Retrieves one or more messages (up to 10), from the specified queue. Using the `WaitTimeSeconds` parameter enables long-poll support. For more information, see [Amazon SQS Long Polling](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-long-polling.html) in the *Amazon SQS Developer Guide*.

Short poll is the default behavior where a weighted random set of machines is sampled on a `ReceiveMessage` call. Therefore, only the messages on the sampled machines are returned. If the number of messages in the queue is small (fewer than 1,000), you most likely get fewer messages than you requested per `ReceiveMessage` call. If the number of messages in the queue is extremely small, you might not receive any messages in a particular `ReceiveMessage` response. If this happens, repeat the request.

For each message returned, the response includes the following:
+ The message body.
+ An MD5 digest of the message body. For information about MD5, see [RFC1321](https://www.ietf.org/rfc/rfc1321.txt).
+ The `MessageId` you received when you sent the message to the queue.
+ The receipt handle.
+ The message attributes.
+ An MD5 digest of the message attributes.

The receipt handle is the identifier you must provide when deleting the message. For more information, see [Queue and Message Identifiers](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-queue-message-identifiers.html) in the *Amazon SQS Developer Guide*.

You can provide the `VisibilityTimeout` parameter in your request. The parameter is applied to the messages that Amazon SQS returns in the response. If you don't include the parameter, the overall visibility timeout for the queue is used for the returned messages. The default visibility timeout for a queue is 30 seconds.

**Note**
In the future, new attributes might be added. If you write code that calls this action, we recommend that you structure your code so that it can handle new attributes gracefully.

## Request Syntax
<a name="API_ReceiveMessage_RequestSyntax"></a>

```
{
   "AttributeNames": [ "{{string}}" ],
   "MaxNumberOfMessages": {{number}},
   "MessageAttributeNames": [ "{{string}}" ],
   "MessageSystemAttributeNames": [ "{{string}}" ],
   "QueueUrl": "{{string}}",
   "ReceiveRequestAttemptId": "{{string}}",
   "VisibilityTimeout": {{number}},
   "WaitTimeSeconds": {{number}}
}
```

## Request Parameters
<a name="API_ReceiveMessage_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AttributeNames](#API_ReceiveMessage_RequestSyntax) **   <a name="SQS-ReceiveMessage-request-AttributeNames"></a>
 *This parameter has been deprecated.*
This parameter has been discontinued but will be supported for backward compatibility. To provide attribute names, you are encouraged to use `MessageSystemAttributeNames`.
A list of attributes that need to be returned along with each message. These attributes include:
+  `All` – Returns all values.
+  `ApproximateFirstReceiveTimestamp` – Returns the time the message was first received from the queue ([epoch time](http://en.wikipedia.org/wiki/Unix_time) in milliseconds).
+  `ApproximateReceiveCount` – Returns the number of times a message has been received across all queues but not deleted.
+  `AWSTraceHeader` – Returns the AWS X-Ray trace header string.
+  `SenderId`
  + For a user, returns the user ID, for example `ABCDEFGHI1JKLMNOPQ23R`.
  + For an IAM role, returns the IAM role ID, for example `ABCDE1F2GH3I4JK5LMNOP:i-a123b456`.
+  `SentTimestamp` – Returns the time the message was sent to the queue ([epoch time](http://en.wikipedia.org/wiki/Unix_time) in milliseconds).
+  `SqsManagedSseEnabled` – Enables server-side queue encryption using SQS owned encryption keys. Only one server-side encryption option is supported per queue (for example, [SSE-KMS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-configure-sse-existing-queue.html) or [SSE-SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-configure-sqs-sse-queue.html)).
+  `MessageDeduplicationId` – Returns the value provided by the producer that calls the ` SendMessage ` action.
+  `MessageGroupId` – Returns the value provided by the producer that calls the ` SendMessage ` action.
+  `SequenceNumber` – Returns the value provided by Amazon SQS.
Type: Array of strings
Valid Values: `All | Policy | VisibilityTimeout | MaximumMessageSize | MessageRetentionPeriod | ApproximateNumberOfMessages | ApproximateNumberOfMessagesNotVisible | CreatedTimestamp | LastModifiedTimestamp | QueueArn | ApproximateNumberOfMessagesDelayed | DelaySeconds | ReceiveMessageWaitTimeSeconds | RedrivePolicy | FifoQueue | ContentBasedDeduplication | KmsMasterKeyId | KmsDataKeyReusePeriodSeconds | DeduplicationScope | FifoThroughputLimit | RedriveAllowPolicy | SqsManagedSseEnabled`
Required: No

 ** [MaxNumberOfMessages](#API_ReceiveMessage_RequestSyntax) **   <a name="SQS-ReceiveMessage-request-MaxNumberOfMessages"></a>
The maximum number of messages to return. Amazon SQS never returns more messages than this value (however, fewer messages might be returned). Valid values: 1 to 10. Default: 1.
Type: Integer
Required: No

 ** [MessageAttributeNames](#API_ReceiveMessage_RequestSyntax) **   <a name="SQS-ReceiveMessage-request-MessageAttributeNames"></a>
The name of the message attribute, where *N* is the index.
+ The name can contain alphanumeric characters and the underscore (`_`), hyphen (`-`), and period (`.`).
+ The name is case-sensitive and must be unique among all attribute names for the message.
+ The name must not start with AWS-reserved prefixes such as `AWS.` or `Amazon.` (or any casing variants).
+ The name must not start or end with a period (`.`), and it should not have periods in succession (`..`).
+ The name can be up to 256 characters long.
When using `ReceiveMessage`, you can send a list of attribute names to receive, or you can return all of the attributes by specifying `All` or `.*` in your request. You can also use all message attributes starting with a prefix, for example `bar.*`.
Type: Array of strings
Required: No

 ** [MessageSystemAttributeNames](#API_ReceiveMessage_RequestSyntax) **   <a name="SQS-ReceiveMessage-request-MessageSystemAttributeNames"></a>
A list of attributes that need to be returned along with each message. These attributes include:
+  `All` – Returns all values.
+  `ApproximateFirstReceiveTimestamp` – Returns the time the message was first received from the queue ([epoch time](http://en.wikipedia.org/wiki/Unix_time) in milliseconds).
+  `ApproximateReceiveCount` – Returns the number of times a message has been received across all queues but not deleted.
+  `AWSTraceHeader` – Returns the AWS X-Ray trace header string.
+  `SenderId`
  + For a user, returns the user ID, for example `ABCDEFGHI1JKLMNOPQ23R`.
  + For an IAM role, returns the IAM role ID, for example `ABCDE1F2GH3I4JK5LMNOP:i-a123b456`.
+  `SentTimestamp` – Returns the time the message was sent to the queue ([epoch time](http://en.wikipedia.org/wiki/Unix_time) in milliseconds).
+  `SqsManagedSseEnabled` – Enables server-side queue encryption using SQS owned encryption keys. Only one server-side encryption option is supported per queue (for example, [SSE-KMS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-configure-sse-existing-queue.html) or [SSE-SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-configure-sqs-sse-queue.html)).
+  `MessageDeduplicationId` – Returns the value provided by the producer that calls the ` SendMessage ` action.
+  `MessageGroupId` – Returns the value provided by the producer that calls the ` SendMessage ` action.
+  `SequenceNumber` – Returns the value provided by Amazon SQS.
Type: Array of strings
Valid Values: `All | SenderId | SentTimestamp | ApproximateReceiveCount | ApproximateFirstReceiveTimestamp | SequenceNumber | MessageDeduplicationId | MessageGroupId | AWSTraceHeader | DeadLetterQueueSourceArn`
Required: No

 ** [QueueUrl](#API_ReceiveMessage_RequestSyntax) **   <a name="SQS-ReceiveMessage-request-QueueUrl"></a>
The URL of the Amazon SQS queue from which messages are received.
Queue URLs and names are case-sensitive.
Type: String
Required: Yes

 ** [ReceiveRequestAttemptId](#API_ReceiveMessage_RequestSyntax) **   <a name="SQS-ReceiveMessage-request-ReceiveRequestAttemptId"></a>
This parameter applies only to FIFO (first-in-first-out) queues.
The token used for deduplication of `ReceiveMessage` calls. If a networking issue occurs after a `ReceiveMessage` action, and instead of a response you receive a generic error, it is possible to retry the same action with an identical `ReceiveRequestAttemptId` to retrieve the same set of messages, even if their visibility timeout has not yet expired.
+ You can use `ReceiveRequestAttemptId` only for 5 minutes after a `ReceiveMessage` action.
+ When you set `FifoQueue`, a caller of the `ReceiveMessage` action can provide a `ReceiveRequestAttemptId` explicitly.
+ It is possible to retry the `ReceiveMessage` action with the same `ReceiveRequestAttemptId` if none of the messages have been modified (deleted or had their visibility changes).
+ During a visibility timeout, subsequent calls with the same `ReceiveRequestAttemptId` return the same messages and receipt handles. If a retry occurs within the deduplication interval, it resets the visibility timeout. For more information, see [Visibility Timeout](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-visibility-timeout.html) in the *Amazon SQS Developer Guide*.
**Important**
If a caller of the `ReceiveMessage` action still processes messages when the visibility timeout expires and messages become visible, another worker consuming from the same queue can receive the same messages and therefore process duplicates. Also, if a consumer whose message processing time is longer than the visibility timeout tries to delete the processed messages, the action fails with an error.
To mitigate this effect, ensure that your application observes a safe threshold before the visibility timeout expires and extend the visibility timeout as necessary.
+ While messages with a particular `MessageGroupId` are invisible, no more messages belonging to the same `MessageGroupId` are returned until the visibility timeout expires. You can still receive messages with another `MessageGroupId` from your FIFO queue as long as they are visible.
+ If a caller of `ReceiveMessage` can't track the `ReceiveRequestAttemptId`, no retries work until the original visibility timeout expires. As a result, delays might occur but the messages in the queue remain in a strict order.
The maximum length of `ReceiveRequestAttemptId` is 128 characters. `ReceiveRequestAttemptId` can contain alphanumeric characters (`a-z`, `A-Z`, `0-9`) and punctuation (`!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~`).
For best practices of using `ReceiveRequestAttemptId`, see [Using the ReceiveRequestAttemptId Request Parameter](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/using-receiverequestattemptid-request-parameter.html) in the *Amazon SQS Developer Guide*.
Type: String
Required: No

 ** [VisibilityTimeout](#API_ReceiveMessage_RequestSyntax) **   <a name="SQS-ReceiveMessage-request-VisibilityTimeout"></a>
The duration (in seconds) that the received messages are hidden from subsequent retrieve requests after being retrieved by a `ReceiveMessage` request. If not specified, the default visibility timeout for the queue is used, which is 30 seconds.
Understanding `VisibilityTimeout`:
+ When a message is received from a queue, it becomes temporarily invisible to other consumers for the duration of the visibility timeout. This prevents multiple consumers from processing the same message simultaneously. If the message is not deleted or its visibility timeout is not extended before the timeout expires, it becomes visible again and can be retrieved by other consumers.
+ Setting an appropriate visibility timeout is crucial. If it's too short, the message might become visible again before processing is complete, leading to duplicate processing. If it's too long, it delays the reprocessing of messages if the initial processing fails.
+ You can adjust the visibility timeout using the `--visibility-timeout` parameter in the `receive-message` command to match the processing time required by your application.
+ A message that isn't deleted or a message whose visibility isn't extended before the visibility timeout expires counts as a failed receive. Depending on the configuration of the queue, the message might be sent to the dead-letter queue.
For more information, see [Visibility Timeout](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-visibility-timeout.html) in the *Amazon SQS Developer Guide*.
Type: Integer
Required: No

 ** [WaitTimeSeconds](#API_ReceiveMessage_RequestSyntax) **   <a name="SQS-ReceiveMessage-request-WaitTimeSeconds"></a>
The duration (in seconds) for which the call waits for a message to arrive in the queue before returning. If a message is available, the call returns sooner than `WaitTimeSeconds`. If no messages are available and the wait time expires, the call does not return a message list. If you are using the Java SDK, it returns a `ReceiveMessageResponse` object, which has a empty list instead of a Null object.
To avoid HTTP errors, ensure that the HTTP response timeout for `ReceiveMessage` requests is longer than the `WaitTimeSeconds` parameter. For example, with the Java SDK, you can set HTTP transport settings using the [ NettyNioAsyncHttpClient](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/http/nio/netty/NettyNioAsyncHttpClient.html) for asynchronous clients, or the [ ApacheHttpClient](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/http/apache/ApacheHttpClient.html) for synchronous clients.
Type: Integer
Required: No

## Response Syntax
<a name="API_ReceiveMessage_ResponseSyntax"></a>

```
{
   "Messages": [
      {
         "Attributes": {
            "string" : "string"
         },
         "Body": "string",
         "MD5OfBody": "string",
         "MD5OfMessageAttributes": "string",
         "MessageAttributes": {
            "string" : {
               "BinaryListValues": [ blob ],
               "BinaryValue": blob,
               "DataType": "string",
               "StringListValues": [ "string" ],
               "StringValue": "string"
            }
         },
         "MessageId": "string",
         "ReceiptHandle": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ReceiveMessage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Messages](#API_ReceiveMessage_ResponseSyntax) **   <a name="SQS-ReceiveMessage-response-Messages"></a>
A list of messages.
Type: Array of [Message](API_Message.md) objects

## Errors
<a name="API_ReceiveMessage_Errors"></a>

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md).

 ** InvalidAddress **
The specified ID is invalid.
HTTP Status Code: 400

 ** InvalidSecurity **
The request was not made over HTTPS or did not use SigV4 for signing.
HTTP Status Code: 400

 ** KmsAccessDenied **
The caller doesn't have the required KMS access.
HTTP Status Code: 400

 ** KmsDisabled **
The request was denied due to request throttling.
HTTP Status Code: 400

 ** KmsInvalidKeyUsage **
The request was rejected for one of the following reasons:
+ The KeyUsage value of the KMS key is incompatible with the API operation.
+ The encryption algorithm or signing algorithm specified for the operation is incompatible with the type of key material in the KMS key (KeySpec).
HTTP Status Code: 400

 ** KmsInvalidState **
The request was rejected because the state of the specified resource is not valid for this request.
HTTP Status Code: 400

 ** KmsNotFound **
The request was rejected because the specified entity or resource could not be found.
HTTP Status Code: 400

 ** KmsOptInRequired **
The request was rejected because the specified key policy isn't syntactically or semantically correct.
HTTP Status Code: 400

 ** KmsThrottled **
 AWS KMS throttles requests for the following conditions.
HTTP Status Code: 400

 ** OverLimit **
The specified action violates a limit. For example, `ReceiveMessage` returns this error if the maximum number of in flight messages is reached and `AddPermission` returns this error if the maximum number of permissions for the queue is reached.
HTTP Status Code: 400

 ** QueueDoesNotExist **
Ensure that the `QueueUrl` is correct and that the queue has not been deleted.
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
<a name="API_ReceiveMessage_Examples"></a>

The following example query request receives messages from the specified queue. The structure of `AUTHPARAMS` depends on the signature of the API request. For more information, see [ Examples of Signed Signature Version 4 Requests](https://docs.aws.amazon.com/general/latest/gr/sigv4-signed-request-examples.html) in the * AWS General Reference*.

### Example
<a name="API_ReceiveMessage_Example_1"></a>

 **Using AWS JSON protocol (Default)**

#### Sample Request
<a name="API_ReceiveMessage_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: sqs.us-east-1.amazonaws.com
X-Amz-Target: AmazonSQS.ReceiveMessage
X-Amz-Date: <Date>
Content-Type: application/x-amz-json-1.0
Authorization: <AuthParams>
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
{
    "QueueUrl": "https://sqs.us-east-1.amazonaws.com/177715257436/MyQueue/",
    "MaxNumberOfMessages": 5,
    "VisibilityTimeout": 15,
    "AttributeNames": ["All"]
}
```

#### Sample Response
<a name="API_ReceiveMessage_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <requestId>
Content-Length: <PayloadSizeBytes>
Date: <Date>
Content-Type: application/x-amz-json-1.0
{
    "Messages": [
        {
            "Attributes": {
                "SenderId": "AIDASSYFHUBOBT7F4XT75",
                "ApproximateFirstReceiveTimestamp": "1677112433437",
                "ApproximateReceiveCount": "1",
                "SentTimestamp": "1677112427387"
            },
            "Body": "This is a test message",
            "MD5OfBody": "fafb00f5732ab283681e124bf8747ed1",
            "MessageId": "219f8380-5770-4cc2-8c3e-5c715e145f5e",
            "ReceiptHandle": "AQEBaZ+j5qUoOAoxlmrCQPkBm9njMWXqemmIG6shMHCO6fV20JrQYg/AiZ8JELwLwOu5U61W+aIX5Qzu7GGofxJuvzymr4Ph53RiR0mudj4InLSgpSspYeTRDteBye5tV/txbZDdNZxsi+qqZA9xPnmMscKQqF6pGhnGIKrnkYGl45Nl6GPIZv62LrIRb6mSqOn1fn0yqrvmWuuY3w2UzQbaYunJWGxpzZze21EOBtywknU3Je/g7G9is+c6K9hGniddzhLkK1tHzZKjejOU4jokaiB4nmi0dF3JqLzDsQuPF0Gi8qffhEvw56nl8QCbluSJScFhJYvoagGnDbwOnd9z50L239qtFIgETdpKyirlWwl/NGjWJ45dqWpiW3d2Ws7q"
        }
    ]
}
```

### Example
<a name="API_ReceiveMessage_Example_2"></a>

 **Using AWS query protocol**

#### Sample Request
<a name="API_ReceiveMessage_Example_2_Request"></a>

```
POST /177715257436/MyQueue/ HTTP/1.1
Host: sqs.us-east-1.amazonaws.com
X-Amz-Date: <Date>
Content-Type: application/x-www-form-urlencoded
Authorization: <AuthParams>
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
Action=ReceiveMessage
&MaxNumberOfMessages=5
&VisibilityTimeout=15
&AttributeName=All
```

#### Sample Response
<a name="API_ReceiveMessage_Example_2_Response"></a>

```
HTTP/1.1 200 OK
<ReceiveMessageResponse xmlns="http://queue.amazonaws.com/doc/2012-11-05/">
    <ReceiveMessageResult>
        <Message>
            <MessageId>60e827c3-c8a5-410a-af0e-fb43746e70b1</MessageId>
            <ReceiptHandle>AQEBwPTK2fT2gy97H1iyU5in9umgT+Y4IOxyKGOzpZa8iemEqoR5/aPn0xAodmiVTzyrW7S4e8XwcWbB04XK92jIQzUpiGwRFA4Dl7r3GOw84Qzq/0OBQe/JaKxJw6iilafYA5fo1SJQo5Wg8xXbJHTVlJqgvTXd/UtlByLMhWMi0JMra1UUjYiPsGtYUpLVnOaRkYSPvzRnFFYUbcqCW9lm2Bi/jQKK6KNOZyCCfIh8TooE5i4P2L9N3o9yUHwMdv6p0nb5lKaGurQ2sJwwsyhXf38ZHnVN6pWwsqQnWKYuEXpxPofxd2lcLdgUurMpydS22DzCrkAaf6gmrdxbmCAoeQxE0sFf8alwX9yQmcOjny9aLGe7ro4Vl5o5KMr5hHM4vHEyhwi4wHeKM6MGX0vATA==</ReceiptHandle>
            <MD5OfBody>0e024d309850c78cba5eabbeff7cae71</MD5OfBody>
            <Body>test message body 1</Body>
            <Attribute>
                <Name>SenderId</Name>
                <Value>AIDASSYFHUBOBT7F4XT75</Value>
            </Attribute>
            <Attribute>
                <Name>ApproximateFirstReceiveTimestamp</Name>
                <Value>1677112300463</Value>
            </Attribute>
            <Attribute>
                <Name>ApproximateReceiveCount</Name>
                <Value>1</Value>
            </Attribute>
            <Attribute>
                <Name>SentTimestamp</Name>
                <Value>1677111805489</Value>
            </Attribute>
        </Message>
    </ReceiveMessageResult>
    <ResponseMetadata>
        <RequestId>5ba605cc-1e4b-58ba-93db-59bca8677ec9</RequestId>
    </ResponseMetadata>
</ReceiveMessageResponse>
```

### Example
<a name="API_ReceiveMessage_Example_3"></a>

The following example enables long polling by calling the `ReceiveMessage` action with the `WaitTimeSeconds` parameter set to 10 seconds.

 **Using AWS JSON protocol (Default)**

#### Sample Request
<a name="API_ReceiveMessage_Example_3_Request"></a>

```
POST / HTTP/1.1
Host: sqs.us-east-1.amazonaws.com
X-Amz-Target: AmazonSQS.ReceiveMessage
X-Amz-Date: <Date>
Content-Type: application/x-amz-json-1.0
Authorization: <AuthParams>
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
{
    "QueueUrl": "https://sqs.us-east-1.amazonaws.com/177715257436/MyQueue/",
    "WaitTimeSeconds": 10,
    "MaxNumberOfMessages": 5,
    "VisibilityTimeout": 15,
    "AttributeNames": ["All"]
}
```

### Example
<a name="API_ReceiveMessage_Example_4"></a>

The following example shows the request and response when using the parameter `MessageSystemAttributeNames`.

#### Sample Request
<a name="API_ReceiveMessage_Example_4_Request"></a>

```
aws sqs receive-message \
  --queue-url https://sqs.us-east-1.amazonaws.com/123456789012/MyQueue \
  --message-system-attribute-names SentTimestamp SenderId
```

#### Sample Response
<a name="API_ReceiveMessage_Example_4_Response"></a>

```
{
  "Messages": [
    {
      "MessageId": "abc1234d-5678-90ab-cdef-EXAMPLE11111",
      "ReceiptHandle": "AQEBwJnKyrHigUMZj6rYigCgxlaS3SLy0a...",
      "MD5OfBody": "e99a18c428cb38d5f260853678922e03",
      "Body": "Example message",
      "Attributes": {
        "SenderId": "AIDAEXAMPLE123ABC",
        "SentTimestamp": "1638368280000"
      }
    }
  ]
}
```

### Example
<a name="API_ReceiveMessage_Example_5"></a>

 **Using AWS query protocol**

#### Sample Request
<a name="API_ReceiveMessage_Example_5_Request"></a>

```
POST /177715257436/MyQueue/ HTTP/1.1
Host: sqs.us-east-1.amazonaws.com
X-Amz-Date: <Date>
Content-Type: application/x-www-form-urlencoded
Authorization: <AuthParams>
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
Action=ReceiveMessage
&WaitTimeSeconds=10
&MaxNumberOfMessages=5
&VisibilityTimeout=15
&AttributeName=All
```

## See Also
<a name="API_ReceiveMessage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sqs-2012-11-05/ReceiveMessage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sqs-2012-11-05/ReceiveMessage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sqs-2012-11-05/ReceiveMessage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sqs-2012-11-05/ReceiveMessage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sqs-2012-11-05/ReceiveMessage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sqs-2012-11-05/ReceiveMessage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sqs-2012-11-05/ReceiveMessage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sqs-2012-11-05/ReceiveMessage)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sqs-2012-11-05/ReceiveMessage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sqs-2012-11-05/ReceiveMessage)
