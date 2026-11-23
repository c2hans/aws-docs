---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_payments_CreditMemoDetails.html
---

# CreditMemoDetails

The details of a credit memo: the invoice ID that AWS Invoicing issued for it and the billing period that it applies to.

## Contents
<a name="API_payments_CreditMemoDetails_Contents"></a>

 ** billingPeriod **   <a name="awscostmanagement-Type-payments_CreditMemoDetails-billingPeriod"></a>
The billing period the credit memo applies to: the period of the usage it credits.
Type: [BillingPeriod](API_payments_BillingPeriod.md) object
Required: Yes

 ** invoiceId **   <a name="awscostmanagement-Type-payments_CreditMemoDetails-invoiceId"></a>
The invoice ID that AWS Invoicing issued for the credit memo: the document number printed on it, shown in the AWS Billing and Cost Management console and returned by the AWS Invoicing API as `InvoiceId`. `GetFinancialRecord` and `BatchGetFinancialRecord` also accept it, as `invoiceIdentifier`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `\S(.*\S)?`
Required: Yes

## See Also
<a name="API_payments_CreditMemoDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payments-2026-09-23/CreditMemoDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payments-2026-09-23/CreditMemoDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payments-2026-09-23/CreditMemoDetails)
