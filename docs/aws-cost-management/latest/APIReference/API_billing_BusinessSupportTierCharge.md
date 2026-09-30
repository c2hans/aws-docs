---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_BusinessSupportTierCharge.html
---

# BusinessSupportTierCharge
<a name="API_billing_BusinessSupportTierCharge"></a>

A tier-level charge within a Business Support pricing plan. Business Support uses tiered pricing where different percentage rates apply to different ranges of Support-eligible spend.

## Contents
<a name="API_billing_BusinessSupportTierCharge_Contents"></a>

 ** tierCharge **   <a name="awscostmanagement-Type-billing_BusinessSupportTierCharge-tierCharge"></a>
The Business Support charge amount calculated for this pricing tier.
Type: String
Required: Yes

 ** tierDescription **   <a name="awscostmanagement-Type-billing_BusinessSupportTierCharge-tierDescription"></a>
A human-readable description of the pricing tier, including the spend range and percentage rate applied.
Type: String
Required: Yes

 ** tierRate **   <a name="awscostmanagement-Type-billing_BusinessSupportTierCharge-tierRate"></a>
The percentage rate applied to Support-eligible spend within this pricing tier.
Type: String
Required: Yes

 ** usageSlice **   <a name="awscostmanagement-Type-billing_BusinessSupportTierCharge-usageSlice"></a>
The amount of Support-eligible spend that falls within this pricing tier.
Type: String
Required: Yes

 ** chargePeriodEndDate **   <a name="awscostmanagement-Type-billing_BusinessSupportTierCharge-chargePeriodEndDate"></a>
The end date of the charge period for this tier charge.
Type: Timestamp
Required: No

 ** chargePeriodStartDate **   <a name="awscostmanagement-Type-billing_BusinessSupportTierCharge-chargePeriodStartDate"></a>
The start date of the charge period for this tier charge.
Type: Timestamp
Required: No

## See Also
<a name="API_billing_BusinessSupportTierCharge_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billing-2023-09-07/BusinessSupportTierCharge)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billing-2023-09-07/BusinessSupportTierCharge)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billing-2023-09-07/BusinessSupportTierCharge)
