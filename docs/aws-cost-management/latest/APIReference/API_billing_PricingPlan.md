---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_PricingPlan.html
---

# PricingPlan
<a name="API_billing_PricingPlan"></a>

A pricing plan for Enterprise Support billing.

## Contents
<a name="API_billing_PricingPlan_Contents"></a>

 ** tiers **   <a name="awscostmanagement-Type-billing_PricingPlan-tiers"></a>
The pricing tiers within this plan.
Type: Array of [PricingPlanTier](API_billing_PricingPlanTier.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: Yes

 ** description **   <a name="awscostmanagement-Type-billing_PricingPlan-description"></a>
A description of the pricing plan.
Type: String
Required: No

 ** discountAppliesToMinimumCharge **   <a name="awscostmanagement-Type-billing_PricingPlan-discountAppliesToMinimumCharge"></a>
Whether the discount applies to the minimum Support charge.
Type: Boolean
Required: No

 ** endDate **   <a name="awscostmanagement-Type-billing_PricingPlan-endDate"></a>
The end date of the pricing plan.
Type: Timestamp
Required: No

 ** minimumCharge **   <a name="awscostmanagement-Type-billing_PricingPlan-minimumCharge"></a>
The minimum Support charge amount for this pricing plan.
Type: String
Required: No

 ** name **   <a name="awscostmanagement-Type-billing_PricingPlan-name"></a>
The name of the pricing plan.
Type: String
Required: No

 ** planDiscountPercent **   <a name="awscostmanagement-Type-billing_PricingPlan-planDiscountPercent"></a>
The discount percentage applied by this pricing plan.
Type: String
Required: No

 ** pricingPlanId **   <a name="awscostmanagement-Type-billing_PricingPlan-pricingPlanId"></a>
The unique identifier for the pricing plan.
Type: String
Required: No

 ** startDate **   <a name="awscostmanagement-Type-billing_PricingPlan-startDate"></a>
The start date of the pricing plan.
Type: Timestamp
Required: No

 ** tiered **   <a name="awscostmanagement-Type-billing_PricingPlan-tiered"></a>
Whether the pricing plan uses tiered pricing.
Type: String
Required: No

## See Also
<a name="API_billing_PricingPlan_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billing-2023-09-07/PricingPlan)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billing-2023-09-07/PricingPlan)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billing-2023-09-07/PricingPlan)
