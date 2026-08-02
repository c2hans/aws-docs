---
source_url: https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_TagQueue.html
---

# TagQueue
<a name="API_TagQueue"></a>

Add cost allocation tags to the specified Amazon SQS queue. For an overview, see [Tagging Your Amazon SQS Queues](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-queue-tags.html) in the *Amazon SQS Developer Guide*.

When you use queue tags, keep the following guidelines in mind:
+ Adding more than 50 tags to a queue isn't recommended.
+ Tags don't have any semantic meaning. Amazon SQS interprets tags as character strings.
+ Tags are case-sensitive.
+ A new tag with a key identical to that of an existing tag overwrites the existing tag.

For a full list of tag restrictions, see [Quotas related to queues](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-limits.html#limits-queues) in the *Amazon SQS Developer Guide*.

**Note**
Cross-account permissions don't apply to this action. For more information, see [Grant cross-account permissions to a role and a username](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-customer-managed-policy-examples.html#grant-cross-account-permissions-to-role-and-user-name) in the *Amazon SQS Developer Guide*.

## Request Syntax
<a name="API_TagQueue_RequestSyntax"></a>

```
{
   "QueueUrl": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## Request Parameters
<a name="API_TagQueue_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [QueueUrl](#API_TagQueue_RequestSyntax) **   <a name="SQS-TagQueue-request-QueueUrl"></a>
The URL of the queue.
Type: String
Required: Yes

 ** [Tags](#API_TagQueue_RequestSyntax) **   <a name="SQS-TagQueue-request-Tags"></a>
The list of tags to be added to the specified queue.
Type: String to string map
Required: Yes

## Response Elements
<a name="API_TagQueue_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_TagQueue_Errors"></a>

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md).

 ** InvalidAddress **
The specified ID is invalid.
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
<a name="API_TagQueue_Examples"></a>

This example illustrates one usage of `TagQueue`.

### Example
<a name="API_TagQueue_Example_1"></a>

 **Using AWS JSON protocol (Default)**

#### Sample Request
<a name="API_TagQueue_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: sqs.us-east-1.amazonaws.com
X-Amz-Target: AmazonSQS.TagQueue
X-Amz-Date: <Date>
Content-Type: application/x-amz-json-1.0
Authorization: <AuthParams>
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
{
    "QueueUrl": "https://sqs.us-east-1.amazonaws.com/177715257436/MyQueue/",
    "Tags": {
        "QueueType": "Production"
    }
}
```

#### Sample Response
<a name="API_TagQueue_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <requestId>
Content-Length: 0
Date: <Date>
Content-Type: application/x-amz-json-1.0
```

### Example
<a name="API_TagQueue_Example_2"></a>

 **Using AWS query protocol**

#### Sample Request
<a name="API_TagQueue_Example_2_Request"></a>

```
POST /177715257436/MyQueue/ HTTP/1.1
Host: sqs.us-east-1.amazonaws.com
X-Amz-Date: <Date>
Content-Type: application/x-www-form-urlencoded
Authorization: <AuthParams>
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
Action=TagQueue
&Tag.Key=QueueType
&Tag.Value=Production
```

#### Sample Response
<a name="API_TagQueue_Example_2_Response"></a>

```
HTTP/1.1 200 OK
<?xml version="1.0"?>
<TagQueueResponse xmlns="http://queue.amazonaws.com/doc/2012-11-05/">
    <ResponseMetadata>
        <RequestId>4bc96290-c3b5-5248-aace-3ee0056359b4</RequestId>
    </ResponseMetadata>
</TagQueueResponse>
```

## See Also
<a name="API_TagQueue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sqs-2012-11-05/TagQueue)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sqs-2012-11-05/TagQueue)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sqs-2012-11-05/TagQueue)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sqs-2012-11-05/TagQueue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sqs-2012-11-05/TagQueue)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sqs-2012-11-05/TagQueue)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sqs-2012-11-05/TagQueue)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sqs-2012-11-05/TagQueue)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sqs-2012-11-05/TagQueue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sqs-2012-11-05/TagQueue)
