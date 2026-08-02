---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_GetTask.html
---

# GetTask
<a name="API_GetTask"></a>

Gets a task.

## Request Syntax
<a name="API_GetTask_RequestSyntax"></a>

```
GET /2023-10-12/farms/{{farmId}}/queues/{{queueId}}/jobs/{{jobId}}/steps/{{stepId}}/tasks/{{taskId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetTask_RequestParameters"></a>

The request uses the following URI parameters.

 ** [farmId](#API_GetTask_RequestSyntax) **   <a name="deadlinecloud-GetTask-request-uri-farmId"></a>
The farm ID of the farm connected to the task.
Pattern: `farm-[0-9a-f]{32}`
Required: Yes

 ** [jobId](#API_GetTask_RequestSyntax) **   <a name="deadlinecloud-GetTask-request-uri-jobId"></a>
The job ID of the job connected to the task.
Pattern: `job-[0-9a-f]{32}`
Required: Yes

 ** [queueId](#API_GetTask_RequestSyntax) **   <a name="deadlinecloud-GetTask-request-uri-queueId"></a>
The queue ID for the queue connected to the task.
Pattern: `queue-[0-9a-f]{32}`
Required: Yes

 ** [stepId](#API_GetTask_RequestSyntax) **   <a name="deadlinecloud-GetTask-request-uri-stepId"></a>
The step ID for the step connected to the task.
Pattern: `step-[0-9a-f]{32}`
Required: Yes

 ** [taskId](#API_GetTask_RequestSyntax) **   <a name="deadlinecloud-GetTask-request-uri-taskId"></a>
The task ID.
Pattern: `task-[0-9a-f]{32}-(0|([1-9][0-9]{0,9}))`
Required: Yes

## Request Body
<a name="API_GetTask_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetTask_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "createdAt": "string",
   "createdBy": "string",
   "endedAt": "string",
   "failureRetryCount": number,
   "latestSessionActionId": "string",
   "parameters": {
      "string" : { ... }
   },
   "runStatus": "string",
   "startedAt": "string",
   "targetRunStatus": "string",
   "taskId": "string",
   "updatedAt": "string",
   "updatedBy": "string"
}
```

## Response Elements
<a name="API_GetTask_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_GetTask_ResponseSyntax) **   <a name="deadlinecloud-GetTask-response-createdAt"></a>
The date and time the resource was created.
Type: Timestamp

 ** [createdBy](#API_GetTask_ResponseSyntax) **   <a name="deadlinecloud-GetTask-response-createdBy"></a>
The user or system that created this resource.
Type: String

 ** [endedAt](#API_GetTask_ResponseSyntax) **   <a name="deadlinecloud-GetTask-response-endedAt"></a>
The date and time the resource ended running.
Type: Timestamp

 ** [failureRetryCount](#API_GetTask_ResponseSyntax) **   <a name="deadlinecloud-GetTask-response-failureRetryCount"></a>
The number of times that the task failed and was retried.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 2147483647.

 ** [latestSessionActionId](#API_GetTask_ResponseSyntax) **   <a name="deadlinecloud-GetTask-response-latestSessionActionId"></a>
The latest session action ID for the task.
Type: String
Pattern: `sessionaction-[0-9a-f]{32}-(0|([1-9][0-9]{0,9}))`

 ** [parameters](#API_GetTask_ResponseSyntax) **   <a name="deadlinecloud-GetTask-response-parameters"></a>
The parameters for the task.
Type: String to [TaskParameterValue](API_TaskParameterValue.md) object map

 ** [runStatus](#API_GetTask_ResponseSyntax) **   <a name="deadlinecloud-GetTask-response-runStatus"></a>
The run status for the task.
Type: String
Valid Values: `PENDING | READY | ASSIGNED | STARTING | SCHEDULED | INTERRUPTING | RUNNING | SUSPENDED | CANCELED | FAILED | SUCCEEDED | NOT_COMPATIBLE`

 ** [startedAt](#API_GetTask_ResponseSyntax) **   <a name="deadlinecloud-GetTask-response-startedAt"></a>
The date and time the resource started running.
Type: Timestamp

 ** [targetRunStatus](#API_GetTask_ResponseSyntax) **   <a name="deadlinecloud-GetTask-response-targetRunStatus"></a>
The run status with which to start the task.
Type: String
Valid Values: `READY | FAILED | SUCCEEDED | CANCELED | SUSPENDED | PENDING`

 ** [taskId](#API_GetTask_ResponseSyntax) **   <a name="deadlinecloud-GetTask-response-taskId"></a>
The task ID.
Type: String
Pattern: `task-[0-9a-f]{32}-(0|([1-9][0-9]{0,9}))`

 ** [updatedAt](#API_GetTask_ResponseSyntax) **   <a name="deadlinecloud-GetTask-response-updatedAt"></a>
The date and time the resource was updated.
Type: Timestamp

 ** [updatedBy](#API_GetTask_ResponseSyntax) **   <a name="deadlinecloud-GetTask-response-updatedBy"></a>
The user or system that updated this resource.
Type: String

## Errors
<a name="API_GetTask_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permission to perform the action.
 ** context **
Information about the resources in use when the exception was thrown.
HTTP Status Code: 403

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
<a name="API_GetTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/GetTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/deadline-2023-10-12/GetTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/GetTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/GetTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/GetTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/GetTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/GetTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/GetTask)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/GetTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/GetTask)
