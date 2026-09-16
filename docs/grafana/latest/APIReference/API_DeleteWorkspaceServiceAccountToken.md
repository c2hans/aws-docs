---
source_url: https://docs.aws.amazon.com/grafana/latest/APIReference/API_DeleteWorkspaceServiceAccountToken.html
---

# DeleteWorkspaceServiceAccountToken
<a name="API_DeleteWorkspaceServiceAccountToken"></a>

Deletes a token for the workspace service account.

This will disable the key associated with the token. If any automation is currently using the key, it will no longer be authenticated or authorized to perform actions with the Grafana HTTP APIs.

Service accounts are only available for workspaces that are compatible with Grafana version 9 and above.

## Request Syntax
<a name="API_DeleteWorkspaceServiceAccountToken_RequestSyntax"></a>

```
DELETE /workspaces/{{workspaceId}}/serviceaccounts/{{serviceAccountId}}/tokens/{{tokenId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteWorkspaceServiceAccountToken_RequestParameters"></a>

The request uses the following URI parameters.

 ** [serviceAccountId](#API_DeleteWorkspaceServiceAccountToken_RequestSyntax) **   <a name="ManagedGrafana-DeleteWorkspaceServiceAccountToken-request-uri-serviceAccountId"></a>
The ID of the service account from which to delete the token.
Required: Yes

 ** [tokenId](#API_DeleteWorkspaceServiceAccountToken_RequestSyntax) **   <a name="ManagedGrafana-DeleteWorkspaceServiceAccountToken-request-uri-tokenId"></a>
The ID of the token to delete.
Required: Yes

 ** [workspaceId](#API_DeleteWorkspaceServiceAccountToken_RequestSyntax) **   <a name="ManagedGrafana-DeleteWorkspaceServiceAccountToken-request-uri-workspaceId"></a>
The ID of the workspace from which to delete the token.
Pattern: `g-[0-9a-f]{10}`
Required: Yes

## Request Body
<a name="API_DeleteWorkspaceServiceAccountToken_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteWorkspaceServiceAccountToken_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "serviceAccountId": "string",
   "tokenId": "string",
   "workspaceId": "string"
}
```

## Response Elements
<a name="API_DeleteWorkspaceServiceAccountToken_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [serviceAccountId](#API_DeleteWorkspaceServiceAccountToken_ResponseSyntax) **   <a name="ManagedGrafana-DeleteWorkspaceServiceAccountToken-response-serviceAccountId"></a>
The ID of the service account where the token was deleted.
Type: String

 ** [tokenId](#API_DeleteWorkspaceServiceAccountToken_ResponseSyntax) **   <a name="ManagedGrafana-DeleteWorkspaceServiceAccountToken-response-tokenId"></a>
The ID of the token that was deleted.
Type: String

 ** [workspaceId](#API_DeleteWorkspaceServiceAccountToken_ResponseSyntax) **   <a name="ManagedGrafana-DeleteWorkspaceServiceAccountToken-response-workspaceId"></a>
The ID of the workspace where the token was deleted.
Type: String
Pattern: `g-[0-9a-f]{10}`

## Errors
<a name="API_DeleteWorkspaceServiceAccountToken_Errors"></a>

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
<a name="API_DeleteWorkspaceServiceAccountToken_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/grafana-2020-08-18/DeleteWorkspaceServiceAccountToken)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/grafana-2020-08-18/DeleteWorkspaceServiceAccountToken)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/grafana-2020-08-18/DeleteWorkspaceServiceAccountToken)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/grafana-2020-08-18/DeleteWorkspaceServiceAccountToken)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/grafana-2020-08-18/DeleteWorkspaceServiceAccountToken)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/grafana-2020-08-18/DeleteWorkspaceServiceAccountToken)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/grafana-2020-08-18/DeleteWorkspaceServiceAccountToken)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/grafana-2020-08-18/DeleteWorkspaceServiceAccountToken)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/grafana-2020-08-18/DeleteWorkspaceServiceAccountToken)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/grafana-2020-08-18/DeleteWorkspaceServiceAccountToken)
