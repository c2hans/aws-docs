---
source_url: https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_ExecuteQuery.html
---

# ExecuteQuery
<a name="API_ExecuteQuery"></a>

Execute an openCypher query.

 When invoking this operation in a Neptune Analytics cluster, the IAM user or role making the request must have a policy attached that allows one of the following IAM actions in that cluster, depending on the query:
+ neptune-graph:ReadDataViaQuery
+ neptune-graph:WriteDataViaQuery
+ neptune-graph:DeleteDataViaQuery

## Request Syntax
<a name="API_ExecuteQuery_RequestSyntax"></a>

```
POST /queries HTTP/1.1
graphIdentifier: {{graphIdentifier}}
Content-type: application/json

{
   "explain": "{{string}}",
   "language": "{{string}}",
   "parameters": {
      "{{string}}" : {{JSON value}}
   },
   "planCache": "{{string}}",
   "query": "{{string}}",
   "queryTimeoutMilliseconds": {{number}}
}
```

## URI Request Parameters
<a name="API_ExecuteQuery_RequestParameters"></a>

The request uses the following URI parameters.

 ** [graphIdentifier](#API_ExecuteQuery_RequestSyntax) **   <a name="neptunegraph-ExecuteQuery-request-graphIdentifier"></a>
The unique identifier of the Neptune Analytics graph.
Pattern: `g-[a-z0-9]{10}`
Required: Yes

## Request Body
<a name="API_ExecuteQuery_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [explain](#API_ExecuteQuery_RequestSyntax) **   <a name="neptunegraph-ExecuteQuery-request-explain"></a>
The explain mode parameter returns a query explain instead of the actual query results. A query explain can be used to gather insights about the query execution such as planning decisions, time spent on each operator, solutions flowing etc.
Type: String
Valid Values: `STATIC | DETAILS`
Required: No

 ** [language](#API_ExecuteQuery_RequestSyntax) **   <a name="neptunegraph-ExecuteQuery-request-language"></a>
The query language the query is written in. Currently only openCypher is supported.
Type: String
Valid Values: `OPEN_CYPHER`
Required: Yes

 ** [parameters](#API_ExecuteQuery_RequestSyntax) **   <a name="neptunegraph-ExecuteQuery-request-parameters"></a>
The data parameters the query can use in JSON format. For example: {"name": "john", "age": 20}. (optional)
Type: String to JSON value map
Required: No

 ** [planCache](#API_ExecuteQuery_RequestSyntax) **   <a name="neptunegraph-ExecuteQuery-request-planCache"></a>
Query plan cache is a feature that saves the query plan and reuses it on successive executions of the same query. This reduces query latency, and works for both `READ` and `UPDATE` queries. The plan cache is an LRU cache with a 5 minute TTL and a capacity of 1000.
Type: String
Valid Values: `ENABLED | DISABLED | AUTO`
Required: No

 ** [query](#API_ExecuteQuery_RequestSyntax) **   <a name="neptunegraph-ExecuteQuery-request-query"></a>
The query string to be executed.
Type: String
Required: Yes

 ** [queryTimeoutMilliseconds](#API_ExecuteQuery_RequestSyntax) **   <a name="neptunegraph-ExecuteQuery-request-queryTimeoutMilliseconds"></a>
Specifies the query timeout duration, in milliseconds. (optional)
Type: Integer
Required: No

## Response Syntax
<a name="API_ExecuteQuery_ResponseSyntax"></a>

```
HTTP/1.1 200

{{payload}}
```

## Response Elements
<a name="API_ExecuteQuery_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The response returns the following as the HTTP body.

 ** [payload](#API_ExecuteQuery_ResponseSyntax) **   <a name="neptunegraph-ExecuteQuery-response-payload"></a>
The query results.

## Errors
<a name="API_ExecuteQuery_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Raised in case of an authentication or authorization failure.
 ** message **
A message describing the problem.
HTTP Status Code: 403

 ** ConflictException **
Raised when a conflict is encountered.
 ** message **
A message describing the problem.
 ** reason **
The reason for the conflict exception.
HTTP Status Code: 409

 ** InternalServerException **
A failure occurred on the server.
 ** message **
A message describing the problem.
HTTP Status Code: 500

 ** ThrottlingException **
The exception was interrupted by throttling.
 ** message **
A message describing the problem.
HTTP Status Code: 429

 ** UnprocessableException **
Request cannot be processed due to known reasons. Eg. partition full.
 ** reason **
The reason for the unprocessable exception.
HTTP Status Code: 422

 ** ValidationException **
A resource could not be validated.
 ** message **
A message describing the problem.
 ** reason **
The reason that the resource could not be validated.
HTTP Status Code: 400

## See Also
<a name="API_ExecuteQuery_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/neptune-graph-2023-11-29/ExecuteQuery)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/neptune-graph-2023-11-29/ExecuteQuery)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-graph-2023-11-29/ExecuteQuery)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/neptune-graph-2023-11-29/ExecuteQuery)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-graph-2023-11-29/ExecuteQuery)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/neptune-graph-2023-11-29/ExecuteQuery)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/neptune-graph-2023-11-29/ExecuteQuery)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/neptune-graph-2023-11-29/ExecuteQuery)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/neptune-graph-2023-11-29/ExecuteQuery)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-graph-2023-11-29/ExecuteQuery)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for NeptuneAnalyticsAPI. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune-analytics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
