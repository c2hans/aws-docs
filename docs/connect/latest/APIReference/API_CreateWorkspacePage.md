---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_CreateWorkspacePage.html
---

# CreateWorkspacePage
<a name="API_CreateWorkspacePage"></a>

Associates a view with a page in a workspace, defining what users see when they navigate to that page.

## Request Syntax
<a name="API_CreateWorkspacePage_RequestSyntax"></a>

```
PUT /workspaces/{{InstanceId}}/{{WorkspaceId}}/pages HTTP/1.1
Content-type: application/json

{
   "InputData": "{{string}}",
   "Page": "{{string}}",
   "ResourceArn": "{{string}}",
   "Slug": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateWorkspacePage_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_CreateWorkspacePage_RequestSyntax) **   <a name="connect-CreateWorkspacePage-request-uri-InstanceId"></a>
The identifier of the Amazon Connect instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [WorkspaceId](#API_CreateWorkspacePage_RequestSyntax) **   <a name="connect-CreateWorkspacePage-request-uri-WorkspaceId"></a>
The identifier of the workspace.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## Request Body
<a name="API_CreateWorkspacePage_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [InputData](#API_CreateWorkspacePage_RequestSyntax) **   <a name="connect-CreateWorkspacePage-request-InputData"></a>
A JSON string containing input parameters for the view, validated against the view's input schema.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Required: No

 ** [Page](#API_CreateWorkspacePage_RequestSyntax) **   <a name="connect-CreateWorkspacePage-request-Page"></a>
The page identifier. Valid system pages include `HOME` and `AGENT_EXPERIENCE`. Custom pages cannot use the `aws:` or `connect:` prefixes.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 25.
Pattern: `^(?!\\.$)(?!\\.\\.$)[\\p{L}\\p{Z}\\p{N}\\-_.:=@'|]+$`
Required: Yes

 ** [ResourceArn](#API_CreateWorkspacePage_RequestSyntax) **   <a name="connect-CreateWorkspacePage-request-ResourceArn"></a>
The Amazon Resource Name (ARN) of the view to associate with the page.
Type: String
Required: Yes

 ** [Slug](#API_CreateWorkspacePage_RequestSyntax) **   <a name="connect-CreateWorkspacePage-request-Slug"></a>
The URL-friendly identifier for the page.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `^$|^[\\p{L}\\p{Z}\\p{N}\\-_.:=@'|]{3,}$`
Required: No

## Response Syntax
<a name="API_CreateWorkspacePage_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_CreateWorkspacePage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_CreateWorkspacePage_Errors"></a>

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

 ** LimitExceededException **
The allowed limit for the resource has been exceeded.
 ** Message **
The message about the limit.
HTTP Status Code: 429

 ** ResourceConflictException **
A resource already has that name.
HTTP Status Code: 409

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The service quota has been exceeded.
 ** Reason **
The reason for the exception.
HTTP Status Code: 402

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_CreateWorkspacePage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/CreateWorkspacePage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/CreateWorkspacePage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/CreateWorkspacePage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/CreateWorkspacePage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/CreateWorkspacePage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/CreateWorkspacePage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/CreateWorkspacePage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/CreateWorkspacePage)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/CreateWorkspacePage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/CreateWorkspacePage)
