---
source_url: https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_RemovePermission.html
---

# RemovePermission
<a name="API_RemovePermission"></a>

Revokes any permissions in the queue policy that matches the specified `Label` parameter.

**Note**
Only the owner of a queue can remove permissions from it.
Cross-account permissions don't apply to this action. For more information, see [Grant cross-account permissions to a role and a username](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-customer-managed-policy-examples.html#grant-cross-account-permissions-to-role-and-user-name) in the *Amazon SQS Developer Guide*.
To remove the ability to change queue permissions, you must deny permission to the `AddPermission`, `RemovePermission`, and `SetQueueAttributes` actions in your IAM policy.

## Request Syntax
<a name="API_RemovePermission_RequestSyntax"></a>

```
{
   "Label": "{{string}}",
   "QueueUrl": "{{string}}"
}
```

## Request Parameters
<a name="API_RemovePermission_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Label](#API_RemovePermission_RequestSyntax) **   <a name="SQS-RemovePermission-request-Label"></a>
The identification of the permission to remove. This is the label added using the ` AddPermission ` action.
Type: String
Required: Yes

 ** [QueueUrl](#API_RemovePermission_RequestSyntax) **   <a name="SQS-RemovePermission-request-QueueUrl"></a>
The URL of the Amazon SQS queue from which permissions are removed.
Queue URLs and names are case-sensitive.
Type: String
Required: Yes

## Response Elements
<a name="API_RemovePermission_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_RemovePermission_Errors"></a>

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
<a name="API_RemovePermission_Examples"></a>

The following example query request removes the `MyLabel` permission from the queue named `MyQueue`. The structure of `AUTHPARAMS` depends on the signature of the API request. For more information, see [ Examples of Signed Signature Version 4 Requests](https://docs.aws.amazon.com/general/latest/gr/sigv4-signed-request-examples.html) in the * AWS General Reference*.

### Example
<a name="API_RemovePermission_Example_1"></a>

 **Using AWS JSON protocol (Default)**

#### Sample Request
<a name="API_RemovePermission_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: sqs.us-east-1.amazonaws.com
X-Amz-Target: AmazonSQS.RemovePermission
X-Amz-Date: <Date>
Content-Type: application/x-amz-json-1.0
Authorization: <AuthParams>
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
{
    "QueueUrl": "https://sqs.us-east-1.amazonaws.com/177715257436/MyQueue/",
    "Label": "MyLabel"
}
```

#### Sample Response
<a name="API_RemovePermission_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <requestId>
Content-Length: 0
Date: <Date>
Content-Type: application/x-amz-json-1.0
```

### Example
<a name="API_RemovePermission_Example_2"></a>

 **Using AWS query protocol**

#### Sample Request
<a name="API_RemovePermission_Example_2_Request"></a>

```
POST /177715257436/MyQueue/ HTTP/1.1
Host: sqs.us-east-1.amazonaws.com
X-Amz-Date: <Date>
Content-Type: application/x-www-form-urlencoded
Authorization: <AuthParams>
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
Action=RemovePermission&Label=MyLabel
```

#### Sample Response
<a name="API_RemovePermission_Example_2_Response"></a>

```
HTTP/1.1 200 OK
<?xml version="1.0"?>
<RemovePermissionResponse xmlns="http://queue.amazonaws.com/doc/2012-11-05/">
    <ResponseMetadata>
        <RequestId>133cc8b8-21a1-5aba-b65a-94c8e50d917f</RequestId>
    </ResponseMetadata>
</RemovePermissionResponse>
```

## See Also
<a name="API_RemovePermission_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sqs-2012-11-05/RemovePermission)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sqs-2012-11-05/RemovePermission)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sqs-2012-11-05/RemovePermission)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sqs-2012-11-05/RemovePermission)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sqs-2012-11-05/RemovePermission)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sqs-2012-11-05/RemovePermission)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sqs-2012-11-05/RemovePermission)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sqs-2012-11-05/RemovePermission)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sqs-2012-11-05/RemovePermission)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sqs-2012-11-05/RemovePermission)
