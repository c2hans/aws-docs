---
source_url: https://docs.aws.amazon.com/grafana/latest/APIReference/API_ListWorkspaceServiceAccounts.html
---

# ListWorkspaceServiceAccounts
<a name="API_ListWorkspaceServiceAccounts"></a>

Returns a list of service accounts for a workspace.

Service accounts are only available for workspaces that are compatible with Grafana version 9 and above.

## Request Syntax
<a name="API_ListWorkspaceServiceAccounts_RequestSyntax"></a>

```
GET /workspaces/{{workspaceId}}/serviceaccounts?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListWorkspaceServiceAccounts_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListWorkspaceServiceAccounts_RequestSyntax) **   <a name="ManagedGrafana-ListWorkspaceServiceAccounts-request-uri-maxResults"></a>
The maximum number of service accounts to include in the results.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListWorkspaceServiceAccounts_RequestSyntax) **   <a name="ManagedGrafana-ListWorkspaceServiceAccounts-request-uri-nextToken"></a>
The token for the next set of service accounts to return. (You receive this token from a previous `ListWorkspaceServiceAccounts` operation.)

 ** [workspaceId](#API_ListWorkspaceServiceAccounts_RequestSyntax) **   <a name="ManagedGrafana-ListWorkspaceServiceAccounts-request-uri-workspaceId"></a>
The workspace for which to list service accounts.
Pattern: `g-[0-9a-f]{10}`
Required: Yes

## Request Body
<a name="API_ListWorkspaceServiceAccounts_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListWorkspaceServiceAccounts_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "serviceAccounts": [
      {
         "grafanaRole": "string",
         "id": "string",
         "isDisabled": "string",
         "name": "string"
      }
   ],
   "workspaceId": "string"
}
```

## Response Elements
<a name="API_ListWorkspaceServiceAccounts_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListWorkspaceServiceAccounts_ResponseSyntax) **   <a name="ManagedGrafana-ListWorkspaceServiceAccounts-response-nextToken"></a>
The token to use when requesting the next set of service accounts.
Type: String

 ** [serviceAccounts](#API_ListWorkspaceServiceAccounts_ResponseSyntax) **   <a name="ManagedGrafana-ListWorkspaceServiceAccounts-response-serviceAccounts"></a>
An array of structures containing information about the service accounts.
Type: Array of [ServiceAccountSummary](API_ServiceAccountSummary.md) objects

 ** [workspaceId](#API_ListWorkspaceServiceAccounts_ResponseSyntax) **   <a name="ManagedGrafana-ListWorkspaceServiceAccounts-response-workspaceId"></a>
The workspace to which the service accounts are associated.
Type: String
Pattern: `g-[0-9a-f]{10}`

## Errors
<a name="API_ListWorkspaceServiceAccounts_Errors"></a>

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
<a name="API_ListWorkspaceServiceAccounts_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/grafana-2020-08-18/ListWorkspaceServiceAccounts)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/grafana-2020-08-18/ListWorkspaceServiceAccounts)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/grafana-2020-08-18/ListWorkspaceServiceAccounts)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/grafana-2020-08-18/ListWorkspaceServiceAccounts)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/grafana-2020-08-18/ListWorkspaceServiceAccounts)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/grafana-2020-08-18/ListWorkspaceServiceAccounts)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/grafana-2020-08-18/ListWorkspaceServiceAccounts)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/grafana-2020-08-18/ListWorkspaceServiceAccounts)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/grafana-2020-08-18/ListWorkspaceServiceAccounts)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/grafana-2020-08-18/ListWorkspaceServiceAccounts)
