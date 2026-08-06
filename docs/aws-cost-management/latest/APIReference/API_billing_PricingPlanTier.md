---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_PricingPlanTier.html
---

# PricingPlanTier
<a name="API_billing_PricingPlanTier"></a>

A tier within an Enterprise Support pricing plan.

## Contents
<a name="API_billing_PricingPlanTier_Contents"></a>

 ** additionalPercentageOfAggregateCharges **   <a name="awscostmanagement-Type-billing_PricingPlanTier-additionalPercentageOfAggregateCharges"></a>
The additional percentage applied to aggregate charges in this tier.
Type: String
Required: Yes

 ** aggregateChargesAdjustment **   <a name="awscostmanagement-Type-billing_PricingPlanTier-aggregateChargesAdjustment"></a>
The adjustment applied to aggregate charges.
Type: String
Required: Yes

 ** baseCharge **   <a name="awscostmanagement-Type-billing_PricingPlanTier-baseCharge"></a>
The base charge for this tier.
Type: String
Required: Yes

 ** incremental **   <a name="awscostmanagement-Type-billing_PricingPlanTier-incremental"></a>
Whether the tier charges are calculated incrementally.
Type: Boolean
Required: Yes

 ** tierMinimum **   <a name="awscostmanagement-Type-billing_PricingPlanTier-tierMinimum"></a>
The minimum spend threshold for this tier.
Type: String
Required: Yes

 ** increment **   <a name="awscostmanagement-Type-billing_PricingPlanTier-increment"></a>
The increment amount for incremental tier calculations.
Type: String
Required: No

 ** incrementCharge **   <a name="awscostmanagement-Type-billing_PricingPlanTier-incrementCharge"></a>
The charge per increment.
Type: String
Required: No

 ** tierMaximum **   <a name="awscostmanagement-Type-billing_PricingPlanTier-tierMaximum"></a>
The maximum spend threshold for this tier.
Type: String
Required: No

## See Also
<a name="API_billing_PricingPlanTier_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billing-2023-09-07/PricingPlanTier)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billing-2023-09-07/PricingPlanTier)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billing-2023-09-07/PricingPlanTier)
