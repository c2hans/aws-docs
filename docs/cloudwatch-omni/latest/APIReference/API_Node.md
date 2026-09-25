---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_Node.html
---

# Node
<a name="API_Node"></a>

A node in the context graph representing a service, resource, or remote service.

## Contents
<a name="API_Node_Contents"></a>

 ** alternateNames **   <a name="cloudwatchomni-Type-Node-alternateNames"></a>
Other names this node was observed under. A node that merged across sources reports one resolved name, and the names it was merged away from appear here.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** edges **   <a name="cloudwatchomni-Type-Node-edges"></a>
Outbound edges originating from this node. Each edge carries its `from`.
Type: Array of [Edge](API_Edge.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5000 items.
Required: No

 ** firstObservedAt **   <a name="cloudwatchomni-Type-Node-firstObservedAt"></a>
When this node was first observed (UTC), at minute granularity. For a node that merged across sources, this is the earliest value any source reported.
Type: Timestamp
Required: No

 ** lastObservedAt **   <a name="cloudwatchomni-Type-Node-lastObservedAt"></a>
When this node was most recently observed (UTC), at minute granularity. For a node that merged across sources, this is the latest value any source reported.
Type: Timestamp
Required: No

 ** metadata **   <a name="cloudwatchomni-Type-Node-metadata"></a>
Descriptive metadata about the node. Present only when the request sets includeMetadata.
Type: [Metadata](API_Metadata.md) object
Required: No

 ** name **   <a name="cloudwatchomni-Type-Node-name"></a>
The primary display name of the node.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** nodeId **   <a name="cloudwatchomni-Type-Node-nodeId"></a>
The unique identifier of the node within the context graph.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** nodeProperties **   <a name="cloudwatchomni-Type-Node-nodeProperties"></a>
Identity attributes promoted out of the flat attribute map onto typed members.
Type: [NodeProperties](API_NodeProperties.md) object
Required: No

 ** nodeType **   <a name="cloudwatchomni-Type-Node-nodeType"></a>
Whether the node is a service, a resource, or a remote service.
Type: String
Valid Values: `SERVICE | RESOURCE | REMOTE_SERVICE`
Required: No

 ** operationDetails **   <a name="cloudwatchomni-Type-Node-operationDetails"></a>
The operations observed on this node, keyed by operation name. Each value lists the dimension sets that identify the metric series for that operation.
Type: String to array of string to string maps map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 256.
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 256.
Value Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** signalTypes **   <a name="cloudwatchomni-Type-Node-signalTypes"></a>
The kinds of telemetry signal observed on this node.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Valid Values: `LOGS | METRICS | TRACES | CONFIG | UNKNOWN`
Required: No

 ** sources **   <a name="cloudwatchomni-Type-Node-sources"></a>
The discovery sources that contributed this node.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Valid Values: `VPC_FLOW_LOG | CLOUDTRAIL | IAM_POLICY | CODE_SEMANTICS | TELEMETRY | AZURE_VNET_FLOW_LOG | ELB_ACCESS_LOG | CLOUDFRONT_ACCESS_LOG | S3_ACCESS_LOG | WAF_ACCESS_LOG | AWS_INTEGRATION | CONFIG`
Required: No

 ** tags **   <a name="cloudwatchomni-Type-Node-tags"></a>
The tags observed on the underlying resource.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** telemetryAttributes **   <a name="cloudwatchomni-Type-Node-telemetryAttributes"></a>
The node's OpenTelemetry (OTel) attributes, as emitted by telemetry — the raw values, as opposed to the normalized `nodeProperties`. A key promoted onto a `nodeProperties` member is removed here, so no value appears twice.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 100 items.
Required: No

## See Also
<a name="API_Node_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/Node)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/Node)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/Node)
