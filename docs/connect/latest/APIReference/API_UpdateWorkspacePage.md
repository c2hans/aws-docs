---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdateWorkspacePage.html
---

# UpdateWorkspacePage
<a name="API_UpdateWorkspacePage"></a>

Updates the configuration of a page in a workspace, including the associated view and input data.

## Request Syntax
<a name="API_UpdateWorkspacePage_RequestSyntax"></a>

```
POST /workspaces/{{InstanceId}}/{{WorkspaceId}}/pages/{{Page}} HTTP/1.1
Content-type: application/json

{
   "InputData": "{{string}}",
   "NewPage": "{{string}}",
   "ResourceArn": "{{string}}",
   "Slug": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateWorkspacePage_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_UpdateWorkspacePage_RequestSyntax) **   <a name="connect-UpdateWorkspacePage-request-uri-InstanceId"></a>
The identifier of the Amazon Connect instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [Page](#API_UpdateWorkspacePage_RequestSyntax) **   <a name="connect-UpdateWorkspacePage-request-uri-Page"></a>
The current page identifier.
Length Constraints: Minimum length of 1. Maximum length of 25.
Pattern: `^(?!\\.$)(?!\\.\\.$)[\\p{L}\\p{Z}\\p{N}\\-_.:=@'|]+$`
Required: Yes

 ** [WorkspaceId](#API_UpdateWorkspacePage_RequestSyntax) **   <a name="connect-UpdateWorkspacePage-request-uri-WorkspaceId"></a>
The identifier of the workspace.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## Request Body
<a name="API_UpdateWorkspacePage_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [InputData](#API_UpdateWorkspacePage_RequestSyntax) **   <a name="connect-UpdateWorkspacePage-request-InputData"></a>
A JSON string containing input parameters for the view.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Required: No

 ** [NewPage](#API_UpdateWorkspacePage_RequestSyntax) **   <a name="connect-UpdateWorkspacePage-request-NewPage"></a>
The new page identifier, if changing the page name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 25.
Pattern: `^(?!\\.$)(?!\\.\\.$)[\\p{L}\\p{Z}\\p{N}\\-_.:=@'|]+$`
Required: No

 ** [ResourceArn](#API_UpdateWorkspacePage_RequestSyntax) **   <a name="connect-UpdateWorkspacePage-request-ResourceArn"></a>
The Amazon Resource Name (ARN) of the view to associate with the page.
Type: String
Required: No

 ** [Slug](#API_UpdateWorkspacePage_RequestSyntax) **   <a name="connect-UpdateWorkspacePage-request-Slug"></a>
The URL-friendly identifier for the page.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `^$|^[\\p{L}\\p{Z}\\p{N}\\-_.:=@'|]{3,}$`
Required: No

## Response Syntax
<a name="API_UpdateWorkspacePage_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateWorkspacePage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateWorkspacePage_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** DuplicateResourceException **
A resource with the specified name already exists.
HTTP Status Code: 409

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidParameterException **
One or more of the specified parameters are not valid.
 ** Message **
The message about the parameters.
HTTP Status Code: 400

 ** InvalidRequestException **
The request is not valid.
 ** Message **
The message about the request.
 ** Reason **
Reason why the request was invalid.
HTTP Status Code: 400

 ** ResourceConflictException **
A resource already has that name.
HTTP Status Code: 409

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_UpdateWorkspacePage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/UpdateWorkspacePage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/UpdateWorkspacePage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/UpdateWorkspacePage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/UpdateWorkspacePage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/UpdateWorkspacePage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/UpdateWorkspacePage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/UpdateWorkspacePage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/UpdateWorkspacePage)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/UpdateWorkspacePage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/UpdateWorkspacePage)
