---
source_url: https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_CreateQueue.html
---

# CreateQueue
<a name="API_CreateQueue"></a>

Creates a new standard or FIFO queue. You can pass one or more attributes in the request. Keep the following in mind:
+ If you don't specify the `FifoQueue` attribute, Amazon SQS creates a standard queue.
**Note**
You can't change the queue type after you create it and you can't convert an existing standard queue into a FIFO queue. You must either create a new FIFO queue for your application or delete your existing standard queue and recreate it as a FIFO queue. For more information, see [Moving From a standard queue to a FIFO queue](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues.html#FIFO-queues-moving) in the *Amazon SQS Developer Guide*.
+ If you don't provide a value for an attribute, the queue is created with the default value for the attribute.
+ If you delete a queue, you must wait at least 60 seconds before creating a queue with the same name.

To successfully create a new queue, you must provide a queue name that adheres to the [limits related to queues](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/limits-queues.html) and is unique within the scope of your queues.

**Note**
After you create a queue, you must wait at least one second after the queue is created to be able to use the queue.

To retrieve the URL of a queue, use the [https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_GetQueueUrl.html](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_GetQueueUrl.html) action. This action only requires the [https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_CreateQueue.html#API_CreateQueue_RequestSyntax](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_CreateQueue.html#API_CreateQueue_RequestSyntax) parameter.

When creating queues, keep the following points in mind:
+ If you specify the name of an existing queue and provide the exact same names and values for all its attributes, the [https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_CreateQueue.html](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_CreateQueue.html) action will return the URL of the existing queue instead of creating a new one.
+ If you attempt to create a queue with a name that already exists but with different attribute names or values, the `CreateQueue` action will return an error. This ensures that existing queues are not inadvertently altered.

**Note**
Cross-account permissions don't apply to this action. For more information, see [Grant cross-account permissions to a role and a username](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-customer-managed-policy-examples.html#grant-cross-account-permissions-to-role-and-user-name) in the *Amazon SQS Developer Guide*.

## Request Syntax
<a name="API_CreateQueue_RequestSyntax"></a>

```
{
   "Attributes": {
      "{{string}}" : "{{string}}"
   },
   "QueueName": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## Request Parameters
<a name="API_CreateQueue_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Attributes](#API_CreateQueue_RequestSyntax) **   <a name="SQS-CreateQueue-request-Attributes"></a>
A map of attributes with their corresponding values.
The following lists the names, descriptions, and values of the special request parameters that the `CreateQueue` action uses:
+  `DelaySeconds` – The length of time, in seconds, for which the delivery of all messages in the queue is delayed. Valid values: An integer from 0 to 900 seconds (15 minutes). Default: 0.
+  `MaximumMessageSize` – The limit of how many bytes a message can contain before Amazon SQS rejects it. Valid values: An integer from 1,024 bytes (1 KiB) to 1,048,576 bytes (1 MiB). Default: 1,048,576 bytes (1 MiB).
+  `MessageRetentionPeriod` – The length of time, in seconds, for which Amazon SQS retains a message. Valid values: An integer from 60 seconds (1 minute) to 1,209,600 seconds (14 days). Default: 345,600 (4 days). When you change a queue's attributes, the change can take up to 60 seconds for most of the attributes to propagate throughout the Amazon SQS system. Changes made to the `MessageRetentionPeriod` attribute can take up to 15 minutes and will impact existing messages in the queue potentially causing them to be expired and deleted if the `MessageRetentionPeriod` is reduced below the age of existing messages.
+  `Policy` – The queue's policy. A valid AWS policy. For more information about policy structure, see [Overview of AWS IAM Policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/PoliciesOverview.html) in the *IAM User Guide*.
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
+  `KmsMasterKeyId` – The ID of an AWS managed customer master key (CMK) for Amazon SQS or a custom CMK. For more information, see [Key Terms](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-server-side-encryption.html#sqs-sse-key-terms). While the alias of the AWS managed CMK for Amazon SQS is always `alias/aws/sqs`, the alias of a custom CMK can, for example, be `alias/MyAlias `. For more examples, see [KeyId](https://docs.aws.amazon.com/kms/latest/APIReference/API_DescribeKey.html#API_DescribeKey_RequestParameters) in the * AWS Key Management Service API Reference*.
+  `KmsDataKeyReusePeriodSeconds` – The length of time, in seconds, for which Amazon SQS can reuse a [data key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#data-keys) to encrypt or decrypt messages before calling AWS KMS again. An integer representing seconds, between 60 seconds (1 minute) and 86,400 seconds (24 hours). Default: 300 (5 minutes). A shorter time period provides better security but results in more calls to KMS which might incur charges after Free Tier. For more information, see [How Does the Data Key Reuse Period Work?](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-server-side-encryption.html#sqs-how-does-the-data-key-reuse-period-work)
+  `SqsManagedSseEnabled` – Enables server-side queue encryption using SQS owned encryption keys. Only one server-side encryption option is supported per queue (for example, [SSE-KMS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-configure-sse-existing-queue.html) or [SSE-SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-configure-sqs-sse-queue.html)).
The following attributes apply only to [FIFO (first-in-first-out) queues](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues.html):
+  `FifoQueue` – Designates a queue as FIFO. Valid values are `true` and `false`. If you don't specify the `FifoQueue` attribute, Amazon SQS creates a standard queue. You can provide this attribute only during queue creation. You can't change it for an existing queue. When you set this attribute, you must also provide the `MessageGroupId` for your messages explicitly.

  For more information, see [FIFO queue logic](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues-understanding-logic.html) in the *Amazon SQS Developer Guide*.
+  `ContentBasedDeduplication` – Enables content-based deduplication. Valid values are `true` and `false`. For more information, see [Exactly-once processing](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues-exactly-once-processing.html) in the *Amazon SQS Developer Guide*. Note the following:
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
Required: No

 ** [QueueName](#API_CreateQueue_RequestSyntax) **   <a name="SQS-CreateQueue-request-QueueName"></a>
The name of the new queue. The following limits apply to this name:
+ A queue name can have up to 80 characters.
+ Valid values: alphanumeric characters, hyphens (`-`), and underscores (`_`).
+ A FIFO queue name must end with the `.fifo` suffix.
Queue URLs and names are case-sensitive.
Type: String
Required: Yes

 ** [tags](#API_CreateQueue_RequestSyntax) **   <a name="SQS-CreateQueue-request-tags"></a>
Add cost allocation tags to the specified Amazon SQS queue. For an overview, see [Tagging Your Amazon SQS Queues](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-queue-tags.html) in the *Amazon SQS Developer Guide*.
When you use queue tags, keep the following guidelines in mind:
+ Adding more than 50 tags to a queue isn't recommended.
+ Tags don't have any semantic meaning. Amazon SQS interprets tags as character strings.
+ Tags are case-sensitive.
+ A new tag with a key identical to that of an existing tag overwrites the existing tag.
For a full list of tag restrictions, see [Quotas related to queues](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-limits.html#limits-queues) in the *Amazon SQS Developer Guide*.
To be able to tag a queue on creation, you must have the `sqs:CreateQueue` and `sqs:TagQueue` permissions.
Cross-account permissions don't apply to this action. For more information, see [Grant cross-account permissions to a role and a username](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-customer-managed-policy-examples.html#grant-cross-account-permissions-to-role-and-user-name) in the *Amazon SQS Developer Guide*.
Type: String to string map
Required: No

## Response Syntax
<a name="API_CreateQueue_ResponseSyntax"></a>

```
{
   "QueueUrl": "string"
}
```

## Response Elements
<a name="API_CreateQueue_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [QueueUrl](#API_CreateQueue_ResponseSyntax) **   <a name="SQS-CreateQueue-response-QueueUrl"></a>
The URL of the created Amazon SQS queue.
Type: String

## Errors
<a name="API_CreateQueue_Errors"></a>

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

 ** QueueDeletedRecently **
You must wait 60 seconds after deleting a queue before you can create another queue with the same name.
HTTP Status Code: 400

 ** QueueNameExists **
A queue with this name already exists. Amazon SQS returns this error only if the request includes attributes whose values differ from those of the existing queue.
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
<a name="API_CreateQueue_Examples"></a>

The following example query requests create a new queue named `MyQueue`. The structure of `AUTHPARAMS` depends on the signature of the API request. For more information, see [ Examples of Signed Signature Version 4 Requests](https://docs.aws.amazon.com/general/latest/gr/sigv4-signed-request-examples.html) in the * AWS General Reference*.

### Example
<a name="API_CreateQueue_Example_1"></a>

 **Using AWS JSON protocol (Default)**

#### Sample Request
<a name="API_CreateQueue_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: sqs.us-east-1.amazonaws.com
X-Amz-Target: AmazonSQS.CreateQueue
X-Amz-Date: <Date>
Content-Type: application/x-amz-json-1.0
Authorization: <AuthParams>
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
{
    "QueueName":"MyQueue",
    "Attributes": {
        "VisibilityTimeout": "40"
    },
    "tags": {
        "QueueType": "Production"
    }
}
```

#### Sample Response
<a name="API_CreateQueue_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <requestId>
Content-Length: <PayloadSizeBytes>
Date: <Date>
Content-Type: application/x-amz-json-1.0
{
    "QueueUrl":"https://sqs.us-east-1.amazonaws.com/177715257436/MyQueue"
}
```

### Example
<a name="API_CreateQueue_Example_2"></a>

 **Using AWS query protocol**

#### Sample Request
<a name="API_CreateQueue_Example_2_Request"></a>

```
POST / HTTP/1.1
Host: sqs.us-east-1.amazonaws.com
Content-Type: application/x-www-form-urlencoded
X-Amz-Date: <Date>
Authorization: <AuthParams>
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
Action=CreateQueue
&QueueName=MyQueue
&Attribute.1.Name=VisibilityTimeout
&Attribute.1.Value=40
&Tag.Key=QueueType
&Tag.Value=Production
```

#### Sample Response
<a name="API_CreateQueue_Example_2_Response"></a>

```
HTTP/1.1 200 OK
<?xml version="1.0"?>
<CreateQueueResponse xmlns="http://queue.amazonaws.com/doc/2012-11-05/">
    <CreateQueueResult>
        <QueueUrl>https://sqs.us-east-1.amazonaws.com/177715257436/MyQueue</QueueUrl>
    </CreateQueueResult>
    <ResponseMetadata>
        <RequestId>9b20926c-8b35-5d8e-9559-ce1c22e754dc</RequestId>
    </ResponseMetadata>
</CreateQueueResponse>
```

### Example
<a name="API_CreateQueue_Example_3"></a>

The following example creates a delay queue which hides each message from consumers for the first 45 seconds that the message is in the queue by calling the `CreateQueue` action with the `DelaySeconds` attribute set to 45 seconds.

**Note**
Queue URLs and names are case-sensitive.

#### Sample Request
<a name="API_CreateQueue_Example_3_Request"></a>

```
https://sqs.us-east-2.amazonaws.com/123456789012/MyQueue/
?Action=CreateQueue
&QueueName=MyQueue
&Attribute.1.Name=DelaySeconds
&Attribute.1.Value=45
&Expires=2020-12-20T22%3A52%3A43PST
&Version=2012-11-05
&AUTHPARAMS
```

## See Also
<a name="API_CreateQueue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sqs-2012-11-05/CreateQueue)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sqs-2012-11-05/CreateQueue)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sqs-2012-11-05/CreateQueue)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sqs-2012-11-05/CreateQueue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sqs-2012-11-05/CreateQueue)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sqs-2012-11-05/CreateQueue)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sqs-2012-11-05/CreateQueue)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sqs-2012-11-05/CreateQueue)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sqs-2012-11-05/CreateQueue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sqs-2012-11-05/CreateQueue)
