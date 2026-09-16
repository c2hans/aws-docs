---
source_url: https://docs.aws.amazon.com/snowball/latest/api-reference/API_devicemanagement_DescribeExecution.html
---

# DescribeExecution
<a name="API_devicemanagement_DescribeExecution"></a>

Checks the status of a remote task running on one or more target devices.

## Request Syntax
<a name="API_devicemanagement_DescribeExecution_RequestSyntax"></a>

```
POST /task/{{taskId}}/execution/{{managedDeviceId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_devicemanagement_DescribeExecution_RequestParameters"></a>

The request uses the following URI parameters.

 ** [managedDeviceId](#API_devicemanagement_DescribeExecution_RequestSyntax) **   <a name="Snowball-devicemanagement_DescribeExecution-request-uri-managedDeviceId"></a>
The ID of the managed device.
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** [taskId](#API_devicemanagement_DescribeExecution_RequestSyntax) **   <a name="Snowball-devicemanagement_DescribeExecution-request-uri-taskId"></a>
The ID of the task that the action is describing.
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

## Request Body
<a name="API_devicemanagement_DescribeExecution_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_devicemanagement_DescribeExecution_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "executionId": "string",
   "lastUpdatedAt": number,
   "managedDeviceId": "string",
   "startedAt": number,
   "state": "string",
   "taskId": "string"
}
```

## Response Elements
<a name="API_devicemanagement_DescribeExecution_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [executionId](#API_devicemanagement_DescribeExecution_ResponseSyntax) **   <a name="Snowball-devicemanagement_DescribeExecution-response-executionId"></a>
The ID of the execution.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [lastUpdatedAt](#API_devicemanagement_DescribeExecution_ResponseSyntax) **   <a name="Snowball-devicemanagement_DescribeExecution-response-lastUpdatedAt"></a>
When the status of the execution was last updated.
Type: Timestamp

 ** [managedDeviceId](#API_devicemanagement_DescribeExecution_ResponseSyntax) **   <a name="Snowball-devicemanagement_DescribeExecution-response-managedDeviceId"></a>
The ID of the managed device that the task is being executed on.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [startedAt](#API_devicemanagement_DescribeExecution_ResponseSyntax) **   <a name="Snowball-devicemanagement_DescribeExecution-response-startedAt"></a>
When the execution began.
Type: Timestamp

 ** [state](#API_devicemanagement_DescribeExecution_ResponseSyntax) **   <a name="Snowball-devicemanagement_DescribeExecution-response-state"></a>
The current state of the execution.
Type: String
Valid Values: `QUEUED | IN_PROGRESS | CANCELED | FAILED | SUCCEEDED | REJECTED | TIMED_OUT`

 ** [taskId](#API_devicemanagement_DescribeExecution_ResponseSyntax) **   <a name="Snowball-devicemanagement_DescribeExecution-response-taskId"></a>
The ID of the task being executed on the device.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.

## Errors
<a name="API_devicemanagement_DescribeExecution_Errors"></a>

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
<a name="API_devicemanagement_DescribeExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/snow-device-management-2021-08-04/DescribeExecution)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/snow-device-management-2021-08-04/DescribeExecution)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/snow-device-management-2021-08-04/DescribeExecution)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/snow-device-management-2021-08-04/DescribeExecution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/snow-device-management-2021-08-04/DescribeExecution)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/snow-device-management-2021-08-04/DescribeExecution)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/snow-device-management-2021-08-04/DescribeExecution)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/snow-device-management-2021-08-04/DescribeExecution)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/snow-device-management-2021-08-04/DescribeExecution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/snow-device-management-2021-08-04/DescribeExecution)
