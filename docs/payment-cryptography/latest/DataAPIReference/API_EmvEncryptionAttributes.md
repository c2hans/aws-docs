---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_EmvEncryptionAttributes.html
---

# EmvEncryptionAttributes
<a name="API_EmvEncryptionAttributes"></a>

Parameters for plaintext encryption using EMV keys.

## Contents
<a name="API_EmvEncryptionAttributes_Contents"></a>

 ** MajorKeyDerivationMode **   <a name="paymentcryptographydata-Type-EmvEncryptionAttributes-MajorKeyDerivationMode"></a>
The EMV derivation mode to use for ICC master key derivation as per EMV version 4.3 book 2.
Type: String
Valid Values: `EMV_OPTION_A | EMV_OPTION_B`
Required: Yes

 ** PanSequenceNumber **   <a name="paymentcryptographydata-Type-EmvEncryptionAttributes-PanSequenceNumber"></a>
A number that identifies and differentiates payment cards with the same Primary Account Number (PAN). Typically 00 is used, if no value is provided by the terminal.
Type: String
Length Constraints: Fixed length of 2.
Pattern: `[0-9]+`
Required: Yes

 ** PrimaryAccountNumber **   <a name="paymentcryptographydata-Type-EmvEncryptionAttributes-PrimaryAccountNumber"></a>
The Primary Account Number (PAN), a unique identifier for a payment credit or debit card and associates the card to a specific account holder.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 19.
Pattern: `[0-9]+`
Required: Yes

 ** SessionDerivationData **   <a name="paymentcryptographydata-Type-EmvEncryptionAttributes-SessionDerivationData"></a>
The derivation value used to derive the ICC session key. It is typically the application transaction counter value padded with zeros or previous ARQC value padded with zeros as per EMV version 4.3 book 2.
Type: String
Length Constraints: Fixed length of 16.
Pattern: `[0-9a-fA-F]+`
Required: Yes

 ** InitializationVector **   <a name="paymentcryptographydata-Type-EmvEncryptionAttributes-InitializationVector"></a>
An input used to provide the intial state. If no value is provided, AWS Payment Cryptography defaults it to zero.
Type: String
Length Constraints: Minimum length of 16. Maximum length of 32.
Pattern: `(?:[0-9a-fA-F]{16}|[0-9a-fA-F]{32})`
Required: No

 ** Mode **   <a name="paymentcryptographydata-Type-EmvEncryptionAttributes-Mode"></a>
The block cipher method to use for encryption.
Type: String
Valid Values: `ECB | CBC`
Required: No

## See Also
<a name="API_EmvEncryptionAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payment-cryptography-data-2022-02-03/EmvEncryptionAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payment-cryptography-data-2022-02-03/EmvEncryptionAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payment-cryptography-data-2022-02-03/EmvEncryptionAttributes)
