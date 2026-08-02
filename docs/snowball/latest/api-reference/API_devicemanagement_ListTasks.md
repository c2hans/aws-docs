---
source_url: https://docs.aws.amazon.com/snowball/latest/api-reference/API_devicemanagement_ListTasks.html
---

# ListTasks
<a name="API_devicemanagement_ListTasks"></a>

Returns a list of tasks that can be filtered by state.

## Request Syntax
<a name="API_devicemanagement_ListTasks_RequestSyntax"></a>

```
GET /tasks?maxResults={{maxResults}}&nextToken={{nextToken}}&state={{state}} HTTP/1.1
```

## URI Request Parameters
<a name="API_devicemanagement_ListTasks_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_devicemanagement_ListTasks_RequestSyntax) **   <a name="Snowball-devicemanagement_ListTasks-request-uri-maxResults"></a>
The maximum number of tasks per page.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_devicemanagement_ListTasks_RequestSyntax) **   <a name="Snowball-devicemanagement_ListTasks-request-uri-nextToken"></a>
A pagination token to continue to the next page of tasks.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[a-zA-Z0-9+/=]*`

 ** [state](#API_devicemanagement_ListTasks_RequestSyntax) **   <a name="Snowball-devicemanagement_ListTasks-request-uri-state"></a>
A structure used to filter the list of tasks.
Valid Values: `IN_PROGRESS | CANCELED | COMPLETED`

## Request Body
<a name="API_devicemanagement_ListTasks_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_devicemanagement_ListTasks_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "tasks": [
      {
         "state": "string",
         "tags": {
            "string" : "string"
         },
         "taskArn": "string",
         "taskId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_devicemanagement_ListTasks_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_devicemanagement_ListTasks_ResponseSyntax) **   <a name="Snowball-devicemanagement_ListTasks-response-nextToken"></a>
A pagination token to continue to the next page of tasks.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[a-zA-Z0-9+/=]*`

 ** [tasks](#API_devicemanagement_ListTasks_ResponseSyntax) **   <a name="Snowball-devicemanagement_ListTasks-response-tasks"></a>
A list of task structures containing details about each task.
Type: Array of [TaskSummary](API_devicemanagement_TaskSummary.md) objects

## Errors
<a name="API_devicemanagement_ListTasks_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error occurred while processing the request.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_devicemanagement_ListTasks_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/snow-device-management-2021-08-04/ListTasks)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/snow-device-management-2021-08-04/ListTasks)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/snow-device-management-2021-08-04/ListTasks)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/snow-device-management-2021-08-04/ListTasks)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/snow-device-management-2021-08-04/ListTasks)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/snow-device-management-2021-08-04/ListTasks)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/snow-device-management-2021-08-04/ListTasks)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/snow-device-management-2021-08-04/ListTasks)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/snow-device-management-2021-08-04/ListTasks)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/snow-device-management-2021-08-04/ListTasks)
