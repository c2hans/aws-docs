---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_InvestmentSummary.html
---

# InvestmentSummary
<a name="API_billing_InvestmentSummary"></a>

Detailed information about an investment summary within a contract or a private pricing addendum.

## Contents
<a name="API_billing_InvestmentSummary_Contents"></a>

 ** investmentName **   <a name="awscostmanagement-Type-billing_InvestmentSummary-investmentName"></a>
The name of the investment summary, used to reference the investment against a term in the physical contract. This value is 1–400 characters.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 400.
Required: Yes

 ** investmentSummaryId **   <a name="awscostmanagement-Type-billing_InvestmentSummary-investmentSummaryId"></a>
The identifier of the investment summary. Pass this value to `ListContractualInvestments` to list the investments within the summary, and to `CreateContractualInvestmentAttestation` to attest an investment. This value is 1–36 characters.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Pattern: `[a-zA-Z0-9_\-]+`
Required: Yes

 ** investmentType **   <a name="awscostmanagement-Type-billing_InvestmentSummary-investmentType"></a>
The type of the investment summary. Valid values are `MILESTONE_BASED` and `OUTCOME_BASED`. `OUTCOME_BASED` investments can be attested to, upon completion of outcomes. `MILESTONE_BASED` are automatically triggered by AWS, based on the time schedule in the contract.
Type: String
Valid Values: `MILESTONE_BASED | OUTCOME_BASED`
Required: Yes

 ** maxAllowedInvestmentDisbursementValue **   <a name="awscostmanagement-Type-billing_InvestmentSummary-maxAllowedInvestmentDisbursementValue"></a>
The maximum monetary value that can be disbursed against the investment summary, inclusive of all outcomes combined under the summary.
Type: [Amount](API_billing_Amount.md) object
Required: No

## See Also
<a name="API_billing_InvestmentSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billing-2023-09-07/InvestmentSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billing-2023-09-07/InvestmentSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billing-2023-09-07/InvestmentSummary)
