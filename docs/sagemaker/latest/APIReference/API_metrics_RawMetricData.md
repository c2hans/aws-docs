---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_metrics_RawMetricData.html
---

# RawMetricData
<a name="API_metrics_RawMetricData"></a>

The raw metric data to associate with the resource.

## Contents
<a name="API_metrics_RawMetricData_Contents"></a>

 ** MetricName **   <a name="sagemaker-Type-metrics_RawMetricData-MetricName"></a>
The name of the metric.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `.+`
Required: Yes

 ** Timestamp **   <a name="sagemaker-Type-metrics_RawMetricData-Timestamp"></a>
The time that the metric was recorded.
Type: Timestamp
Required: Yes

 ** Value **   <a name="sagemaker-Type-metrics_RawMetricData-Value"></a>
The metric value.
Type: Double
Required: Yes

 ** Step **   <a name="sagemaker-Type-metrics_RawMetricData-Step"></a>
The metric step (epoch).
Type: Integer
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_metrics_RawMetricData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-metrics-2022-09-30/RawMetricData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-metrics-2022-09-30/RawMetricData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-metrics-2022-09-30/RawMetricData)
