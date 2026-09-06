---
source_url: https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_PerformanceInsightsMetric.html
---

# PerformanceInsightsMetric
<a name="API_PerformanceInsightsMetric"></a>

This data type helps to determine Performance Insights metric to render for the insight.

## Contents
<a name="API_PerformanceInsightsMetric_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Dimensions **   <a name="performanceinsights-Type-PerformanceInsightsMetric-Dimensions"></a>
A dimension map that contains the dimensions for this partition.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 2000.
Key Pattern: `^.*$`
Value Length Constraints: Minimum length of 1. Maximum length of 2000.
Value Pattern: `^.*$`
Required: No

 ** DisplayName **   <a name="performanceinsights-Type-PerformanceInsightsMetric-DisplayName"></a>
The Performance Insights metric name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Pattern: `^.*$`
Required: No

 ** Filter **   <a name="performanceinsights-Type-PerformanceInsightsMetric-Filter"></a>
The filter for the Performance Insights metric.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 2000.
Key Pattern: `^.*$`
Value Length Constraints: Minimum length of 1. Maximum length of 2000.
Value Pattern: `^.*$`
Required: No

 ** Metric **   <a name="performanceinsights-Type-PerformanceInsightsMetric-Metric"></a>
The Performance Insights metric.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Pattern: `^.*$`
Required: No

 ** Value **   <a name="performanceinsights-Type-PerformanceInsightsMetric-Value"></a>
The value of the metric. For example, `9` for `db.load.avg`.
Type: Double
Required: No

## See Also
<a name="API_PerformanceInsightsMetric_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pi-2018-02-27/PerformanceInsightsMetric)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pi-2018-02-27/PerformanceInsightsMetric)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pi-2018-02-27/PerformanceInsightsMetric)
