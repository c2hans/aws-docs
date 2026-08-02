---
source_url: https://docs.aws.amazon.com/neptune/latest/data-api/API_ListLoaderJobs.html
---

# ListLoaderJobs
<a name="API_ListLoaderJobs"></a>

Retrieves a list of the `loadIds` for all active loader jobs.

When invoking this operation in a Neptune cluster that has IAM authentication enabled, the IAM user or role making the request must have a policy attached that allows the [neptune-db:ListLoaderJobs](https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#listloaderjobs) IAM action in that cluster..

## Request Syntax
<a name="API_ListLoaderJobs_RequestSyntax"></a>

```
GET /loader?includeQueuedLoads={{includeQueuedLoads}}&limit={{limit}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListLoaderJobs_RequestParameters"></a>

The request uses the following URI parameters.

 ** [includeQueuedLoads](#API_ListLoaderJobs_RequestSyntax) **   <a name="neptunedata-ListLoaderJobs-request-uri-includeQueuedLoads"></a>
An optional parameter that can be used to exclude the load IDs of queued load requests when requesting a list of load IDs by setting the parameter to `FALSE`. The default value is `TRUE`.

 ** [limit](#API_ListLoaderJobs_RequestSyntax) **   <a name="neptunedata-ListLoaderJobs-request-uri-limit"></a>
The number of load IDs to list. Must be a positive integer greater than zero and not more than `100` (which is the default).
Valid Range: Minimum value of 1. Maximum value of 100.

## Request Body
<a name="API_ListLoaderJobs_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListLoaderJobs_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "payload": {
      "loadIds": [ "string" ]
   },
   "status": "string"
}
```

## Response Elements
<a name="API_ListLoaderJobs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [payload](#API_ListLoaderJobs_ResponseSyntax) **   <a name="neptunedata-ListLoaderJobs-response-payload"></a>
The requested list of job IDs.
Type: [LoaderIdResult](API_LoaderIdResult.md) object

 ** [status](#API_ListLoaderJobs_ResponseSyntax) **   <a name="neptunedata-ListLoaderJobs-response-status"></a>
Returns the status of the job list request.
Type: String

## Errors
<a name="API_ListLoaderJobs_Errors"></a>

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
<a name="API_ListLoaderJobs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/neptunedata-2023-08-01/ListLoaderJobs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/neptunedata-2023-08-01/ListLoaderJobs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptunedata-2023-08-01/ListLoaderJobs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/neptunedata-2023-08-01/ListLoaderJobs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptunedata-2023-08-01/ListLoaderJobs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/neptunedata-2023-08-01/ListLoaderJobs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/neptunedata-2023-08-01/ListLoaderJobs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/neptunedata-2023-08-01/ListLoaderJobs)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/neptunedata-2023-08-01/ListLoaderJobs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptunedata-2023-08-01/ListLoaderJobs)
