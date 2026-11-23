---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_payments_FinancialRecordDetails.html
---

# FinancialRecordDetails

The attributes that exist only for one type of financial record. The populated member matches the record's `type`.

## Contents
<a name="API_payments_FinancialRecordDetails_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** creditMemoDetails **   <a name="awscostmanagement-Type-payments_FinancialRecordDetails-creditMemoDetails"></a>
The details of a credit memo. Populated when `type` is `CREDIT_MEMO`.
Type: [CreditMemoDetails](API_payments_CreditMemoDetails.md) object
Required: No

 ** invoiceDetails **   <a name="awscostmanagement-Type-payments_FinancialRecordDetails-invoiceDetails"></a>
The details of an invoice. Populated when `type` is `INVOICE`.
Type: [InvoiceDetails](API_payments_InvoiceDetails.md) object
Required: No

## See Also
<a name="API_payments_FinancialRecordDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payments-2026-09-23/FinancialRecordDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payments-2026-09-23/FinancialRecordDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payments-2026-09-23/FinancialRecordDetails)
