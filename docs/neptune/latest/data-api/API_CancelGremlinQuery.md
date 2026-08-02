---
source_url: https://docs.aws.amazon.com/neptune/latest/data-api/API_CancelGremlinQuery.html
---

# CancelGremlinQuery
<a name="API_CancelGremlinQuery"></a>

Cancels a Gremlin query. See [Gremlin query cancellation](https://docs.aws.amazon.com/neptune/latest/userguide/gremlin-api-status-cancel.html) for more information.

When invoking this operation in a Neptune cluster that has IAM authentication enabled, the IAM user or role making the request must have a policy attached that allows the [neptune-db:CancelQuery](https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#cancelquery) IAM action in that cluster.

## Request Syntax
<a name="API_CancelGremlinQuery_RequestSyntax"></a>

```
DELETE /gremlin/status/{{queryId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_CancelGremlinQuery_RequestParameters"></a>

The request uses the following URI parameters.

 ** [queryId](#API_CancelGremlinQuery_RequestSyntax) **   <a name="neptunedata-CancelGremlinQuery-request-uri-queryId"></a>
The unique identifier that identifies the query to be canceled.
Required: Yes

## Request Body
<a name="API_CancelGremlinQuery_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_CancelGremlinQuery_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "status": "string"
}
```

## Response Elements
<a name="API_CancelGremlinQuery_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [status](#API_CancelGremlinQuery_ResponseSyntax) **   <a name="neptunedata-CancelGremlinQuery-response-status"></a>
The status of the cancelation
Type: String

## Errors
<a name="API_CancelGremlinQuery_Errors"></a>

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

 ** ClientTimeoutException **
Raised when a request timed out in the client.
 ** code **
The HTTP status code returned with the exception.
 ** detailedMessage **
A detailed message describing the problem.
 ** requestId **
The ID of the request in question.
HTTP Status Code: 408

 ** ConcurrentModificationException **
Raised when a request attempts to modify data that is concurrently being modified by another process.
 ** code **
The HTTP status code returned with the exception.
 ** detailedMessage **
A detailed message describing the problem.
 ** requestId **
The ID of the request in question.
HTTP Status Code: 500

 ** ConstraintViolationException **
Raised when a value in a request field did not satisfy required constraints.
 ** code **
The HTTP status code returned with the exception.
 ** detailedMessage **
A detailed message describing the problem.
 ** requestId **
The ID of the request in question.
HTTP Status Code: 400

 ** FailureByQueryException **
Raised when a request fails.
 ** code **
The HTTP status code returned with the exception.
 ** detailedMessage **
A detailed message describing the problem.
 ** requestId **
The ID of the request in question.
HTTP Status Code: 500

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

 ** ParsingException **
Raised when a parsing issue is encountered.
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

 ** TimeLimitExceededException **
Raised when the an operation exceeds the time limit allowed for it.
 ** code **
The HTTP status code returned with the exception.
 ** detailedMessage **
A detailed message describing the problem.
 ** requestId **
The ID of the request that could not be processed for this reason.
HTTP Status Code: 500

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
<a name="API_CancelGremlinQuery_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/neptunedata-2023-08-01/CancelGremlinQuery)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/neptunedata-2023-08-01/CancelGremlinQuery)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptunedata-2023-08-01/CancelGremlinQuery)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/neptunedata-2023-08-01/CancelGremlinQuery)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptunedata-2023-08-01/CancelGremlinQuery)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/neptunedata-2023-08-01/CancelGremlinQuery)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/neptunedata-2023-08-01/CancelGremlinQuery)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/neptunedata-2023-08-01/CancelGremlinQuery)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/neptunedata-2023-08-01/CancelGremlinQuery)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptunedata-2023-08-01/CancelGremlinQuery)
