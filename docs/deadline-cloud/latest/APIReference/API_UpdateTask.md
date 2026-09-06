---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_UpdateTask.html
---

# UpdateTask
<a name="API_UpdateTask"></a>

Updates a task.

## Request Syntax
<a name="API_UpdateTask_RequestSyntax"></a>

```
PATCH /2023-10-12/farms/{{farmId}}/queues/{{queueId}}/jobs/{{jobId}}/steps/{{stepId}}/tasks/{{taskId}} HTTP/1.1
X-Amz-Client-Token: {{clientToken}}
Content-type: application/json

{
   "targetRunStatus": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateTask_RequestParameters"></a>

The request uses the following URI parameters.

 ** [clientToken](#API_UpdateTask_RequestSyntax) **   <a name="deadlinecloud-UpdateTask-request-clientToken"></a>
The unique token which the server uses to recognize retries of the same request.
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [farmId](#API_UpdateTask_RequestSyntax) **   <a name="deadlinecloud-UpdateTask-request-uri-farmId"></a>
The farm ID to update.
Pattern: `farm-[0-9a-f]{32}`
Required: Yes

 ** [jobId](#API_UpdateTask_RequestSyntax) **   <a name="deadlinecloud-UpdateTask-request-uri-jobId"></a>
The job ID to update.
Pattern: `job-[0-9a-f]{32}`
Required: Yes

 ** [queueId](#API_UpdateTask_RequestSyntax) **   <a name="deadlinecloud-UpdateTask-request-uri-queueId"></a>
The queue ID to update.
Pattern: `queue-[0-9a-f]{32}`
Required: Yes

 ** [stepId](#API_UpdateTask_RequestSyntax) **   <a name="deadlinecloud-UpdateTask-request-uri-stepId"></a>
The step ID to update.
Pattern: `step-[0-9a-f]{32}`
Required: Yes

 ** [taskId](#API_UpdateTask_RequestSyntax) **   <a name="deadlinecloud-UpdateTask-request-uri-taskId"></a>
The task ID to update.
Pattern: `task-[0-9a-f]{32}-(0|([1-9][0-9]{0,9}))`
Required: Yes

## Request Body
<a name="API_UpdateTask_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [targetRunStatus](#API_UpdateTask_RequestSyntax) **   <a name="deadlinecloud-UpdateTask-request-targetRunStatus"></a>
The run status with which to start the task.
Type: String
Valid Values: `READY | FAILED | SUCCEEDED | CANCELED | SUSPENDED | PENDING`
Required: Yes

## Response Syntax
<a name="API_UpdateTask_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateTask_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateTask_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permission to perform the action.
 ** context **
Information about the resources in use when the exception was thrown.
HTTP Status Code: 403

 ** ConflictException **
Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.
 ** context **
Information about the resources in use when the exception was thrown.
 ** reason **
A description of the error.
 ** resourceId **
The identifier of the resource in use.
 ** resourceType **
The type of the resource in use.
HTTP Status Code: 409

 ** InternalServerErrorException **
Deadline Cloud can't process your request right now. Try again later.
 ** retryAfterSeconds **
The number of seconds a client should wait before retrying the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested resource can't be found.
 ** context **
Information about the resources in use when the exception was thrown.
 ** resourceId **
The identifier of the resource that couldn't be found.
 ** resourceType **
The type of the resource that couldn't be found.
HTTP Status Code: 404

 ** ThrottlingException **
Your request exceeded a request rate quota.
 ** context **
Information about the resources in use when the exception was thrown.
 ** quotaCode **
Identifies the quota that is being throttled.
 ** retryAfterSeconds **
The number of seconds a client should wait before retrying the request.
 ** serviceCode **
Identifies the service that is being throttled.
HTTP Status Code: 429

 ** ValidationException **
The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.
 ** context **
Information about the resources in use when the exception was thrown.
 ** fieldList **
A list of fields that failed validation.
 ** reason **
The reason that the request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_UpdateTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/UpdateTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/deadline-2023-10-12/UpdateTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/UpdateTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/UpdateTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/UpdateTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/UpdateTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/UpdateTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/UpdateTask)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/UpdateTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/UpdateTask)
