---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_MetricMetadata.html
---

# MetricMetadata
<a name="API_MetricMetadata"></a>

A single metric observed on a context graph node.

## Contents
<a name="API_MetricMetadata_Contents"></a>

 ** attributes **   <a name="cloudwatchomni-Type-MetricMetadata-attributes"></a>
Per-metric qualifying attributes used to query this metric's telemetry. Keys are the metric store's own label names, not bare OTel attribute names: service identity arrives as "@resource.service.name" and "@resource.service.namespace", and the instrumentation scope as "@instrumentation.@name", while span-derived metrics label the service as a bare "service.name". Cloud provider, account and region are not repeated per metric — read those from the node. Values are RAW, deliberately NOT the node's normalized or merged identity, so a selector built from them matches the emitted series. A merged node can carry different values per metric, which is why these live here rather than on the node.
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
