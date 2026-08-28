---
source_url: https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_GetGraphSummary.html
---

# GetGraphSummary
<a name="API_GetGraphSummary"></a>

Gets a graph summary for a property graph.

## Request Syntax
<a name="API_GetGraphSummary_RequestSyntax"></a>

```
GET /summary?mode={{mode}} HTTP/1.1
graphIdentifier: {{graphIdentifier}}
```

## URI Request Parameters
<a name="API_GetGraphSummary_RequestParameters"></a>

The request uses the following URI parameters.

 ** [graphIdentifier](#API_GetGraphSummary_RequestSyntax) **   <a name="neptunegraph-GetGraphSummary-request-graphIdentifier"></a>
The unique identifier of the Neptune Analytics graph.
Pattern: `g-[a-z0-9]{10}`
Required: Yes

 ** [mode](#API_GetGraphSummary_RequestSyntax) **   <a name="neptunegraph-GetGraphSummary-request-uri-mode"></a>
The summary mode can take one of two values: `basic` (the default), and `detailed`.
Valid Values: `BASIC | DETAILED`

## Request Body
<a name="API_GetGraphSummary_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetGraphSummary_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "graphSummary": {
      "edgeLabels": [ "string" ],
      "edgeProperties": [
         {
            "string" : number
         }
      ],
      "edgeStructures": [
         {
            "count": number,
            "edgeProperties": [ "string" ]
         }
      ],
      "nodeLabels": [ "string" ],
      "nodeProperties": [
         {
            "string" : number
         }
      ],
      "nodeStructures": [
         {
            "count": number,
            "distinctOutgoingEdgeLabels": [ "string" ],
            "nodeProperties": [ "string" ]
         }
      ],
      "numEdgeLabels": number,
      "numEdgeProperties": number,
      "numEdges": number,
      "numNodeLabels": number,
      "numNodeProperties": number,
      "numNodes": number,
      "totalEdgePropertyValues": number,
      "totalNodePropertyValues": number
   },
   "lastStatisticsComputationTime": "string",
   "version": "string"
}
```

## Response Elements
<a name="API_GetGraphSummary_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [graphSummary](#API_GetGraphSummary_ResponseSyntax) **   <a name="neptunegraph-GetGraphSummary-response-graphSummary"></a>
The graph summary.
Type: [GraphDataSummary](API_GraphDataSummary.md) object

 ** [lastStatisticsComputationTime](#API_GetGraphSummary_ResponseSyntax) **   <a name="neptunegraph-GetGraphSummary-response-lastStatisticsComputationTime"></a>
The timestamp, in ISO 8601 format, of the time at which Neptune Analytics last computed statistics.
Type: Timestamp

 ** [version](#API_GetGraphSummary_ResponseSyntax) **   <a name="neptunegraph-GetGraphSummary-response-version"></a>
Display the version of this tool.
Type: String

## Errors
<a name="API_GetGraphSummary_Errors"></a>

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
<a name="API_GetGraphSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/neptune-graph-2023-11-29/GetGraphSummary)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/neptune-graph-2023-11-29/GetGraphSummary)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-graph-2023-11-29/GetGraphSummary)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/neptune-graph-2023-11-29/GetGraphSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-graph-2023-11-29/GetGraphSummary)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/neptune-graph-2023-11-29/GetGraphSummary)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/neptune-graph-2023-11-29/GetGraphSummary)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/neptune-graph-2023-11-29/GetGraphSummary)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/neptune-graph-2023-11-29/GetGraphSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-graph-2023-11-29/GetGraphSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for NeptuneAnalyticsAPI. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune-analytics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
