---
source_url: https://docs.aws.amazon.com/snowball/latest/api-reference/API_devicemanagement_CreateTask.html
---

# CreateTask
<a name="API_devicemanagement_CreateTask"></a>

Instructs one or more devices to start a task, such as unlocking or rebooting.

## Request Syntax
<a name="API_devicemanagement_CreateTask_RequestSyntax"></a>

```
POST /task HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "command": { ... },
   "description": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "targets": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_devicemanagement_CreateTask_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_devicemanagement_CreateTask_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_devicemanagement_CreateTask_RequestSyntax) **   <a name="Snowball-devicemanagement_CreateTask-request-clientToken"></a>
A token ensuring that the action is called only once with the specified details.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[!-~]+`
Required: No

 ** [command](#API_devicemanagement_CreateTask_RequestSyntax) **   <a name="Snowball-devicemanagement_CreateTask-request-command"></a>
The task to be performed. Only one task is executed on a device at a time.
Type: [Command](API_devicemanagement_Command.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [description](#API_devicemanagement_CreateTask_RequestSyntax) **   <a name="Snowball-devicemanagement_CreateTask-request-description"></a>
A description of the task and its targets.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[A-Za-z0-9 _.,!#]*`
Required: No

 ** [tags](#API_devicemanagement_CreateTask_RequestSyntax) **   <a name="Snowball-devicemanagement_CreateTask-request-tags"></a>
Optional metadata that you assign to a resource. You can use tags to categorize a resource in different ways, such as by purpose, owner, or environment.
Type: String to string map
Required: No

 ** [targets](#API_devicemanagement_CreateTask_RequestSyntax) **   <a name="Snowball-devicemanagement_CreateTask-request-targets"></a>
A list of managed device IDs.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: Yes

## Response Syntax
<a name="API_devicemanagement_CreateTask_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "taskArn": "string",
   "taskId": "string"
}
```

## Response Elements
<a name="API_devicemanagement_CreateTask_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [taskArn](#API_devicemanagement_CreateTask_ResponseSyntax) **   <a name="Snowball-devicemanagement_CreateTask-response-taskArn"></a>
The Amazon Resource Name (ARN) of the task that you created.
Type: String

 ** [taskId](#API_devicemanagement_CreateTask_ResponseSyntax) **   <a name="Snowball-devicemanagement_CreateTask-response-taskId"></a>
The ID of the task that you created.
Type: String

## Errors
<a name="API_devicemanagement_CreateTask_Errors"></a>

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

 ** ServiceQuotaExceededException **
The request would cause a service quota to be exceeded.
HTTP Status Code: 402

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_devicemanagement_CreateTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/snow-device-management-2021-08-04/CreateTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/snow-device-management-2021-08-04/CreateTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/snow-device-management-2021-08-04/CreateTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/snow-device-management-2021-08-04/CreateTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/snow-device-management-2021-08-04/CreateTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/snow-device-management-2021-08-04/CreateTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/snow-device-management-2021-08-04/CreateTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/snow-device-management-2021-08-04/CreateTask)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/snow-device-management-2021-08-04/CreateTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/snow-device-management-2021-08-04/CreateTask)
