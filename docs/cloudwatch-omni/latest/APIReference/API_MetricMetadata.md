---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_MetricMetadata.html
---

# MetricMetadata
<a name="API_MetricMetadata"></a>

A single metric observed on a context graph node.

## Contents
<a name="API_MetricMetadata_Contents"></a>

 ** attributes **   <a name="cloudwatchomni-Type-MetricMetadata-attributes"></a>
Per-metric qualifying attributes the console uses to query this metric's telemetry. These are the RAW, store-matching values keyed by their OTel names ("service.name", "service.namespace", "cloud.provider", "cloud.account.id", "cloud.region", "instrumentation\_scope") — deliberately NOT the node's normalized/merged identity, so the query selectors match the emitted series. A merged node can carry different values per metric, which is why they live here rather than on the node.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** metricType **   <a name="cloudwatchomni-Type-MetricMetadata-metricType"></a>
OTel metric kind: "gauge", "sum", "histogram", "exponential\_histogram", or "summary" (CloudWatch-vended metrics carry the same kinds). Absent when the producer did not report one.
Type: String
Required: No

 ** name **   <a name="cloudwatchomni-Type-MetricMetadata-name"></a>
The metric name as emitted, such as "Duration".
Type: String
Required: No

 ** namespace **   <a name="cloudwatchomni-Type-MetricMetadata-namespace"></a>
DEPRECATED: read attributes["service.namespace"] instead. Retained (deprecated) for backward compatibility with existing consumers; will be removed once they migrate. The logical service grouping the metric belongs to.
Type: String
Required: No

 ** preferredStat **   <a name="cloudwatchomni-Type-MetricMetadata-preferredStat"></a>
The statistic to chart or alarm on, such as "p99" or "Sum". Free-form and frequently absent.
Type: String
Required: No

 ** semantics **   <a name="cloudwatchomni-Type-MetricMetadata-semantics"></a>
What the metric means and the unit it is reported in.
Type: [MetricSemantics](API_MetricSemantics.md) object
Required: No

## See Also
<a name="API_MetricMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/MetricMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/MetricMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/MetricMetadata)
