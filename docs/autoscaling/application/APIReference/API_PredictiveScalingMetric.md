---
source_url: https://docs.aws.amazon.com/autoscaling/application/APIReference/API_PredictiveScalingMetric.html
---

# PredictiveScalingMetric
<a name="API_PredictiveScalingMetric"></a>

 Describes the scaling metric.

## Contents
<a name="API_PredictiveScalingMetric_Contents"></a>

 ** Dimensions **   <a name="autoscaling-Type-PredictiveScalingMetric-Dimensions"></a>
 Describes the dimensions of the metric.
Type: Array of [PredictiveScalingMetricDimension](API_PredictiveScalingMetricDimension.md) objects
Required: No

 ** MetricName **   <a name="autoscaling-Type-PredictiveScalingMetric-MetricName"></a>
 The name of the metric.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** Namespace **   <a name="autoscaling-Type-PredictiveScalingMetric-Namespace"></a>
 The namespace of the metric.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

## See Also
<a name="API_PredictiveScalingMetric_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-autoscaling-2016-02-06/PredictiveScalingMetric)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-autoscaling-2016-02-06/PredictiveScalingMetric)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-autoscaling-2016-02-06/PredictiveScalingMetric)
