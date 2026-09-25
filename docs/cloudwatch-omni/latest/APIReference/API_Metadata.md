---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_Metadata.html
---

# Metadata
<a name="API_Metadata"></a>

Descriptive information about a context graph node or edge, as opposed to its identity and structure. Returned only when the request sets includeMetadata.

## Contents
<a name="API_Metadata_Contents"></a>

 ** logs **   <a name="cloudwatchomni-Type-Metadata-logs"></a>
Per-signal LOGS query selectors: a LIST of blocks the console ORs, each an AND of exact store column -> raw values. Node-level (edges carry only traces). Populated when the request sets includeMetadata; derived labels (logSourceType) are added by the service projection, not stored here.
Type: Array of [LogMetadata](API_LogMetadata.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** metrics **   <a name="cloudwatchomni-Type-Metadata-metrics"></a>
The metrics observed on the element.
Type: Array of [MetricMetadata](API_MetricMetadata.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** semantics **   <a name="cloudwatchomni-Type-Metadata-semantics"></a>
Semantic description of the node. Absent on an edge, because semantics describe a service rather than a relationship.
Type: [NodeSemantics](API_NodeSemantics.md) object
Required: No

 ** traces **   <a name="cloudwatchomni-Type-Metadata-traces"></a>
Per-signal TRACES query selectors (same block shape as logs). Present on both node and edge metadata. serviceName is derived at the service projection, not stored here.
Type: Array of [TraceMetadata](API_TraceMetadata.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

## See Also
<a name="API_Metadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/Metadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/Metadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/Metadata)
