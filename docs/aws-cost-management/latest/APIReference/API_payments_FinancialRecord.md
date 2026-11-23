---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_payments_FinancialRecord.html
---

# FinancialRecord

An invoice or a credit memo on your account, with the details that are specific to its type.

## Contents
<a name="API_payments_FinancialRecord_Contents"></a>

 ** amount **   <a name="awscostmanagement-Type-payments_FinancialRecord-amount"></a>
The total amount of the financial record, in the currency that the record was issued in. The amount doesn't change as the record is settled. `balances` shows how much of it is in each settlement state.
Type: [CurrencyAmount](API_payments_CurrencyAmount.md) object
Required: Yes

 ** balances **   <a name="awscostmanagement-Type-payments_FinancialRecord-balances"></a>
How much of `amount` is outstanding, processing, settled, and canceled.
Type: [Balances](API_payments_Balances.md) object
Required: Yes

 ** businessUnit **   <a name="awscostmanagement-Type-payments_FinancialRecord-businessUnit"></a>
The AWS business unit that issued the record: its merchant of record and its line of business.
Type: [BusinessUnit](API_payments_BusinessUnit.md) object
Required: Yes

 ** details **   <a name="awscostmanagement-Type-payments_FinancialRecord-details"></a>
The attributes that exist only for the record's type. The populated member matches `type`: `invoiceDetails` for an `INVOICE`, `creditMemoDetails` for a `CREDIT_MEMO`.
Type: [FinancialRecordDetails](API_payments_FinancialRecordDetails.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** id **   <a name="awscostmanagement-Type-payments_FinancialRecord-id"></a>
The ID that AWS Payments issued for the record, such as `INV-5364-6253-7364-1342`. To retrieve the record again, pass this value to `GetFinancialRecord` or `BatchGetFinancialRecord` as `identifier`.
Type: String
Length Constraints: Minimum length of 17. Maximum length of 23.
Pattern: `[A-Z]{2,3}-[0-9]{4}-[0-9]{4}-[0-9]{4}(-[0-9]{4})?`
Required: Yes

 ** issuedAt **   <a name="awscostmanagement-Type-payments_FinancialRecord-issuedAt"></a>
The date and time, in UTC, when this record was issued.
Type: Timestamp
Required: Yes

 ** settlementStatus **   <a name="awscostmanagement-Type-payments_FinancialRecord-settlementStatus"></a>
Whether the record is open or closed. If you receive a `status` value that you don't recognize, use this member to tell open records from closed ones. The following values are valid:
+  `OPEN` – Part of the amount is outstanding or processing. The `status` is `OUTSTANDING` or `PROCESSING`.
+  `CLOSED` – The whole amount is settled or canceled. The `status` is `SETTLED` or `CANCELED`.
A `CLOSED` record becomes `OPEN` again if a payment or credit applied to it is reversed. Its `closedAt` is then absent until the record closes again.
Type: String
Valid Values: `OPEN | CLOSED`
Required: Yes

 ** status **   <a name="awscostmanagement-Type-payments_FinancialRecord-status"></a>
The settlement stage of the record. The following values are valid:
+  `OUTSTANDING` – Part of the amount isn't settled, and no settlement is in progress on the record. For an invoice, `dueStatus` shows whether it's due or past due. The `settlementStatus` is `OPEN`.
+  `PROCESSING` – A settlement of part or all of the amount is in progress, for example a payment that's submitted but not yet confirmed. `PROCESSING` takes precedence over `OUTSTANDING`: while any part of the amount is processing, the status is `PROCESSING`, even if another part is still outstanding. The `settlementStatus` is `OPEN`.
+  `SETTLED` – The whole amount is settled. The `settlementStatus` is `CLOSED`.
+  `CANCELED` – The record is canceled. The part of the amount that wasn't settled isn't collected or applied. The `settlementStatus` is `CLOSED`.
Type: String
Valid Values: `OUTSTANDING | PROCESSING | SETTLED | CANCELED`
Required: Yes

 ** type **   <a name="awscostmanagement-Type-payments_FinancialRecord-type"></a>
The type of the financial record. The populated member of `details` matches this type. The following values are valid:
+  `INVOICE` – An invoice: a bill from AWS. Payments and credit memos applied to the invoice settle it.
+  `CREDIT_MEMO` – A credit memo: a credit issued to your account, for example for a billing correction or a service credit. Applying it to one or more invoices settles it.
Type: String
Valid Values: `INVOICE | CREDIT_MEMO`
Required: Yes

 ** closedAt **   <a name="awscostmanagement-Type-payments_FinancialRecord-closedAt"></a>
The date and time, in UTC, when the record was last closed, that is, when its `status` last became `SETTLED` or `CANCELED`. This member is absent while the `settlementStatus` is `OPEN`, including after a closed record reopens.
Type: Timestamp
Required: No

## See Also
<a name="API_payments_FinancialRecord_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payments-2026-09-23/FinancialRecord)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payments-2026-09-23/FinancialRecord)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payments-2026-09-23/FinancialRecord)
