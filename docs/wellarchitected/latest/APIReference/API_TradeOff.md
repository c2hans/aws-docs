---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_TradeOff.html
---

# TradeOff
<a name="API_TradeOff"></a>

A negative trade-off from acting on the recommendation.

## Contents
<a name="API_TradeOff_Contents"></a>

 ** description **   <a name="wellarchitected-Type-TradeOff-description"></a>
A description of the specific risk and the condition that triggers it.
Type: String
Length Constraints: Minimum length of 30. Maximum length of 450.
Required: Yes

 ** mitigation **   <a name="wellarchitected-Type-TradeOff-mitigation"></a>
A specific action to mitigate the trade-off and when to take it.
Type: String
Length Constraints: Minimum length of 30. Maximum length of 450.
Required: Yes

 ** pillar **   <a name="wellarchitected-Type-TradeOff-pillar"></a>
The pillar that could be negatively impacted.
Type: String
Valid Values: `COST_OPTIMIZATION | SECURITY | RESILIENCE | PERFORMANCE | OPERATIONAL_EXCELLENCE`
Required: Yes

 ** risk **   <a name="wellarchitected-Type-TradeOff-risk"></a>
The risk rating for the trade-off.
Type: String
Valid Values: `LOW | MEDIUM | HIGH`
Required: Yes

 ** title **   <a name="wellarchitected-Type-TradeOff-title"></a>
A short phrase describing what is lost or degraded.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 80.
Required: Yes

 ** riskExplanation **   <a name="wellarchitected-Type-TradeOff-riskExplanation"></a>
An optional explanation providing additional context for the risk rating.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 160.
Required: No

## See Also
<a name="API_TradeOff_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/TradeOff)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/TradeOff)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/TradeOff)
