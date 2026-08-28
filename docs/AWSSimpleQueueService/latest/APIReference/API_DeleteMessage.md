---
source_url: https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_DeleteMessage.html
---

# DeleteMessage
<a name="API_DeleteMessage"></a>

Deletes the specified message from the specified queue. To select the message to delete, use the `ReceiptHandle` of the message (*not* the `MessageId` which you receive when you send the message). Amazon SQS can delete a message from a queue even if a visibility timeout setting causes the message to be locked by another consumer. Amazon SQS automatically deletes messages left in a queue longer than the retention period configured for the queue.

**Note**
Each time you receive a message, meaning when a consumer retrieves a message from the queue, it comes with a unique `ReceiptHandle`. If you receive the same message more than once, you will get a different `ReceiptHandle` each time. When you want to delete a message using the `DeleteMessage` action, you must use the `ReceiptHandle` from the most recent time you received the message. If you use an old `ReceiptHandle`, the request will succeed, but the message might not be deleted.
For standard queues, it is possible to receive a message even after you delete it. This might happen on rare occasions if one of the servers which stores a copy of the message is unavailable when you send the request to delete the message. The copy remains on the server and might be returned to you during a subsequent receive request. You should ensure that your application is idempotent, so that receiving a message more than once does not cause issues.

## Request Syntax
<a name="API_DeleteMessage_RequestSyntax"></a>

```
{
   "QueueUrl": "{{string}}",
   "ReceiptHandle": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteMessage_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [QueueUrl](#API_DeleteMessage_RequestSyntax) **   <a name="SQS-DeleteMessage-request-QueueUrl"></a>
The URL of the Amazon SQS queue from which messages are deleted.
Queue URLs and names are case-sensitive.
Type: String
Required: Yes

 ** [ReceiptHandle](#API_DeleteMessage_RequestSyntax) **   <a name="SQS-DeleteMessage-request-ReceiptHandle"></a>
The receipt handle associated with the message to delete.
Type: String
Required: Yes

## Response Elements
<a name="API_DeleteMessage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteMessage_Errors"></a>

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md).

 ** InvalidAddress **
The specified ID is invalid.
HTTP Status Code: 400

 ** InvalidIdFormat **
 *This error has been deprecated.*
The specified receipt handle isn't valid for the current version.
HTTP Status Code: 400

 ** InvalidSecurity **
The request was not made over HTTPS or did not use SigV4 for signing.
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
<a name="API_DeleteMessage_Examples"></a>

The following example query request deletes a message from the queue named `MyQueue`. The structure of `AUTHPARAMS` depends on the signature of the API request. For more information, see [ Examples of Signed Signature Version 4 Requests](https://docs.aws.amazon.com/general/latest/gr/sigv4-signed-request-examples.html) in the * AWS General Reference*.

### Example
<a name="API_DeleteMessage_Example_1"></a>

 **Using AWS JSON protocol (Default)**

#### Sample Request
<a name="API_DeleteMessage_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: sqs.us-east-1.amazonaws.com
X-Amz-Target: AmazonSQS.DeleteMessage
X-Amz-Date: <Date>
Content-Type: application/x-amz-json-1.0
Authorization: <AuthParams>
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
{
    "QueueUrl": "https://sqs.us-east-1.amazonaws.com/177715257436/MyQueue/",
    "ReceiptHandle": "AQEB3LQoW7GQWgodQCEJXHjMvO/QkeCHiRldRfLC/E6RUggm+BjpthqxfoUOUn6Vs271qmrBaufFqEmnMKgk2n1EuUBne1pe+hZcrDE8IveUUPmqkUT54FGhAAjPX3oEIryz/XeQ/muKAuLclcZvt2Q+ZDPW8DvZqMa1RoHxOqSq+6kQ4PwgQxB+VqDYvIc/LpHOoL4PTROBXgLPjWrzz/knK6HTzKpqC4ESvFdJ/dkk2nvS0iqYOly5VQknK/lv/rTUOgEYevjJSrNLIPDgZGyvgcLwbm6+yo1cW/c9cPDiVm96gIhVkuiCZ1gtskoOtyroZVPcY71clDG2EPZJeY8akMd3u+sXEMWhiOPFs1cgWQs2ugsL+vdwMCbsZRkXbJv7"
}
```

#### Sample Response
<a name="API_DeleteMessage_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <requestId>
Content-Length: 0
Date: <Date>
Content-Type: application/x-amz-json-1.0
```

### Example
<a name="API_DeleteMessage_Example_2"></a>

 **Using AWS query protocol**

#### Sample Request
<a name="API_DeleteMessage_Example_2_Request"></a>

```
POST /177715257436/MyQueue/ HTTP/1.1
Host: sqs.us-east-1.amazonaws.com
Content-Type: application/x-www-form-urlencoded
X-Amz-Date: <Date>
Authorization: <AuthParams>
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
Action=DeleteMessage
&ReceiptHandle=AQEBMeG2RcZZrIcgBkDFb6lHqL9B9tbbEHNh+4uxMIG+CPupPjqJtRswDlOr6hOTzgcq105i0iZNci5GS5RTnHTkD2zipM9gHfSP2tWPhY7HHsU5GCTZ+egzS5HiEvmGZ71g71Lucdk7mes1/WGXnmU27K26Koo9GGrB0AKTv16dync1ezCMNyrBHEMUyIWS2lUTbrSj7fw93dgZSg2eWTk+thSVUB/ibOwpmj+wBN99nKQQklsZHtZd4exT1V3JHwP4kqz+D3C2RGn7js3nNdFpH41lBH8rCTZDU8DQp9eQNHLIL6RUf1WrI8gv8L7NErGlIH4Y3wZbFEOMKilVHenfpP2G6ElMuxyM3y+qdlZq4m00VGIIZeMg9PPmVsLtB7u9mruLyNFraN5ihKMjzQoKgA==
```

#### Sample Response
<a name="API_DeleteMessage_Example_2_Response"></a>

```
HTTP/1.1 200 OK
<?xml version="1.0"?>
<DeleteMessageResponse xmlns="http://queue.amazonaws.com/doc/2012-11-05/">
    <ResponseMetadata>
        <RequestId>b5293cb5-d306-4a17-9048-b263635abe42</RequestId>
    </ResponseMetadata>
</DeleteMessageResponse>
```

## See Also
<a name="API_DeleteMessage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sqs-2012-11-05/DeleteMessage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sqs-2012-11-05/DeleteMessage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sqs-2012-11-05/DeleteMessage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sqs-2012-11-05/DeleteMessage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sqs-2012-11-05/DeleteMessage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sqs-2012-11-05/DeleteMessage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sqs-2012-11-05/DeleteMessage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sqs-2012-11-05/DeleteMessage)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sqs-2012-11-05/DeleteMessage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sqs-2012-11-05/DeleteMessage)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Queue Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSSimpleQueueService` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
