---
source_url: https://docs.aws.amazon.com/autoscaling/application/APIReference/API_PredictiveScalingMetricStat.html
---

# PredictiveScalingMetricStat
<a name="API_PredictiveScalingMetricStat"></a>

 This structure defines the CloudWatch metric to return, along with the statistic and unit.

## Contents
<a name="API_PredictiveScalingMetricStat_Contents"></a>

 ** Metric **   <a name="autoscaling-Type-PredictiveScalingMetricStat-Metric"></a>
 The CloudWatch metric to return, including the metric name, namespace, and dimensions. To get the exact metric name, namespace, and dimensions, inspect the [Metric](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_Metric.html) object that is returned by a call to [ListMetrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_ListMetrics.html).
Type: [PredictiveScalingMetric](API_PredictiveScalingMetric.md) object
Required: Yes

 ** Stat **   <a name="autoscaling-Type-PredictiveScalingMetricStat-Stat"></a>
 The statistic to return. It can include any CloudWatch statistic or extended statistic. For a list of valid values, see the table in [Statistics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Statistic) in the *Amazon CloudWatch User Guide*.
The most commonly used metrics for predictive scaling are `Average` and `Sum`.
Type: String
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: Yes

 ** Unit **   <a name="autoscaling-Type-PredictiveScalingMetricStat-Unit"></a>
 The unit to use for the returned data points. For a complete list of the units that CloudWatch supports, see the [MetricDatum](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_MetricDatum.html) data type in the *Amazon CloudWatch API Reference*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1023.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

## See Also
<a name="API_PredictiveScalingMetricStat_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-autoscaling-2016-02-06/PredictiveScalingMetricStat)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-autoscaling-2016-02-06/PredictiveScalingMetricStat)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-autoscaling-2016-02-06/PredictiveScalingMetricStat)
