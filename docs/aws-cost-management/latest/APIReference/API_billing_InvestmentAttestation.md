---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_InvestmentAttestation.html
---

# InvestmentAttestation
<a name="API_billing_InvestmentAttestation"></a>

A summary of a submitted investment attestation, as returned by `ListContractualInvestmentAttestations`.

## Contents
<a name="API_billing_InvestmentAttestation_Contents"></a>

 ** attestationId **   <a name="awscostmanagement-Type-billing_InvestmentAttestation-attestationId"></a>
The identifier of the attestation. This value is returned by `CreateContractualInvestmentAttestation` and is used to cancel the attestation with `CancelContractualInvestmentAttestation`. This value is 1–36 characters.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Pattern: `[a-zA-Z0-9_\-]+`
Required: Yes

 ** attestationStatus **   <a name="awscostmanagement-Type-billing_InvestmentAttestation-attestationStatus"></a>
The current status of the attestation. Valid values are `PENDING_REVIEW`, `PENDING_C_LEVEL_APPROVAL`, `PENDING_CANCELLATION`, `REJECTED`, `CANCELLED`, and `DISBURSED`. The values `DISBURSED`, `REJECTED`, and `CANCELLED` are terminal. The other values indicate the attestation is still in progress.
Type: String
Valid Values: `PENDING_REVIEW | PENDING_C_LEVEL_APPROVAL | PENDING_CANCELLATION | REJECTED | CANCELLED | DISBURSED`
Required: Yes

 ** attestedAt **   <a name="awscostmanagement-Type-billing_InvestmentAttestation-attestedAt"></a>
The date on which the attestation was submitted.
Type: Timestamp
Required: Yes

 ** investmentId **   <a name="awscostmanagement-Type-billing_InvestmentAttestation-investmentId"></a>
The identifier of the investment that was attested, as returned by `ListContractualInvestments`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Pattern: `[a-zA-Z0-9_\-]+`
Required: Yes

 ** investmentName **   <a name="awscostmanagement-Type-billing_InvestmentAttestation-investmentName"></a>
The name of the investment summary that contains the attested outcome. This value is 1–400 characters.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 400.
Required: Yes

 ** investmentSummaryId **   <a name="awscostmanagement-Type-billing_InvestmentAttestation-investmentSummaryId"></a>
The identifier of the investment summary that was attested, as returned by `ListContractualInvestmentSummaries`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Pattern: `[a-zA-Z0-9_\-]+`
Required: Yes

 ** outcomeDescription **   <a name="awscostmanagement-Type-billing_InvestmentAttestation-outcomeDescription"></a>
The description of the attested outcome. This value is 1–2048 characters.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** updatedAt **   <a name="awscostmanagement-Type-billing_InvestmentAttestation-updatedAt"></a>
The date on which the attestation was last updated.
Type: Timestamp
Required: Yes

 ** attestedValue **   <a name="awscostmanagement-Type-billing_InvestmentAttestation-attestedValue"></a>
The monetary value attested.
Type: [Amount](API_billing_Amount.md) object
Required: No

 ** investmentDisbursedAt **   <a name="awscostmanagement-Type-billing_InvestmentAttestation-investmentDisbursedAt"></a>
The start date on which the investment is disbursed to the investment accounts. This is not the same as the time of disbursement, but reflects the date you submitted with the attestation.
Type: Timestamp
Required: No

 ** investmentDistributions **   <a name="awscostmanagement-Type-billing_InvestmentAttestation-investmentDistributions"></a>
The distribution of the attested investment across the eligible investment accounts. The list contains at most 200 distributions.
Type: Array of [InvestmentDistribution](API_billing_InvestmentDistribution.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

 ** isCancellable **   <a name="awscostmanagement-Type-billing_InvestmentAttestation-isCancellable"></a>
Indicates whether the attestation can be canceled with `CancelContractualInvestmentAttestation`.
Type: Boolean
Required: No

 ** rejectionReasons **   <a name="awscostmanagement-Type-billing_InvestmentAttestation-rejectionReasons"></a>
The reasons the attestation was rejected. This value is present only when `attestationStatus` is `REJECTED`. The list contains at most 30 reasons.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 30 items.
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: No

## See Also
<a name="API_billing_InvestmentAttestation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billing-2023-09-07/InvestmentAttestation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billing-2023-09-07/InvestmentAttestation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billing-2023-09-07/InvestmentAttestation)
