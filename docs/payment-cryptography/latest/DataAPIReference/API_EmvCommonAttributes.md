---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_EmvCommonAttributes.html
---

# EmvCommonAttributes
<a name="API_EmvCommonAttributes"></a>

Parameters to derive the confidentiality and integrity keys for an Emv common payment card.

## Contents
<a name="API_EmvCommonAttributes_Contents"></a>

 ** ApplicationCryptogram **   <a name="paymentcryptographydata-Type-EmvCommonAttributes-ApplicationCryptogram"></a>
The application cryptogram for the current transaction that is provided by the terminal during transaction processing.
Type: String
Length Constraints: Fixed length of 16.
Pattern: `[0-9a-fA-F]+`
Required: Yes

 ** MajorKeyDerivationMode **   <a name="paymentcryptographydata-Type-EmvCommonAttributes-MajorKeyDerivationMode"></a>
The method to use when deriving the master key for the payment card.
Type: String
Valid Values: `EMV_OPTION_A | EMV_OPTION_B`
Required: Yes

 ** Mode **   <a name="paymentcryptographydata-Type-EmvCommonAttributes-Mode"></a>
The block cipher method to use for encryption.
Type: String
Valid Values: `ECB | CBC`
Required: Yes

 ** PanSequenceNumber **   <a name="paymentcryptographydata-Type-EmvCommonAttributes-PanSequenceNumber"></a>
A number that identifies and differentiates payment cards with the same Primary Account Number (PAN). Typically 00 is used, if no value is provided by the terminal.
Type: String
Length Constraints: Fixed length of 2.
Pattern: `[0-9]+`
Required: Yes

 ** PinBlockLengthPosition **   <a name="paymentcryptographydata-Type-EmvCommonAttributes-PinBlockLengthPosition"></a>
Specifies if PIN block length should be added to front of the pin block.
If value is set to `FRONT_OF_PIN_BLOCK`, then PIN block padding type should be `ISO_IEC_7816_4`.
Type: String
Valid Values: `NONE | FRONT_OF_PIN_BLOCK`
Required: Yes

 ** PinBlockPaddingType **   <a name="paymentcryptographydata-Type-EmvCommonAttributes-PinBlockPaddingType"></a>
The padding to be added to the PIN block prior to encryption.
Padding type should be `ISO_IEC_7816_4`, if `PinBlockLengthPosition` is set to `FRONT_OF_PIN_BLOCK`. No padding is required, if `PinBlockLengthPosition` is set to `NONE`.
Type: String
Valid Values: `NO_PADDING | ISO_IEC_7816_4`
Required: Yes

 ** PrimaryAccountNumber **   <a name="paymentcryptographydata-Type-EmvCommonAttributes-PrimaryAccountNumber"></a>
The Primary Account Number (PAN) of the cardholder.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 19.
Pattern: `[0-9]+`
Required: Yes

## See Also
<a name="API_EmvCommonAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payment-cryptography-data-2022-02-03/EmvCommonAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payment-cryptography-data-2022-02-03/EmvCommonAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payment-cryptography-data-2022-02-03/EmvCommonAttributes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Payment Cryptography Data Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query payment-cryptography` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
