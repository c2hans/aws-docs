---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_payments_Card.html
---

# Card

The details of a card payment instrument.

## Contents
<a name="API_payments_Card_Contents"></a>

 ** last4 **   <a name="awscostmanagement-Type-payments_Card-last4"></a>
The last four digits of the card number.
Type: String
Length Constraints: Fixed length of 4.
Pattern: `[0-9]{4}`
Required: Yes

 ** brand **   <a name="awscostmanagement-Type-payments_Card-brand"></a>
The network the card runs on.
Type: String
Valid Values: `VISA | MASTERCARD | AMEX | DISCOVER | JCB | RUPAY | CHINA_UNIONPAY`
Required: No

 ** cardType **   <a name="awscostmanagement-Type-payments_Card-cardType"></a>
Whether the card is a credit card or a debit card.
Type: String
Valid Values: `CREDIT | DEBIT`
Required: No

 ** expirationMonth **   <a name="awscostmanagement-Type-payments_Card-expirationMonth"></a>
The calendar month that the card expires in.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 12.
Required: No

 ** expirationYear **   <a name="awscostmanagement-Type-payments_Card-expirationYear"></a>
The calendar year that the card expires in.
Type: Integer
Valid Range: Minimum value of 2000. Maximum value of 2300.
Required: No

 ** issuerCountry **   <a name="awscostmanagement-Type-payments_Card-issuerCountry"></a>
The country of the bank that issued the card.
Type: String
Length Constraints: Fixed length of 2.
Pattern: `[A-Z]{2}`
Required: No

 ** issuingBank **   <a name="awscostmanagement-Type-payments_Card-issuingBank"></a>
The bank that issued the card.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_payments_Card_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payments-2026-09-23/Card)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payments-2026-09-23/Card)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payments-2026-09-23/Card)
