---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_CreditAllocationHistoryEntry.html
---

# CreditAllocationHistoryEntry
<a name="API_billing_CreditAllocationHistoryEntry"></a>

A single entry in the credit allocation history, representing how a credit was applied to a specific service during a billing month.

## Contents
<a name="API_billing_CreditAllocationHistoryEntry_Contents"></a>

 ** accountId **   <a name="awscostmanagement-Type-billing_CreditAllocationHistoryEntry-accountId"></a>
The AWS account the credit was applied to.
Type: String
Pattern: `[0-9]{12}`
Required: Yes

 ** appliedServiceName **   <a name="awscostmanagement-Type-billing_CreditAllocationHistoryEntry-appliedServiceName"></a>
The AWS service the credit was applied to.
Type: String
Required: Yes

 ** billingMonth **   <a name="awscostmanagement-Type-billing_CreditAllocationHistoryEntry-billingMonth"></a>
The billing month of the application in `YYYY-MM` format.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 7.
Required: Yes

 ** creditAmount **   <a name="awscostmanagement-Type-billing_CreditAllocationHistoryEntry-creditAmount"></a>
The amount of credit applied. Negative values represent credits that reduced the bill.
Type: [Amount](API_billing_Amount.md) object
Required: Yes

 ** creditId **   <a name="awscostmanagement-Type-billing_CreditAllocationHistoryEntry-creditId"></a>
The identifier of the credit that was applied.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[0-9]+`
Required: Yes

 ** isEstimatedBill **   <a name="awscostmanagement-Type-billing_CreditAllocationHistoryEntry-isEstimatedBill"></a>
 `true` when the entry was applied to an in-flight bill that has not yet been finalized.
Type: Boolean
Required: Yes

 ** description **   <a name="awscostmanagement-Type-billing_CreditAllocationHistoryEntry-description"></a>
A human-readable description of the credit allocation.
Type: String
Required: No

## See Also
<a name="API_billing_CreditAllocationHistoryEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billing-2023-09-07/CreditAllocationHistoryEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billing-2023-09-07/CreditAllocationHistoryEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billing-2023-09-07/CreditAllocationHistoryEntry)
