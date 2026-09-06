---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_EventSourceMappingMetricsConfig.html
---

# EventSourceMappingMetricsConfig
<a name="API_EventSourceMappingMetricsConfig"></a>

The metrics configuration for your event source. Use this configuration object to define which metrics you want your event source mapping to produce.

## Contents
<a name="API_EventSourceMappingMetricsConfig_Contents"></a>

 ** Metrics **   <a name="lambda-Type-EventSourceMappingMetricsConfig-Metrics"></a>
 The metrics you want your event source mapping to produce, including `EventCount`, `ErrorCount`, `KafkaMetrics`.
+  `EventCount` to receive metrics related to the number of events processed by your event source mapping.
+  `ErrorCount` (Amazon MSK and self-managed Apache Kafka) to receive metrics related to the number of errors in your event source mapping processing.
+  `KafkaMetrics` (Amazon MSK and self-managed Apache Kafka) to receive metrics related to the Kafka consumers from your event source mapping.
 For more information about these metrics, see [ Event source mapping metrics](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-metrics-types.html#event-source-mapping-metrics).
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 3 items.
Valid Values: `EventCount | ErrorCount | KafkaMetrics`
Required: No

## See Also
<a name="API_EventSourceMappingMetricsConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/EventSourceMappingMetricsConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/EventSourceMappingMetricsConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/EventSourceMappingMetricsConfig)
