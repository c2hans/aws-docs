---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdateWorkspaceVisibility.html
---

# UpdateWorkspaceVisibility
<a name="API_UpdateWorkspaceVisibility"></a>

Updates the visibility setting of a workspace, controlling whether it is available to all users, assigned users only, or none.

## Request Syntax
<a name="API_UpdateWorkspaceVisibility_RequestSyntax"></a>

```
POST /workspaces/{{InstanceId}}/{{WorkspaceId}}/visibility HTTP/1.1
Content-type: application/json

{
   "Visibility": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateWorkspaceVisibility_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_UpdateWorkspaceVisibility_RequestSyntax) **   <a name="connect-UpdateWorkspaceVisibility-request-uri-InstanceId"></a>
The identifier of the Amazon Connect instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [WorkspaceId](#API_UpdateWorkspaceVisibility_RequestSyntax) **   <a name="connect-UpdateWorkspaceVisibility-request-uri-WorkspaceId"></a>
The identifier of the workspace.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## Request Body
<a name="API_UpdateWorkspaceVisibility_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Visibility](#API_UpdateWorkspaceVisibility_RequestSyntax) **   <a name="connect-UpdateWorkspaceVisibility-request-Visibility"></a>
The visibility setting for the workspace. Valid values are: `ALL` (available to all users), `ASSIGNED` (available only to assigned users and routing profiles), and `NONE` (not visible to any users).
Type: String
Valid Values: `ALL | ASSIGNED | NONE`
Required: Yes

## Response Syntax
<a name="API_UpdateWorkspaceVisibility_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateWorkspaceVisibility_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateWorkspaceVisibility_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

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

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_UpdateWorkspaceVisibility_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/UpdateWorkspaceVisibility)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/UpdateWorkspaceVisibility)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/UpdateWorkspaceVisibility)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/UpdateWorkspaceVisibility)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/UpdateWorkspaceVisibility)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/UpdateWorkspaceVisibility)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/UpdateWorkspaceVisibility)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/UpdateWorkspaceVisibility)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/UpdateWorkspaceVisibility)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/UpdateWorkspaceVisibility)
