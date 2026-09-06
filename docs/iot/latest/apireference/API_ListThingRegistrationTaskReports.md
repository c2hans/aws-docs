---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_ListThingRegistrationTaskReports.html
---

# ListThingRegistrationTaskReports
<a name="API_ListThingRegistrationTaskReports"></a>

Information about the thing registration tasks.

## Request Syntax
<a name="API_ListThingRegistrationTaskReports_RequestSyntax"></a>

```
GET /thing-registration-tasks/{{taskId}}/reports?maxResults={{maxResults}}&nextToken={{nextToken}}&reportType={{reportType}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListThingRegistrationTaskReports_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListThingRegistrationTaskReports_RequestSyntax) **   <a name="iot-ListThingRegistrationTaskReports-request-uri-maxResults"></a>
The maximum number of results to return per request.
Valid Range: Minimum value of 1. Maximum value of 250.

 ** [nextToken](#API_ListThingRegistrationTaskReports_RequestSyntax) **   <a name="iot-ListThingRegistrationTaskReports-request-uri-nextToken"></a>
To retrieve the next set of results, the `nextToken` value from a previous response; otherwise **null** to receive the first set of results.

 ** [reportType](#API_ListThingRegistrationTaskReports_RequestSyntax) **   <a name="iot-ListThingRegistrationTaskReports-request-uri-reportType"></a>
The type of task report.
Valid Values: `ERRORS | RESULTS`
Required: Yes

 ** [taskId](#API_ListThingRegistrationTaskReports_RequestSyntax) **   <a name="iot-ListThingRegistrationTaskReports-request-uri-taskId"></a>
The id of the task.
Length Constraints: Maximum length of 40.
Required: Yes

## Request Body
<a name="API_ListThingRegistrationTaskReports_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListThingRegistrationTaskReports_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "reportType": "string",
   "resourceLinks": [ "string" ]
}
```

## Response Elements
<a name="API_ListThingRegistrationTaskReports_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListThingRegistrationTaskReports_ResponseSyntax) **   <a name="iot-ListThingRegistrationTaskReports-response-nextToken"></a>
The token to use to get the next set of results, or **null** if there are no additional results.
Type: String

 ** [reportType](#API_ListThingRegistrationTaskReports_ResponseSyntax) **   <a name="iot-ListThingRegistrationTaskReports-response-reportType"></a>
The type of task report.
Type: String
Valid Values: `ERRORS | RESULTS`

 ** [resourceLinks](#API_ListThingRegistrationTaskReports_ResponseSyntax) **   <a name="iot-ListThingRegistrationTaskReports-response-resourceLinks"></a>
Links to the task resources.
Type: Array of strings
Length Constraints: Maximum length of 65535.

## Errors
<a name="API_ListThingRegistrationTaskReports_Errors"></a>

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
<a name="API_ListThingRegistrationTaskReports_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/ListThingRegistrationTaskReports)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/ListThingRegistrationTaskReports)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/ListThingRegistrationTaskReports)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/ListThingRegistrationTaskReports)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/ListThingRegistrationTaskReports)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/ListThingRegistrationTaskReports)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/ListThingRegistrationTaskReports)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/ListThingRegistrationTaskReports)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/ListThingRegistrationTaskReports)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/ListThingRegistrationTaskReports)
