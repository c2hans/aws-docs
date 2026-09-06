---
source_url: https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_ListQueries.html
---

# ListQueries
<a name="API_ListQueries"></a>

Lists active openCypher queries.

## Request Syntax
<a name="API_ListQueries_RequestSyntax"></a>

```
GET /queries?maxResults={{maxResults}}&state={{state}} HTTP/1.1
graphIdentifier: {{graphIdentifier}}
```

## URI Request Parameters
<a name="API_ListQueries_RequestParameters"></a>

The request uses the following URI parameters.

 ** [graphIdentifier](#API_ListQueries_RequestSyntax) **   <a name="neptunegraph-ListQueries-request-graphIdentifier"></a>
The unique identifier of the Neptune Analytics graph.
Pattern: `g-[a-z0-9]{10}`
Required: Yes

 ** [maxResults](#API_ListQueries_RequestSyntax) **   <a name="neptunegraph-ListQueries-request-uri-maxResults"></a>
The maximum number of results to be fetched by the API.
Required: Yes

 ** [state](#API_ListQueries_RequestSyntax) **   <a name="neptunegraph-ListQueries-request-uri-state"></a>
Filtered list of queries based on state.
Valid Values: `ALL | RUNNING | WAITING | CANCELLING`

## Request Body
<a name="API_ListQueries_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListQueries_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "queries": [
      {
         "elapsed": number,
         "id": "string",
         "queryString": "string",
         "state": "string",
         "waited": number
      }
   ]
}
```

## Response Elements
<a name="API_ListQueries_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [queries](#API_ListQueries_ResponseSyntax) **   <a name="neptunegraph-ListQueries-response-queries"></a>
A list of current openCypher queries.
Type: Array of [QuerySummary](API_QuerySummary.md) objects

## Errors
<a name="API_ListQueries_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Raised in case of an authentication or authorization failure.
 ** message **
A message describing the problem.
HTTP Status Code: 403

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

 ** ValidationException **
A resource could not be validated.
 ** message **
A message describing the problem.
 ** reason **
The reason that the resource could not be validated.
HTTP Status Code: 400

## See Also
<a name="API_ListQueries_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/neptune-graph-2023-11-29/ListQueries)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/neptune-graph-2023-11-29/ListQueries)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-graph-2023-11-29/ListQueries)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/neptune-graph-2023-11-29/ListQueries)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-graph-2023-11-29/ListQueries)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/neptune-graph-2023-11-29/ListQueries)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/neptune-graph-2023-11-29/ListQueries)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/neptune-graph-2023-11-29/ListQueries)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/neptune-graph-2023-11-29/ListQueries)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-graph-2023-11-29/ListQueries)
