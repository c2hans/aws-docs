---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_PrivatePricingAddendum.html
---

# PrivatePricingAddendum
<a name="API_billing_PrivatePricingAddendum"></a>

The details of a private pricing addendum contract.

## Contents
<a name="API_billing_PrivatePricingAddendum_Contents"></a>

 ** contractArn **   <a name="awscostmanagement-Type-billing_PrivatePricingAddendum-contractArn"></a>
The Amazon Resource Name (ARN) of the private pricing addendum.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Pattern: `arn:aws[a-z-]*:billing::[0-9]{12}:contract/[a-zA-Z0-9_\+=\.\@-]{0,70}[a-zA-Z0-9]`
Required: Yes

 ** contractTerm **   <a name="awscostmanagement-Type-billing_PrivatePricingAddendum-contractTerm"></a>
The contract term period of the private pricing addendum, expressed as an interval with an inclusive start date and an inclusive end date.
Type: [Interval](API_billing_Interval.md) object
Required: Yes

 ** eligiblePayerAccounts **   <a name="awscostmanagement-Type-billing_PrivatePricingAddendum-eligiblePayerAccounts"></a>
The payer accounts that are eligible under the private pricing addendum. The list contains at most 100 account IDs.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Pattern: `[0-9]{12}`
Required: Yes

 ** investmentAccounts **   <a name="awscostmanagement-Type-billing_PrivatePricingAddendum-investmentAccounts"></a>
The accounts that are eligible to receive investments under the private pricing addendum. An `InvestmentDistribution` must target one of these accounts. The list contains at most 100 account IDs.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Pattern: `[0-9]{12}`
Required: Yes

 ** legalEntities **   <a name="awscostmanagement-Type-billing_PrivatePricingAddendum-legalEntities"></a>
The legal entities on the private pricing addendum. The list contains at most 10 legal entities.
Type: Array of [LegalEntity](API_billing_LegalEntity.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: Yes

 ** contractRestrictions **   <a name="awscostmanagement-Type-billing_PrivatePricingAddendum-contractRestrictions"></a>
The restrictions that limit the self-service actions you can take on the private pricing addendum. An empty or absent value indicates that no restrictions apply. The list contains at most 10 restrictions.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Valid Values: `ATTESTATION_SELF_SERVICE_BLOCKED`
Required: No

## See Also
<a name="API_billing_PrivatePricingAddendum_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billing-2023-09-07/PrivatePricingAddendum)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billing-2023-09-07/PrivatePricingAddendum)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billing-2023-09-07/PrivatePricingAddendum)
