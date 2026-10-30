---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_ContractSummary.html
---

# ContractSummary
<a name="API_billing_ContractSummary"></a>

A summary of a private pricing contract visible to your account. `ListContracts` returns these summaries.

## Contents
<a name="API_billing_ContractSummary_Contents"></a>

 ** associationStatus **   <a name="awscostmanagement-Type-billing_ContractSummary-associationStatus"></a>
Indicates whether the contract is currently associated with your account. Valid values are `ASSOCIATED` and `NOT_ASSOCIATED`. `ASSOCIATED` means the contract is associated with your account. `NOT_ASSOCIATED` means the contract is not associated with your account.
Type: String
Valid Values: `ASSOCIATED | NOT_ASSOCIATED`
Required: Yes

 ** contractArn **   <a name="awscostmanagement-Type-billing_ContractSummary-contractArn"></a>
The Amazon Resource Name (ARN) of the contract. Pass this value to operations such as `GetContractInformation`, `ListContractualInvestmentSummaries`, and `AssociateContract`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Pattern: `arn:aws[a-z-]*:billing::[0-9]{12}:contract/[a-zA-Z0-9_\+=\.\@-]{0,70}[a-zA-Z0-9]`
Required: Yes

 ** contractTerm **   <a name="awscostmanagement-Type-billing_ContractSummary-contractTerm"></a>
The contract term period of the contract, expressed as an interval with an inclusive start date and an inclusive end date.
Type: [Interval](API_billing_Interval.md) object
Required: Yes

 ** contractType **   <a name="awscostmanagement-Type-billing_ContractSummary-contractType"></a>
The classification of the contract. Valid values are `Cross-Service`, `Service-Specific`, and `Other`. `Cross-Service` applies across multiple AWS services. `Service-Specific` applies to a specific AWS service. `Other` applies to other arrangements.
Type: String
Valid Values: `Cross-Service | Service-Specific | Other`
Required: No

 ** lastUpdatedAt **   <a name="awscostmanagement-Type-billing_ContractSummary-lastUpdatedAt"></a>
The time when the contract was last associated with your account.
Type: Timestamp
Required: No

## See Also
<a name="API_billing_ContractSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billing-2023-09-07/ContractSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billing-2023-09-07/ContractSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billing-2023-09-07/ContractSummary)
