---
source_url: https://docs.aws.amazon.com/neptune/latest/data-api/API_ExecuteGremlinProfileQuery.html
---

# ExecuteGremlinProfileQuery
<a name="API_ExecuteGremlinProfileQuery"></a>

Executes a Gremlin Profile query, which runs a specified traversal, collects various metrics about the run, and produces a profile report as output. See [Gremlin profile API in Neptune](https://docs.aws.amazon.com/neptune/latest/userguide/gremlin-profile-api.html) for details.

When invoking this operation in a Neptune cluster that has IAM authentication enabled, the IAM user or role making the request must have a policy attached that allows the [neptune-db:ReadDataViaQuery](https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#readdataviaquery) IAM action in that cluster.

Note that the [neptune-db:QueryLanguage:Gremlin](https://docs.aws.amazon.com/neptune/latest/userguide/iam-data-condition-keys.html#iam-neptune-condition-keys) IAM condition key can be used in the policy document to restrict the use of Gremlin queries (see [Condition keys available in Neptune IAM data-access policy statements](https://docs.aws.amazon.com/neptune/latest/userguide/iam-data-condition-keys.html)).

## Request Syntax
<a name="API_ExecuteGremlinProfileQuery_RequestSyntax"></a>

```
POST /gremlin/profile HTTP/1.1
Content-type: application/json

{
   "profile.chop": {{number}},
   "gremlin": "{{string}}",
   "profile.indexOps": {{boolean}},
   "profile.results": {{boolean}},
   "profile.serializer": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ExecuteGremlinProfileQuery_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ExecuteGremlinProfileQuery_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [profile.chop](#API_ExecuteGremlinProfileQuery_RequestSyntax) **   <a name="neptunedata-ExecuteGremlinProfileQuery-request-profile.chop"></a>
If non-zero, causes the results string to be truncated at that number of characters. If set to zero, the string contains all the results.
Type: Integer
Required: No

 ** [gremlin](#API_ExecuteGremlinProfileQuery_RequestSyntax) **   <a name="neptunedata-ExecuteGremlinProfileQuery-request-gremlin"></a>
The Gremlin query string to profile.
Type: String
Required: Yes

 ** [profile.indexOps](#API_ExecuteGremlinProfileQuery_RequestSyntax) **   <a name="neptunedata-ExecuteGremlinProfileQuery-request-profile.indexOps"></a>
If this flag is set to `TRUE`, the results include a detailed report of all index operations that took place during query execution and serialization.
Type: Boolean
Required: No

 ** [profile.results](#API_ExecuteGremlinProfileQuery_RequestSyntax) **   <a name="neptunedata-ExecuteGremlinProfileQuery-request-profile.results"></a>
If this flag is set to `TRUE`, the query results are gathered and displayed as part of the profile report. If `FALSE`, only the result count is displayed.
Type: Boolean
Required: No

 ** [profile.serializer](#API_ExecuteGremlinProfileQuery_RequestSyntax) **   <a name="neptunedata-ExecuteGremlinProfileQuery-request-profile.serializer"></a>
If non-null, the gathered results are returned in a serialized response message in the format specified by this parameter. See [Gremlin profile API in Neptune](https://docs.aws.amazon.com/neptune/latest/userguide/gremlin-profile-api.html) for more information.
Type: String
Required: No

## Response Syntax
<a name="API_ExecuteGremlinProfileQuery_ResponseSyntax"></a>

```
HTTP/1.1 200

{{output}}
```

## Response Elements
<a name="API_ExecuteGremlinProfileQuery_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The response returns the following as the HTTP body.

 ** [output](#API_ExecuteGremlinProfileQuery_ResponseSyntax) **   <a name="neptunedata-ExecuteGremlinProfileQuery-response-output"></a>
A text blob containing the Gremlin Profile result. See [Gremlin profile API in Neptune](https://docs.aws.amazon.com/neptune/latest/userguide/gremlin-profile-api.html) for details.

## Errors
<a name="API_ExecuteGremlinProfileQuery_Errors"></a>

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

 ** CancelledByUserException **
Raised when a user cancelled a request.
 ** code **
The HTTP status code returned with the exception.
 ** detailedMessage **
A detailed message describing the problem.
 ** requestId **
The ID of the request in question.
HTTP Status Code: 500

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

 ** MalformedQueryException **
Raised when a query is submitted that is syntactically incorrect or does not pass additional validation.
 ** code **
The HTTP status code returned with the exception.
 ** detailedMessage **
A detailed message describing the problem.
 ** requestId **
The ID of the malformed query request.
HTTP Status Code: 400

 ** MemoryLimitExceededException **
Raised when a request fails because of insufficient memory resources. The request can be retried.
 ** code **
The HTTP status code returned with the exception.
 ** detailedMessage **
A detailed message describing the problem.
 ** requestId **
The ID of the request that failed.
HTTP Status Code: 500

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

 ** QueryLimitExceededException **
Raised when the number of active queries exceeds what the server can process. The query in question can be retried when the system is less busy.
 ** code **
The HTTP status code returned with the exception.
 ** detailedMessage **
A detailed message describing the problem.
 ** requestId **
The ID of the request which exceeded the limit.
HTTP Status Code: 500

 ** QueryLimitException **
Raised when the size of a query exceeds the system limit.
 ** code **
The HTTP status code returned with the exception.
 ** detailedMessage **
A detailed message describing the problem.
 ** requestId **
The ID of the request that exceeded the limit.
HTTP Status Code: 400

 ** QueryTooLargeException **
Raised when the body of a query is too large.
 ** code **
The HTTP status code returned with the exception.
 ** detailedMessage **
A detailed message describing the problem.
 ** requestId **
The ID of the request that is too large.
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
<a name="API_ExecuteGremlinProfileQuery_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/neptunedata-2023-08-01/ExecuteGremlinProfileQuery)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/neptunedata-2023-08-01/ExecuteGremlinProfileQuery)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptunedata-2023-08-01/ExecuteGremlinProfileQuery)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/neptunedata-2023-08-01/ExecuteGremlinProfileQuery)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptunedata-2023-08-01/ExecuteGremlinProfileQuery)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/neptunedata-2023-08-01/ExecuteGremlinProfileQuery)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/neptunedata-2023-08-01/ExecuteGremlinProfileQuery)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/neptunedata-2023-08-01/ExecuteGremlinProfileQuery)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/neptunedata-2023-08-01/ExecuteGremlinProfileQuery)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptunedata-2023-08-01/ExecuteGremlinProfileQuery)
