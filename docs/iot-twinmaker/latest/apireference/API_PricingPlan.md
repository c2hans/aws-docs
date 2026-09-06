---
source_url: https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_PricingPlan.html
---

# PricingPlan
<a name="API_PricingPlan"></a>

The pricing plan.

## Contents
<a name="API_PricingPlan_Contents"></a>

 ** effectiveDateTime **   <a name="tm-Type-PricingPlan-effectiveDateTime"></a>
The effective date and time of the pricing plan.
Type: Timestamp
Required: Yes

 ** pricingMode **   <a name="tm-Type-PricingPlan-pricingMode"></a>
The pricing mode.
Type: String
Valid Values: `BASIC | STANDARD | TIERED_BUNDLE`
Required: Yes

 ** updateDateTime **   <a name="tm-Type-PricingPlan-updateDateTime"></a>
The set date and time for updating a pricing plan.
Type: Timestamp
Required: Yes

 ** updateReason **   <a name="tm-Type-PricingPlan-updateReason"></a>
The update reason for changing a pricing plan.
Type: String
Valid Values: `DEFAULT | PRICING_TIER_UPDATE | ENTITY_COUNT_UPDATE | PRICING_MODE_UPDATE | OVERWRITTEN`
Required: Yes

 ** billableEntityCount **   <a name="tm-Type-PricingPlan-billableEntityCount"></a>
The billable entity count.
Type: Long
Required: No

 ** bundleInformation **   <a name="tm-Type-PricingPlan-bundleInformation"></a>
The pricing plan's bundle information.
Type: [BundleInformation](API_BundleInformation.md) object
Required: No

## See Also
<a name="API_PricingPlan_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iottwinmaker-2021-11-29/PricingPlan)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iottwinmaker-2021-11-29/PricingPlan)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iottwinmaker-2021-11-29/PricingPlan)
