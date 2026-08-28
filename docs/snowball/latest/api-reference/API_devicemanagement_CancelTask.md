---
source_url: https://docs.aws.amazon.com/snowball/latest/api-reference/API_devicemanagement_CancelTask.html
---

# CancelTask
<a name="API_devicemanagement_CancelTask"></a>

Sends a cancel request for a specified task. You can cancel a task only if it's still in a `QUEUED` state. Tasks that are already running can't be cancelled.

**Note**
A task might still run if it's processed from the queue before the `CancelTask` operation changes the task's state.

## Request Syntax
<a name="API_devicemanagement_CancelTask_RequestSyntax"></a>

```
POST /task/{{taskId}}/cancel HTTP/1.1
```

## URI Request Parameters
<a name="API_devicemanagement_CancelTask_RequestParameters"></a>

The request uses the following URI parameters.

 ** [taskId](#API_devicemanagement_CancelTask_RequestSyntax) **   <a name="Snowball-devicemanagement_CancelTask-request-uri-taskId"></a>
The ID of the task that you are attempting to cancel. You can retrieve a task ID by using the `ListTasks` operation.
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

## Request Body
<a name="API_devicemanagement_CancelTask_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_devicemanagement_CancelTask_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "taskId": "string"
}
```

## Response Elements
<a name="API_devicemanagement_CancelTask_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [taskId](#API_devicemanagement_CancelTask_ResponseSyntax) **   <a name="Snowball-devicemanagement_CancelTask-response-taskId"></a>
The ID of the task that you are attempting to cancel.
Type: String

## Errors
<a name="API_devicemanagement_CancelTask_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error occurred while processing the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request references a resource that doesn't exist.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_devicemanagement_CancelTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/snow-device-management-2021-08-04/CancelTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/snow-device-management-2021-08-04/CancelTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/snow-device-management-2021-08-04/CancelTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/snow-device-management-2021-08-04/CancelTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/snow-device-management-2021-08-04/CancelTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/snow-device-management-2021-08-04/CancelTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/snow-device-management-2021-08-04/CancelTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/snow-device-management-2021-08-04/CancelTask)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/snow-device-management-2021-08-04/CancelTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/snow-device-management-2021-08-04/CancelTask)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Snowball. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query snowball` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
