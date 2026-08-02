---
source_url: https://docs.aws.amazon.com/grafana/latest/APIReference/API_CreateWorkspaceServiceAccount.html
---

# CreateWorkspaceServiceAccount
<a name="API_CreateWorkspaceServiceAccount"></a>

Creates a service account for the workspace. A service account can be used to call Grafana HTTP APIs, and run automated workloads. After creating the service account with the correct `GrafanaRole` for your use case, use `CreateWorkspaceServiceAccountToken` to create a token that can be used to authenticate and authorize Grafana HTTP API calls.

You can only create service accounts for workspaces that are compatible with Grafana version 9 and above.

**Note**
For more information about service accounts, see [Service accounts](https://docs.aws.amazon.com/grafana/latest/userguide/service-accounts.html) in the *Amazon Managed Grafana User Guide*.
For more information about the Grafana HTTP APIs, see [Using Grafana HTTP APIs](https://docs.aws.amazon.com/grafana/latest/userguide/Using-Grafana-APIs.html) in the *Amazon Managed Grafana User Guide*.

## Request Syntax
<a name="API_CreateWorkspaceServiceAccount_RequestSyntax"></a>

```
POST /workspaces/{{workspaceId}}/serviceaccounts HTTP/1.1
Content-type: application/json

{
   "grafanaRole": "{{string}}",
   "name": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateWorkspaceServiceAccount_RequestParameters"></a>

The request uses the following URI parameters.

 ** [workspaceId](#API_CreateWorkspaceServiceAccount_RequestSyntax) **   <a name="ManagedGrafana-CreateWorkspaceServiceAccount-request-uri-workspaceId"></a>
The ID of the workspace within which to create the service account.
Pattern: `g-[0-9a-f]{10}`
Required: Yes

## Request Body
<a name="API_CreateWorkspaceServiceAccount_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [grafanaRole](#API_CreateWorkspaceServiceAccount_RequestSyntax) **   <a name="ManagedGrafana-CreateWorkspaceServiceAccount-request-grafanaRole"></a>
The permission level to use for this service account.
For more information about the roles and the permissions each has, see [User roles](https://docs.aws.amazon.com/grafana/latest/userguide/Grafana-user-roles.html) in the *Amazon Managed Grafana User Guide*.
Type: String
Valid Values: `ADMIN | EDITOR | VIEWER`
Required: Yes

 ** [name](#API_CreateWorkspaceServiceAccount_RequestSyntax) **   <a name="ManagedGrafana-CreateWorkspaceServiceAccount-request-name"></a>
A name for the service account. The name must be unique within the workspace, as it determines the ID associated with the service account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

## Response Syntax
<a name="API_CreateWorkspaceServiceAccount_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "grafanaRole": "string",
   "id": "string",
   "name": "string",
   "workspaceId": "string"
}
```

## Response Elements
<a name="API_CreateWorkspaceServiceAccount_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [grafanaRole](#API_CreateWorkspaceServiceAccount_ResponseSyntax) **   <a name="ManagedGrafana-CreateWorkspaceServiceAccount-response-grafanaRole"></a>
The permission level given to the service account.
Type: String
Valid Values: `ADMIN | EDITOR | VIEWER`

 ** [id](#API_CreateWorkspaceServiceAccount_ResponseSyntax) **   <a name="ManagedGrafana-CreateWorkspaceServiceAccount-response-id"></a>
The ID of the service account.
Type: String

 ** [name](#API_CreateWorkspaceServiceAccount_ResponseSyntax) **   <a name="ManagedGrafana-CreateWorkspaceServiceAccount-response-name"></a>
The name of the service account.
Type: String

 ** [workspaceId](#API_CreateWorkspaceServiceAccount_ResponseSyntax) **   <a name="ManagedGrafana-CreateWorkspaceServiceAccount-response-workspaceId"></a>
The workspace with which the service account is associated.
Type: String
Pattern: `g-[0-9a-f]{10}`

## Errors
<a name="API_CreateWorkspaceServiceAccount_Errors"></a>

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

 ** ServiceQuotaExceededException **
The request would cause a service quota to be exceeded.
 ** message **
A description of the error.
 ** quotaCode **
The ID of the service quota that was exceeded.
 ** resourceId **
The ID of the resource that is associated with the error.
 ** resourceType **
The type of the resource that is associated with the error.
 ** serviceCode **
The value of a parameter in the request caused an error.
HTTP Status Code: 402

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
<a name="API_CreateWorkspaceServiceAccount_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/grafana-2020-08-18/CreateWorkspaceServiceAccount)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/grafana-2020-08-18/CreateWorkspaceServiceAccount)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/grafana-2020-08-18/CreateWorkspaceServiceAccount)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/grafana-2020-08-18/CreateWorkspaceServiceAccount)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/grafana-2020-08-18/CreateWorkspaceServiceAccount)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/grafana-2020-08-18/CreateWorkspaceServiceAccount)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/grafana-2020-08-18/CreateWorkspaceServiceAccount)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/grafana-2020-08-18/CreateWorkspaceServiceAccount)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/grafana-2020-08-18/CreateWorkspaceServiceAccount)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/grafana-2020-08-18/CreateWorkspaceServiceAccount)
