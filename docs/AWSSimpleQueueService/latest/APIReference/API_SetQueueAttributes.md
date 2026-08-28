---
source_url: https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_SetQueueAttributes.html
---

# SetQueueAttributes
<a name="API_SetQueueAttributes"></a>

Sets the value of one or more queue attributes, like a policy. When you change a queue's attributes, the change can take up to 60 seconds for most of the attributes to propagate throughout the Amazon SQS system. Changes made to the `MessageRetentionPeriod` attribute can take up to 15 minutes and will impact existing messages in the queue potentially causing them to be expired and deleted if the `MessageRetentionPeriod` is reduced below the age of existing messages.

**Note**
In the future, new attributes might be added. If you write code that calls this action, we recommend that you structure your code so that it can handle new attributes gracefully.
Cross-account permissions don't apply to this action. For more information, see [Grant cross-account permissions to a role and a username](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-customer-managed-policy-examples.html#grant-cross-account-permissions-to-role-and-user-name) in the *Amazon SQS Developer Guide*.
To remove the ability to change queue permissions, you must deny permission to the `AddPermission`, `RemovePermission`, and `SetQueueAttributes` actions in your IAM policy.

## Request Syntax
<a name="API_SetQueueAttributes_RequestSyntax"></a>

```
{
   "Attributes": {
      "{{string}}" : "{{string}}"
   },
   "QueueUrl": "{{string}}"
}
```

## Request Parameters
<a name="API_SetQueueAttributes_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Attributes](#API_SetQueueAttributes_RequestSyntax) **   <a name="SQS-SetQueueAttributes-request-Attributes"></a>
A map of attributes to set.
The following lists the names, descriptions, and values of the special request parameters that the `SetQueueAttributes` action uses:
+  `DelaySeconds` – The length of time, in seconds, for which the delivery of all messages in the queue is delayed. Valid values: An integer from 0 to 900 (15 minutes). Default: 0.
+  `MaximumMessageSize` – The limit of how many bytes a message can contain before Amazon SQS rejects it. Valid values: An integer from 1,024 bytes (1 KiB) up to 1,048,576 bytes (1 MiB). Default: 1,048,576 bytes (1 MiB).
+  `MessageRetentionPeriod` – The length of time, in seconds, for which Amazon SQS retains a message. Valid values: An integer representing seconds, from 60 (1 minute) to 1,209,600 (14 days). Default: 345,600 (4 days). When you change a queue's attributes, the change can take up to 60 seconds for most of the attributes to propagate throughout the Amazon SQS system. Changes made to the `MessageRetentionPeriod` attribute can take up to 15 minutes and will impact existing messages in the queue potentially causing them to be expired and deleted if the `MessageRetentionPeriod` is reduced below the age of existing messages.
+  `Policy` – The queue's policy. A valid AWS policy. For more information about policy structure, see [Overview of AWS IAM Policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/PoliciesOverview.html) in the * AWS Identity and Access Management User Guide*.
+  `ReceiveMessageWaitTimeSeconds` – The length of time, in seconds, for which a ` ReceiveMessage ` action waits for a message to arrive. Valid values: An integer from 0 to 20 (seconds). Default: 0.
+  `VisibilityTimeout` – The visibility timeout for the queue, in seconds. Valid values: An integer from 0 to 43,200 (12 hours). Default: 30. For more information about the visibility timeout, see [Visibility Timeout](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-visibility-timeout.html) in the *Amazon SQS Developer Guide*.
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
+  `KmsMasterKeyId` – The ID of an AWS managed customer master key (CMK) for Amazon SQS or a custom CMK. For more information, see [Key Terms](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-server-side-encryption.html#sqs-sse-key-terms). While the alias of the AWS-managed CMK for Amazon SQS is always `alias/aws/sqs`, the alias of a custom CMK can, for example, be `alias/MyAlias `. For more examples, see [KeyId](https://docs.aws.amazon.com/kms/latest/APIReference/API_DescribeKey.html#API_DescribeKey_RequestParameters) in the * AWS Key Management Service API Reference*.
+  `KmsDataKeyReusePeriodSeconds` – The length of time, in seconds, for which Amazon SQS can reuse a [data key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#data-keys) to encrypt or decrypt messages before calling AWS KMS again. An integer representing seconds, between 60 seconds (1 minute) and 86,400 seconds (24 hours). Default: 300 (5 minutes). A shorter time period provides better security but results in more calls to KMS which might incur charges after Free Tier. For more information, see [How Does the Data Key Reuse Period Work?](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-server-side-encryption.html#sqs-how-does-the-data-key-reuse-period-work).
+  `SqsManagedSseEnabled` – Enables server-side queue encryption using SQS owned encryption keys. Only one server-side encryption option is supported per queue (for example, [SSE-KMS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-configure-sse-existing-queue.html) or [SSE-SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-configure-sqs-sse-queue.html)).
The following attribute applies only to [FIFO (first-in-first-out) queues](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues.html):
+  `ContentBasedDeduplication` – Enables content-based deduplication. For more information, see [Exactly-once processing](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues-exactly-once-processing.html) in the *Amazon SQS Developer Guide*. Note the following:
  + Every message must have a unique `MessageDeduplicationId`.
    + You may provide a `MessageDeduplicationId` explicitly.
    + If you aren't able to provide a `MessageDeduplicationId` and you enable `ContentBasedDeduplication` for your queue, Amazon SQS uses a SHA-256 hash to generate the `MessageDeduplicationId` using the body of the message (but not the attributes of the message).
    + If you don't provide a `MessageDeduplicationId` and the queue doesn't have `ContentBasedDeduplication` set, the action fails with an error.
    + If the queue has `ContentBasedDeduplication` set, your `MessageDeduplicationId` overrides the generated one.
  + When `ContentBasedDeduplication` is in effect, messages with identical content sent within the deduplication interval are treated as duplicates and only one copy of the message is delivered.
  + If you send one message with `ContentBasedDeduplication` enabled and then another message with a `MessageDeduplicationId` that is the same as the one generated for the first `MessageDeduplicationId`, the two messages are treated as duplicates and only one copy of the message is delivered.
The following attributes apply only to [high throughput for FIFO queues](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/high-throughput-fifo.html):
+  `DeduplicationScope` – Specifies whether message deduplication occurs at the message group or queue level. Valid values are `messageGroup` and `queue`.
+  `FifoThroughputLimit` – Specifies whether the FIFO queue throughput quota applies to the entire queue or per message group. Valid values are `perQueue` and `perMessageGroupId`. The `perMessageGroupId` value is allowed only when the value for `DeduplicationScope` is `messageGroup`.
To enable high throughput for FIFO queues, do the following:
+ Set `DeduplicationScope` to `messageGroup`.
+ Set `FifoThroughputLimit` to `perMessageGroupId`.
If you set these attributes to anything other than the values shown for enabling high throughput, normal throughput is in effect and deduplication occurs as specified.
For information on throughput quotas, see [Quotas related to messages](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/quotas-messages.html) in the *Amazon SQS Developer Guide*.
Type: String to string map
Valid Keys: `All | Policy | VisibilityTimeout | MaximumMessageSize | MessageRetentionPeriod | ApproximateNumberOfMessages | ApproximateNumberOfMessagesNotVisible | CreatedTimestamp | LastModifiedTimestamp | QueueArn | ApproximateNumberOfMessagesDelayed | DelaySeconds | ReceiveMessageWaitTimeSeconds | RedrivePolicy | FifoQueue | ContentBasedDeduplication | KmsMasterKeyId | KmsDataKeyReusePeriodSeconds | DeduplicationScope | FifoThroughputLimit | RedriveAllowPolicy | SqsManagedSseEnabled`
Required: Yes

 ** [QueueUrl](#API_SetQueueAttributes_RequestSyntax) **   <a name="SQS-SetQueueAttributes-request-QueueUrl"></a>
The URL of the Amazon SQS queue whose attributes are set.
Queue URLs and names are case-sensitive.
Type: String
Required: Yes

## Response Elements
<a name="API_SetQueueAttributes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_SetQueueAttributes_Errors"></a>

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md).

 ** InvalidAddress **
The specified ID is invalid.
HTTP Status Code: 400

 ** InvalidAttributeName **
The specified attribute doesn't exist.
HTTP Status Code: 400

 ** InvalidAttributeValue **
A queue attribute value is invalid.
HTTP Status Code: 400

 ** InvalidSecurity **
The request was not made over HTTPS or did not use SigV4 for signing.
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
<a name="API_SetQueueAttributes_Examples"></a>

The following example query request sets a policy that gives all users ` ReceiveMessage ` permission for a queue named `MyQueue`. For more examples of policies, see [Custom Amazon SQS Access Policy Language Examples](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-creating-custom-policies-access-policy-examples.html) in the *Amazon SQS Developer Guide*. The structure of `AUTHPARAMS` depends on the signature of the API request. For more information, see [ Examples of Signed Signature Version 4 Requests](https://docs.aws.amazon.com/general/latest/gr/sigv4-signed-request-examples.html) in the * AWS General Reference*.

### Example
<a name="API_SetQueueAttributes_Example_1"></a>

 **Using AWS JSON protocol (Default)**

#### Sample Request
<a name="API_SetQueueAttributes_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: sqs.us-east-1.amazonaws.com
X-Amz-Target: AmazonSQS.SetQueueAtrributes
X-Amz-Date: <Date>
Content-Type: application/x-amz-json-1.0
Authorization: <AuthParams>
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive {
    "QueueUrl": "https://sqs.us-east-1.amazonaws.com/177715257436/MyQueue/",
    "Attributes": {
        "Policy": "{\"Version\":\"2012-10-17\",\"Id\":\"Policy1677095510157\",\"Statement\":[{\"Sid\":\"Stmt1677095506939\",\"Effect\":\"Allow\",\"Principal\":\"*\",\"Action\":\"sqs:ReceiveMessage\",\"Resource\":\"arn:aws:sqs:us-east-1:555555555555:MyQueue6\"}]}"
    }
}
```

#### Sample Response
<a name="API_SetQueueAttributes_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <requestId>
Content-Length: <PayloadSizeBytes>
Date: 0
Content-Type: application/x-amz-json-1.0
```

### Example
<a name="API_SetQueueAttributes_Example_2"></a>

 **Using AWS query protocol**

#### Sample Request
<a name="API_SetQueueAttributes_Example_2_Request"></a>

```
POST /177715257436/MyQueue/ HTTP/1.1
Host: sqs.us-east-1.amazonaws.com
X-Amz-Date: <Date>
Content-Type: application/x-www-form-urlencoded
Authorization: <AuthParams>
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
Action=SetQueueAttributes
&Attribute.Name=Policy
&Attribute.Value=%7B%22Version%22%3A%222012-10-17%22%2C%22Id%22%3A%22UseCase1%22%2C%22Statement%22%3A%5B%7B%22Sid%22%3A%22Queue1ReceiveMessage%22%2C%22Effect%22%3A%22Allow%22%2C%22Principal%22%3A%7B%22AWS%22%3A%22*%22%7D%2C%22Action%22%3A%22SQS%3AReceiveMessage%22%2C%22Resource%22%3A%22arn%3Aaws%3Asqs%3Aus-east-1%3A555555555555%3AMyQueue6%22%7D%5D%7D
```

#### Sample Response
<a name="API_SetQueueAttributes_Example_2_Response"></a>

```
HTTP/1.1 200 OK
<?xml version="1.0"?>
<SetQueueAttributesResponse xmlns="http://queue.amazonaws.com/doc/2012-11-05/">
    <ResponseMetadata>
        <RequestId>5798727f-61f0-5457-99f0-2e0fa7fce329</RequestId>
    </ResponseMetadata>
</SetQueueAttributesResponse>
```

### Example
<a name="API_SetQueueAttributes_Example_3"></a>

The following example query request sets the visibility timeout to 35 seconds for a queue named `MyQueue`. The structure of `AUTHPARAMS` depends on the signature of the API request. For more information, see [ Examples of Signed Signature Version 4 Requests](https://docs.aws.amazon.com/general/latest/gr/sigv4-signed-request-examples.html) in the * AWS General Reference*.

**Note**
An Amazon SQS message has three basic states:
Sent to a queue by a producer.
Received from the queue by a consumer.
Deleted from the queue.
A message is considered to be *stored* after it is sent to a queue by a producer, but not yet received from the queue by a consumer (that is, between states 1 and 2). There is no limit to the number of stored messages. A message is considered to be *in flight* after it is received from a queue by a consumer, but not yet deleted from the queue (that is, between states 2 and 3). There is a limit to the number of in flight messages.
Limits that apply to in flight messages are unrelated to the *unlimited* number of stored messages.
For most standard queues (depending on queue traffic and message backlog), there can be a maximum of approximately 120,000 in flight messages (received from a queue by a consumer, but not yet deleted from the queue). If you reach this limit, Amazon SQS returns the `OverLimit` error message. To avoid reaching the limit, you should delete messages from the queue after they're processed. You can also increase the number of queues you use to process your messages. To request a limit increase, [file a support request](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase&limitType=service-code-sqs).
For FIFO queues, there can be a maximum of 120,000 in flight messages (received from a queue by a consumer, but not yet deleted from the queue). If you reach this limit, Amazon SQS returns no error messages.

 **Using AWS JSON protocol (Default)**

#### Sample Request
<a name="API_SetQueueAttributes_Example_3_Request"></a>

```
POST / HTTP/1.1
Host: sqs.us-east-1.amazonaws.com
X-Amz-Target: AmazonSQS.SetQueueAtrributes
X-Amz-Date: <Date>
Content-Type: application/x-amz-json-1.0
Authorization: <AuthParams>
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive {
    "QueueUrl": "https://sqs.us-east-1.amazonaws.com/177715257436/MyQueue/",
    "Attributes": {
        "VisibilityTimeout": "35"
    }
}
```

#### Sample Response
<a name="API_SetQueueAttributes_Example_3_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <requestId>
Content-Length: <PayloadSizeBytes>
Date: 0
Content-Type: application/x-amz-json-1.0
```

### Example
<a name="API_SetQueueAttributes_Example_4"></a>

 **Using AWS query protocol**

#### Sample Request
<a name="API_SetQueueAttributes_Example_4_Request"></a>

```
POST /177715257436/MyQueue/ HTTP/1.1
Host: sqs.us-east-1.amazonaws.com
X-Amz-Date: <Date>
Content-Type: application/x-www-form-urlencoded
Authorization: <AuthParams>
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
Action=SetQueueAttributes
&Attribute.Name=VisibilityTimeout
&Attribute.Value=35
```

#### Sample Response
<a name="API_SetQueueAttributes_Example_4_Response"></a>

```
HTTP/1.1 200 OK
<?xml version="1.0"?>
<SetQueueAttributesResponse xmlns="http://queue.amazonaws.com/doc/2012-11-05/">
    <ResponseMetadata>
        <RequestId>e5cca473-4fc0-4198-a451-8abb94d02c75</RequestId>
    </ResponseMetadata>
</SetQueueAttributesResponse>
```

### Example
<a name="API_SetQueueAttributes_Example_5"></a>

The following example sets a queue named `MyDeadLetterQueue` as the dead-letter queue for a queue name `MySourceQueue` by calling the `SetQueueAttributes` action with the configuration details for the dead-letter queue.

**Note**
Queue URLs and names are case-sensitive.

 **Using AWS JSON protocol (Default)**

#### Sample Request
<a name="API_SetQueueAttributes_Example_5_Request"></a>

```
POST / HTTP/1.1
Host: sqs.us-east-1.amazonaws.com
X-Amz-Target: AmazonSQS.SetQueueAtrributes
X-Amz-Date: <Date>
Content-Type: application/x-amz-json-1.0
Authorization: <AuthParams>
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive {
    "QueueUrl": "https://sqs.us-east-1.amazonaws.com/177715257436/MyQueue/",
    "Attributes": {
        "RedrivePolicy": "{\"maxReceiveCount\":\"5\",\"deadLetterTargetArn\":\"arn:aws:sqs:us-east-1:555555555555:MyDeadLetterQueue\"}"
    }
}
```

#### Sample Response
<a name="API_SetQueueAttributes_Example_5_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <requestId>
Content-Length: <PayloadSizeBytes>
Date: 0
Content-Type: application/x-amz-json-1.0
```

### Example
<a name="API_SetQueueAttributes_Example_6"></a>

 **Using AWS query protocol**

#### Sample Request
<a name="API_SetQueueAttributes_Example_6_Request"></a>

```
POST /177715257436/MyQueue/ HTTP/1.1
Host: sqs.us-east-1.amazonaws.com
X-Amz-Date: <Date>
Content-Type: application/x-www-form-urlencoded
Authorization: <AuthParams>
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
Action=SetQueueAttributes
&Attribute.Name=RedrivePolicy
&Attribute.Value=%7B%22maxReceiveCount%22%3A%225%22%2C%20%22deadLetterTargetArn%22%3A%22arn%3Aaws%3Asqs%3Aus-east-1%3A555555555555%3AMyDeadLetterQueue%22%7D
```

#### Sample Response
<a name="API_SetQueueAttributes_Example_6_Response"></a>

```
HTTP/1.1 200 OK
<?xml version="1.0"?>
<SetQueueAttributesResponse xmlns="http://queue.amazonaws.com/doc/2012-11-05/">
    <ResponseMetadata>
        <RequestId>627e8ac6-73bf-515c-a359-d654eebaa6c3</RequestId>
    </ResponseMetadata>
</SetQueueAttributesResponse>
```

### Example
<a name="API_SetQueueAttributes_Example_7"></a>

The following example enables long polling by calling the `SetQueueAttributes` action with the `ReceiveMessageWaitTimeSeconds` parameter set to 20 seconds.

 **Using AWS JSON protocol (Default)**

#### Sample Request
<a name="API_SetQueueAttributes_Example_7_Request"></a>

```
POST / HTTP/1.1
Host: sqs.us-east-1.amazonaws.com
X-Amz-Target: AmazonSQS.SetQueueAtrributes
X-Amz-Date: <Date>
Content-Type: application/x-amz-json-1.0
Authorization: <AuthParams>
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive {
    "QueueUrl": "https://sqs.us-east-1.amazonaws.com/177715257436/MyQueue/",
    "Attributes": {
        "ReceiveMessageWaitTimeSeconds": "20"
    }
}
```

#### Sample Response
<a name="API_SetQueueAttributes_Example_7_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <requestId>
Content-Length: <PayloadSizeBytes>
Date: 0
Content-Type: application/x-amz-json-1.0
```

### Example
<a name="API_SetQueueAttributes_Example_8"></a>

 **Using AWS query protocol**

#### Sample Request
<a name="API_SetQueueAttributes_Example_8_Request"></a>

```
POST /177715257436/MyQueue/ HTTP/1.1
Host: sqs.us-east-1.amazonaws.com
X-Amz-Date: <Date>
Content-Type: application/x-www-form-urlencoded
Authorization: <AuthParams>
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
Action=SetQueueAttributes
&Attribute.Name=ReceiveMessageWaitTimeSeconds
&Attribute.Value=20
```

#### Sample Response
<a name="API_SetQueueAttributes_Example_8_Response"></a>

```
HTTP/1.1 200 OK
<?xml version="1.0"?>
<SetQueueAttributesResponse xmlns="http://queue.amazonaws.com/doc/2012-11-05/">
    <ResponseMetadata>
        <RequestId>3949c1a7-1e69-564c-ad00-9d3583174f09</RequestId>
    </ResponseMetadata>
</SetQueueAttributesResponse>
```

### Example
<a name="API_SetQueueAttributes_Example_9"></a>

The following example changes an existing queue into a delay queue by calling the `SetQueueAttributes` action with the `DelaySeconds` attribute set to 45 seconds. Changing the `DelaySeconds` attribute from its default value of `0` to a positive integer less than or equal to `900` changes the queue into a delay queue.

 **Using AWS JSON protocol (Default)**

#### Sample Request
<a name="API_SetQueueAttributes_Example_9_Request"></a>

```
POST / HTTP/1.1
Host: sqs.us-east-1.amazonaws.com
X-Amz-Target: AmazonSQS.SetQueueAtrributes
X-Amz-Date: <Date>
Content-Type: application/x-amz-json-1.0
Authorization: <AuthParams>
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive {
    "QueueUrl": "https://sqs.us-east-1.amazonaws.com/177715257436/MyQueue/",
    "Attributes": {
        "DelaySeconds": "45"
    }
}
```

#### Sample Response
<a name="API_SetQueueAttributes_Example_9_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <requestId>
Content-Length: <PayloadSizeBytes>
Date: 0
Content-Type: application/x-amz-json-1.0
```

### Example
<a name="API_SetQueueAttributes_Example_10"></a>

 **Using AWS query protocol**

#### Sample Request
<a name="API_SetQueueAttributes_Example_10_Request"></a>

```
POST /177715257436/MyQueue/ HTTP/1.1
Host: sqs.us-east-1.amazonaws.com
X-Amz-Date: <Date>
Content-Type: application/x-www-form-urlencoded
Authorization: <AuthParams>
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
Action=SetQueueAttributes
&Attribute.Name=DelaySeconds
&Attribute.Value=45
```

#### Sample Response
<a name="API_SetQueueAttributes_Example_10_Response"></a>

```
HTTP/1.1 200 OK
<?xml version="1.0"?>
<SetQueueAttributesResponse xmlns="http://queue.amazonaws.com/doc/2012-11-05/">
    <ResponseMetadata>
        <RequestId>e4761152-39b6-556e-84a0-4dc0a78f4927</RequestId>
    </ResponseMetadata>
</SetQueueAttributesResponse>
```

## See Also
<a name="API_SetQueueAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sqs-2012-11-05/SetQueueAttributes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sqs-2012-11-05/SetQueueAttributes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sqs-2012-11-05/SetQueueAttributes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sqs-2012-11-05/SetQueueAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sqs-2012-11-05/SetQueueAttributes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sqs-2012-11-05/SetQueueAttributes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sqs-2012-11-05/SetQueueAttributes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sqs-2012-11-05/SetQueueAttributes)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sqs-2012-11-05/SetQueueAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sqs-2012-11-05/SetQueueAttributes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Queue Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSSimpleQueueService` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
