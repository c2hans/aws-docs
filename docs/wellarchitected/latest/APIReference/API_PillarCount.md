---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_PillarCount.html
---

# PillarCount
<a name="API_PillarCount"></a>

Pair of a Well-Architected pillar and the number of recommendations attributed to it in a CoverageSummary.

## Contents
<a name="API_PillarCount_Contents"></a>

 ** count **   <a name="wellarchitected-Type-PillarCount-count"></a>
Non-negative count of recommendations in the report that are attributed to this pillar.
Type: Long
Required: Yes

 ** pillar **   <a name="wellarchitected-Type-PillarCount-pillar"></a>
Well-Architected pillar this count is attributed to.
Type: String
Valid Values: `COST_OPTIMIZATION | SECURITY | RESILIENCE | PERFORMANCE | OPERATIONAL_EXCELLENCE`
Required: Yes

## See Also
<a name="API_PillarCount_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/PillarCount)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/PillarCount)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/PillarCount)
