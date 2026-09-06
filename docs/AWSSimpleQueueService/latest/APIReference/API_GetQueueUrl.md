---
source_url: https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_GetQueueUrl.html
---

# GetQueueUrl
<a name="API_GetQueueUrl"></a>

The `GetQueueUrl` API returns the URL of an existing Amazon SQS queue. This is useful when you know the queue's name but need to retrieve its URL for further operations.

To access a queue owned by another AWS account, use the `QueueOwnerAWSAccountId` parameter to specify the account ID of the queue's owner. Note that the queue owner must grant you the necessary permissions to access the queue. For more information about accessing shared queues, see the ` AddPermission ` API or [Allow developers to write messages to a shared queue](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-writing-an-sqs-policy.html#write-messages-to-shared-queue) in the *Amazon SQS Developer Guide*.

## Request Syntax
<a name="API_GetQueueUrl_RequestSyntax"></a>

```
{
   "QueueName": "{{string}}",
   "QueueOwnerAWSAccountId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetQueueUrl_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [QueueName](#API_GetQueueUrl_RequestSyntax) **   <a name="SQS-GetQueueUrl-request-QueueName"></a>
(Required) The name of the queue for which you want to fetch the URL. The name can be up to 80 characters long and can include alphanumeric characters, hyphens (-), and underscores (\_). Queue URLs and names are case-sensitive.
Type: String
Required: Yes

 ** [QueueOwnerAWSAccountId](#API_GetQueueUrl_RequestSyntax) **   <a name="SQS-GetQueueUrl-request-QueueOwnerAWSAccountId"></a>
(Optional) The AWS account ID of the account that created the queue. This is only required when you are attempting to access a queue owned by another AWS account.
Type: String
Required: No

## Response Syntax
<a name="API_GetQueueUrl_ResponseSyntax"></a>

```
{
   "QueueUrl": "string"
}
```

## Response Elements
<a name="API_GetQueueUrl_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [QueueUrl](#API_GetQueueUrl_ResponseSyntax) **   <a name="SQS-GetQueueUrl-response-QueueUrl"></a>
The URL of the queue.
Type: String

## Errors
<a name="API_GetQueueUrl_Errors"></a>

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
<a name="API_GetQueueUrl_Examples"></a>

The following are examples of using the `GetQueueUrl` API via both JSON and query protocols. The structure of `AUTHPARAMS` depends on the signature of the API request. For more information, see [ Examples of Signed Signature Version 4 Requests](https://docs.aws.amazon.com/general/latest/gr/sigv4-signed-request-examples.html) in the * AWS General Reference*.

### Example
<a name="API_GetQueueUrl_Example_1"></a>

 **Using AWS JSON protocol (Default)**

#### Sample Request
<a name="API_GetQueueUrl_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: sqs.us-east-1.amazonaws.com
X-Amz-Target: AmazonSQS.GetQueueUrl
X-Amz-Date: <Date>
Content-Type: application/x-amz-json-1.0
Authorization: <AuthParams>
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
{
    "QueueName": "MyQueue"
}
```

#### Sample Response
<a name="API_GetQueueUrl_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <requestId>
Content-Length: <PayloadSizeBytes>
Date: <Date>
Content-Type: application/x-amz-json-1.0
{
    "QueueUrl": "https://sqs.us-east-1.amazonaws.com/177715257436/MyQueue"
}
```

### Example
<a name="API_GetQueueUrl_Example_2"></a>

 **Using AWS query protocol**

#### Sample Request
<a name="API_GetQueueUrl_Example_2_Request"></a>

```
POST / HTTP/1.1
Host: sqs.us-east-1.amazonaws.com
Content-Type: application/x-www-form-urlencoded
X-Amz-Date: <Date>
Authorization: <AuthParams>
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
Action=GetQueueUrl
&QueueName=MyQueue
```

#### Sample Response
<a name="API_GetQueueUrl_Example_2_Response"></a>

```
HTTP/1.1 200 OK
<?xml version="1.0"?>
<GetQueueUrlResponse xmlns="http://queue.amazonaws.com/doc/2012-11-05/">
    <GetQueueUrlResult>
        <QueueUrl>https://sqs.us-east-1.amazonaws.com/177715257436/MyQueue</QueueUrl>
    </GetQueueUrlResult>
    <ResponseMetadata>
        <RequestId>552d6f30-4c8e-5b32-aaed-33408c7d6c38</RequestId>
    </ResponseMetadata>
</GetQueueUrlResponse>
```

## See Also
<a name="API_GetQueueUrl_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sqs-2012-11-05/GetQueueUrl)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sqs-2012-11-05/GetQueueUrl)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sqs-2012-11-05/GetQueueUrl)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sqs-2012-11-05/GetQueueUrl)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sqs-2012-11-05/GetQueueUrl)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sqs-2012-11-05/GetQueueUrl)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sqs-2012-11-05/GetQueueUrl)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sqs-2012-11-05/GetQueueUrl)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sqs-2012-11-05/GetQueueUrl)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sqs-2012-11-05/GetQueueUrl)
