---
source_url: https://docs.aws.amazon.com/grafana/latest/APIReference/API_CreateWorkspaceApiKey.html
---

# CreateWorkspaceApiKey
<a name="API_CreateWorkspaceApiKey"></a>

Creates a Grafana API key for the workspace. This key can be used to authenticate requests sent to the workspace's HTTP API. See [https://docs.aws.amazon.com/grafana/latest/userguide/Using-Grafana-APIs.html](https://docs.aws.amazon.com/grafana/latest/userguide/Using-Grafana-APIs.html) for available APIs and example requests.

**Note**
In workspaces compatible with Grafana version 9 or above, use workspace service accounts instead of API keys. API keys will be removed in a future release.

## Request Syntax
<a name="API_CreateWorkspaceApiKey_RequestSyntax"></a>

```
POST /workspaces/{{workspaceId}}/apikeys HTTP/1.1
Content-type: application/json

{
   "keyName": "{{string}}",
   "keyRole": "{{string}}",
   "secondsToLive": {{number}}
}
```

## URI Request Parameters
<a name="API_CreateWorkspaceApiKey_RequestParameters"></a>

The request uses the following URI parameters.

 ** [workspaceId](#API_CreateWorkspaceApiKey_RequestSyntax) **   <a name="ManagedGrafana-CreateWorkspaceApiKey-request-uri-workspaceId"></a>
The ID of the workspace to create an API key.
Pattern: `g-[0-9a-f]{10}`
Required: Yes

## Request Body
<a name="API_CreateWorkspaceApiKey_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [keyName](#API_CreateWorkspaceApiKey_RequestSyntax) **   <a name="ManagedGrafana-CreateWorkspaceApiKey-request-keyName"></a>
Specifies the name of the key. Keynames must be unique to the workspace.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [keyRole](#API_CreateWorkspaceApiKey_RequestSyntax) **   <a name="ManagedGrafana-CreateWorkspaceApiKey-request-keyRole"></a>
Specifies the permission level of the key.
 Valid values: `ADMIN`\|`EDITOR`\|`VIEWER`
Type: String
Required: Yes

 ** [secondsToLive](#API_CreateWorkspaceApiKey_RequestSyntax) **   <a name="ManagedGrafana-CreateWorkspaceApiKey-request-secondsToLive"></a>
Specifies the time in seconds until the key expires. Keys can be valid for up to 30 days.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 2592000.
Required: Yes

## Response Syntax
<a name="API_CreateWorkspaceApiKey_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "key": "string",
   "keyName": "string",
   "workspaceId": "string"
}
```

## Response Elements
<a name="API_CreateWorkspaceApiKey_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [key](#API_CreateWorkspaceApiKey_ResponseSyntax) **   <a name="ManagedGrafana-CreateWorkspaceApiKey-response-key"></a>
The key token. Use this value as a bearer token to authenticate HTTP requests to the workspace.
Type: String

 ** [keyName](#API_CreateWorkspaceApiKey_ResponseSyntax) **   <a name="ManagedGrafana-CreateWorkspaceApiKey-response-keyName"></a>
The name of the key that was created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.

 ** [workspaceId](#API_CreateWorkspaceApiKey_ResponseSyntax) **   <a name="ManagedGrafana-CreateWorkspaceApiKey-response-workspaceId"></a>
The ID of the workspace that the key is valid for.
Type: String
Pattern: `g-[0-9a-f]{10}`

## Errors
<a name="API_CreateWorkspaceApiKey_Errors"></a>

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
<a name="API_CreateWorkspaceApiKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/grafana-2020-08-18/CreateWorkspaceApiKey)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/grafana-2020-08-18/CreateWorkspaceApiKey)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/grafana-2020-08-18/CreateWorkspaceApiKey)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/grafana-2020-08-18/CreateWorkspaceApiKey)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/grafana-2020-08-18/CreateWorkspaceApiKey)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/grafana-2020-08-18/CreateWorkspaceApiKey)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/grafana-2020-08-18/CreateWorkspaceApiKey)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/grafana-2020-08-18/CreateWorkspaceApiKey)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/grafana-2020-08-18/CreateWorkspaceApiKey)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/grafana-2020-08-18/CreateWorkspaceApiKey)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Grafana. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query grafana` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
