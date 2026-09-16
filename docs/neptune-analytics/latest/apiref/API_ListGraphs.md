---
source_url: https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_ListGraphs.html
---

# ListGraphs
<a name="API_ListGraphs"></a>

Lists available Neptune Analytics graphs.

## Request Syntax
<a name="API_ListGraphs_RequestSyntax"></a>

```
GET /graphs?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListGraphs_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListGraphs_RequestSyntax) **   <a name="neptunegraph-ListGraphs-request-uri-maxResults"></a>
The total number of records to return in the command's output.
If the total number of records available is more than the value specified, `nextToken` is provided in the command's output. To resume pagination, provide the `nextToken` output value in the `nextToken` argument of a subsequent command. Do not use the `nextToken` response element directly outside of the Amazon CLI.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListGraphs_RequestSyntax) **   <a name="neptunegraph-ListGraphs-request-uri-nextToken"></a>
Pagination token used to paginate output.
When this value is provided as input, the service returns results from where the previous response left off. When this value is present in output, it indicates that there are more results to retrieve.
Length Constraints: Minimum length of 1. Maximum length of 8192.

## Request Body
<a name="API_ListGraphs_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListGraphs_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "graphs": [
      {
         "arn": "string",
         "deletionProtection": boolean,
         "endpoint": "string",
         "id": "string",
         "kmsKeyIdentifier": "string",
         "name": "string",
         "provisionedMemory": number,
         "publicConnectivity": boolean,
         "replicaCount": number,
         "status": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListGraphs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [graphs](#API_ListGraphs_ResponseSyntax) **   <a name="neptunegraph-ListGraphs-response-graphs"></a>
A list of the graphs.
Type: Array of [GraphSummary](API_GraphSummary.md) objects

 ** [nextToken](#API_ListGraphs_ResponseSyntax) **   <a name="neptunegraph-ListGraphs-response-nextToken"></a>
Pagination token used to paginate output.
When this value is provided as input, the service returns results from where the previous response left off. When this value is present in output, it indicates that there are more results to retrieve.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.

## Errors
<a name="API_ListGraphs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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

## See Also
<a name="API_ListGraphs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/neptune-graph-2023-11-29/ListGraphs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/neptune-graph-2023-11-29/ListGraphs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-graph-2023-11-29/ListGraphs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/neptune-graph-2023-11-29/ListGraphs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-graph-2023-11-29/ListGraphs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/neptune-graph-2023-11-29/ListGraphs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/neptune-graph-2023-11-29/ListGraphs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/neptune-graph-2023-11-29/ListGraphs)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/neptune-graph-2023-11-29/ListGraphs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-graph-2023-11-29/ListGraphs)
