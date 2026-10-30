---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_MilestoneBasedInvestment.html
---

# MilestoneBasedInvestment
<a name="API_billing_MilestoneBasedInvestment"></a>

An investment with a fixed value that is disbursed on a schedule. This corresponds to the `MILESTONE_BASED` investment type.

## Contents
<a name="API_billing_MilestoneBasedInvestment_Contents"></a>

 ** investmentDisbursedAt **   <a name="awscostmanagement-Type-billing_MilestoneBasedInvestment-investmentDisbursedAt"></a>
The date on which the investment is disbursed to the investment accounts.
Type: Timestamp
Required: Yes

 ** investmentId **   <a name="awscostmanagement-Type-billing_MilestoneBasedInvestment-investmentId"></a>
The identifier of the investment, as returned by `ListContractualInvestments`. This value is 1–36 characters.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Pattern: `[a-zA-Z0-9_\-]+`
Required: Yes

 ** investmentValue **   <a name="awscostmanagement-Type-billing_MilestoneBasedInvestment-investmentValue"></a>
The total value of the investment, including its currency and amount.
Type: [Amount](API_billing_Amount.md) object
Required: Yes

## See Also
<a name="API_billing_MilestoneBasedInvestment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billing-2023-09-07/MilestoneBasedInvestment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billing-2023-09-07/MilestoneBasedInvestment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billing-2023-09-07/MilestoneBasedInvestment)
