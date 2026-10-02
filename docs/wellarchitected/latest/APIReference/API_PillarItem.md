---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_PillarItem.html
---

# PillarItem
<a name="API_PillarItem"></a>

Item configuration for a specific AWS Well-Architected Framework pillar.

## Contents
<a name="API_PillarItem_Contents"></a>

 ** ids **   <a name="wellarchitected-Type-PillarItem-ids"></a>
A list of item IDs to process for this pillar, such as best practice IDs, AWS service names, or resource ARNs.
Type: Array of strings
Array Members: Minimum number of 1 item.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** pillar **   <a name="wellarchitected-Type-PillarItem-pillar"></a>
The pillar this item configuration applies to.
Type: String
Valid Values: `COST_OPTIMIZATION | SECURITY | RESILIENCE | PERFORMANCE | OPERATIONAL_EXCELLENCE`
Required: Yes

## See Also
<a name="API_PillarItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/PillarItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/PillarItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/PillarItem)
