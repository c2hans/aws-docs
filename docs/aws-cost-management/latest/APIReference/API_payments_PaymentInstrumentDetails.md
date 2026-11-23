---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_payments_PaymentInstrumentDetails.html
---

# PaymentInstrumentDetails

The details that are specific to a payment instrument's payment method.

## Contents
<a name="API_payments_PaymentInstrumentDetails_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** card **   <a name="awscostmanagement-Type-payments_PaymentInstrumentDetails-card"></a>
The details of a card payment instrument.
Type: [Card](API_payments_Card.md) object
Required: No

 ** cnBankRedirect **   <a name="awscostmanagement-Type-payments_PaymentInstrumentDetails-cnBankRedirect"></a>
The details of a China bank redirect instrument.
Type: [CnBankRedirect](API_payments_CnBankRedirect.md) object
Required: No

 ** inNetBanking **   <a name="awscostmanagement-Type-payments_PaymentInstrumentDetails-inNetBanking"></a>
The details of an India net banking instrument.
Type: [InNetBanking](API_payments_InNetBanking.md) object
Required: No

 ** sepaBankAccount **   <a name="awscostmanagement-Type-payments_PaymentInstrumentDetails-sepaBankAccount"></a>
The details of a bank account that is debited over Single Euro Payments Area (SEPA) Direct Debit.
Type: [SepaBankAccount](API_payments_SepaBankAccount.md) object
Required: No

 ** ukBacsBankAccount **   <a name="awscostmanagement-Type-payments_PaymentInstrumentDetails-ukBacsBankAccount"></a>
The details of a bank account that is debited over Bacs Direct Debit.
Type: [UkBacsBankAccount](API_payments_UkBacsBankAccount.md) object
Required: No

 ** upi **   <a name="awscostmanagement-Type-payments_PaymentInstrumentDetails-upi"></a>
The details of a Unified Payments Interface (UPI) instrument.
Type: [Upi](API_payments_Upi.md) object
Required: No

 ** usAchBankAccount **   <a name="awscostmanagement-Type-payments_PaymentInstrumentDetails-usAchBankAccount"></a>
The details of a bank account that is debited over Automated Clearing House (ACH).
Type: [UsAchBankAccount](API_payments_UsAchBankAccount.md) object
Required: No

## See Also
<a name="API_payments_PaymentInstrumentDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payments-2026-09-23/PaymentInstrumentDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payments-2026-09-23/PaymentInstrumentDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payments-2026-09-23/PaymentInstrumentDetails)
