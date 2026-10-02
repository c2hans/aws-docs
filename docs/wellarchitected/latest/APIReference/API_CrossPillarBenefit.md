---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_CrossPillarBenefit.html
---

# CrossPillarBenefit
<a name="API_CrossPillarBenefit"></a>

A benefit on a different pillar from acting on the recommendation.

## Contents
<a name="API_CrossPillarBenefit_Contents"></a>

 ** description **   <a name="wellarchitected-Type-CrossPillarBenefit-description"></a>
A description of what changes and why it matters.
Type: String
Length Constraints: Minimum length of 30. Maximum length of 300.
Required: Yes

 ** impact **   <a name="wellarchitected-Type-CrossPillarBenefit-impact"></a>
The severity of the benefit.
Type: String
Valid Values: `HIGH | MEDIUM | LOW`
Required: Yes

 ** pillar **   <a name="wellarchitected-Type-CrossPillarBenefit-pillar"></a>
The pillar that would be positively impacted.
Type: String
Valid Values: `COST_OPTIMIZATION | SECURITY | RESILIENCE | PERFORMANCE | OPERATIONAL_EXCELLENCE`
Required: Yes

 ** title **   <a name="wellarchitected-Type-CrossPillarBenefit-title"></a>
A short phrase describing the outcome.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 80.
Required: Yes

## See Also
<a name="API_CrossPillarBenefit_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/CrossPillarBenefit)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/CrossPillarBenefit)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/CrossPillarBenefit)
