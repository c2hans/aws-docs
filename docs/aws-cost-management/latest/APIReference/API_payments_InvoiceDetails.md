---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_payments_InvoiceDetails.html
---

# InvoiceDetails

The details of an invoice: the invoice ID that AWS Invoicing issued, the billing period that the invoice covers, its due date and due status, its payment terms, and its frequency.

## Contents
<a name="API_payments_InvoiceDetails_Contents"></a>

 ** billingPeriod **   <a name="awscostmanagement-Type-payments_InvoiceDetails-billingPeriod"></a>
The billing period the invoice covers: the period of the usage it bills.
Type: [BillingPeriod](API_payments_BillingPeriod.md) object
Required: Yes

 ** dueDate **   <a name="awscostmanagement-Type-payments_InvoiceDetails-dueDate"></a>
The calendar date by which the invoice must be paid, as the timestamp of 00:00:00 UTC on that day. The invoice is past due from the following day.
Type: Timestamp
Required: Yes

 ** invoiceFrequency **   <a name="awscostmanagement-Type-payments_InvoiceDetails-invoiceFrequency"></a>
Whether the invoice was issued once or as part of a billing cycle. The following values are valid:
+  `ONE_TIME` – A single invoice that isn't part of a billing cycle.
+  `RECURRING` – One invoice of a billing cycle, such as your monthly invoice.
Type: String
Valid Values: `ONE_TIME | RECURRING`
Required: Yes

 ** invoiceId **   <a name="awscostmanagement-Type-payments_InvoiceDetails-invoiceId"></a>
The invoice ID that AWS Invoicing issued for the invoice: the document number printed on it, shown in the AWS Billing and Cost Management console and returned by the AWS Invoicing API as `InvoiceId`. `GetFinancialRecord` and `BatchGetFinancialRecord` also accept it, as `invoiceIdentifier`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `\S(.*\S)?`
Required: Yes

 ** dueStatus **   <a name="awscostmanagement-Type-payments_InvoiceDetails-dueStatus"></a>
Whether the invoice is due or past its due date. This member is present only while the invoice's `status` is `OUTSTANDING`. It's absent when the `status` is `PROCESSING`, `SETTLED`, or `CANCELED`. The following values are valid:
+  `DUE` – The due date hasn't passed.
+  `PAST_DUE` – The due date has passed, and the invoice is still outstanding.
Type: String
Valid Values: `DUE | PAST_DUE`
Required: No

 ** paymentTerms **   <a name="awscostmanagement-Type-payments_InvoiceDetails-paymentTerms"></a>
The payment terms for the invoice, as AWS Invoicing issued them, such as `Net30`. The due date follows from these terms. This member is absent when AWS Invoicing didn't issue payment terms for the invoice.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `[-a-zA-Z0-9]+`
Required: No

## See Also
<a name="API_payments_InvoiceDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payments-2026-09-23/InvoiceDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payments-2026-09-23/InvoiceDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payments-2026-09-23/InvoiceDetails)
