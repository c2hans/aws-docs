---
source_url: https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_AnomalySourceDetails.html
---

# AnomalySourceDetails
<a name="API_AnomalySourceDetails"></a>

 Details about the source of the anomalous operational data that triggered the anomaly.

## Contents
<a name="API_AnomalySourceDetails_Contents"></a>

 ** CloudWatchMetrics **   <a name="DevOpsGuru-Type-AnomalySourceDetails-CloudWatchMetrics"></a>
An array of `CloudWatchMetricsDetail` objects that contain information about analyzed CloudWatch metrics that show anomalous behavior.
Type: Array of [CloudWatchMetricsDetail](API_CloudWatchMetricsDetail.md) objects
Required: No

 ** PerformanceInsightsMetrics **   <a name="DevOpsGuru-Type-AnomalySourceDetails-PerformanceInsightsMetrics"></a>
An array of `PerformanceInsightsMetricsDetail` objects that contain information about analyzed Performance Insights metrics that show anomalous behavior.
Type: Array of [PerformanceInsightsMetricsDetail](API_PerformanceInsightsMetricsDetail.md) objects
Required: No

## See Also
<a name="API_AnomalySourceDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-guru-2020-12-01/AnomalySourceDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-guru-2020-12-01/AnomalySourceDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-guru-2020-12-01/AnomalySourceDetails)
