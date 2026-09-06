---
source_url: https://docs.aws.amazon.com/snowball/latest/api-reference/API_devicemanagement_DescribeTask.html
---

# DescribeTask
<a name="API_devicemanagement_DescribeTask"></a>

Checks the metadata for a given task on a device.

## Request Syntax
<a name="API_devicemanagement_DescribeTask_RequestSyntax"></a>

```
POST /task/{{taskId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_devicemanagement_DescribeTask_RequestParameters"></a>

The request uses the following URI parameters.

 ** [taskId](#API_devicemanagement_DescribeTask_RequestSyntax) **   <a name="Snowball-devicemanagement_DescribeTask-request-uri-taskId"></a>
The ID of the task to be described.
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

## Request Body
<a name="API_devicemanagement_DescribeTask_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_devicemanagement_DescribeTask_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "completedAt": number,
   "createdAt": number,
   "description": "string",
   "lastUpdatedAt": number,
   "state": "string",
   "tags": {
      "string" : "string"
   },
   "targets": [ "string" ],
   "taskArn": "string",
   "taskId": "string"
}
```

## Response Elements
<a name="API_devicemanagement_DescribeTask_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [completedAt](#API_devicemanagement_DescribeTask_ResponseSyntax) **   <a name="Snowball-devicemanagement_DescribeTask-response-completedAt"></a>
When the task was completed.
Type: Timestamp

 ** [createdAt](#API_devicemanagement_DescribeTask_ResponseSyntax) **   <a name="Snowball-devicemanagement_DescribeTask-response-createdAt"></a>
When the `CreateTask` operation was called.
Type: Timestamp

 ** [description](#API_devicemanagement_DescribeTask_ResponseSyntax) **   <a name="Snowball-devicemanagement_DescribeTask-response-description"></a>
The description provided of the task and managed devices.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[A-Za-z0-9 _.,!#]*`

 ** [lastUpdatedAt](#API_devicemanagement_DescribeTask_ResponseSyntax) **   <a name="Snowball-devicemanagement_DescribeTask-response-lastUpdatedAt"></a>
When the state of the task was last updated.
Type: Timestamp

 ** [state](#API_devicemanagement_DescribeTask_ResponseSyntax) **   <a name="Snowball-devicemanagement_DescribeTask-response-state"></a>
The current state of the task.
Type: String
Valid Values: `IN_PROGRESS | CANCELED | COMPLETED`

 ** [tags](#API_devicemanagement_DescribeTask_ResponseSyntax) **   <a name="Snowball-devicemanagement_DescribeTask-response-tags"></a>
Optional metadata that you assign to a resource. You can use tags to categorize a resource in different ways, such as by purpose, owner, or environment.
Type: String to string map

 ** [targets](#API_devicemanagement_DescribeTask_ResponseSyntax) **   <a name="Snowball-devicemanagement_DescribeTask-response-targets"></a>
The managed devices that the task was sent to.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.

 ** [taskArn](#API_devicemanagement_DescribeTask_ResponseSyntax) **   <a name="Snowball-devicemanagement_DescribeTask-response-taskArn"></a>
The Amazon Resource Name (ARN) of the task.
Type: String

 ** [taskId](#API_devicemanagement_DescribeTask_ResponseSyntax) **   <a name="Snowball-devicemanagement_DescribeTask-response-taskId"></a>
The ID of the task.
Type: String

## Errors
<a name="API_devicemanagement_DescribeTask_Errors"></a>

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
<a name="API_devicemanagement_DescribeTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/snow-device-management-2021-08-04/DescribeTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/snow-device-management-2021-08-04/DescribeTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/snow-device-management-2021-08-04/DescribeTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/snow-device-management-2021-08-04/DescribeTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/snow-device-management-2021-08-04/DescribeTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/snow-device-management-2021-08-04/DescribeTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/snow-device-management-2021-08-04/DescribeTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/snow-device-management-2021-08-04/DescribeTask)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/snow-device-management-2021-08-04/DescribeTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/snow-device-management-2021-08-04/DescribeTask)
