---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_BatchUpdateTask.html
---

# BatchUpdateTask
<a name="API_BatchUpdateTask"></a>

Updates multiple tasks in a single request. This is a batch version of the `UpdateTask` API.

The result of updating each task is reported individually in the response. Because the batch request can result in a combination of successful and unsuccessful actions, you should check for batch errors even when the call returns an HTTP status code of 200.

## Request Syntax
<a name="API_BatchUpdateTask_RequestSyntax"></a>

```
PATCH /2023-10-12/batch-update-task HTTP/1.1
X-Amz-Client-Token: {{clientToken}}
Content-type: application/json

{
   "tasks": [
      {
         "farmId": "{{string}}",
         "jobId": "{{string}}",
         "queueId": "{{string}}",
         "stepId": "{{string}}",
         "targetRunStatus": "{{string}}",
         "taskId": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_BatchUpdateTask_RequestParameters"></a>

The request uses the following URI parameters.

 ** [clientToken](#API_BatchUpdateTask_RequestSyntax) **   <a name="deadlinecloud-BatchUpdateTask-request-clientToken"></a>
The unique token which the server uses to recognize retries of the same request.
Length Constraints: Minimum length of 1. Maximum length of 64.

## Request Body
<a name="API_BatchUpdateTask_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [tasks](#API_BatchUpdateTask_RequestSyntax) **   <a name="deadlinecloud-BatchUpdateTask-request-tasks"></a>
The list of tasks to update. You can specify up to 100 tasks per request.
Type: Array of [BatchUpdateTaskItem](API_BatchUpdateTaskItem.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: Yes

## Response Syntax
<a name="API_BatchUpdateTask_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "errors": [
      {
         "code": "string",
         "farmId": "string",
         "jobId": "string",
         "message": "string",
         "queueId": "string",
         "stepId": "string",
         "taskId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_BatchUpdateTask_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [errors](#API_BatchUpdateTask_ResponseSyntax) **   <a name="deadlinecloud-BatchUpdateTask-response-errors"></a>
A list of errors for tasks that could not be updated.
Type: Array of [BatchUpdateTaskError](API_BatchUpdateTaskError.md) objects

## Errors
<a name="API_BatchUpdateTask_Errors"></a>

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
<a name="API_BatchUpdateTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/BatchUpdateTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/deadline-2023-10-12/BatchUpdateTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/BatchUpdateTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/BatchUpdateTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/BatchUpdateTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/BatchUpdateTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/BatchUpdateTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/BatchUpdateTask)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/BatchUpdateTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/BatchUpdateTask)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
