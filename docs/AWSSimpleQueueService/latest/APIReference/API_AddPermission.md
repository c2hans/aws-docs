---
source_url: https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_AddPermission.html
---

# AddPermission
<a name="API_AddPermission"></a>

Adds a permission to a queue for a specific [principal](https://docs.aws.amazon.com/general/latest/gr/glos-chap.html#P). This allows sharing access to the queue.

When you create a queue, you have full control access rights for the queue. Only you, the owner of the queue, can grant or deny permissions to the queue. For more information about these permissions, see [Allow Developers to Write Messages to a Shared Queue](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-writing-an-sqs-policy.html#write-messages-to-shared-queue) in the *Amazon SQS Developer Guide*.

**Note**
 `AddPermission` generates a policy for you. You can use ` SetQueueAttributes ` to upload your policy. For more information, see [Using Custom Policies with the Amazon SQS Access Policy Language](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-creating-custom-policies.html) in the *Amazon SQS Developer Guide*.
An Amazon SQS policy can have a maximum of seven actions per statement.
To remove the ability to change queue permissions, you must deny permission to the `AddPermission`, `RemovePermission`, and `SetQueueAttributes` actions in your IAM policy.
Amazon SQS `AddPermission` does not support adding a non-account principal.

**Note**
Cross-account permissions don't apply to this action. For more information, see [Grant cross-account permissions to a role and a username](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-customer-managed-policy-examples.html#grant-cross-account-permissions-to-role-and-user-name) in the *Amazon SQS Developer Guide*.

## Request Syntax
<a name="API_AddPermission_RequestSyntax"></a>

```
{
   "Actions": [ "{{string}}" ],
   "AWSAccountIds": [ "{{string}}" ],
   "Label": "{{string}}",
   "QueueUrl": "{{string}}"
}
```

## Request Parameters
<a name="API_AddPermission_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Actions](#API_AddPermission_RequestSyntax) **   <a name="SQS-AddPermission-request-Actions"></a>
The action the client wants to allow for the specified principal. Valid values: the name of any action or `*`.
For more information about these actions, see [Overview of Managing Access Permissions to Your Amazon Simple Queue Service Resource](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-overview-of-managing-access.html) in the *Amazon SQS Developer Guide*.
Specifying `SendMessage`, `DeleteMessage`, or `ChangeMessageVisibility` for `ActionName.n` also grants permissions for the corresponding batch versions of those actions: `SendMessageBatch`, `DeleteMessageBatch`, and `ChangeMessageVisibilityBatch`.
Type: Array of strings
Required: Yes

 ** [AWSAccountIds](#API_AddPermission_RequestSyntax) **   <a name="SQS-AddPermission-request-AWSAccountIds"></a>
The AWS account numbers of the [principals](https://docs.aws.amazon.com/general/latest/gr/glos-chap.html#P) who are to receive permission. For information about locating the AWS account identification, see [Your AWS Identifiers](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-making-api-requests.html#sqs-api-request-authentication) in the *Amazon SQS Developer Guide*.
Type: Array of strings
Required: Yes

 ** [Label](#API_AddPermission_RequestSyntax) **   <a name="SQS-AddPermission-request-Label"></a>
The unique identification of the permission you're setting (for example, `AliceSendMessage`). Maximum 80 characters. Allowed characters include alphanumeric characters, hyphens (`-`), and underscores (`_`).
Type: String
Required: Yes

 ** [QueueUrl](#API_AddPermission_RequestSyntax) **   <a name="SQS-AddPermission-request-QueueUrl"></a>
The URL of the Amazon SQS queue to which permissions are added.
Queue URLs and names are case-sensitive.
Type: String
Required: Yes

## Response Elements
<a name="API_AddPermission_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_AddPermission_Errors"></a>

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md).

 ** InvalidAddress **
The specified ID is invalid.
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
<a name="API_AddPermission_Examples"></a>

The following example query requests grant a ` SendMessage ` permission to the principal whose AWS account number is 177715257436 and a ` ReceiveMessage ` permission to the principal whose AWS account number is 111111111111. The structure of `AUTHPARAMS` depends on the signature of the API request. For more information, see [ Examples of Signed Signature Version 4 Requests](https://docs.aws.amazon.com/general/latest/gr/sigv4-signed-request-examples.html) in the * AWS General Reference*.

### Example
<a name="API_AddPermission_Example_1"></a>

 **Using AWS JSON protocol (Default)**

#### Sample Request
<a name="API_AddPermission_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: sqs.us-east-1.amazonaws.com
X-Amz-Target: AmazonSQS.AddPermission
X-Amz-Date: <Date>
Content-Type: application/x-amz-json-1.0
Authorization: <AuthParams>
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
{
    "QueueUrl": "https://sqs.us-east-1.amazonaws.com/177715257436/MyQueue/",
    "Label": "MyLabel",
    "Actions": ["SendMessage", "ReceiveMessage"],
    "AWSAccountIds": ["177715257436", "111111111111"]
}
```

#### Sample Response
<a name="API_AddPermission_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <requestId>
Content-Length: 0
Date: <Date>
Content-Type: application/x-amz-json-1.0
```

### Example
<a name="API_AddPermission_Example_2"></a>

 **Using AWS query protocol**

#### Sample Request
<a name="API_AddPermission_Example_2_Request"></a>

```
POST /177715257436/MyQueue HTTP/1.1
Host: sqs.us-east-1.amazonaws.com
X-Amz-Date: <Date>
Content-Type: application/x-www-form-urlencoded
Authorization: <AuthParams>
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
Action=AddPermission
&Label=MyLabel
&AWSAccountId.1=177715257436
&ActionName.1=SendMessage
&AWSAccountId.2=111111111111
&ActionName.2=ReceiveMessage
```

#### Sample Response
<a name="API_AddPermission_Example_2_Response"></a>

```
HTTP/1.1 200 OK
<?xml version="1.0"?>
<AddPermissionResponse xmlns="http://queue.amazonaws.com/doc/2012-11-05/">
    <ResponseMetadata>
        <RequestId>b05e862e-c961-5213-bd8d-da5e6667b7d7</RequestId>
    </ResponseMetadata>
</AddPermissionResponse>
```

## See Also
<a name="API_AddPermission_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sqs-2012-11-05/AddPermission)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sqs-2012-11-05/AddPermission)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sqs-2012-11-05/AddPermission)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sqs-2012-11-05/AddPermission)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sqs-2012-11-05/AddPermission)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sqs-2012-11-05/AddPermission)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sqs-2012-11-05/AddPermission)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sqs-2012-11-05/AddPermission)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sqs-2012-11-05/AddPermission)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sqs-2012-11-05/AddPermission)
