---
source_url: https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_SendMessageBatch.html
---

# SendMessageBatch
<a name="API_SendMessageBatch"></a>

You can use `SendMessageBatch` to send up to 10 messages to the specified queue by assigning either identical or different values to each message (or by not assigning values at all). This is a batch version of ` SendMessage.` For a FIFO queue, multiple messages within a single batch are enqueued in the order they are sent.

The result of sending each message is reported individually in the response. Because the batch request can result in a combination of successful and unsuccessful actions, you should check for batch errors even when the call returns an HTTP status code of `200`.

The maximum allowed individual message size and the maximum total payload size (the sum of the individual lengths of all of the batched messages) are both 1 MiB 1,048,576 bytes.

**Important**
A message can include only XML, JSON, and unformatted text. The following Unicode characters are allowed. For more information, see the [W3C specification for characters](http://www.w3.org/TR/REC-xml/#charsets).
 `#x9` \| `#xA` \| `#xD` \| `#x20` to `#xD7FF` \| `#xE000` to `#xFFFD` \| `#x10000` to `#x10FFFF`
If a message contains characters outside the allowed set, Amazon SQS rejects the message and returns an InvalidMessageContents error. Ensure that your message body includes only valid characters to avoid this exception.

If you don't specify the `DelaySeconds` parameter for an entry, Amazon SQS uses the default value for the queue.

## Request Syntax
<a name="API_SendMessageBatch_RequestSyntax"></a>

```
{
   "Entries": [
      {
         "DelaySeconds": {{number}},
         "Id": "{{string}}",
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
         }
      }
   ],
   "QueueUrl": "{{string}}"
}
```

## Request Parameters
<a name="API_SendMessageBatch_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Entries](#API_SendMessageBatch_RequestSyntax) **   <a name="SQS-SendMessageBatch-request-Entries"></a>
A list of ` SendMessageBatchRequestEntry ` items.
Type: Array of [SendMessageBatchRequestEntry](API_SendMessageBatchRequestEntry.md) objects
Required: Yes

 ** [QueueUrl](#API_SendMessageBatch_RequestSyntax) **   <a name="SQS-SendMessageBatch-request-QueueUrl"></a>
The URL of the Amazon SQS queue to which batched messages are sent.
Queue URLs and names are case-sensitive.
Type: String
Required: Yes

## Response Syntax
<a name="API_SendMessageBatch_ResponseSyntax"></a>

```
{
   "Failed": [
      {
         "Code": "string",
         "Id": "string",
         "Message": "string",
         "SenderFault": boolean
      }
   ],
   "Successful": [
      {
         "Id": "string",
         "MD5OfMessageAttributes": "string",
         "MD5OfMessageBody": "string",
         "MD5OfMessageSystemAttributes": "string",
         "MessageId": "string",
         "SequenceNumber": "string"
      }
   ]
}
```

## Response Elements
<a name="API_SendMessageBatch_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Failed](#API_SendMessageBatch_ResponseSyntax) **   <a name="SQS-SendMessageBatch-response-Failed"></a>
A list of ` BatchResultErrorEntry ` items with error details about each message that can't be enqueued.
Type: Array of [BatchResultErrorEntry](API_BatchResultErrorEntry.md) objects

 ** [Successful](#API_SendMessageBatch_ResponseSyntax) **   <a name="SQS-SendMessageBatch-response-Successful"></a>
A list of ` SendMessageBatchResultEntry ` items.
Type: Array of [SendMessageBatchResultEntry](API_SendMessageBatchResultEntry.md) objects

## Errors
<a name="API_SendMessageBatch_Errors"></a>

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md).

 ** BatchEntryIdsNotDistinct **
Two or more batch entries in the request have the same `Id`.
HTTP Status Code: 400

 ** BatchRequestTooLong **
The length of all the messages put together is more than the limit.
HTTP Status Code: 400

 ** EmptyBatchRequest **
The batch request doesn't contain any entries.
HTTP Status Code: 400

 ** InvalidAddress **
The specified ID is invalid.
HTTP Status Code: 400

 ** InvalidBatchEntryId **
The `Id` of a batch entry in a batch request doesn't abide by the specification.
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

 ** TooManyEntriesInBatchRequest **
The batch request contains more entries than permissible. For Amazon SQS, the maximum number of entries you can include in a single [SendMessageBatch](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_SendMessageBatch.html), [DeleteMessageBatch](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_DeleteMessageBatch.html), or [ChangeMessageVisibilityBatch](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ChangeMessageVisibilityBatch.html) request is 10.
HTTP Status Code: 400

 ** UnsupportedOperation **
Error code 400. Unsupported operation.
HTTP Status Code: 400

## Examples
<a name="API_SendMessageBatch_Examples"></a>

The following example `SendMessageBatch` request sends two messages to the queue. You must URL-encode the entire URL. However, in this example only the message body is URL-encoded to make the example easier to read. The structure of `AUTHPARAMS` depends on the signature of the API request. For more information, see [ Examples of Signed Signature Version 4 Requests](https://docs.aws.amazon.com/general/latest/gr/sigv4-signed-request-examples.html) in the * AWS General Reference*.

### Example
<a name="API_SendMessageBatch_Example_1"></a>

 **Using AWS JSON protocol (Default)**

#### Sample Request
<a name="API_SendMessageBatch_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: sqs.us-east-1.amazonaws.com
X-Amz-Target: AmazonSQS.SendMessageBatch
X-Amz-Date: <Date>
Content-Type: application/x-amz-json-1.0
Authorization: <AuthParams>
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
{
    "QueueUrl": "https://sqs.us-east-1.amazonaws.com/177715257436/MyQueue/",
    "Entries": [
        {
            "Id": "test_msg_001",
            "MessageBody": "test message body 1"
        },
        {
            "Id": "test_msg_002",
            "MessageBody": "test message body 2",
            "DelaySeconds": 60,
            "MessageAttributes": {
                "my_attribute_name_1": {
                    "DataType": "String",
                    "StringValue": "my_attribute_value_1"
                }
            }
        }
    ]
}
```

#### Sample Response
<a name="API_SendMessageBatch_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <requestId>
Content-Length: <PayloadSizeBytes>
Date: <Date>
Content-Type: application/x-amz-json-1.0
{
   "Failed": [],
    "Successful": [
        {
            "Id": "test_msg_001",
            "MD5OfMessageBody": "0e024d309850c78cba5eabbeff7cae71",
            "MessageId": "f4eb349f-cd33-4bc4-bdc2-e557c900d41d"
        },
        {
            "Id": "test_msg_002",
            "MD5OfMessageAttributes": "8ef4d60dbc8efda9f260e1dfd09d29f3",
            "MD5OfMessageBody": "27118326006d3829667a400ad23d5d98",
            "MessageId": "1dcfcd50-5a67-45ae-ae4c-1c152b5effb9"
        }
    ]
}
```

### Example
<a name="API_SendMessageBatch_Example_2"></a>

 **Using AWS query protocol**

#### Sample Request
<a name="API_SendMessageBatch_Example_2_Request"></a>

```
POST /177715257436/MyQueue/ HTTP/1.1
Host: sqs.us-east-1.amazonaws.com
X-Amz-Date: <Date>
Content-Type: application/x-www-form-urlencoded
Authorization: <AuthParams>
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
Action=SendMessageBatch
&SendMessageBatchRequestEntry.1.Id=test_msg_001
&SendMessageBatchRequestEntry.1.MessageBody=test%20message%20body%201
&SendMessageBatchRequestEntry.2.Id=test_msg_002
&SendMessageBatchRequestEntry.2.MessageBody=test%20message%20body%202
&SendMessageBatchRequestEntry.2.DelaySeconds=60
&SendMessageBatchRequestEntry.2.MessageAttribute.1.Name=test_attribute_name_1
&SendMessageBatchRequestEntry.2.MessageAttribute.1.Value.StringValue=test_attribute_value_1
&SendMessageBatchRequestEntry.2.MessageAttribute.1.Value.DataType=String
```

#### Sample Response
<a name="API_SendMessageBatch_Example_2_Response"></a>

```
HTTP/1.1 200 OK
<?xml version="1.0"?>
<SendMessageBatchResponse xmlns="http://queue.amazonaws.com/doc/2012-11-05/">
    <SendMessageBatchResult>
        <SendMessageBatchResultEntry>
            <Id>test_msg_001</Id>
            <MessageId>60e827c3-c8a5-410a-af0e-fb43746e70b1</MessageId>
            <MD5OfMessageBody>0e024d309850c78cba5eabbeff7cae71</MD5OfMessageBody>
        </SendMessageBatchResultEntry>
        <SendMessageBatchResultEntry>
            <Id>test_msg_00</Id>
            <MessageId>c6e7fc6a-b802-4724-be06-59833004578b</MessageId>
            <MD5OfMessageBody>7fb8146a82f95e0af155278f406862c2</MD5OfMessageBody>
            <MD5OfMessageAttributes>ba056227cfd9533dba1f72ad9816d233</MD5OfMessageAttributes>
        </SendMessageBatchResultEntry>
    </SendMessageBatchResult>
    <ResponseMetadata>
        <RequestId>5150a701-14f7-5609-b136-fb71a0ca744a</RequestId>
    </ResponseMetadata>
</SendMessageBatchResponse>
```

### Example
<a name="API_SendMessageBatch_Example_3"></a>

The following example sends multiple messages with *message timers*—applying a visibility delay of variable length to the messages in the batch—by calling the `SendMessageBatch` action *without* a value for `DelaySeconds` for the first message and with the values of 45 seconds and 2 minutes for the second and third messages.

**Note**
If you don't set a value for the `DelaySeconds` parameter, the message might still be subject to a delay if you add the message to a *delay queue*. For more information about using delay queues, see [Amazon SQS Delay Queues](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-delay-queues.html) in the *Amazon SQS Developer Guide*.

 **Using AWS JSON protocol (Default)**

#### Sample Request
<a name="API_SendMessageBatch_Example_3_Request"></a>

```
POST / HTTP/1.1
Host: sqs.us-east-1.amazonaws.com
X-Amz-Target: AmazonSQS.SendMessageBatch
X-Amz-Date: <Date>
Content-Type: application/x-amz-json-1.0
Authorization: <AuthParams>
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
{
    "QueueUrl": "https://sqs.us-east-1.amazonaws.com/177715257436/MyQueue/",
    "Entries": [
        {
            "Id": "test_msg_no_message_timer",
            "MessageBody": "test message body 1"
        },
        {
            "Id": "test_msg_delay_45_seconds",
            "MessageBody": "test message body 2",
            "DelaySeconds": 45
        },
        {
            "Id": "test_msg_delay_2_minutes",
            "MessageBody": "test message body 3",
            "DelaySeconds": 120
        }
    ]
}
```

### Example
<a name="API_SendMessageBatch_Example_4"></a>

 **Using AWS query protocol**

#### Sample Request
<a name="API_SendMessageBatch_Example_4_Request"></a>

```
POST /177715257436/MyQueue/ HTTP/1.1
Host: sqs.us-east-1.amazonaws.com
X-Amz-Date: <Date>
Content-Type: application/x-www-form-urlencoded
Authorization: <AuthParams>
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
Action=SendMessageBatch
&SendMessageBatchRequestEntry.1.Id=test_msg_no_message_timer
&SendMessageBatchRequestEntry.1.MessageBody=test%20message%20body%201
&SendMessageBatchRequestEntry.2.Id=test_msg_delay_45_seconds
&SendMessageBatchRequestEntry.2.MessageBody=test%20message%20body%202
&SendMessageBatchRequestEntry.2.DelaySeconds=45
&SendMessageBatchRequestEntry.3.Id=test_msg_delay_2_minutes
&SendMessageBatchRequestEntry.3.MessageBody=test%20message%20body%203
&SendMessageBatchRequestEntry.3.DelaySeconds=120
```

## See Also
<a name="API_SendMessageBatch_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sqs-2012-11-05/SendMessageBatch)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sqs-2012-11-05/SendMessageBatch)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sqs-2012-11-05/SendMessageBatch)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sqs-2012-11-05/SendMessageBatch)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sqs-2012-11-05/SendMessageBatch)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sqs-2012-11-05/SendMessageBatch)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sqs-2012-11-05/SendMessageBatch)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sqs-2012-11-05/SendMessageBatch)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sqs-2012-11-05/SendMessageBatch)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sqs-2012-11-05/SendMessageBatch)
