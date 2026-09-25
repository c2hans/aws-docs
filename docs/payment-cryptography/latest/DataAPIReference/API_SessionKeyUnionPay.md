---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_SessionKeyUnionPay.html
---

# SessionKeyUnionPay
<a name="API_SessionKeyUnionPay"></a>

Parameters to derive session key for a UnionPay payment card for Authorization Request Cryptogram (ARQC) generation and verification.

## Contents
<a name="API_SessionKeyUnionPay_Contents"></a>

 ** ApplicationTransactionCounter **   <a name="paymentcryptographydata-Type-SessionKeyUnionPay-ApplicationTransactionCounter"></a>
The transaction counter that the terminal provides during transaction processing. This value is in hexadecimal format. For example, enter a decimal counter of 109 as `006D`.
Type: String
Length Constraints: Fixed length of 4.
Pattern: `[0-9a-fA-F]+`
Required: Yes

 ** PanSequenceNumber **   <a name="paymentcryptographydata-Type-SessionKeyUnionPay-PanSequenceNumber"></a>
A number that identifies and differentiates payment cards with the same Primary Account Number (PAN). If not used, enter `00`.
Type: String
Length Constraints: Fixed length of 2.
Pattern: `[0-9]+`
Required: Yes

 ** PrimaryAccountNumber **   <a name="paymentcryptographydata-Type-SessionKeyUnionPay-PrimaryAccountNumber"></a>
The Primary Account Number (PAN) of the cardholder. A PAN is a unique identifier for a payment credit or debit card and associates the card to a specific account holder.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 19.
Pattern: `[0-9]+`
Required: Yes

## See Also
<a name="API_SessionKeyUnionPay_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payment-cryptography-data-2022-02-03/SessionKeyUnionPay)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payment-cryptography-data-2022-02-03/SessionKeyUnionPay)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payment-cryptography-data-2022-02-03/SessionKeyUnionPay)
