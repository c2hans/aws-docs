---
source_url: https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_SendMessage.html
---

# SendMessage
<a name="API_SendMessage"></a>

Delivers a message to the specified queue.

**Important**
A message can include only XML, JSON, and unformatted text. The following Unicode characters are allowed. For more information, see the [W3C specification for characters](http://www.w3.org/TR/REC-xml/#charsets).
 `#x9` \| `#xA` \| `#xD` \| `#x20` to `#xD7FF` \| `#xE000` to `#xFFFD` \| `#x10000` to `#x10FFFF`
If a message contains characters outside the allowed set, Amazon SQS rejects the message and returns an InvalidMessageContents error. Ensure that your message body includes only valid characters to avoid this exception.

## Request Syntax
<a name="API_SendMessage_RequestSyntax"></a>

```
{
   "DelaySeconds": {{number}},
   "MessageAttributes": {
      "{{string}}" : {
         "BinaryListValues": [ {{blob}} ],
         "BinaryValue": {{blob}},
         "DataType": "{{string}}",
         "StringListValues": [ "{{string}}" ],
         "StringValue": "{{string}}"
      }
   },
   "MessageBody": "{{string}}",
   "MessageDeduplicationId": "{{string}}",
   "MessageGroupId": "{{string}}",
   "MessageSystemAttributes": {
      "{{string}}" : {
         "BinaryListValues": [ {{blob}} ],
         "BinaryValue": {{blob}},
         "DataType": "{{string}}",
         "StringListValues": [ "{{string}}" ],
         "StringValue": "{{string}}"
      }
   },
   "QueueUrl": "{{string}}"
}
```

## Request Parameters
<a name="API_SendMessage_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DelaySeconds](#API_SendMessage_RequestSyntax) **   <a name="SQS-SendMessage-request-DelaySeconds"></a>
 The length of time, in seconds, for which to delay a specific message. Valid values: 0 to 900. Maximum: 15 minutes. Messages with a positive `DelaySeconds` value become available for processing after the delay period is finished. If you don't specify a value, the default value for the queue applies.
When you set `FifoQueue`, you can't set `DelaySeconds` per message. You can set this parameter only on a queue level.
Type: Integer
Required: No

 ** [MessageAttributes](#API_SendMessage_RequestSyntax) **   <a name="SQS-SendMessage-request-MessageAttributes"></a>
Each message attribute consists of a `Name`, `Type`, and `Value`. For more information, see [Amazon SQS message attributes](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-message-metadata.html#sqs-message-attributes) in the *Amazon SQS Developer Guide*.
Type: String to [MessageAttributeValue](API_MessageAttributeValue.md) object map
Required: No

 ** [MessageBody](#API_SendMessage_RequestSyntax) **   <a name="SQS-SendMessage-request-MessageBody"></a>
The message to send. The minimum size is one character. The maximum size is 1 MiB or 1,048,576 bytes
A message can include only XML, JSON, and unformatted text. The following Unicode characters are allowed. For more information, see the [W3C specification for characters](http://www.w3.org/TR/REC-xml/#charsets).
 `#x9` \| `#xA` \| `#xD` \| `#x20` to `#xD7FF` \| `#xE000` to `#xFFFD` \| `#x10000` to `#x10FFFF`
If a message contains characters outside the allowed set, Amazon SQS rejects the message and returns an InvalidMessageContents error. Ensure that your message body includes only valid characters to avoid this exception.
Type: String
Required: Yes

 ** [MessageDeduplicationId](#API_SendMessage_RequestSyntax) **   <a name="SQS-SendMessage-request-MessageDeduplicationId"></a>
This parameter applies only to FIFO (first-in-first-out) queues.
The token used for deduplication of sent messages. If a message with a particular `MessageDeduplicationId` is sent successfully, any messages sent with the same `MessageDeduplicationId` are accepted successfully but aren't delivered during the 5-minute deduplication interval. For more information, see [ Exactly-once processing](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues-exactly-once-processing.html) in the *Amazon SQS Developer Guide*.
+ Every message must have a unique `MessageDeduplicationId`,
  + You may provide a `MessageDeduplicationId` explicitly.
  + If you aren't able to provide a `MessageDeduplicationId` and you enable `ContentBasedDeduplication` for your queue, Amazon SQS uses a SHA-256 hash to generate the `MessageDeduplicationId` using the body of the message (but not the attributes of the message).
  + If you don't provide a `MessageDeduplicationId` and the queue doesn't have `ContentBasedDeduplication` set, the action fails with an error.
  + If the queue has `ContentBasedDeduplication` set, your `MessageDeduplicationId` overrides the generated one.
+ When `ContentBasedDeduplication` is in effect, messages with identical content sent within the deduplication interval are treated as duplicates and only one copy of the message is delivered.
+ If you send one message with `ContentBasedDeduplication` enabled and then another message with a `MessageDeduplicationId` that is the same as the one generated for the first `MessageDeduplicationId`, the two messages are treated as duplicates and only one copy of the message is delivered.
The `MessageDeduplicationId` is available to the consumer of the message (this can be useful for troubleshooting delivery issues).
If a message is sent successfully but the acknowledgement is lost and the message is resent with the same `MessageDeduplicationId` after the deduplication interval, Amazon SQS can't detect duplicate messages.
Amazon SQS continues to keep track of the message deduplication ID even after the message is received and deleted.
The maximum length of `MessageDeduplicationId` is 128 characters. `MessageDeduplicationId` can contain alphanumeric characters (`a-z`, `A-Z`, `0-9`) and punctuation (`!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~`).
For best practices of using `MessageDeduplicationId`, see [Using the MessageDeduplicationId Property](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/using-messagededuplicationid-property.html) in the *Amazon SQS Developer Guide*.
Type: String
Required: No

 ** [MessageGroupId](#API_SendMessage_RequestSyntax) **   <a name="SQS-SendMessage-request-MessageGroupId"></a>
 `MessageGroupId` is an attribute used in Amazon SQS FIFO (First-In-First-Out) and standard queues. In FIFO queues, `MessageGroupId` organizes messages into distinct groups. Messages within the same message group are always processed one at a time, in strict order, ensuring that no two messages from the same group are processed simultaneously. In standard queues, using `MessageGroupId` enables fair queues. It is used to identify the tenant a message belongs to, helping maintain consistent message dwell time across all tenants during noisy neighbor events. Unlike FIFO queues, messages with the same `MessageGroupId` can be processed in parallel, maintaining the high throughput of standard queues.
+  **FIFO queues:** `MessageGroupId` acts as the tag that specifies that a message belongs to a specific message group. Messages that belong to the same message group are processed in a FIFO manner (however, messages in different message groups might be processed out of order). To interleave multiple ordered streams within a single queue, use `MessageGroupId` values (for example, session data for multiple users). In this scenario, multiple consumers can process the queue, but the session data of each user is processed in a FIFO fashion.

  If you do not provide a `MessageGroupId` when sending a message to a FIFO queue, the action fails.

   `ReceiveMessage` might return messages with multiple `MessageGroupId` values. For each `MessageGroupId`, the messages are sorted by time sent.
+  **Standard queues:**Use `MessageGroupId` in standard queues to enable fair queues. The `MessageGroupId` identifies the tenant a message belongs to. A tenant can be any entity that shares a queue with others, such as your customer, a client application, or a request type. When one tenant sends a disproportionately large volume of messages or has messages that require longer processing time, fair queues ensure other tenants' messages maintain low dwell time. This preserves quality of service for all tenants while maintaining the scalability and throughput of standard queues. We recommend that you include a `MessageGroupId` in all messages when using fair queues.
The length of `MessageGroupId` is 128 characters. Valid values: alphanumeric characters and punctuation `(!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~)`.
For best practices of using `MessageGroupId`, see [Using the MessageGroupId Property](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/using-messagegroupid-property.html) in the *Amazon SQS Developer Guide*.
Type: String
Required: No

 ** [MessageSystemAttributes](#API_SendMessage_RequestSyntax) **   <a name="SQS-SendMessage-request-MessageSystemAttributes"></a>
The message system attribute to send. Each message system attribute consists of a `Name`, `Type`, and `Value`.
+ Currently, the only supported message system attribute is `AWSTraceHeader`. Its type must be `String` and its value must be a correctly formatted AWS X-Ray trace header string.
+ The size of a message system attribute doesn't count towards the total size of a message.
Type: String to [MessageSystemAttributeValue](API_MessageSystemAttributeValue.md) object map
Valid Keys: `AWSTraceHeader`
Required: No

 ** [QueueUrl](#API_SendMessage_RequestSyntax) **   <a name="SQS-SendMessage-request-QueueUrl"></a>
The URL of the Amazon SQS queue to which a message is sent.
Queue URLs and names are case-sensitive.
Type: String
Required: Yes

## Response Syntax
<a name="API_SendMessage_ResponseSyntax"></a>

```
{
   "MD5OfMessageAttributes": "string",
   "MD5OfMessageBody": "string",
   "MD5OfMessageSystemAttributes": "string",
   "MessageId": "string",
   "SequenceNumber": "string"
}
```

## Response Elements
<a name="API_SendMessage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [MD5OfMessageAttributes](#API_SendMessage_ResponseSyntax) **   <a name="SQS-SendMessage-response-MD5OfMessageAttributes"></a>
An MD5 digest of the non-URL-encoded message attribute string. You can use this attribute to verify that Amazon SQS received the message correctly. Amazon SQS URL-decodes the message before creating the MD5 digest. For information about MD5, see [RFC1321](https://www.ietf.org/rfc/rfc1321.txt).
Type: String

 ** [MD5OfMessageBody](#API_SendMessage_ResponseSyntax) **   <a name="SQS-SendMessage-response-MD5OfMessageBody"></a>
An MD5 digest of the non-URL-encoded message body string. You can use this attribute to verify that Amazon SQS received the message correctly. Amazon SQS URL-decodes the message before creating the MD5 digest. For information about MD5, see [RFC1321](https://www.ietf.org/rfc/rfc1321.txt).
Type: String

 ** [MD5OfMessageSystemAttributes](#API_SendMessage_ResponseSyntax) **   <a name="SQS-SendMessage-response-MD5OfMessageSystemAttributes"></a>
An MD5 digest of the non-URL-encoded message system attribute string. You can use this attribute to verify that Amazon SQS received the message correctly. Amazon SQS URL-decodes the message before creating the MD5 digest.
Type: String

 ** [MessageId](#API_SendMessage_ResponseSyntax) **   <a name="SQS-SendMessage-response-MessageId"></a>
An attribute containing the `MessageId` of the message sent to the queue. For more information, see [Queue and Message Identifiers](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-queue-message-identifiers.html) in the *Amazon SQS Developer Guide*.
Type: String

 ** [SequenceNumber](#API_SendMessage_ResponseSyntax) **   <a name="SQS-SendMessage-response-SequenceNumber"></a>
This parameter applies only to FIFO (first-in-first-out) queues.
The large, non-consecutive number that Amazon SQS assigns to each message.
The length of `SequenceNumber` is 128 bits. `SequenceNumber` continues to increase for a particular `MessageGroupId`.
Type: String

## Errors
<a name="API_SendMessage_Errors"></a>

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md).

 ** InvalidAddress **
The specified ID is invalid.
HTTP Status Code: 400

 ** InvalidMessageContents **
The message contains characters outside the allowed set.
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
<a name="API_SendMessage_Examples"></a>

The following example `SendMessage` request sends a message containing `This is a test message` to the queue. You must URL-encode the entire URL. However, in this example only the message body is URL-encoded to make the example easier to read. The structure of `AUTHPARAMS` depends on the signature of the API request. For more information, see [ Examples of Signed Signature Version 4 Requests](https://docs.aws.amazon.com/general/latest/gr/sigv4-signed-request-examples.html) in the * AWS General Reference*.

### Example
<a name="API_SendMessage_Example_1"></a>

 **Using AWS JSON protocol (Default)**

#### Sample Request
<a name="API_SendMessage_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: sqs.us-east-1.amazonaws.com
X-Amz-Target: AmazonSQS.SendMessage
X-Amz-Date: <Date>
Content-Type: application/x-amz-json-1.0
Authorization: <AuthParams>
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
{
    "QueueUrl": "https://sqs.us-east-1.amazonaws.com/177715257436/MyQueue/",
    "MessageBody": "This is a test message",
    "MessageAttributes": {
        "my_attribute_name_1": {
            "DataType": "String",
            "StringValue": "my_attribute_value_1"
        },
        "my_attribute_name_2": {
            "DataType": "String",
            "StringValue": "my_attribute_value_2"
        }
    }
}
```

#### Sample Response
<a name="API_SendMessage_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <requestId>
Content-Length: <PayloadSizeBytes>
Date: <Date>
Content-Type: application/x-amz-json-1.0
{
    "MD5OfMessageAttributes": "c48838208d2b4e14e3ca0093a8443f09",
    "MD5OfMessageBody": "fafb00f5732ab283681e124bf8747ed1",
    "MessageId": "219f8380-5770-4cc2-8c3e-5c715e145f5e"
}
```

### Example
<a name="API_SendMessage_Example_2"></a>

 **Using AWS query protocol**

#### Sample Request
<a name="API_SendMessage_Example_2_Request"></a>

```
POST /177715257436/MyQueue/ HTTP/1.1
Host: sqs.us-east-1.amazonaws.com
X-Amz-Date: <Date>
Content-Type: application/x-www-form-urlencoded
Authorization: <AuthParams>
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
Action=SendMessage
&MessageBody=This+is+a+test+message
&MessageAttribute.1.Name=my_attribute_name_1
&MessageAttribute.1.Value.StringValue=my_attribute_value_1
&MessageAttribute.1.Value.DataType=String
&MessageAttribute.2.Name=my_attribute_name_2
&MessageAttribute.2.Value.StringValue=my_attribute_value_2
&MessageAttribute.2.Value.DataType=String
```

#### Sample Response
<a name="API_SendMessage_Example_2_Response"></a>

```
HTTP/1.1 200 OK
<?xml version="1.0"?>
<SendMessageResponse xmlns="http://queue.amazonaws.com/doc/2012-11-05/">
    <SendMessageResult>
        <MessageId>374cec7b-d0c8-4a2e-ad0b-67be763cf97e</MessageId>
        <MD5OfMessageBody>fafb00f5732ab283681e124bf8747ed1</MD5OfMessageBody>
        <MD5OfMessageAttributes>c48838208d2b4e14e3ca0093a8443f09</MD5OfMessageAttributes>
    </SendMessageResult>
    <ResponseMetadata>
        <RequestId>7fe4446e-b452-53f7-8f85-181e06f2dd99</RequestId>
    </ResponseMetadata>
</SendMessageResponse>
```

### Example
<a name="API_SendMessage_Example_3"></a>

The following example creates a *message timer*—applying a 45-second initial visibility delay to a single message— by calling the `SendMessage` action with the `DelaySeconds` parameter set to 45 seconds.

**Note**
Queue URLs and names are case-sensitive.

 **Using AWS JSON protocol (Default)**

#### Sample Request
<a name="API_SendMessage_Example_3_Request"></a>

```
POST / HTTP/1.1
Host: sqs.us-east-1.amazonaws.com
X-Amz-Target: AmazonSQS.SendMessage
X-Amz-Date: <Date>
Content-Type: application/x-amz-json-1.0
Authorization: <AuthParams>
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
{
    "QueueUrl": "https://sqs.us-east-1.amazonaws.com/177715257436/MyQueue/",
    "MessageBody": "This is a test message",
    "DelaySeconds": 45
}
```

### Example
<a name="API_SendMessage_Example_4"></a>

 **Using AWS query protocol**

#### Sample Request
<a name="API_SendMessage_Example_4_Request"></a>

```
POST /177715257436/MyQueue/ HTTP/1.1
Host: sqs.us-east-1.amazonaws.com
X-Amz-Date: <Date>
Content-Type: application/x-www-form-urlencoded
Authorization: <AuthParams>
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
Action=SendMessage
&MessageBody=This+is+a+test+message
&DelaySeconds=45
```

## See Also
<a name="API_SendMessage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sqs-2012-11-05/SendMessage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sqs-2012-11-05/SendMessage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sqs-2012-11-05/SendMessage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sqs-2012-11-05/SendMessage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sqs-2012-11-05/SendMessage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sqs-2012-11-05/SendMessage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sqs-2012-11-05/SendMessage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sqs-2012-11-05/SendMessage)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sqs-2012-11-05/SendMessage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sqs-2012-11-05/SendMessage)
