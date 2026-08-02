---
source_url: https://docs.aws.amazon.com/neptune/latest/data-api/API_GetLoaderJobStatus.html
---

# GetLoaderJobStatus
<a name="API_GetLoaderJobStatus"></a>

Gets status information about a specified load job. Neptune keeps track of the most recent 1,024 bulk load jobs, and stores the last 10,000 error details per job.

See [Neptune Loader Get-Status API](https://docs.aws.amazon.com/neptune/latest/userguide/load-api-reference-status.htm) for more information.

When invoking this operation in a Neptune cluster that has IAM authentication enabled, the IAM user or role making the request must have a policy attached that allows the [neptune-db:GetLoaderJobStatus](https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#getloaderjobstatus) IAM action in that cluster..

## Request Syntax
<a name="API_GetLoaderJobStatus_RequestSyntax"></a>

```
GET /loader/{{loadId}}?details={{details}}&errors={{errors}}&errorsPerPage={{errorsPerPage}}&page={{page}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetLoaderJobStatus_RequestParameters"></a>

The request uses the following URI parameters.

 ** [details](#API_GetLoaderJobStatus_RequestSyntax) **   <a name="neptunedata-GetLoaderJobStatus-request-uri-details"></a>
Flag indicating whether or not to include details beyond the overall status (`TRUE` or `FALSE`; the default is `FALSE`).

 ** [errors](#API_GetLoaderJobStatus_RequestSyntax) **   <a name="neptunedata-GetLoaderJobStatus-request-uri-errors"></a>
Flag indicating whether or not to include a list of errors encountered (`TRUE` or `FALSE`; the default is `FALSE`).
The list of errors is paged. The `page` and `errorsPerPage` parameters allow you to page through all the errors.

 ** [errorsPerPage](#API_GetLoaderJobStatus_RequestSyntax) **   <a name="neptunedata-GetLoaderJobStatus-request-uri-errorsPerPage"></a>
The number of errors returned in each page (a positive integer; the default is `10`). Only valid when the `errors` parameter set to `TRUE`.
Valid Range: Minimum value of 1.

 ** [loadId](#API_GetLoaderJobStatus_RequestSyntax) **   <a name="neptunedata-GetLoaderJobStatus-request-uri-loadId"></a>
The load ID of the load job to get the status of.
Required: Yes

 ** [page](#API_GetLoaderJobStatus_RequestSyntax) **   <a name="neptunedata-GetLoaderJobStatus-request-uri-page"></a>
The error page number (a positive integer; the default is `1`). Only valid when the `errors` parameter is set to `TRUE`.
Valid Range: Minimum value of 1.

## Request Body
<a name="API_GetLoaderJobStatus_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetLoaderJobStatus_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "payload": JSON value,
   "status": "string"
}
```

## Response Elements
<a name="API_GetLoaderJobStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [payload](#API_GetLoaderJobStatus_ResponseSyntax) **   <a name="neptunedata-GetLoaderJobStatus-response-payload"></a>
Status information about the load job, in a layout that could look like this:
Type: JSON value

 ** [status](#API_GetLoaderJobStatus_ResponseSyntax) **   <a name="neptunedata-GetLoaderJobStatus-response-status"></a>
The HTTP response code for the request.
Type: String

## Errors
<a name="API_GetLoaderJobStatus_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
Raised when a request is submitted that cannot be processed.
 ** code **
The HTTP status code returned with the exception.
 ** detailedMessage **
A detailed message describing the problem.
 ** requestId **
The ID of the bad request.
HTTP Status Code: 400

 ** BulkLoadIdNotFoundException **
Raised when a specified bulk-load job ID cannot be found.
 ** code **
The HTTP status code returned with the exception.
 ** detailedMessage **
A detailed message describing the problem.
 ** requestId **
The bulk-load job ID that could not be found.
HTTP Status Code: 404

 ** ClientTimeoutException **
Raised when a request timed out in the client.
 ** code **
The HTTP status code returned with the exception.
 ** detailedMessage **
A detailed message describing the problem.
 ** requestId **
The ID of the request in question.
HTTP Status Code: 408

 ** ConstraintViolationException **
Raised when a value in a request field did not satisfy required constraints.
 ** code **
The HTTP status code returned with the exception.
 ** detailedMessage **
A detailed message describing the problem.
 ** requestId **
The ID of the request in question.
HTTP Status Code: 400

 ** IllegalArgumentException **
Raised when an argument in a request is not supported.
 ** code **
The HTTP status code returned with the exception.
 ** detailedMessage **
A detailed message describing the problem.
 ** requestId **
The ID of the request in question.
HTTP Status Code: 400

 ** InternalFailureException **
Raised when the processing of the request failed unexpectedly.
 ** code **
The HTTP status code returned with the exception.
 ** detailedMessage **
A detailed message describing the problem.
 ** requestId **
The ID of the request in question.
HTTP Status Code: 500

 ** InvalidArgumentException **
Raised when an argument in a request has an invalid value.
 ** code **
The HTTP status code returned with the exception.
 ** detailedMessage **
A detailed message describing the problem.
 ** requestId **
The ID of the request in question.
HTTP Status Code: 400

 ** InvalidParameterException **
Raised when a parameter value is not valid.
 ** code **
The HTTP status code returned with the exception.
 ** detailedMessage **
A detailed message describing the problem.
 ** requestId **
The ID of the request that includes an invalid parameter.
HTTP Status Code: 400

 ** LoadUrlAccessDeniedException **
Raised when access is denied to a specified load URL.
 ** code **
The HTTP status code returned with the exception.
 ** detailedMessage **
A detailed message describing the problem.
 ** requestId **
The ID of the request in question.
HTTP Status Code: 400

 ** MissingParameterException **
Raised when a required parameter is missing.
 ** code **
The HTTP status code returned with the exception.
 ** detailedMessage **
A detailed message describing the problem.
 ** requestId **
The ID of the request in which the parameter is missing.
HTTP Status Code: 400

 ** PreconditionsFailedException **
Raised when a precondition for processing a request is not satisfied.
 ** code **
The HTTP status code returned with the exception.
 ** detailedMessage **
A detailed message describing the problem.
 ** requestId **
The ID of the request in question.
HTTP Status Code: 400

 ** TooManyRequestsException **
Raised when the number of requests being processed exceeds the limit.
 ** code **
The HTTP status code returned with the exception.
 ** detailedMessage **
A detailed message describing the problem.
 ** requestId **
The ID of the request that could not be processed for this reason.
HTTP Status Code: 429

 ** UnsupportedOperationException **
Raised when a request attempts to initiate an operation that is not supported.
 ** code **
The HTTP status code returned with the exception.
 ** detailedMessage **
A detailed message describing the problem.
 ** requestId **
The ID of the request in question.
HTTP Status Code: 400

## See Also
<a name="API_GetLoaderJobStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/neptunedata-2023-08-01/GetLoaderJobStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/neptunedata-2023-08-01/GetLoaderJobStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptunedata-2023-08-01/GetLoaderJobStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/neptunedata-2023-08-01/GetLoaderJobStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptunedata-2023-08-01/GetLoaderJobStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/neptunedata-2023-08-01/GetLoaderJobStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/neptunedata-2023-08-01/GetLoaderJobStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/neptunedata-2023-08-01/GetLoaderJobStatus)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/neptunedata-2023-08-01/GetLoaderJobStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptunedata-2023-08-01/GetLoaderJobStatus)
