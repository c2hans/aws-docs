---
source_url: https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_PerformanceInsightsReferenceComparisonValues.html
---

# PerformanceInsightsReferenceComparisonValues
<a name="API_PerformanceInsightsReferenceComparisonValues"></a>

Reference scalar values and other metrics that DevOps Guru displays on a graph in its console along with the actual metrics it analyzed. Compare these reference values to your actual metrics to help you understand anomalous behavior that DevOps Guru detected.

## Contents
<a name="API_PerformanceInsightsReferenceComparisonValues_Contents"></a>

 ** ReferenceMetric **   <a name="DevOpsGuru-Type-PerformanceInsightsReferenceComparisonValues-ReferenceMetric"></a>
A metric that DevOps Guru compares to actual metric values. This reference metric is used to determine if an actual metric should be considered anomalous.
Type: [PerformanceInsightsReferenceMetric](API_PerformanceInsightsReferenceMetric.md) object
Required: No

 ** ReferenceScalar **   <a name="DevOpsGuru-Type-PerformanceInsightsReferenceComparisonValues-ReferenceScalar"></a>
A scalar value DevOps Guru for a metric that DevOps Guru compares to actual metric values. This reference value is used to determine if an actual metric value should be considered anomalous.
Type: [PerformanceInsightsReferenceScalar](API_PerformanceInsightsReferenceScalar.md) object
Required: No

## See Also
<a name="API_PerformanceInsightsReferenceComparisonValues_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-guru-2020-12-01/PerformanceInsightsReferenceComparisonValues)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-guru-2020-12-01/PerformanceInsightsReferenceComparisonValues)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-guru-2020-12-01/PerformanceInsightsReferenceComparisonValues)
