---
source_url: https://docs.aws.amazon.com/nova-act/latest/APIReference/API_CreateAct.html
---

# CreateAct
<a name="API_CreateAct"></a>

Creates a new AI task (act) within a session that can interact with tools and perform specific actions.

## Request Syntax
<a name="API_CreateAct_RequestSyntax"></a>

```
PUT /workflow-definitions/{{workflowDefinitionName}}/workflow-runs/{{workflowRunId}}/sessions/{{sessionId}}/acts HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "task": "{{string}}",
   "toolSpecs": [
      {
         "description": "{{string}}",
         "inputSchema": { ... },
         "name": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_CreateAct_RequestParameters"></a>

The request uses the following URI parameters.

 ** [sessionId](#API_CreateAct_RequestSyntax) **   <a name="novaact-CreateAct-request-uri-sessionId"></a>
The unique identifier of the session to create the act in.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** [workflowDefinitionName](#API_CreateAct_RequestSyntax) **   <a name="novaact-CreateAct-request-uri-workflowDefinitionName"></a>
The name of the workflow definition containing the session.
Length Constraints: Minimum length of 1. Maximum length of 40.
Pattern: `[a-zA-Z0-9_-]{1,40}`
Required: Yes

 ** [workflowRunId](#API_CreateAct_RequestSyntax) **   <a name="novaact-CreateAct-request-uri-workflowRunId"></a>
The unique identifier of the workflow run containing the session.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

## Request Body
<a name="API_CreateAct_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateAct_RequestSyntax) **   <a name="novaact-CreateAct-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
Type: String
Length Constraints: Minimum length of 33. Maximum length of 256.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`
Required: No

 ** [task](#API_CreateAct_RequestSyntax) **   <a name="novaact-CreateAct-request-task"></a>
The task description that defines what the act should accomplish.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10000.
Required: Yes

 ** [toolSpecs](#API_CreateAct_RequestSyntax) **   <a name="novaact-CreateAct-request-toolSpecs"></a>
A list of tool specifications that the act can invoke to complete its task.
Type: Array of [ToolSpec](API_ToolSpec.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: No

## Response Syntax
<a name="API_CreateAct_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "actId": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_CreateAct_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [actId](#API_CreateAct_ResponseSyntax) **   <a name="novaact-CreateAct-response-actId"></a>
The unique identifier for the created act.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`

 ** [status](#API_CreateAct_ResponseSyntax) **   <a name="novaact-CreateAct-response-status"></a>
The initial status of the act after creation.
Type: String
Valid Values: `RUNNING | PENDING_CLIENT_ACTION | PENDING_HUMAN_ACTION | SUCCEEDED | FAILED | TIMED_OUT`

## Errors
<a name="API_CreateAct_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 [AccessDeniedException](API_AccessDeniedException.md)
You don't have sufficient permissions to perform this action.
 ** message **
You don't have sufficient permissions to perform this action. Verify your IAM permissions and try again.
HTTP Status Code: 403

 [ConflictException](API_ConflictException.md)
The request could not be completed due to a conflict with the current state of the resource.
 ** message **
The requested operation conflicts with the current state of the resource.
 ** resourceId **
The identifier of the resource that caused the conflict.
 ** resourceType **
The type of resource that caused the conflict.
HTTP Status Code: 409

 [InternalServerException](API_InternalServerException.md)
An internal server error occurred. Please try again later.
 ** message **
The service encountered an internal error. Try again later.
 ** reason **
The reason for the internal server error.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
HTTP Status Code: 500

 [ResourceNotFoundException](API_ResourceNotFoundException.md)
The requested resource was not found.
 ** message **
The specified resource was not found.
 ** resourceId **
The identifier of the resource that wasn't found.
 ** resourceType **
The type of resource that wasn't found.
HTTP Status Code: 404

 [ServiceQuotaExceededException](API_ServiceQuotaExceededException.md)
The request would exceed a service quota limit.
 ** message **
The request would exceed one or more service quotas for your account.
 ** quotaCode **
The code for the specific quota that was exceeded.
 ** resourceId **
The identifier of the resource that exceeded the quota.
 ** resourceType **
The type of resource that exceeded the quota.
 ** serviceCode **
The service code for the quota that was exceeded.
HTTP Status Code: 402

 [ThrottlingException](API_ThrottlingException.md)
The request was throttled due to too many requests. Please try again later.
 ** message **
The request was denied due to request throttling.
 ** quotaCode **
The quota code related to the throttling.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the throttled request.
 ** serviceCode **
The service code where throttling occurred.
HTTP Status Code: 429

 [ValidationException](API_ValidationException.md)
The input parameters for the request are invalid.
 ** fieldList **
The list of fields that failed validation.
 ** message **
The input fails to satisfy the constraints specified by the service.
 ** reason **
The reason for the validation failure.
HTTP Status Code: 400

## See Also
<a name="API_CreateAct_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/nova-act-2025-08-22/CreateAct)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/nova-act-2025-08-22/CreateAct)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/nova-act-2025-08-22/CreateAct)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/nova-act-2025-08-22/CreateAct)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/nova-act-2025-08-22/CreateAct)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/nova-act-2025-08-22/CreateAct)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/nova-act-2025-08-22/CreateAct)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/nova-act-2025-08-22/CreateAct)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/nova-act-2025-08-22/CreateAct)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/nova-act-2025-08-22/CreateAct)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Nova Act. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query nova-act` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
