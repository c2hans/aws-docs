---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_payments_PaymentInstrumentSummary.html
---

# PaymentInstrumentSummary

A payment instrument as it appears in `ListPaymentInstruments`. Call `GetPaymentInstrument` for the full instrument, including the details specific to its payment method such as a card's last four digits and expiration.

## Contents
<a name="API_payments_PaymentInstrumentSummary_Contents"></a>

 ** arn **   <a name="awscostmanagement-Type-payments_PaymentInstrumentSummary-arn"></a>
The Amazon Resource Name (ARN) of the instrument. To allow or deny `GetPaymentInstrument` for this instrument, use the ARN in the `Resource` element of an AWS Identity and Access Management (IAM) policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:[a-z0-9-]+:payments::[0-9]{12}:payment-instrument:[a-z0-9-]+`
Required: Yes

 ** id **   <a name="awscostmanagement-Type-payments_PaymentInstrumentSummary-id"></a>
The ID of the instrument, unique within your account. It's the last segment of the instrument's ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9-]+`
Required: Yes

 ** paymentMethod **   <a name="awscostmanagement-Type-payments_PaymentInstrumentSummary-paymentMethod"></a>
The payment method of the instrument. The following values are valid:
+  `CARD` – A credit or debit card.
+  `US_ACH_BANK_ACCOUNT` – A US bank account debited over Automated Clearing House (ACH).
+  `SEPA_BANK_ACCOUNT` – A bank account debited over Single Euro Payments Area (SEPA) Direct Debit.
+  `UK_BACS_BANK_ACCOUNT` – A UK bank account debited over Bacs Direct Debit.
+  `IN_NET_BANKING` – India net banking. You authorize each payment on your bank's website.
+  `CN_BANK_REDIRECT` – China bank redirect. You authorize each payment on your bank's website.
+  `UPI` – Unified Payments Interface, the India real-time payment system.
+  `PIX` – Pix, the Brazilian Central Bank instant payment system.
+  `PAY_BY_INVOICE` – Pay by invoice. You pay each invoice yourself, for example by bank transfer, instead of AWS collecting payment from a card or a bank account.
Type: String
Valid Values: `CARD | US_ACH_BANK_ACCOUNT | SEPA_BANK_ACCOUNT | UK_BACS_BANK_ACCOUNT | IN_NET_BANKING | CN_BANK_REDIRECT | UPI | PIX | PAY_BY_INVOICE`
Required: Yes

 ** status **   <a name="awscostmanagement-Type-payments_PaymentInstrumentSummary-status"></a>
The current status of the instrument. The following values are valid:
+  `ACTIVE` – The instrument is set up, and AWS can use it for payments. `ACTIVE` doesn't confirm that the instrument is verified or that a payment with it will succeed. You don't need to take action.
+  `INVALID` – AWS can't use the instrument for payments, for example because its Direct Debit or UPI mandate is no longer valid. This status is permanent. The instrument doesn't return to `ACTIVE`. To pay with this payment method again, add a new payment instrument.
+  `PENDING_SETUP` – The instrument needs an action from you before AWS can use it, such as resuming a paused UPI mandate in your UPI app. AWS doesn't use the instrument for payments until you complete that action.
+  `SETUP_IN_PROGRESS` – You completed the setup steps, and setup of the instrument is in progress, for example while a Direct Debit or UPI mandate waits for confirmation. AWS doesn't use the instrument for payments until setup is complete. You don't need to take action.
Type: String
Valid Values: `ACTIVE | PENDING_SETUP | SETUP_IN_PROGRESS | INVALID`
Required: Yes

 ** createdAt **   <a name="awscostmanagement-Type-payments_PaymentInstrumentSummary-createdAt"></a>
The date and time, in UTC, when the instrument was registered.
Type: Timestamp
Required: No

 ** updatedAt **   <a name="awscostmanagement-Type-payments_PaymentInstrumentSummary-updatedAt"></a>
The date and time, in UTC, when the instrument was last changed.
Type: Timestamp
Required: No

## See Also
<a name="API_payments_PaymentInstrumentSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payments-2026-09-23/PaymentInstrumentSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payments-2026-09-23/PaymentInstrumentSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payments-2026-09-23/PaymentInstrumentSummary)
