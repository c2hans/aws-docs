---
source_url: https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_UpdateTieringInput.html
---

# UpdateTieringInput
<a name="API_UpdateTieringInput"></a>

 The set of tiering configurations for the pricing rule.

## Contents
<a name="API_UpdateTieringInput_Contents"></a>

 ** CustomTiers **   <a name="billingconductor-Type-UpdateTieringInput-CustomTiers"></a>
 The set of custom tiers for the pricing rule.
Type: Array of [CustomTier](API_CustomTier.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** FreeTier **   <a name="billingconductor-Type-UpdateTieringInput-FreeTier"></a>
 The possible AWS Free Tier configurations.
Type: [UpdateFreeTierConfig](API_UpdateFreeTierConfig.md) object
Required: No

## See Also
<a name="API_UpdateTieringInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billingconductor-2021-07-30/UpdateTieringInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billingconductor-2021-07-30/UpdateTieringInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billingconductor-2021-07-30/UpdateTieringInput)
