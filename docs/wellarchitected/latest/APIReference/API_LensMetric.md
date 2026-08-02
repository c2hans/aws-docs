---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_LensMetric.html
---

# LensMetric
<a name="API_LensMetric"></a>

A metric for a particular lens in a workload.

## Contents
<a name="API_LensMetric_Contents"></a>

 ** LensArn **   <a name="wellarchitected-Type-LensMetric-LensArn"></a>
The lens ARN.
Type: String
Required: No

 ** Pillars **   <a name="wellarchitected-Type-LensMetric-Pillars"></a>
The metrics for the pillars in a lens.
Type: Array of [PillarMetric](API_PillarMetric.md) objects
Required: No

 ** RiskCounts **   <a name="wellarchitected-Type-LensMetric-RiskCounts"></a>
A map from risk names to the count of how many questions have that rating.
Type: String to integer map
Valid Keys: `UNANSWERED | HIGH | MEDIUM | NONE | NOT_APPLICABLE`
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_LensMetric_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/LensMetric)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/LensMetric)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/LensMetric)
