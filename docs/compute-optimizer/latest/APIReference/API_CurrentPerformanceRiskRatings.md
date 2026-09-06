---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_CurrentPerformanceRiskRatings.html
---

# CurrentPerformanceRiskRatings
<a name="API_CurrentPerformanceRiskRatings"></a>

Describes the performance risk ratings for a given resource type.

Resources with a `high` or `medium` rating are at risk of not meeting the performance needs of their workloads, while resources with a `low` rating are performing well in their workloads.

## Contents
<a name="API_CurrentPerformanceRiskRatings_Contents"></a>

 ** high **   <a name="computeoptimizer-Type-CurrentPerformanceRiskRatings-high"></a>
A count of the applicable resource types with a high performance risk rating.
Type: Long
Required: No

 ** low **   <a name="computeoptimizer-Type-CurrentPerformanceRiskRatings-low"></a>
A count of the applicable resource types with a low performance risk rating.
Type: Long
Required: No

 ** medium **   <a name="computeoptimizer-Type-CurrentPerformanceRiskRatings-medium"></a>
A count of the applicable resource types with a medium performance risk rating.
Type: Long
Required: No

 ** veryLow **   <a name="computeoptimizer-Type-CurrentPerformanceRiskRatings-veryLow"></a>
A count of the applicable resource types with a very low performance risk rating.
Type: Long
Required: No

## See Also
<a name="API_CurrentPerformanceRiskRatings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-2019-11-01/CurrentPerformanceRiskRatings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-2019-11-01/CurrentPerformanceRiskRatings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-2019-11-01/CurrentPerformanceRiskRatings)
