---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_UpdateBacklogTask.html
---

# UpdateBacklogTask
<a name="API_UpdateBacklogTask"></a>

Update an existing backlog task.

## Request Syntax
<a name="API_UpdateBacklogTask_RequestSyntax"></a>

```
PATCH /backlog/agent-space/{{agentSpaceId}}/tasks/{{taskId}} HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "taskStatus": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateBacklogTask_RequestParameters"></a>

The request uses the following URI parameters.

 ** [agentSpaceId](#API_UpdateBacklogTask_RequestSyntax) **   <a name="devopsagent-UpdateBacklogTask-request-uri-agentSpaceId"></a>
The unique identifier for the agent space containing the task
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** [taskId](#API_UpdateBacklogTask_RequestSyntax) **   <a name="devopsagent-UpdateBacklogTask-request-uri-taskId"></a>
The unique identifier of the task to update
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

## Request Body
<a name="API_UpdateBacklogTask_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_UpdateBacklogTask_RequestSyntax) **   <a name="devopsagent-UpdateBacklogTask-request-clientToken"></a>
Client-provided token for idempotent operations
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\x21-\x7E]+`
Required: No

 ** [taskStatus](#API_UpdateBacklogTask_RequestSyntax) **   <a name="devopsagent-UpdateBacklogTask-request-taskStatus"></a>
Updated task status
Type: String
Valid Values: `PENDING_TRIAGE | LINKED | PENDING_START | IN_PROGRESS | PENDING_CUSTOMER_APPROVAL | COMPLETED | FAILED | TIMED_OUT | CANCELED | SKIPPED | WAITING`
Required: No

## Response Syntax
<a name="API_UpdateBacklogTask_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "task": {
      "agentSpaceId": "string",
      "createdAt": "string",
      "description": "string",
      "executionId": "string",
      "hasLinkedTasks": boolean,
      "metadata": JSON value,
      "primaryTaskId": "string",
      "priority": "string",
      "reference": {
         "associationId": "string",
         "referenceId": "string",
         "referenceUrl": "string",
         "system": "string",
         "title": "string"
      },
      "status": "string",
      "statusReason": "string",
      "supportMetadata": JSON value,
      "taskId": "string",
      "taskType": "string",
      "title": "string",
      "updatedAt": "string",
      "version": number
   }
}
```

## Response Elements
<a name="API_UpdateBacklogTask_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [task](#API_UpdateBacklogTask_ResponseSyntax) **   <a name="devopsagent-UpdateBacklogTask-response-task"></a>
The updated task object
Type: [Task](API_Task.md) object

## Errors
<a name="API_UpdateBacklogTask_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to the requested resource is denied due to insufficient permissions.
 ** message **
Detailed error message describing why access was denied.
HTTP Status Code: 403

 ** ConflictException **
The request conflicts with the current state of the resource.
 ** message **
Detailed error message describing the conflict.
HTTP Status Code: 409

 ** ContentSizeExceededException **
This exception is thrown when the content size exceeds the allowed limit.
HTTP Status Code: 413

 ** InternalServerException **
This exception is thrown when an unexpected error occurs in the processing of a request.
HTTP Status Code: 500

 ** InvalidParameterException **
One or more parameters provided in the request are invalid.
 ** message **
Detailed error message describing which parameter is invalid and why.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The requested resource could not be found.
 ** message **
Detailed error message describing which resource was not found.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The request would exceed the service quota limit.
 ** message **
Detailed error message describing which quota was exceeded.
HTTP Status Code: 402

 ** ThrottlingException **
The request was throttled due to too many requests. Please slow down and try again.
 ** message **
Detailed error message describing the throttling condition.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by the service.
 ** fieldList **
A list of specific failures encountered while validating the input. A member can appear in this list more than once if it failed to satisfy multiple constraints.
 ** message **
A summary of the validation failure.
HTTP Status Code: 400

## See Also
<a name="API_UpdateBacklogTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/devops-agent-2026-01-01/UpdateBacklogTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/devops-agent-2026-01-01/UpdateBacklogTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/UpdateBacklogTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/devops-agent-2026-01-01/UpdateBacklogTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/UpdateBacklogTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/devops-agent-2026-01-01/UpdateBacklogTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/devops-agent-2026-01-01/UpdateBacklogTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/devops-agent-2026-01-01/UpdateBacklogTask)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/devops-agent-2026-01-01/UpdateBacklogTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/UpdateBacklogTask)
