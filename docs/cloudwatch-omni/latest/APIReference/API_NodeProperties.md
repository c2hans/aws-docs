---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_NodeProperties.html
---

# NodeProperties
<a name="API_NodeProperties"></a>

Node identity attributes promoted out of the flat attribute map onto typed members. The first four are part of the node's merge key, so a node that merged across sources reports one resolved value for each.

## Contents
<a name="API_NodeProperties_Contents"></a>

 ** category **   <a name="cloudwatchomni-Type-NodeProperties-category"></a>
What kind of thing the node is, coarser than nodeType.
Type: String
Valid Values: `GEN_AI_AGENT | GEN_AI_MODEL | DATABASE | MESSAGING_QUEUE | COMPUTE | STORAGE | NETWORK`
Required: No

 ** cloudProvider **   <a name="cloudwatchomni-Type-NodeProperties-cloudProvider"></a>
The cloud provider hosting the node, resolved from the reported provider, platform, or vendor namespace, and defaulting to "aws".
Type: String
Required: No

 ** namespace **   <a name="cloudwatchomni-Type-NodeProperties-namespace"></a>
The logical service grouping the node belongs to. This is not a metric namespace.
Type: String
Required: No

 ** region **   <a name="cloudwatchomni-Type-NodeProperties-region"></a>
The region the node runs in. Falls back to the region the telemetry was ingested from when the node does not report one.
Type: String
Required: No

 ** sourceAccountId **   <a name="cloudwatchomni-Type-NodeProperties-sourceAccountId"></a>
The account that produced the telemetry this node was discovered from.
Type: String
Required: No

 ** stage **   <a name="cloudwatchomni-Type-NodeProperties-stage"></a>
The node's deployment environment. A node may be observed in several; this is the highest-precedence one. Match any of them with NodeFilters.stage.
Type: String
Required: No

## See Also
<a name="API_NodeProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/NodeProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/NodeProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/NodeProperties)
