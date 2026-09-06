---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_RDSDatabaseRecommendedOptionProjectedMetric.html
---

# RDSDatabaseRecommendedOptionProjectedMetric
<a name="API_RDSDatabaseRecommendedOptionProjectedMetric"></a>

 Describes the projected metrics of an Amazon Aurora and RDS database recommendation option.

 To determine the performance difference between your current Amazon Aurora and RDS database and the recommended option, compare the metric data of your service against its projected metric data.

## Contents
<a name="API_RDSDatabaseRecommendedOptionProjectedMetric_Contents"></a>

 ** projectedMetrics **   <a name="computeoptimizer-Type-RDSDatabaseRecommendedOptionProjectedMetric-projectedMetrics"></a>
 An array of objects that describe the projected metric.
Type: Array of [RDSDatabaseProjectedMetric](API_RDSDatabaseProjectedMetric.md) objects
Required: No

 ** rank **   <a name="computeoptimizer-Type-RDSDatabaseRecommendedOptionProjectedMetric-rank"></a>
 The rank identifier of the Amazon Aurora or RDS DB instance recommendation option.
Type: Integer
Required: No

 ** recommendedDBInstanceClass **   <a name="computeoptimizer-Type-RDSDatabaseRecommendedOptionProjectedMetric-recommendedDBInstanceClass"></a>
 The recommended DB instance class for the Amazon Aurora or RDS database.
Type: String
Required: No

## See Also
<a name="API_RDSDatabaseRecommendedOptionProjectedMetric_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-2019-11-01/RDSDatabaseRecommendedOptionProjectedMetric)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-2019-11-01/RDSDatabaseRecommendedOptionProjectedMetric)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-2019-11-01/RDSDatabaseRecommendedOptionProjectedMetric)
