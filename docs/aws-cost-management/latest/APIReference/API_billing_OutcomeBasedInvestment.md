---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_OutcomeBasedInvestment.html
---

# OutcomeBasedInvestment
<a name="API_billing_OutcomeBasedInvestment"></a>

An investment that is awarded upon completion of a defined outcome. This corresponds to the `OUTCOME_BASED` investment type and is claimed through `CreateContractualInvestmentAttestation`.

## Contents
<a name="API_billing_OutcomeBasedInvestment_Contents"></a>

 ** attestationWindow **   <a name="awscostmanagement-Type-billing_OutcomeBasedInvestment-attestationWindow"></a>
The time window, expressed as an interval with inclusive start and end dates, during which outcomes can be attested to.
Type: [Interval](API_billing_Interval.md) object
Required: Yes

 ** disbursedValue **   <a name="awscostmanagement-Type-billing_OutcomeBasedInvestment-disbursedValue"></a>
The total value already disbursed against the investment. This value can be distributed among the investment accounts distribution.
Type: [Amount](API_billing_Amount.md) object
Required: Yes

 ** investmentId **   <a name="awscostmanagement-Type-billing_OutcomeBasedInvestment-investmentId"></a>
The identifier of the investment, as returned by `ListContractualInvestments`. This value is 1–36 characters.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Pattern: `[a-zA-Z0-9_\-]+`
Required: Yes

 ** outcomeDescription **   <a name="awscostmanagement-Type-billing_OutcomeBasedInvestment-outcomeDescription"></a>
The description of what must be completed to attest the outcome. This value is 1–2048 characters.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** investmentMultipliers **   <a name="awscostmanagement-Type-billing_OutcomeBasedInvestment-investmentMultipliers"></a>
The multipliers used to compute the investment value from the attestation input. The list contains at most 200 multipliers. Multipliers are derived from the terms of the private pricing contract.
Type: Array of [InvestmentMultiplier](API_billing_InvestmentMultiplier.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

 ** investmentRestrictions **   <a name="awscostmanagement-Type-billing_OutcomeBasedInvestment-investmentRestrictions"></a>
The restrictions that cap the value that can be disbursed for the investment. The list contains at most 10 restrictions.
Type: Array of [InvestmentRestriction](API_billing_InvestmentRestriction.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

## See Also
<a name="API_billing_OutcomeBasedInvestment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billing-2023-09-07/OutcomeBasedInvestment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billing-2023-09-07/OutcomeBasedInvestment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billing-2023-09-07/OutcomeBasedInvestment)
