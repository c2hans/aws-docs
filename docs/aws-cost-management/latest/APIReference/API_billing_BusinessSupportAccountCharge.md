---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_BusinessSupportAccountCharge.html
---

# BusinessSupportAccountCharge
<a name="API_billing_BusinessSupportAccountCharge"></a>

Business Support charges for a linked account.

## Contents
<a name="API_billing_BusinessSupportAccountCharge_Contents"></a>

 ** accountId **   <a name="awscostmanagement-Type-billing_BusinessSupportAccountCharge-accountId"></a>
The linked account ID.
Type: String
Pattern: `[0-9]{12}`
Required: Yes

 ** supportPlanName **   <a name="awscostmanagement-Type-billing_BusinessSupportAccountCharge-supportPlanName"></a>
The Support plan name for this account. Valid values: `AWSSupportBusiness` (Business Support plan), `AWSSupportDeveloper` (Developer Support plan), `AWSSupportEssential` (Basic Support plan).
Type: String
Required: Yes

 ** totalCharge **   <a name="awscostmanagement-Type-billing_BusinessSupportAccountCharge-totalCharge"></a>
The total Business Support charge amount for this account in the billing month.
Type: String
Required: Yes

 ** totalUsageBasis **   <a name="awscostmanagement-Type-billing_BusinessSupportAccountCharge-totalUsageBasis"></a>
The total Support-eligible spend used as the basis for calculating the Business Support charge for this account.
Type: String
Required: Yes

 ** supportDiscount **   <a name="awscostmanagement-Type-billing_BusinessSupportAccountCharge-supportDiscount"></a>
The discount applied to the Business Support charge for this account, if any. This field is absent when no discount applies.
Type: [BusinessSupportDiscount](API_billing_BusinessSupportDiscount.md) object
Required: No

 ** supportEligibleSpendByService **   <a name="awscostmanagement-Type-billing_BusinessSupportAccountCharge-supportEligibleSpendByService"></a>
The Support-eligible spend broken down by contributing service for this account.
Type: Array of [BusinessSupportServiceSpend](API_billing_BusinessSupportServiceSpend.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** tierCharges **   <a name="awscostmanagement-Type-billing_BusinessSupportAccountCharge-tierCharges"></a>
The tier-level charges that make up the total Business Support charge for this account. Each tier represents a spend range with its own rate.
Type: Array of [BusinessSupportTierCharge](API_billing_BusinessSupportTierCharge.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: No

## See Also
<a name="API_billing_BusinessSupportAccountCharge_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billing-2023-09-07/BusinessSupportAccountCharge)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billing-2023-09-07/BusinessSupportAccountCharge)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billing-2023-09-07/BusinessSupportAccountCharge)
