---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_payments_Balances.html
---

# Balances

How much of the record's `amount` is outstanding, processing, settled, and canceled. The four balances add up to `amount`. Each balance is in the currency of `amount`, and a balance with nothing in it is 0.

## Contents
<a name="API_payments_Balances_Contents"></a>

 ** canceled **   <a name="awscostmanagement-Type-payments_Balances-canceled"></a>
The part of the amount that was canceled and isn't settled, for example when an invoice is voided. When a partly settled record is canceled, it keeps its `settled` balance, and the rest of the amount moves to `canceled`. This balance is more than 0 only when the `status` is `CANCELED`.
Type: [CurrencyAmount](API_payments_CurrencyAmount.md) object
Required: Yes

 ** outstanding **   <a name="awscostmanagement-Type-payments_Balances-outstanding"></a>
The part of the amount that isn't settled and has no settlement in progress. For an invoice, this is what remains to pay. For a credit memo, this is the credit that isn't yet applied. This balance doesn't include `processing`.
Type: [CurrencyAmount](API_payments_CurrencyAmount.md) object
Required: Yes

 ** processing **   <a name="awscostmanagement-Type-payments_Balances-processing"></a>
The part of the amount with a settlement in progress, for example a payment that's submitted but not yet confirmed. It moves to `settled` when the settlement completes, and back to `outstanding` when the settlement fails. This balance is more than 0 only when the `status` is `PROCESSING`.
Type: [CurrencyAmount](API_payments_CurrencyAmount.md) object
Required: Yes

 ** settled **   <a name="awscostmanagement-Type-payments_Balances-settled"></a>
The part of the amount that is settled. For an invoice, this is the amount paid or covered by credit memos. For a credit memo, this is the amount applied to invoices. This balance is 0 when nothing is settled yet.
Type: [CurrencyAmount](API_payments_CurrencyAmount.md) object
Required: Yes

## See Also
<a name="API_payments_Balances_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payments-2026-09-23/Balances)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payments-2026-09-23/Balances)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payments-2026-09-23/Balances)
