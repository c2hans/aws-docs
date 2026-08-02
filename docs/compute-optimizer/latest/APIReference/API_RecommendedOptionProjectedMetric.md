---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_RecommendedOptionProjectedMetric.html
---

# RecommendedOptionProjectedMetric
<a name="API_RecommendedOptionProjectedMetric"></a>

Describes a projected utilization metric of a recommendation option.

**Note**
The `Cpu` and `Memory` metrics are the only projected utilization metrics returned when you run the [GetEC2RecommendationProjectedMetrics](API_GetEC2RecommendationProjectedMetrics.md) action. Additionally, the `Memory` metric is returned only for resources that have the unified CloudWatch agent installed on them. For more information, see [Enabling Memory Utilization with the CloudWatch Agent](https://docs.aws.amazon.com/compute-optimizer/latest/ug/metrics.html#cw-agent).

## Contents
<a name="API_RecommendedOptionProjectedMetric_Contents"></a>

 ** projectedMetrics **   <a name="computeoptimizer-Type-RecommendedOptionProjectedMetric-projectedMetrics"></a>
An array of objects that describe a projected utilization metric.
Type: Array of [ProjectedMetric](API_ProjectedMetric.md) objects
Required: No

 ** rank **   <a name="computeoptimizer-Type-RecommendedOptionProjectedMetric-rank"></a>
The rank of the recommendation option projected metric.
The top recommendation option is ranked as `1`.
The projected metric rank correlates to the recommendation option rank. For example, the projected metric ranked as `1` is related to the recommendation option that is also ranked as `1` in the same response.
Type: Integer
Required: No

 ** recommendedInstanceType **   <a name="computeoptimizer-Type-RecommendedOptionProjectedMetric-recommendedInstanceType"></a>
The recommended instance type.
Type: String
Required: No

## See Also
<a name="API_RecommendedOptionProjectedMetric_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-2019-11-01/RecommendedOptionProjectedMetric)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-2019-11-01/RecommendedOptionProjectedMetric)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-2019-11-01/RecommendedOptionProjectedMetric)
