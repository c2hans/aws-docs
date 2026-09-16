---
source_url: https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_ListPrivateGraphEndpoints.html
---

# ListPrivateGraphEndpoints
<a name="API_ListPrivateGraphEndpoints"></a>

Lists private endpoints for a specified Neptune Analytics graph.

## Request Syntax
<a name="API_ListPrivateGraphEndpoints_RequestSyntax"></a>

```
GET /graphs/{{graphIdentifier}}/endpoints/?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListPrivateGraphEndpoints_RequestParameters"></a>

The request uses the following URI parameters.

 ** [graphIdentifier](#API_ListPrivateGraphEndpoints_RequestSyntax) **   <a name="neptunegraph-ListPrivateGraphEndpoints-request-uri-graphIdentifier"></a>
The unique identifier of the Neptune Analytics graph.
Pattern: `g-[a-z0-9]{10}`
Required: Yes

 ** [maxResults](#API_ListPrivateGraphEndpoints_RequestSyntax) **   <a name="neptunegraph-ListPrivateGraphEndpoints-request-uri-maxResults"></a>
The total number of records to return in the command's output.
If the total number of records available is more than the value specified, `nextToken` is provided in the command's output. To resume pagination, provide the `nextToken` output value in the `nextToken` argument of a subsequent command. Do not use the `nextToken` response element directly outside of the Amazon CLI.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListPrivateGraphEndpoints_RequestSyntax) **   <a name="neptunegraph-ListPrivateGraphEndpoints-request-uri-nextToken"></a>
Pagination token used to paginate output.
When this value is provided as input, the service returns results from where the previous response left off. When this value is present in output, it indicates that there are more results to retrieve.
Length Constraints: Minimum length of 1. Maximum length of 8192.

## Request Body
<a name="API_ListPrivateGraphEndpoints_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListPrivateGraphEndpoints_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "privateGraphEndpoints": [
      {
         "status": "string",
         "subnetIds": [ "string" ],
         "vpcEndpointId": "string",
         "vpcId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListPrivateGraphEndpoints_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListPrivateGraphEndpoints_ResponseSyntax) **   <a name="neptunegraph-ListPrivateGraphEndpoints-response-nextToken"></a>
Pagination token used to paginate output.
When this value is provided as input, the service returns results from where the previous response left off. When this value is present in output, it indicates that there are more results to retrieve.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.

 ** [privateGraphEndpoints](#API_ListPrivateGraphEndpoints_ResponseSyntax) **   <a name="neptunegraph-ListPrivateGraphEndpoints-response-privateGraphEndpoints"></a>
A list of private endpoints for the specified Neptune Analytics graph.
Type: Array of [PrivateGraphEndpointSummary](API_PrivateGraphEndpointSummary.md) objects

## Errors
<a name="API_ListPrivateGraphEndpoints_Errors"></a>

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

 ** ValidationException **
A resource could not be validated.
 ** message **
A message describing the problem.
 ** reason **
The reason that the resource could not be validated.
HTTP Status Code: 400

## See Also
<a name="API_ListPrivateGraphEndpoints_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/neptune-graph-2023-11-29/ListPrivateGraphEndpoints)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/neptune-graph-2023-11-29/ListPrivateGraphEndpoints)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-graph-2023-11-29/ListPrivateGraphEndpoints)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/neptune-graph-2023-11-29/ListPrivateGraphEndpoints)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-graph-2023-11-29/ListPrivateGraphEndpoints)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/neptune-graph-2023-11-29/ListPrivateGraphEndpoints)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/neptune-graph-2023-11-29/ListPrivateGraphEndpoints)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/neptune-graph-2023-11-29/ListPrivateGraphEndpoints)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/neptune-graph-2023-11-29/ListPrivateGraphEndpoints)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-graph-2023-11-29/ListPrivateGraphEndpoints)
