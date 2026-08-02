---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_ListThingRegistrationTasks.html
---

# ListThingRegistrationTasks
<a name="API_ListThingRegistrationTasks"></a>

List bulk thing provisioning tasks.

Requires permission to access the [ListThingRegistrationTasks](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_ListThingRegistrationTasks_RequestSyntax"></a>

```
GET /thing-registration-tasks?maxResults={{maxResults}}&nextToken={{nextToken}}&status={{status}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListThingRegistrationTasks_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListThingRegistrationTasks_RequestSyntax) **   <a name="iot-ListThingRegistrationTasks-request-uri-maxResults"></a>
The maximum number of results to return at one time.
Valid Range: Minimum value of 1. Maximum value of 250.

 ** [nextToken](#API_ListThingRegistrationTasks_RequestSyntax) **   <a name="iot-ListThingRegistrationTasks-request-uri-nextToken"></a>
To retrieve the next set of results, the `nextToken` value from a previous response; otherwise **null** to receive the first set of results.

 ** [status](#API_ListThingRegistrationTasks_RequestSyntax) **   <a name="iot-ListThingRegistrationTasks-request-uri-status"></a>
The status of the bulk thing provisioning task.
Valid Values: `InProgress | Completed | Failed | Cancelled | Cancelling`

## Request Body
<a name="API_ListThingRegistrationTasks_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListThingRegistrationTasks_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "taskIds": [ "string" ]
}
```

## Response Elements
<a name="API_ListThingRegistrationTasks_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListThingRegistrationTasks_ResponseSyntax) **   <a name="iot-ListThingRegistrationTasks-response-nextToken"></a>
The token to use to get the next set of results, or **null** if there are no additional results.
Type: String

 ** [taskIds](#API_ListThingRegistrationTasks_ResponseSyntax) **   <a name="iot-ListThingRegistrationTasks-response-taskIds"></a>
A list of bulk thing provisioning task IDs.
Type: Array of strings
Length Constraints: Maximum length of 40.

## Errors
<a name="API_ListThingRegistrationTasks_Errors"></a>

 ** InternalFailureException **
An unexpected error has occurred.
 ** message **
The message for the exception.
HTTP Status Code: 500

 ** InvalidRequestException **
The request is not valid.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** ThrottlingException **
The rate exceeds the limit.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** UnauthorizedException **
You are not authorized to perform this operation.
 ** message **
The message for the exception.
HTTP Status Code: 401

## See Also
<a name="API_ListThingRegistrationTasks_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/ListThingRegistrationTasks)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/ListThingRegistrationTasks)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/ListThingRegistrationTasks)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/ListThingRegistrationTasks)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/ListThingRegistrationTasks)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/ListThingRegistrationTasks)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/ListThingRegistrationTasks)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/ListThingRegistrationTasks)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/ListThingRegistrationTasks)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/ListThingRegistrationTasks)
