---
source_url: https://docs.aws.amazon.com/neptune/latest/data-api/API_DeletePropertygraphStatistics.html
---

# DeletePropertygraphStatistics
<a name="API_DeletePropertygraphStatistics"></a>

Deletes statistics for Gremlin and openCypher (property graph) data.

When invoking this operation in a Neptune cluster that has IAM authentication enabled, the IAM user or role making the request must have a policy attached that allows the [neptune-db:DeleteStatistics](https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#deletestatistics) IAM action in that cluster.

## Request Syntax
<a name="API_DeletePropertygraphStatistics_RequestSyntax"></a>

```
DELETE /propertygraph/statistics HTTP/1.1
```

## URI Request Parameters
<a name="API_DeletePropertygraphStatistics_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DeletePropertygraphStatistics_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeletePropertygraphStatistics_ResponseSyntax"></a>

```
HTTP/1.1 {{statusCode}}
Content-type: application/json

{
   "payload": {
      "active": boolean,
      "statisticsId": "string"
   },
   "status": "string"
}
```

## Response Elements
<a name="API_DeletePropertygraphStatistics_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [statusCode](#API_DeletePropertygraphStatistics_ResponseSyntax) **   <a name="neptunedata-DeletePropertygraphStatistics-response-statusCode"></a>
The HTTP response code: 200 if the delete was successful, or 204 if there were no statistics to delete.

The following data is returned in JSON format by the service.

 ** [payload](#API_DeletePropertygraphStatistics_ResponseSyntax) **   <a name="neptunedata-DeletePropertygraphStatistics-response-payload"></a>
The deletion payload.
Type: [DeleteStatisticsValueMap](API_DeleteStatisticsValueMap.md) object

 ** [status](#API_DeletePropertygraphStatistics_ResponseSyntax) **   <a name="neptunedata-DeletePropertygraphStatistics-response-status"></a>
The cancel status.
Type: String

## Errors
<a name="API_DeletePropertygraphStatistics_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Raised in case of an authentication or authorization failure.
 ** code **
The HTTP status code returned with the exception.
 ** detailedMessage **
A detailed message describing the problem.
 ** requestId **
The ID of the request in question.
HTTP Status Code: 403

 ** BadRequestException **
Raised when a request is submitted that cannot be processed.
 ** code **
The HTTP status code returned with the exception.
 ** detailedMessage **
A detailed message describing the problem.
 ** requestId **
The ID of the bad request.
HTTP Status Code: 400

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

 ** ReadOnlyViolationException **
Raised when a request attempts to write to a read-only resource.
 ** code **
The HTTP status code returned with the exception.
 ** detailedMessage **
A detailed message describing the problem.
 ** requestId **
The ID of the request in which the parameter is missing.
HTTP Status Code: 400

 ** StatisticsNotAvailableException **
Raised when statistics needed to satisfy a request are not available.
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
<a name="API_DeletePropertygraphStatistics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/neptunedata-2023-08-01/DeletePropertygraphStatistics)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/neptunedata-2023-08-01/DeletePropertygraphStatistics)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptunedata-2023-08-01/DeletePropertygraphStatistics)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/neptunedata-2023-08-01/DeletePropertygraphStatistics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptunedata-2023-08-01/DeletePropertygraphStatistics)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/neptunedata-2023-08-01/DeletePropertygraphStatistics)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/neptunedata-2023-08-01/DeletePropertygraphStatistics)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/neptunedata-2023-08-01/DeletePropertygraphStatistics)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/neptunedata-2023-08-01/DeletePropertygraphStatistics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptunedata-2023-08-01/DeletePropertygraphStatistics)
