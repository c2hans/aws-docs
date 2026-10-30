---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_Investment.html
---

# Investment
<a name="API_billing_Investment"></a>

An investment within an investment summary. This is a union in which exactly one member is set. The `milestoneBasedInvestment` member represents a fixed, scheduled investment. The `outcomeBasedInvestment` member represents an attestable investment awarded upon completion of a defined outcome. Check which member is present to determine the investment type.

## Contents
<a name="API_billing_Investment_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** milestoneBasedInvestment **   <a name="awscostmanagement-Type-billing_Investment-milestoneBasedInvestment"></a>
An investment with a fixed value that is disbursed on a schedule. This member is set for a milestone-based investment and corresponds to the `MILESTONE_BASED` investment type.
Type: [MilestoneBasedInvestment](API_billing_MilestoneBasedInvestment.md) object
Required: No

 ** outcomeBasedInvestment **   <a name="awscostmanagement-Type-billing_Investment-outcomeBasedInvestment"></a>
An investment that is awarded upon completion of a defined outcome. This member is set for an outcome-based (attestable) investment and corresponds to the `OUTCOME_BASED` investment type.
Type: [OutcomeBasedInvestment](API_billing_OutcomeBasedInvestment.md) object
Required: No

## See Also
<a name="API_billing_Investment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billing-2023-09-07/Investment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billing-2023-09-07/Investment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billing-2023-09-07/Investment)
