---
source_url: https://docs.aws.amazon.com/grafana/latest/APIReference/API_DeleteWorkspaceServiceAccount.html
---

# DeleteWorkspaceServiceAccount
<a name="API_DeleteWorkspaceServiceAccount"></a>

Deletes a workspace service account from the workspace.

This will delete any tokens created for the service account, as well. If the tokens are currently in use, the will fail to authenticate / authorize after they are deleted.

Service accounts are only available for workspaces that are compatible with Grafana version 9 and above.

## Request Syntax
<a name="API_DeleteWorkspaceServiceAccount_RequestSyntax"></a>

```
DELETE /workspaces/{{workspaceId}}/serviceaccounts/{{serviceAccountId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteWorkspaceServiceAccount_RequestParameters"></a>

The request uses the following URI parameters.

 ** [serviceAccountId](#API_DeleteWorkspaceServiceAccount_RequestSyntax) **   <a name="ManagedGrafana-DeleteWorkspaceServiceAccount-request-uri-serviceAccountId"></a>
The ID of the service account to delete.
Required: Yes

 ** [workspaceId](#API_DeleteWorkspaceServiceAccount_RequestSyntax) **   <a name="ManagedGrafana-DeleteWorkspaceServiceAccount-request-uri-workspaceId"></a>
The ID of the workspace where the service account resides.
Pattern: `g-[0-9a-f]{10}`
Required: Yes

## Request Body
<a name="API_DeleteWorkspaceServiceAccount_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteWorkspaceServiceAccount_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "serviceAccountId": "string",
   "workspaceId": "string"
}
```

## Response Elements
<a name="API_DeleteWorkspaceServiceAccount_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [serviceAccountId](#API_DeleteWorkspaceServiceAccount_ResponseSyntax) **   <a name="ManagedGrafana-DeleteWorkspaceServiceAccount-response-serviceAccountId"></a>
The ID of the service account deleted.
Type: String

 ** [workspaceId](#API_DeleteWorkspaceServiceAccount_ResponseSyntax) **   <a name="ManagedGrafana-DeleteWorkspaceServiceAccount-response-workspaceId"></a>
The ID of the workspace where the service account was deleted.
Type: String
Pattern: `g-[0-9a-f]{10}`

## Errors
<a name="API_DeleteWorkspaceServiceAccount_Errors"></a>

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
<a name="API_DeleteWorkspaceServiceAccount_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/grafana-2020-08-18/DeleteWorkspaceServiceAccount)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/grafana-2020-08-18/DeleteWorkspaceServiceAccount)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/grafana-2020-08-18/DeleteWorkspaceServiceAccount)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/grafana-2020-08-18/DeleteWorkspaceServiceAccount)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/grafana-2020-08-18/DeleteWorkspaceServiceAccount)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/grafana-2020-08-18/DeleteWorkspaceServiceAccount)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/grafana-2020-08-18/DeleteWorkspaceServiceAccount)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/grafana-2020-08-18/DeleteWorkspaceServiceAccount)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/grafana-2020-08-18/DeleteWorkspaceServiceAccount)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/grafana-2020-08-18/DeleteWorkspaceServiceAccount)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Grafana. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query grafana` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
