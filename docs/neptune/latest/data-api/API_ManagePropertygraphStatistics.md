---
source_url: https://docs.aws.amazon.com/neptune/latest/data-api/API_ManagePropertygraphStatistics.html
---

# ManagePropertygraphStatistics
<a name="API_ManagePropertygraphStatistics"></a>

Manages the generation and use of property graph statistics.

When invoking this operation in a Neptune cluster that has IAM authentication enabled, the IAM user or role making the request must have a policy attached that allows the [neptune-db:ManageStatistics](https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#managestatistics) IAM action in that cluster.

## Request Syntax
<a name="API_ManagePropertygraphStatistics_RequestSyntax"></a>

```
POST /propertygraph/statistics HTTP/1.1
Content-type: application/json

{
   "mode": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ManagePropertygraphStatistics_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ManagePropertygraphStatistics_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [mode](#API_ManagePropertygraphStatistics_RequestSyntax) **   <a name="neptunedata-ManagePropertygraphStatistics-request-mode"></a>
The statistics generation mode. One of: `DISABLE_AUTOCOMPUTE`, `ENABLE_AUTOCOMPUTE`, or `REFRESH`, the last of which manually triggers DFE statistics generation.
Type: String
Valid Values: `disableAutoCompute | enableAutoCompute | refresh`
Required: No

## Response Syntax
<a name="API_ManagePropertygraphStatistics_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "payload": {
      "statisticsId": "string"
   },
   "status": "string"
}
```

## Response Elements
<a name="API_ManagePropertygraphStatistics_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [payload](#API_ManagePropertygraphStatistics_ResponseSyntax) **   <a name="neptunedata-ManagePropertygraphStatistics-response-payload"></a>
This is only returned for refresh mode.
Type: [RefreshStatisticsIdMap](API_RefreshStatisticsIdMap.md) object

 ** [status](#API_ManagePropertygraphStatistics_ResponseSyntax) **   <a name="neptunedata-ManagePropertygraphStatistics-response-status"></a>
The HTTP return code of the request. If the request succeeded, the code is 200.
Type: String

## Errors
<a name="API_ManagePropertygraphStatistics_Errors"></a>

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
<a name="API_ManagePropertygraphStatistics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/neptunedata-2023-08-01/ManagePropertygraphStatistics)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/neptunedata-2023-08-01/ManagePropertygraphStatistics)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptunedata-2023-08-01/ManagePropertygraphStatistics)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/neptunedata-2023-08-01/ManagePropertygraphStatistics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptunedata-2023-08-01/ManagePropertygraphStatistics)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/neptunedata-2023-08-01/ManagePropertygraphStatistics)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/neptunedata-2023-08-01/ManagePropertygraphStatistics)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/neptunedata-2023-08-01/ManagePropertygraphStatistics)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/neptunedata-2023-08-01/ManagePropertygraphStatistics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptunedata-2023-08-01/ManagePropertygraphStatistics)
