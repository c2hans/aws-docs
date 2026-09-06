---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_SessionKeyAmex.html
---

# SessionKeyAmex
<a name="API_SessionKeyAmex"></a>

Parameters to derive session key for an Amex payment card.

## Contents
<a name="API_SessionKeyAmex_Contents"></a>

 ** PanSequenceNumber **   <a name="paymentcryptographydata-Type-SessionKeyAmex-PanSequenceNumber"></a>
A number that identifies and differentiates payment cards with the same Primary Account Number (PAN).
Type: String
Length Constraints: Fixed length of 2.
Pattern: `[0-9]+`
Required: Yes

 ** PrimaryAccountNumber **   <a name="paymentcryptographydata-Type-SessionKeyAmex-PrimaryAccountNumber"></a>
The Primary Account Number (PAN) of the cardholder. A PAN is a unique identifier for a payment credit or debit card and associates the card to a specific account holder.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 19.
Pattern: `[0-9]+`
Required: Yes

## See Also
<a name="API_SessionKeyAmex_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payment-cryptography-data-2022-02-03/SessionKeyAmex)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payment-cryptography-data-2022-02-03/SessionKeyAmex)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payment-cryptography-data-2022-02-03/SessionKeyAmex)
