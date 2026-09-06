---
source_url: https://docs.aws.amazon.com/neptune/latest/data-api/API_ListGremlinQueries.html
---

# ListGremlinQueries
<a name="API_ListGremlinQueries"></a>

Lists active Gremlin queries. See [Gremlin query status API](https://docs.aws.amazon.com/neptune/latest/userguide/gremlin-api-status.html) for details about the output.

When invoking this operation in a Neptune cluster that has IAM authentication enabled, the IAM user or role making the request must have a policy attached that allows the [neptune-db:GetQueryStatus](https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#getquerystatus) IAM action in that cluster.

Note that the [neptune-db:QueryLanguage:Gremlin](https://docs.aws.amazon.com/neptune/latest/userguide/iam-data-condition-keys.html#iam-neptune-condition-keys) IAM condition key can be used in the policy document to restrict the use of Gremlin queries (see [Condition keys available in Neptune IAM data-access policy statements](https://docs.aws.amazon.com/neptune/latest/userguide/iam-data-condition-keys.html)).

## Request Syntax
<a name="API_ListGremlinQueries_RequestSyntax"></a>

```
GET /gremlin/status?includeWaiting={{includeWaiting}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListGremlinQueries_RequestParameters"></a>

The request uses the following URI parameters.

 ** [includeWaiting](#API_ListGremlinQueries_RequestSyntax) **   <a name="neptunedata-ListGremlinQueries-request-uri-includeWaiting"></a>
If set to `TRUE`, the list returned includes waiting queries. The default is `FALSE`;

## Request Body
<a name="API_ListGremlinQueries_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListGremlinQueries_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "acceptedQueryCount": number,
   "queries": [
      {
         "queryEvalStats": {
            "cancelled": boolean,
            "elapsed": number,
            "subqueries": JSON value,
            "waited": number
         },
         "queryId": "string",
         "queryString": "string"
      }
   ],
   "runningQueryCount": number
}
```

## Response Elements
<a name="API_ListGremlinQueries_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [acceptedQueryCount](#API_ListGremlinQueries_ResponseSyntax) **   <a name="neptunedata-ListGremlinQueries-response-acceptedQueryCount"></a>
The number of queries that have been accepted but not yet completed, including queries in the queue.
Type: Integer

 ** [queries](#API_ListGremlinQueries_ResponseSyntax) **   <a name="neptunedata-ListGremlinQueries-response-queries"></a>
A list of the current queries.
Type: Array of [GremlinQueryStatus](API_GremlinQueryStatus.md) objects

 ** [runningQueryCount](#API_ListGremlinQueries_ResponseSyntax) **   <a name="neptunedata-ListGremlinQueries-response-runningQueryCount"></a>
The number of Gremlin queries currently running.
Type: Integer

## Errors
<a name="API_ListGremlinQueries_Errors"></a>

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

 ** ReadOnlyViolationException **
Raised when a request attempts to write to a read-only resource.
 ** code **
The HTTP status code returned with the exception.
 ** detailedMessage **
A detailed message describing the problem.
 ** requestId **
The ID of the request in which the parameter is missing.
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
<a name="API_ListGremlinQueries_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/neptunedata-2023-08-01/ListGremlinQueries)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/neptunedata-2023-08-01/ListGremlinQueries)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptunedata-2023-08-01/ListGremlinQueries)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/neptunedata-2023-08-01/ListGremlinQueries)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptunedata-2023-08-01/ListGremlinQueries)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/neptunedata-2023-08-01/ListGremlinQueries)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/neptunedata-2023-08-01/ListGremlinQueries)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/neptunedata-2023-08-01/ListGremlinQueries)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/neptunedata-2023-08-01/ListGremlinQueries)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptunedata-2023-08-01/ListGremlinQueries)
