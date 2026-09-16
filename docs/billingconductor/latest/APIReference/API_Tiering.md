---
source_url: https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_Tiering.html
---

# Tiering
<a name="API_Tiering"></a>

 The set of tiering configurations for the pricing rule.

## Contents
<a name="API_Tiering_Contents"></a>

 ** CustomTiers **   <a name="billingconductor-Type-Tiering-CustomTiers"></a>
 The set of custom tiers for the pricing rule.
Type: Array of [CustomTier](API_CustomTier.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** FreeTier **   <a name="billingconductor-Type-Tiering-FreeTier"></a>
 The possible AWS Free Tier configurations.
Type: [FreeTierConfig](API_FreeTierConfig.md) object
Required: No

## See Also
<a name="API_Tiering_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billingconductor-2021-07-30/Tiering)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billingconductor-2021-07-30/Tiering)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billingconductor-2021-07-30/Tiering)
