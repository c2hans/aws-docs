---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_GetContextGraph.html
---

# GetContextGraph
<a name="API_GetContextGraph"></a>

Queries the context graph with filtering, traversal, and pagination support.

Pagination note: nodes and edges are returned together as a coherent subgraph. Pagination cursors advance over nodes (the primary collection); each page includes all edges connecting nodes within that page. Callers should treat nodes as the paginated collection and edges as supplementary relationship data attached to those nodes.

## Request Parameters
<a name="API_GetContextGraph_RequestParameters"></a>

 ** depth **
How many hops to traverse out from the nodes matched by nodeFilters. 0 returns only the matched nodes themselves.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 3.
Required: No

 ** edgeFilters **
Criteria restricting which edges are returned.
Type: [EdgeFilters](API_EdgeFilters.md) object
Required: No

 ** endTime **
End of the time range (UTC), inclusive.
Type: Timestamp
Required: Yes

 ** includeMetadata **
Whether to return the metadata block, semantics included, on each node and edge. Off by default because it costs an extra lookup per returned node.
Type: Boolean
Required: No

 ** maxEdgesPerNode **
The maximum number of edges to return per node, bounding the fan-out of a densely connected node.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** maxResults **
The maximum number of nodes to return in a single page.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** nextToken **
Pagination token from a previous response, to retrieve the next page.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** nodeFilters **
Criteria restricting which nodes are returned.
Type: [NodeFilters](API_NodeFilters.md) object
Required: No

 ** startTime **
Start of the time range (UTC), inclusive.
Type: Timestamp
Required: Yes

## Response Elements
<a name="API_GetContextGraph_ResponseElements"></a>

The following elements are returned by the service.

 ** nextToken **
Pagination token for the next page; absent when there are no more results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** nodes **
The page of nodes matching the request. This is the paginated collection.
Type: Array of [Node](API_Node.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1000 items.

## Errors
<a name="API_GetContextGraph_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The caller is not authorized to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error occurred while processing the request.
 ** errorCode **
The error code associated with the internal error.
HTTP Status Code: 500

 ** ThrottlingException **
The request was throttled due to exceeding the allowed request rate.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request. Not always present.
HTTP Status Code: 429

 ** ValidationException **
A parameter is specified incorrectly.
 ** errorCode **
The error code associated with the validation failure.
HTTP Status Code: 400

## Examples
<a name="API_GetContextGraph_Examples"></a>

### Query a service and its immediate dependencies
<a name="API_GetContextGraph_Example_1"></a>

The following example returns context graph nodes matching the filter and traverses one hop out to their direct dependencies, over a one-hour window. Payloads are shown as JSON; on the wire they are CBOR-encoded.

#### Sample Request
<a name="API_GetContextGraph_Example_1_Request"></a>

```
{
  "depth": 1,
  "endTime": "2026-09-16T01:00:00Z",
  "includeMetadata": false,
  "maxResults": 100,
  "nodeFilters": {
    "namespace": [
      "ecommerce"
    ],
    "nodeType": "SERVICE"
  },
  "startTime": "2026-09-16T00:00:00Z"
}
```

#### Sample Response
<a name="API_GetContextGraph_Example_1_Response"></a>

```
{
  "nextToken": "eyJvZmZzZXQiOjEwMH0=",
  "nodes": [
    {
      "edges": [
        {
          "edgeId": "edge:checkout-service->payments-service",
          "edgeType": "CALLS",
          "firstObservedAt": "2026-09-16T00:03:00Z",
          "from": "svc:checkout-service",
          "lastObservedAt": "2026-09-16T00:58:00Z",
          "operations": [
            "POST /charges"
          ],
          "signalTypes": [
            "TRACES"
          ],
          "sources": [
            "TELEMETRY"
          ],
          "to": "svc:payments-service"
        }
      ],
      "firstObservedAt": "2026-09-16T00:03:00Z",
      "lastObservedAt": "2026-09-16T00:58:00Z",
      "name": "checkout-service",
      "nodeId": "svc:checkout-service",
      "nodeProperties": {
        "cloudProvider": "aws",
        "namespace": "ecommerce",
        "region": "us-east-1",
        "sourceAccountId": "123456789012"
      },
      "nodeType": "SERVICE",
      "signalTypes": [
        "TRACES"
      ],
      "sources": [
        "TELEMETRY"
      ]
    },
    {
      "firstObservedAt": "2026-09-16T00:01:00Z",
      "lastObservedAt": "2026-09-16T00:59:00Z",
      "name": "payments-service",
      "nodeId": "svc:payments-service",
      "nodeProperties": {
        "cloudProvider": "aws",
        "namespace": "ecommerce",
        "region": "us-east-1",
        "sourceAccountId": "123456789012"
      },
      "nodeType": "SERVICE",
      "signalTypes": [
        "TRACES"
      ],
      "sources": [
        "TELEMETRY"
      ]
    }
  ]
}
```

## See Also
<a name="API_GetContextGraph_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudwatchomni-2025-01-01/GetContextGraph)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudwatchomni-2025-01-01/GetContextGraph)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/GetContextGraph)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudwatchomni-2025-01-01/GetContextGraph)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/GetContextGraph)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudwatchomni-2025-01-01/GetContextGraph)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudwatchomni-2025-01-01/GetContextGraph)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudwatchomni-2025-01-01/GetContextGraph)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cloudwatchomni-2025-01-01/GetContextGraph)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/GetContextGraph)
