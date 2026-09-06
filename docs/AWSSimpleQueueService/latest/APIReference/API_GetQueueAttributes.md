---
source_url: https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_GetQueueAttributes.html
---

# GetQueueAttributes
<a name="API_GetQueueAttributes"></a>

Gets attributes for the specified queue.

**Note**
To determine whether a queue is [FIFO](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues.html), you can check whether `QueueName` ends with the `.fifo` suffix.

## Request Syntax
<a name="API_GetQueueAttributes_RequestSyntax"></a>

```
{
   "AttributeNames": [ "{{string}}" ],
   "QueueUrl": "{{string}}"
}
```

## Request Parameters
<a name="API_GetQueueAttributes_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AttributeNames](#API_GetQueueAttributes_RequestSyntax) **   <a name="SQS-GetQueueAttributes-request-AttributeNames"></a>
A list of attributes for which to retrieve information.
The `AttributeNames` parameter is optional, but if you don't specify values for this parameter, the request returns empty results.
In the future, new attributes might be added. If you write code that calls this action, we recommend that you structure your code so that it can handle new attributes gracefully.
The following attributes are supported:
The `ApproximateNumberOfMessagesDelayed`, `ApproximateNumberOfMessagesNotVisible`, and `ApproximateNumberOfMessages` metrics may not achieve consistency until at least 1 minute after the producers stop sending messages. This period is required for the queue metadata to reach eventual consistency.
+  `All` – Returns all values.
+  `ApproximateNumberOfMessages` – Returns the approximate number of messages available for retrieval from the queue.
+  `ApproximateNumberOfMessagesDelayed` – Returns the approximate number of messages in the queue that are delayed and not available for reading immediately. This can happen when the queue is configured as a delay queue or when a message has been sent with a delay parameter.
+  `ApproximateNumberOfMessagesNotVisible` – Returns the approximate number of messages that are in flight. Messages are considered to be *in flight* if they have been sent to a client but have not yet been deleted or have not yet reached the end of their visibility window.
+  `CreatedTimestamp` – Returns the time when the queue was created in seconds ([epoch time](http://en.wikipedia.org/wiki/Unix_time)).
+  `DelaySeconds` – Returns the default delay on the queue in seconds.
+  `LastModifiedTimestamp` – Returns the time when the queue was last changed in seconds ([epoch time](http://en.wikipedia.org/wiki/Unix_time)).
+  `MaximumMessageSize` – Returns the limit of how many bytes a message can contain before Amazon SQS rejects it.
+  `MessageRetentionPeriod` – Returns the length of time, in seconds, for which Amazon SQS retains a message. When you change a queue's attributes, the change can take up to 60 seconds for most of the attributes to propagate throughout the Amazon SQS system. Changes made to the `MessageRetentionPeriod` attribute can take up to 15 minutes and will impact existing messages in the queue potentially causing them to be expired and deleted if the `MessageRetentionPeriod` is reduced below the age of existing messages.
+  `Policy` – Returns the policy of the queue.
+  `QueueArn` – Returns the Amazon resource name (ARN) of the queue.
+  `ReceiveMessageWaitTimeSeconds` – Returns the length of time, in seconds, for which the `ReceiveMessage` action waits for a message to arrive.
+  `VisibilityTimeout` – Returns the visibility timeout for the queue. For more information about the visibility timeout, see [Visibility Timeout](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-visibility-timeout.html) in the *Amazon SQS Developer Guide*.
The following attributes apply only to [dead-letter queues:](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html)
+  `RedrivePolicy` – The string that includes the parameters for the dead-letter queue functionality of the source queue as a JSON object. The parameters are as follows:
  +  `deadLetterTargetArn` – The Amazon Resource Name (ARN) of the dead-letter queue to which Amazon SQS moves messages after the value of `maxReceiveCount` is exceeded.
  +  `maxReceiveCount` – The number of times a message is delivered to the source queue before being moved to the dead-letter queue. Default: 10. When the `ReceiveCount` for a message exceeds the `maxReceiveCount` for a queue, Amazon SQS moves the message to the dead-letter-queue.
+  `RedriveAllowPolicy` – The string that includes the parameters for the permissions for the dead-letter queue redrive permission and which source queues can specify dead-letter queues as a JSON object. The parameters are as follows:
  +  `redrivePermission` – The permission type that defines which source queues can specify the current queue as the dead-letter queue. Valid values are:
    +  `allowAll` – (Default) Any source queues in this AWS account in the same Region can specify this queue as the dead-letter queue.
    +  `denyAll` – No source queues can specify this queue as the dead-letter queue.
    +  `byQueue` – Only queues specified by the `sourceQueueArns` parameter can specify this queue as the dead-letter queue.
  +  `sourceQueueArns` – The Amazon Resource Names (ARN)s of the source queues that can specify this queue as the dead-letter queue and redrive messages. You can specify this parameter only when the `redrivePermission` parameter is set to `byQueue`. You can specify up to 10 source queue ARNs. To allow more than 10 source queues to specify dead-letter queues, set the `redrivePermission` parameter to `allowAll`.
The dead-letter queue of a FIFO queue must also be a FIFO queue. Similarly, the dead-letter queue of a standard queue must also be a standard queue.
The following attributes apply only to [server-side-encryption](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-server-side-encryption.html):
+  `KmsMasterKeyId` – Returns the ID of an AWS managed customer master key (CMK) for Amazon SQS or a custom CMK. For more information, see [Key Terms](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-server-side-encryption.html#sqs-sse-key-terms).
+  `KmsDataKeyReusePeriodSeconds` – Returns the length of time, in seconds, for which Amazon SQS can reuse a data key to encrypt or decrypt messages before calling AWS KMS again. For more information, see [How Does the Data Key Reuse Period Work?](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-server-side-encryption.html#sqs-how-does-the-data-key-reuse-period-work).
+  `SqsManagedSseEnabled` – Returns information about whether the queue is using SSE-SQS encryption using SQS owned encryption keys. Only one server-side encryption option is supported per queue (for example, [SSE-KMS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-configure-sse-existing-queue.html) or [SSE-SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-configure-sqs-sse-queue.html)).
The following attributes apply only to [FIFO (first-in-first-out) queues](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues.html):
+  `FifoQueue` – Returns information about whether the queue is FIFO. For more information, see [FIFO queue logic](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues-understanding-logic.html) in the *Amazon SQS Developer Guide*.
**Note**
To determine whether a queue is [FIFO](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues.html), you can check whether `QueueName` ends with the `.fifo` suffix.
+  `ContentBasedDeduplication` – Returns whether content-based deduplication is enabled for the queue. For more information, see [Exactly-once processing](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues-exactly-once-processing.html) in the *Amazon SQS Developer Guide*.
The following attributes apply only to [high throughput for FIFO queues](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/high-throughput-fifo.html):
+  `DeduplicationScope` – Specifies whether message deduplication occurs at the message group or queue level. Valid values are `messageGroup` and `queue`.
+  `FifoThroughputLimit` – Specifies whether the FIFO queue throughput quota applies to the entire queue or per message group. Valid values are `perQueue` and `perMessageGroupId`. The `perMessageGroupId` value is allowed only when the value for `DeduplicationScope` is `messageGroup`.
To enable high throughput for FIFO queues, do the following:
+ Set `DeduplicationScope` to `messageGroup`.
+ Set `FifoThroughputLimit` to `perMessageGroupId`.
If you set these attributes to anything other than the values shown for enabling high throughput, normal throughput is in effect and deduplication occurs as specified.
For information on throughput quotas, see [Quotas related to messages](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/quotas-messages.html) in the *Amazon SQS Developer Guide*.
Type: Array of strings
Valid Values: `All | Policy | VisibilityTimeout | MaximumMessageSize | MessageRetentionPeriod | ApproximateNumberOfMessages | ApproximateNumberOfMessagesNotVisible | CreatedTimestamp | LastModifiedTimestamp | QueueArn | ApproximateNumberOfMessagesDelayed | DelaySeconds | ReceiveMessageWaitTimeSeconds | RedrivePolicy | FifoQueue | ContentBasedDeduplication | KmsMasterKeyId | KmsDataKeyReusePeriodSeconds | DeduplicationScope | FifoThroughputLimit | RedriveAllowPolicy | SqsManagedSseEnabled`
Required: No

 ** [QueueUrl](#API_GetQueueAttributes_RequestSyntax) **   <a name="SQS-GetQueueAttributes-request-QueueUrl"></a>
The URL of the Amazon SQS queue whose attribute information is retrieved.
Queue URLs and names are case-sensitive.
Type: String
Required: Yes

## Response Syntax
<a name="API_GetQueueAttributes_ResponseSyntax"></a>

```
{
   "Attributes": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_GetQueueAttributes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Attributes](#API_GetQueueAttributes_ResponseSyntax) **   <a name="SQS-GetQueueAttributes-response-Attributes"></a>
A map of attributes to their respective values.
Type: String to string map
Valid Keys: `All | Policy | VisibilityTimeout | MaximumMessageSize | MessageRetentionPeriod | ApproximateNumberOfMessages | ApproximateNumberOfMessagesNotVisible | CreatedTimestamp | LastModifiedTimestamp | QueueArn | ApproximateNumberOfMessagesDelayed | DelaySeconds | ReceiveMessageWaitTimeSeconds | RedrivePolicy | FifoQueue | ContentBasedDeduplication | KmsMasterKeyId | KmsDataKeyReusePeriodSeconds | DeduplicationScope | FifoThroughputLimit | RedriveAllowPolicy | SqsManagedSseEnabled`

## Errors
<a name="API_GetQueueAttributes_Errors"></a>

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md).

 ** InvalidAddress **
The specified ID is invalid.
HTTP Status Code: 400

 ** InvalidAttributeName **
The specified attribute doesn't exist.
HTTP Status Code: 400

 ** InvalidSecurity **
The request was not made over HTTPS or did not use SigV4 for signing.
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
<a name="API_GetQueueAttributes_Examples"></a>

The following example query request gets all the attribute values for the specified queue. The structure of `AUTHPARAMS` depends on the signature of the API request. For more information, see [ Examples of Signed Signature Version 4 Requests](https://docs.aws.amazon.com/general/latest/gr/sigv4-signed-request-examples.html) in the * AWS General Reference*.

### Example
<a name="API_GetQueueAttributes_Example_1"></a>

 **Using AWS JSON protocol (Default)**

#### Sample Request
<a name="API_GetQueueAttributes_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: sqs.us-east-1.amazonaws.com
X-Amz-Target: AmazonSQS.GetQueueAtrributes
X-Amz-Date: <Date>
Content-Type: application/x-amz-json-1.0
Authorization: <AuthParams>
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
{
    "QueueUrl": "https://sqs.us-east-1.amazonaws.com/177715257436/MyQueue/",
    "AttributeNames": ["All"]
}
```

#### Sample Response
<a name="API_GetQueueAttributes_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <requestId>
Content-Length: <PayloadSizeBytes>
Date: <Date>
Content-Type: application/x-amz-json-1.0
{
    "Attributes": {
       "QueueArn": "arn:aws:sqs:us-east-1:555555555555:MyQueue",
        "ApproximateNumberOfMessages": "0",
        "ApproximateNumberOfMessagesNotVisible": "0",
        "ApproximateNumberOfMessagesDelayed": "0",
        "CreatedTimestamp": "1676665337",
        "LastModifiedTimestamp": "1677096375",
        "VisibilityTimeout": "60",
        "MaximumMessageSize": "12345",
        "MessageRetentionPeriod": "345600",
        "DelaySeconds": "0",
        "Policy": "{\"Version\":\"2012-10-17\",\"Id\":\"Policy1677095510157\",\"Statement\":[{\"Sid\":\"Stmt1677095506939\",\"Effect\":\"Allow\",\"Principal\":\"*\",\"Action\":\"sqs:ReceiveMessage\",\"Resource\":\"arn:aws:sqs:us-east-1:555555555555:MyQueue6\"}]}",
        "RedriveAllowPolicy": "{\"redrivePermission\":\"allowAll\"}",
        "ReceiveMessageWaitTimeSeconds": "2",
        "SqsManagedSseEnabled": "true"
    }
}
```

### Example
<a name="API_GetQueueAttributes_Example_2"></a>

 **Using AWS query protocol**

#### Sample Request
<a name="API_GetQueueAttributes_Example_2_Request"></a>

```
POST /177715257436/MyQueue/ HTTP/1.1
Host: sqs.us-east-1.amazonaws.com
Content-Type: application/x-www-form-urlencoded
X-Amz-Date: <Date>
Authorization: <AuthParams>
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
Action=GetQueueAttributes
&AttributeName.1=All
```

#### Sample Response
<a name="API_GetQueueAttributes_Example_2_Response"></a>

```
HTTP/1.1 200 OK
<?xml version="1.0"?>
<GetQueueAttributesResponse xmlns="http://queue.amazonaws.com/doc/2012-11-05/">
    <GetQueueAttributesResult>
        <Attribute>
            <Name>QueueArn</Name>
            <Value>arn:aws:sqs:us-east-1:555555555555:MyQueue</Value>
        </Attribute>
        <Attribute>
            <Name>ApproximateNumberOfMessages</Name>
            <Value>5</Value>
        </Attribute>
        <Attribute>
            <Name>ApproximateNumberOfMessagesNotVisible</Name>
            <Value>0</Value>
        </Attribute>
        <Attribute>
            <Name>ApproximateNumberOfMessagesDelayed</Name>
            <Value>0</Value>
        </Attribute>
        <Attribute>
            <Name>CreatedTimestamp</Name>
            <Value>1677110910</Value>
        </Attribute>
        <Attribute>
            <Name>LastModifiedTimestamp</Name>
            <Value>1677110910</Value>
        </Attribute>
        <Attribute>
            <Name>VisibilityTimeout</Name>
            <Value>40</Value>
        </Attribute>
        <Attribute>
            <Name>MaximumMessageSize</Name>
            <Value>262144</Value>
        </Attribute>
        <Attribute>
            <Name>MessageRetentionPeriod</Name>
            <Value>345600</Value>
        </Attribute>
        <Attribute>
            <Name>DelaySeconds</Name>
            <Value>0</Value>
        </Attribute>
        <Attribute>
            <Name>ReceiveMessageWaitTimeSeconds</Name>
            <Value>0</Value>
        </Attribute>
        <Attribute>
            <Name>SqsManagedSseEnabled</Name>
            <Value>true</Value>
        </Attribute>
    </GetQueueAttributesResult>
    <ResponseMetadata>
        <RequestId>1cffc414-8cb4-54a8-9519-98644ca5f987</RequestId>
    </ResponseMetadata>
</GetQueueAttributesResponse>
```

### Example
<a name="API_GetQueueAttributes_Example_3"></a>

The following example query request gets three attribute values for the specified queue. The structure of `AUTHPARAMS` depends on the signature of the API request. For more information, see [ Examples of Signed Signature Version 4 Requests](https://docs.aws.amazon.com/general/latest/gr/sigv4-signed-request-examples.html) in the * AWS General Reference*.

 **Using AWS JSON protocol (Default)**

#### Sample Request
<a name="API_GetQueueAttributes_Example_3_Request"></a>

```
POST / HTTP/1.1
Host: sqs.us-east-1.amazonaws.com
X-Amz-Target: AmazonSQS.GetQueueAtrributes
X-Amz-Date: <Date>
Content-Type: application/x-amz-json-1.0
Authorization: <AuthParams>
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
{
    "QueueUrl": "https://sqs.us-east-1.amazonaws.com/177715257436/MyQueue/",
    "AttributeNames": ["VisibilityTimeout", "DelaySeconds", "ReceiveMessageWaitTimeSeconds"]
}
```

#### Sample Response
<a name="API_GetQueueAttributes_Example_3_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <requestId>
Content-Length: <PayloadSizeBytes>
Date: <Date>
Content-Type: application/x-amz-json-1.0
{
    "Attributes": {
       "VisibilityTimeout": "35",
       "DelaySeconds": "45",
        "ReceiveMessageWaitTimeSeconds": "20"
    }
}
```

### Example
<a name="API_GetQueueAttributes_Example_4"></a>

 **Using AWS query protocol**

#### Sample Request
<a name="API_GetQueueAttributes_Example_4_Request"></a>

```
POST /177715257436/MyQueue/ HTTP/1.1
Host: sqs.us-east-1.amazonaws.com
Content-Type: application/x-www-form-urlencoded
X-Amz-Date: <Date>
Authorization: <AuthParams>
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
Action=GetQueueAttributes
&AttributeName.1=VisibilityTimeout
&AttributeName.2=DelaySeconds
&AttributeName.3=ReceiveMessageWaitTimeSeconds
```

#### Sample Response
<a name="API_GetQueueAttributes_Example_4_Response"></a>

```
HTTP/1.1 200 OK
<?xml version="1.0"?>
<GetQueueAttributesResponse xmlns="http://queue.amazonaws.com/doc/2012-11-05/">
    <GetQueueAttributesResult>
        <Attribute>
            <Name>VisibilityTimeout</Name>
            <Value>35</Value>
        </Attribute>
        <Attribute>
            <Name>DelaySeconds</Name>
            <Value>45</Value>
        </Attribute>
        <Attribute>
            <Name>ReceiveMessageWaitTimeSeconds</Name>
            <Value>20</Value>
        </Attribute>
    </GetQueueAttributesResult>
    <ResponseMetadata>
        <RequestId>60462930-c7fd-5ef8-b6a0-75a20b5e17b8</RequestId>
    </ResponseMetadata>
</GetQueueAttributesResponse>
```

## See Also
<a name="API_GetQueueAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sqs-2012-11-05/GetQueueAttributes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sqs-2012-11-05/GetQueueAttributes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sqs-2012-11-05/GetQueueAttributes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sqs-2012-11-05/GetQueueAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sqs-2012-11-05/GetQueueAttributes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sqs-2012-11-05/GetQueueAttributes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sqs-2012-11-05/GetQueueAttributes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sqs-2012-11-05/GetQueueAttributes)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sqs-2012-11-05/GetQueueAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sqs-2012-11-05/GetQueueAttributes)
