---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_payments_FinancialRecordKey.html
---

# FinancialRecordKey

A way to identify a financial record. Specify exactly one member: the ID that AWS Payments issued, in `identifier`, or the invoice ID that AWS Invoicing issued, in `invoiceIdentifier`. If you specify both or neither, the request fails with `ValidationException`.

## Contents
<a name="API_payments_FinancialRecordKey_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** identifier **   <a name="awscostmanagement-Type-payments_FinancialRecordKey-identifier"></a>
The ID that AWS Payments issued for the record.
Type: String
Length Constraints: Minimum length of 17. Maximum length of 23.
Pattern: `[A-Z]{2,3}-[0-9]{4}-[0-9]{4}-[0-9]{4}(-[0-9]{4})?`
Required: No

 ** invoiceIdentifier **   <a name="awscostmanagement-Type-payments_FinancialRecordKey-invoiceIdentifier"></a>
The invoice ID that AWS Invoicing issued for an invoice or a credit memo.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `\S(.*\S)?`
Required: No

## See Also
<a name="API_payments_FinancialRecordKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payments-2026-09-23/FinancialRecordKey)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payments-2026-09-23/FinancialRecordKey)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payments-2026-09-23/FinancialRecordKey)
