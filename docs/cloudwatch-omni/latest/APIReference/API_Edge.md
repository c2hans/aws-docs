---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_Edge.html
---

# Edge
<a name="API_Edge"></a>

A directed edge in the context graph connecting two nodes.

## Contents
<a name="API_Edge_Contents"></a>

 ** edgeId **   <a name="cloudwatchomni-Type-Edge-edgeId"></a>
The unique identifier of the edge within the context graph.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** edgeProperties **   <a name="cloudwatchomni-Type-Edge-edgeProperties"></a>
Attributes promoted out of the flat attribute map onto typed members. Which members are present depends on what produced the edge.
Type: [EdgeProperties](API_EdgeProperties.md) object
Required: No

 ** edgeType **   <a name="cloudwatchomni-Type-Edge-edgeType"></a>
The kind of relationship the edge represents.
Type: String
Valid Values: `CALLS | ACCESSES | RUNS_ON`
Required: No

 ** firstObservedAt **   <a name="cloudwatchomni-Type-Edge-firstObservedAt"></a>
When this edge was first observed (UTC), at minute granularity. For an edge that merged across sources, this is the earliest value any source reported.
Type: Timestamp
Required: No

 ** from **   <a name="cloudwatchomni-Type-Edge-from"></a>
The node identifier the edge originates from.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** lastObservedAt **   <a name="cloudwatchomni-Type-Edge-lastObservedAt"></a>
When this edge was most recently observed (UTC), at minute granularity. For an edge that merged across sources, this is the latest value any source reported.
Type: Timestamp
Required: No

 ** metadata **   <a name="cloudwatchomni-Type-Edge-metadata"></a>
Descriptive metadata about the edge. Present only when the request sets includeMetadata.
Type: [Metadata](API_Metadata.md) object
Required: No

 ** operations **   <a name="cloudwatchomni-Type-Edge-operations"></a>
The operations observed on this edge.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** signalTypes **   <a name="cloudwatchomni-Type-Edge-signalTypes"></a>
The kinds of telemetry signal observed on this edge.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Valid Values: `LOGS | METRICS | TRACES | CONFIG | UNKNOWN`
Required: No

 ** sources **   <a name="cloudwatchomni-Type-Edge-sources"></a>
The discovery sources that contributed this edge.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Valid Values: `VPC_FLOW_LOG | CLOUDTRAIL | IAM_POLICY | CODE_SEMANTICS | TELEMETRY | AZURE_VNET_FLOW_LOG | ELB_ACCESS_LOG | CLOUDFRONT_ACCESS_LOG | S3_ACCESS_LOG | WAF_ACCESS_LOG | AWS_INTEGRATION | CONFIG`
Required: No

 ** telemetryAttributes **   <a name="cloudwatchomni-Type-Edge-telemetryAttributes"></a>
The edge's OpenTelemetry (OTel) attributes, as emitted by telemetry. A key promoted onto an `edgeProperties` member is removed here, so no value appears twice.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 100 items.
Required: No

 ** to **   <a name="cloudwatchomni-Type-Edge-to"></a>
The node identifier the edge points to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_Edge_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/Edge)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/Edge)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/Edge)
