---
source_url: https://docs.aws.amazon.com/grafana/latest/APIReference/API_DeleteWorkspaceApiKey.html
---

# DeleteWorkspaceApiKey
<a name="API_DeleteWorkspaceApiKey"></a>

Deletes a Grafana API key for the workspace.

**Note**
In workspaces compatible with Grafana version 9 or above, use workspace service accounts instead of API keys. API keys will be removed in a future release.

## Request Syntax
<a name="API_DeleteWorkspaceApiKey_RequestSyntax"></a>

```
DELETE /workspaces/{{workspaceId}}/apikeys/{{keyName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteWorkspaceApiKey_RequestParameters"></a>

The request uses the following URI parameters.

 ** [keyName](#API_DeleteWorkspaceApiKey_RequestSyntax) **   <a name="ManagedGrafana-DeleteWorkspaceApiKey-request-uri-keyName"></a>
The name of the API key to delete.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [workspaceId](#API_DeleteWorkspaceApiKey_RequestSyntax) **   <a name="ManagedGrafana-DeleteWorkspaceApiKey-request-uri-workspaceId"></a>
The ID of the workspace to delete.
Pattern: `g-[0-9a-f]{10}`
Required: Yes

## Request Body
<a name="API_DeleteWorkspaceApiKey_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteWorkspaceApiKey_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "keyName": "string",
   "workspaceId": "string"
}
```

## Response Elements
<a name="API_DeleteWorkspaceApiKey_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [keyName](#API_DeleteWorkspaceApiKey_ResponseSyntax) **   <a name="ManagedGrafana-DeleteWorkspaceApiKey-response-keyName"></a>
The name of the key that was deleted.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.

 ** [workspaceId](#API_DeleteWorkspaceApiKey_ResponseSyntax) **   <a name="ManagedGrafana-DeleteWorkspaceApiKey-response-workspaceId"></a>
The ID of the workspace where the key was deleted.
Type: String
Pattern: `g-[0-9a-f]{10}`

## Errors
<a name="API_DeleteWorkspaceApiKey_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** ConflictException **
A resource was in an inconsistent state during an update or a deletion.
 ** message **
A description of the error.
 ** resourceId **
The ID of the resource that is associated with the error.
 ** resourceType **
The type of the resource that is associated with the error.
HTTP Status Code: 409

 ** InternalServerException **
Unexpected error while processing the request. Retry the request.
 ** message **
A description of the error.
 ** retryAfterSeconds **
How long to wait before you retry this operation.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request references a resource that does not exist.
 ** message **
The value of a parameter in the request caused an error.
 ** resourceId **
The ID of the resource that is associated with the error.
 ** resourceType **
The type of the resource that is associated with the error.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied because of request throttling. Retry the request.
 ** message **
A description of the error.
 ** quotaCode **
The ID of the service quota that was exceeded.
 ** retryAfterSeconds **
The value of a parameter in the request caused an error.
 ** serviceCode **
The ID of the service that is associated with the error.
HTTP Status Code: 429

 ** ValidationException **
The value of a parameter in the request caused an error.
 ** fieldList **
A list of fields that might be associated with the error.
 ** message **
A description of the error.
 ** reason **
The reason that the operation failed.
HTTP Status Code: 400

## See Also
<a name="API_DeleteWorkspaceApiKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/grafana-2020-08-18/DeleteWorkspaceApiKey)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/grafana-2020-08-18/DeleteWorkspaceApiKey)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/grafana-2020-08-18/DeleteWorkspaceApiKey)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/grafana-2020-08-18/DeleteWorkspaceApiKey)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/grafana-2020-08-18/DeleteWorkspaceApiKey)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/grafana-2020-08-18/DeleteWorkspaceApiKey)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/grafana-2020-08-18/DeleteWorkspaceApiKey)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/grafana-2020-08-18/DeleteWorkspaceApiKey)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/grafana-2020-08-18/DeleteWorkspaceApiKey)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/grafana-2020-08-18/DeleteWorkspaceApiKey)
