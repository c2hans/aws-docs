---
source_url: https://docs.aws.amazon.com/grafana/latest/APIReference/API_CreateWorkspaceServiceAccountToken.html
---

# CreateWorkspaceServiceAccountToken
<a name="API_CreateWorkspaceServiceAccountToken"></a>

Creates a token that can be used to authenticate and authorize Grafana HTTP API operations for the given [workspace service account](https://docs.aws.amazon.com/grafana/latest/userguide/service-accounts.html). The service account acts as a user for the API operations, and defines the permissions that are used by the API.

**Important**
When you create the service account token, you will receive a key that is used when calling Grafana APIs. Do not lose this key, as it will not be retrievable again.
If you do lose the key, you can delete the token and recreate it to receive a new key. This will disable the initial key.

Service accounts are only available for workspaces that are compatible with Grafana version 9 and above.

## Request Syntax
<a name="API_CreateWorkspaceServiceAccountToken_RequestSyntax"></a>

```
POST /workspaces/{{workspaceId}}/serviceaccounts/{{serviceAccountId}}/tokens HTTP/1.1
Content-type: application/json

{
   "name": "{{string}}",
   "secondsToLive": {{number}}
}
```

## URI Request Parameters
<a name="API_CreateWorkspaceServiceAccountToken_RequestParameters"></a>

The request uses the following URI parameters.

 ** [serviceAccountId](#API_CreateWorkspaceServiceAccountToken_RequestSyntax) **   <a name="ManagedGrafana-CreateWorkspaceServiceAccountToken-request-uri-serviceAccountId"></a>
The ID of the service account for which to create a token.
Required: Yes

 ** [workspaceId](#API_CreateWorkspaceServiceAccountToken_RequestSyntax) **   <a name="ManagedGrafana-CreateWorkspaceServiceAccountToken-request-uri-workspaceId"></a>
The ID of the workspace the service account resides within.
Pattern: `g-[0-9a-f]{10}`
Required: Yes

## Request Body
<a name="API_CreateWorkspaceServiceAccountToken_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [name](#API_CreateWorkspaceServiceAccountToken_RequestSyntax) **   <a name="ManagedGrafana-CreateWorkspaceServiceAccountToken-request-name"></a>
A name for the token to create.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** [secondsToLive](#API_CreateWorkspaceServiceAccountToken_RequestSyntax) **   <a name="ManagedGrafana-CreateWorkspaceServiceAccountToken-request-secondsToLive"></a>
Sets how long the token will be valid, in seconds. You can set the time up to 30 days in the future.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 2592000.
Required: Yes

## Response Syntax
<a name="API_CreateWorkspaceServiceAccountToken_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "serviceAccountId": "string",
   "serviceAccountToken": {
      "id": "string",
      "key": "string",
      "name": "string"
   },
   "workspaceId": "string"
}
```

## Response Elements
<a name="API_CreateWorkspaceServiceAccountToken_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [serviceAccountId](#API_CreateWorkspaceServiceAccountToken_ResponseSyntax) **   <a name="ManagedGrafana-CreateWorkspaceServiceAccountToken-response-serviceAccountId"></a>
The ID of the service account where the token was created.
Type: String

 ** [serviceAccountToken](#API_CreateWorkspaceServiceAccountToken_ResponseSyntax) **   <a name="ManagedGrafana-CreateWorkspaceServiceAccountToken-response-serviceAccountToken"></a>
Information about the created token, including the key. Be sure to store the key securely.
Type: [ServiceAccountTokenSummaryWithKey](API_ServiceAccountTokenSummaryWithKey.md) object

 ** [workspaceId](#API_CreateWorkspaceServiceAccountToken_ResponseSyntax) **   <a name="ManagedGrafana-CreateWorkspaceServiceAccountToken-response-workspaceId"></a>
The ID of the workspace where the token was created.
Type: String
Pattern: `g-[0-9a-f]{10}`

## Errors
<a name="API_CreateWorkspaceServiceAccountToken_Errors"></a>

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
<a name="API_CreateWorkspaceServiceAccountToken_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/grafana-2020-08-18/CreateWorkspaceServiceAccountToken)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/grafana-2020-08-18/CreateWorkspaceServiceAccountToken)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/grafana-2020-08-18/CreateWorkspaceServiceAccountToken)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/grafana-2020-08-18/CreateWorkspaceServiceAccountToken)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/grafana-2020-08-18/CreateWorkspaceServiceAccountToken)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/grafana-2020-08-18/CreateWorkspaceServiceAccountToken)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/grafana-2020-08-18/CreateWorkspaceServiceAccountToken)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/grafana-2020-08-18/CreateWorkspaceServiceAccountToken)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/grafana-2020-08-18/CreateWorkspaceServiceAccountToken)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/grafana-2020-08-18/CreateWorkspaceServiceAccountToken)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Grafana. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query grafana` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
