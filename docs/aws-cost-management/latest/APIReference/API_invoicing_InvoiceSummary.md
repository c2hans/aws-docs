---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_InvoiceSummary.html
---

# InvoiceSummary
<a name="API_invoicing_InvoiceSummary"></a>

 The invoice that the API retrieved.

## Contents
<a name="API_invoicing_InvoiceSummary_Contents"></a>

 ** AccountId **   <a name="awscostmanagement-Type-invoicing_InvoiceSummary-AccountId"></a>
 The AWS account ID.
Type: String
Pattern: `\d{12}`
Required: No

 ** BaseCurrencyAmount **   <a name="awscostmanagement-Type-invoicing_InvoiceSummary-BaseCurrencyAmount"></a>
 The summary with the product and service currency.
Type: [InvoiceCurrencyAmount](API_invoicing_InvoiceCurrencyAmount.md) object
Required: No

 ** BillingPeriod **   <a name="awscostmanagement-Type-invoicing_InvoiceSummary-BillingPeriod"></a>
 The billing period of the invoice-related document.
Type: [BillingPeriod](API_invoicing_BillingPeriod.md) object
Required: No

 ** BillSourceAccounts **   <a name="awscostmanagement-Type-invoicing_InvoiceSummary-BillSourceAccounts"></a>
 The list of AWS account IDs that are the bill source of the invoice. Currently, only a single bill source account is returned.
Type: Array of strings
Pattern: `\d{12}`
Required: No

 ** BillSourceAccountsTotalCount **   <a name="awscostmanagement-Type-invoicing_InvoiceSummary-BillSourceAccountsTotalCount"></a>
 The total number of accounts that are the bill source of the invoice.
Type: Integer
Required: No

 ** BillType **   <a name="awscostmanagement-Type-invoicing_InvoiceSummary-BillType"></a>
 The type of the bill.
Type: String
Valid Values: `ANNIVERSARY | PURCHASE | REFUND`
Required: No

 ** CommercialInvoiceId **   <a name="awscostmanagement-Type-invoicing_InvoiceSummary-CommercialInvoiceId"></a>
 The commercial invoice ID. This is only applicable for tax invoices and identifies the associated commercial invoice.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\s\S]*`
Required: No

 ** DueDate **   <a name="awscostmanagement-Type-invoicing_InvoiceSummary-DueDate"></a>
 The invoice due date.
Type: Timestamp
Required: No

 ** EinvoiceDeliveryStatus **   <a name="awscostmanagement-Type-invoicing_InvoiceSummary-EinvoiceDeliveryStatus"></a>
 The e-invoice delivery status.
Type: String
Valid Values: `DELIVERED | NOT_DELIVERED`
Required: No

 ** Entity **   <a name="awscostmanagement-Type-invoicing_InvoiceSummary-Entity"></a>
The organization name providing AWS services.
Type: [Entity](API_invoicing_Entity.md) object
Required: No

 ** InvoiceFrequency **   <a name="awscostmanagement-Type-invoicing_InvoiceSummary-InvoiceFrequency"></a>
 The frequency of the invoice.
Type: String
Valid Values: `ONE_TIME | RECURRING`
Required: No

 ** InvoiceId **   <a name="awscostmanagement-Type-invoicing_InvoiceSummary-InvoiceId"></a>
 The invoice ID.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\s\S]*`
Required: No

 ** InvoiceType **   <a name="awscostmanagement-Type-invoicing_InvoiceSummary-InvoiceType"></a>
 The type of invoice.
Type: String
Valid Values: `INVOICE | CREDIT_MEMO | PAYMENT_RECEIPT`
Required: No

 ** IssuedDate **   <a name="awscostmanagement-Type-invoicing_InvoiceSummary-IssuedDate"></a>
 The issued date of the invoice.
Type: Timestamp
Required: No

 ** OriginalInvoiceId **   <a name="awscostmanagement-Type-invoicing_InvoiceSummary-OriginalInvoiceId"></a>
The initial or original invoice ID.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\s\S]*`
Required: No

 ** PaymentCurrencyAmount **   <a name="awscostmanagement-Type-invoicing_InvoiceSummary-PaymentCurrencyAmount"></a>
 The summary with the customer configured currency.
Type: [InvoiceCurrencyAmount](API_invoicing_InvoiceCurrencyAmount.md) object
Required: No

 ** PurchaseOrderNumber **   <a name="awscostmanagement-Type-invoicing_InvoiceSummary-PurchaseOrderNumber"></a>
 The purchase order number associated to the invoice.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\s\S]*`
Required: No

 ** ReceiverRole **   <a name="awscostmanagement-Type-invoicing_InvoiceSummary-ReceiverRole"></a>
The role of the invoice receiver.
Type: String
Valid Values: `SELLER | RESELLER | BUYER`
Required: No

 ** TaxAuthorityStatus **   <a name="awscostmanagement-Type-invoicing_InvoiceSummary-TaxAuthorityStatus"></a>
 The current status of an invoice as reported to the tax authority. This captures scenarios where an invoice may be cancelled after issuance.
Type: String
Valid Values: `ISSUED | CANCELLED`
Required: No

 ** TaxCurrencyAmount **   <a name="awscostmanagement-Type-invoicing_InvoiceSummary-TaxCurrencyAmount"></a>
 The summary with the tax currency.
Type: [InvoiceCurrencyAmount](API_invoicing_InvoiceCurrencyAmount.md) object
Required: No

## See Also
<a name="API_invoicing_InvoiceSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/invoicing-2024-12-01/InvoiceSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/invoicing-2024-12-01/InvoiceSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/invoicing-2024-12-01/InvoiceSummary)
