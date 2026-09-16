---
source_url: https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_GetQuery.html
---

# GetQuery
<a name="API_GetQuery"></a>

Retrieves the status of a specified query.

**Note**
 When invoking this operation in a Neptune Analytics cluster, the IAM user or role making the request must have the `neptune-graph:GetQueryStatus` IAM action attached.

## Request Syntax
<a name="API_GetQuery_RequestSyntax"></a>

```
GET /queries/{{queryId}} HTTP/1.1
graphIdentifier: {{graphIdentifier}}
```

## URI Request Parameters
<a name="API_GetQuery_RequestParameters"></a>

The request uses the following URI parameters.

 ** [graphIdentifier](#API_GetQuery_RequestSyntax) **   <a name="neptunegraph-GetQuery-request-graphIdentifier"></a>
The unique identifier of the Neptune Analytics graph.
Pattern: `g-[a-z0-9]{10}`
Required: Yes

 ** [queryId](#API_GetQuery_RequestSyntax) **   <a name="neptunegraph-GetQuery-request-uri-queryId"></a>
The ID of the query in question.
Required: Yes

## Request Body
<a name="API_GetQuery_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetQuery_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "elapsed": number,
   "id": "string",
   "queryString": "string",
   "state": "string",
   "waited": number
}
```

## Response Elements
<a name="API_GetQuery_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [elapsed](#API_GetQuery_ResponseSyntax) **   <a name="neptunegraph-GetQuery-response-elapsed"></a>
The number of milliseconds the query has been running.
Type: Integer

 ** [id](#API_GetQuery_ResponseSyntax) **   <a name="neptunegraph-GetQuery-response-id"></a>
The ID of the query in question.
Type: String

 ** [queryString](#API_GetQuery_ResponseSyntax) **   <a name="neptunegraph-GetQuery-response-queryString"></a>
The query in question.
Type: String

 ** [state](#API_GetQuery_ResponseSyntax) **   <a name="neptunegraph-GetQuery-response-state"></a>
State of the query.
Type: String
Valid Values: `RUNNING | WAITING | CANCELLING`

 ** [waited](#API_GetQuery_ResponseSyntax) **   <a name="neptunegraph-GetQuery-response-waited"></a>
Indicates how long the query waited, in milliseconds.
Type: Integer

## Errors
<a name="API_GetQuery_Errors"></a>

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

 ** ResourceNotFoundException **
A specified resource could not be located.
 ** message **
A message describing the problem.
HTTP Status Code: 404

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
<a name="API_GetQuery_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/neptune-graph-2023-11-29/GetQuery)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/neptune-graph-2023-11-29/GetQuery)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-graph-2023-11-29/GetQuery)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/neptune-graph-2023-11-29/GetQuery)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-graph-2023-11-29/GetQuery)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/neptune-graph-2023-11-29/GetQuery)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/neptune-graph-2023-11-29/GetQuery)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/neptune-graph-2023-11-29/GetQuery)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/neptune-graph-2023-11-29/GetQuery)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-graph-2023-11-29/GetQuery)
