---
source_url: https://docs.aws.amazon.com/snowball/latest/api-reference/API_devicemanagement_ListExecutions.html
---

# ListExecutions
<a name="API_devicemanagement_ListExecutions"></a>

Returns the status of tasks for one or more target devices.

## Request Syntax
<a name="API_devicemanagement_ListExecutions_RequestSyntax"></a>

```
GET /executions?maxResults={{maxResults}}&nextToken={{nextToken}}&state={{state}}&taskId={{taskId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_devicemanagement_ListExecutions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_devicemanagement_ListExecutions_RequestSyntax) **   <a name="Snowball-devicemanagement_ListExecutions-request-uri-maxResults"></a>
The maximum number of tasks to list per page.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_devicemanagement_ListExecutions_RequestSyntax) **   <a name="Snowball-devicemanagement_ListExecutions-request-uri-nextToken"></a>
A pagination token to continue to the next page of tasks.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[a-zA-Z0-9+/=]*`

 ** [state](#API_devicemanagement_ListExecutions_RequestSyntax) **   <a name="Snowball-devicemanagement_ListExecutions-request-uri-state"></a>
A structure used to filter the tasks by their current state.
Valid Values: `QUEUED | IN_PROGRESS | CANCELED | FAILED | SUCCEEDED | REJECTED | TIMED_OUT`

 ** [taskId](#API_devicemanagement_ListExecutions_RequestSyntax) **   <a name="Snowball-devicemanagement_ListExecutions-request-uri-taskId"></a>
The ID of the task.
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

## Request Body
<a name="API_devicemanagement_ListExecutions_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_devicemanagement_ListExecutions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "executions": [
      {
         "executionId": "string",
         "managedDeviceId": "string",
         "state": "string",
         "taskId": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_devicemanagement_ListExecutions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [executions](#API_devicemanagement_ListExecutions_ResponseSyntax) **   <a name="Snowball-devicemanagement_ListExecutions-response-executions"></a>
A list of executions. Each execution contains the task ID, the device that the task is executing on, the execution ID, and the status of the execution.
Type: Array of [ExecutionSummary](API_devicemanagement_ExecutionSummary.md) objects

 ** [nextToken](#API_devicemanagement_ListExecutions_ResponseSyntax) **   <a name="Snowball-devicemanagement_ListExecutions-response-nextToken"></a>
A pagination token to continue to the next page of executions.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[a-zA-Z0-9+/=]*`

## Errors
<a name="API_devicemanagement_ListExecutions_Errors"></a>

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
<a name="API_devicemanagement_ListExecutions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/snow-device-management-2021-08-04/ListExecutions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/snow-device-management-2021-08-04/ListExecutions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/snow-device-management-2021-08-04/ListExecutions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/snow-device-management-2021-08-04/ListExecutions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/snow-device-management-2021-08-04/ListExecutions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/snow-device-management-2021-08-04/ListExecutions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/snow-device-management-2021-08-04/ListExecutions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/snow-device-management-2021-08-04/ListExecutions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/snow-device-management-2021-08-04/ListExecutions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/snow-device-management-2021-08-04/ListExecutions)
