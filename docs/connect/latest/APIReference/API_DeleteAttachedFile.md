---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_DeleteAttachedFile.html
---

# DeleteAttachedFile
<a name="API_DeleteAttachedFile"></a>

Deletes an attached file along with the underlying S3 Object.

**Important**
The attached file is **permanently deleted** if S3 bucket versioning is not enabled.

## Request Syntax
<a name="API_DeleteAttachedFile_RequestSyntax"></a>

```
DELETE /attached-files/{{InstanceId}}/{{FileId}}?associatedResourceArn={{AssociatedResourceArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteAttachedFile_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AssociatedResourceArn](#API_DeleteAttachedFile_RequestSyntax) **   <a name="connect-DeleteAttachedFile-request-uri-AssociatedResourceArn"></a>
The resource to which the attached file is (being) uploaded to. The supported resources are [Cases](https://docs.aws.amazon.com/connect/latest/adminguide/cases.html), [Email](https://docs.aws.amazon.com/connect/latest/adminguide/setup-email-channel.html), and [Task](https://docs.aws.amazon.com/connect/latest/adminguide/concepts-getting-started-tasks.html).
This value must be a valid ARN.
Required: Yes

 ** [FileId](#API_DeleteAttachedFile_RequestSyntax) **   <a name="connect-DeleteAttachedFile-request-uri-FileId"></a>
The unique identifier of the attached file resource.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [InstanceId](#API_DeleteAttachedFile_RequestSyntax) **   <a name="connect-DeleteAttachedFile-request-uri-InstanceId"></a>
The unique identifier of the Connect instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_DeleteAttachedFile_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteAttachedFile_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteAttachedFile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteAttachedFile_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidRequestException **
The request is not valid.
 ** Message **
The message about the request.
 ** Reason **
Reason why the request was invalid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_DeleteAttachedFile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/DeleteAttachedFile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/DeleteAttachedFile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/DeleteAttachedFile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/DeleteAttachedFile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/DeleteAttachedFile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/DeleteAttachedFile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/DeleteAttachedFile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/DeleteAttachedFile)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/DeleteAttachedFile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/DeleteAttachedFile)
