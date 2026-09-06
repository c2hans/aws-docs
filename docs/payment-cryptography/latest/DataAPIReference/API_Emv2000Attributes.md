---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_Emv2000Attributes.html
---

# Emv2000Attributes
<a name="API_Emv2000Attributes"></a>

Parameters to derive the confidentiality and integrity keys for a payment card using EMV2000 deruv.

## Contents
<a name="API_Emv2000Attributes_Contents"></a>

 ** ApplicationTransactionCounter **   <a name="paymentcryptographydata-Type-Emv2000Attributes-ApplicationTransactionCounter"></a>
The transaction counter of the current transaction that is provided by the terminal during transaction processing.
Type: String
Length Constraints: Fixed length of 4.
Pattern: `[0-9a-fA-F]+`
Required: Yes

 ** MajorKeyDerivationMode **   <a name="paymentcryptographydata-Type-Emv2000Attributes-MajorKeyDerivationMode"></a>
The method to use when deriving the master key for the payment card.
Type: String
Valid Values: `EMV_OPTION_A | EMV_OPTION_B`
Required: Yes

 ** PanSequenceNumber **   <a name="paymentcryptographydata-Type-Emv2000Attributes-PanSequenceNumber"></a>
A number that identifies and differentiates payment cards with the same Primary Account Number (PAN). Typically 00 is used, if no value is provided by the terminal.
Type: String
Length Constraints: Fixed length of 2.
Pattern: `[0-9]+`
Required: Yes

 ** PrimaryAccountNumber **   <a name="paymentcryptographydata-Type-Emv2000Attributes-PrimaryAccountNumber"></a>
The Primary Account Number (PAN) of the cardholder.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 19.
Pattern: `[0-9]+`
Required: Yes

## See Also
<a name="API_Emv2000Attributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payment-cryptography-data-2022-02-03/Emv2000Attributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payment-cryptography-data-2022-02-03/Emv2000Attributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payment-cryptography-data-2022-02-03/Emv2000Attributes)
