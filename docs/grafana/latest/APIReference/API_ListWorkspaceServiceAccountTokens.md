---
source_url: https://docs.aws.amazon.com/grafana/latest/APIReference/API_ListWorkspaceServiceAccountTokens.html
---

# ListWorkspaceServiceAccountTokens
<a name="API_ListWorkspaceServiceAccountTokens"></a>

Returns a list of tokens for a workspace service account.

**Note**
This does not return the key for each token. You cannot access keys after they are created. To create a new key, delete the token and recreate it.

Service accounts are only available for workspaces that are compatible with Grafana version 9 and above.

## Request Syntax
<a name="API_ListWorkspaceServiceAccountTokens_RequestSyntax"></a>

```
GET /workspaces/{{workspaceId}}/serviceaccounts/{{serviceAccountId}}/tokens?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListWorkspaceServiceAccountTokens_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListWorkspaceServiceAccountTokens_RequestSyntax) **   <a name="ManagedGrafana-ListWorkspaceServiceAccountTokens-request-uri-maxResults"></a>
The maximum number of tokens to include in the results.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListWorkspaceServiceAccountTokens_RequestSyntax) **   <a name="ManagedGrafana-ListWorkspaceServiceAccountTokens-request-uri-nextToken"></a>
The token for the next set of service accounts to return. (You receive this token from a previous `ListWorkspaceServiceAccountTokens` operation.)

 ** [serviceAccountId](#API_ListWorkspaceServiceAccountTokens_RequestSyntax) **   <a name="ManagedGrafana-ListWorkspaceServiceAccountTokens-request-uri-serviceAccountId"></a>
The ID of the service account for which to return tokens.
Required: Yes

 ** [workspaceId](#API_ListWorkspaceServiceAccountTokens_RequestSyntax) **   <a name="ManagedGrafana-ListWorkspaceServiceAccountTokens-request-uri-workspaceId"></a>
The ID of the workspace for which to return tokens.
Pattern: `g-[0-9a-f]{10}`
Required: Yes

## Request Body
<a name="API_ListWorkspaceServiceAccountTokens_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListWorkspaceServiceAccountTokens_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "serviceAccountId": "string",
   "serviceAccountTokens": [
      {
         "createdAt": number,
         "expiresAt": number,
         "id": "string",
         "lastUsedAt": number,
         "name": "string"
      }
   ],
   "workspaceId": "string"
}
```

## Response Elements
<a name="API_ListWorkspaceServiceAccountTokens_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListWorkspaceServiceAccountTokens_ResponseSyntax) **   <a name="ManagedGrafana-ListWorkspaceServiceAccountTokens-response-nextToken"></a>
The token to use when requesting the next set of service accounts.
Type: String

 ** [serviceAccountId](#API_ListWorkspaceServiceAccountTokens_ResponseSyntax) **   <a name="ManagedGrafana-ListWorkspaceServiceAccountTokens-response-serviceAccountId"></a>
The ID of the service account where the tokens reside.
Type: String

 ** [serviceAccountTokens](#API_ListWorkspaceServiceAccountTokens_ResponseSyntax) **   <a name="ManagedGrafana-ListWorkspaceServiceAccountTokens-response-serviceAccountTokens"></a>
An array of structures containing information about the tokens.
Type: Array of [ServiceAccountTokenSummary](API_ServiceAccountTokenSummary.md) objects

 ** [workspaceId](#API_ListWorkspaceServiceAccountTokens_ResponseSyntax) **   <a name="ManagedGrafana-ListWorkspaceServiceAccountTokens-response-workspaceId"></a>
The ID of the workspace where the tokens reside.
Type: String
Pattern: `g-[0-9a-f]{10}`

## Errors
<a name="API_ListWorkspaceServiceAccountTokens_Errors"></a>

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
<a name="API_ListWorkspaceServiceAccountTokens_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/grafana-2020-08-18/ListWorkspaceServiceAccountTokens)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/grafana-2020-08-18/ListWorkspaceServiceAccountTokens)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/grafana-2020-08-18/ListWorkspaceServiceAccountTokens)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/grafana-2020-08-18/ListWorkspaceServiceAccountTokens)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/grafana-2020-08-18/ListWorkspaceServiceAccountTokens)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/grafana-2020-08-18/ListWorkspaceServiceAccountTokens)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/grafana-2020-08-18/ListWorkspaceServiceAccountTokens)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/grafana-2020-08-18/ListWorkspaceServiceAccountTokens)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/grafana-2020-08-18/ListWorkspaceServiceAccountTokens)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/grafana-2020-08-18/ListWorkspaceServiceAccountTokens)
