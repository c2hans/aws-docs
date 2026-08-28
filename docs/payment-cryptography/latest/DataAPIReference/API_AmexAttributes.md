---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_AmexAttributes.html
---

# AmexAttributes
<a name="API_AmexAttributes"></a>

Parameters to derive the confidentiality and integrity keys for a payment card using Amex derivation method.

## Contents
<a name="API_AmexAttributes_Contents"></a>

 ** ApplicationTransactionCounter **   <a name="paymentcryptographydata-Type-AmexAttributes-ApplicationTransactionCounter"></a>
The transaction counter of the current transaction that is provided by the terminal during transaction processing.
Type: String
Length Constraints: Fixed length of 4.
Pattern: `[0-9a-fA-F]+`
Required: Yes

 ** AuthorizationRequestKeyIdentifier **   <a name="paymentcryptographydata-Type-AmexAttributes-AuthorizationRequestKeyIdentifier"></a>
The `keyArn` of the issuer master key for cryptogram (IMK-AC) for the payment card.
Type: String
Length Constraints: Minimum length of 7. Maximum length of 322.
Pattern: `arn:aws:payment-cryptography:[a-z]{2}-[a-z]{1,16}-[0-9]+:[0-9]{12}:(key/[0-9a-zA-Z]{16,64}|alias/[a-zA-Z0-9/_-]+)$|^alias/[a-zA-Z0-9/_-]+`
Required: Yes

 ** MajorKeyDerivationMode **   <a name="paymentcryptographydata-Type-AmexAttributes-MajorKeyDerivationMode"></a>
The method to use when deriving the master key for a payment card using Amex derivation.
Type: String
Valid Values: `EMV_OPTION_A | EMV_OPTION_B`
Required: Yes

 ** PanSequenceNumber **   <a name="paymentcryptographydata-Type-AmexAttributes-PanSequenceNumber"></a>
A number that identifies and differentiates payment cards with the same Primary Account Number (PAN). Typically 00 is used, if no value is provided by the terminal.
Type: String
Length Constraints: Fixed length of 2.
Pattern: `[0-9]+`
Required: Yes

 ** PrimaryAccountNumber **   <a name="paymentcryptographydata-Type-AmexAttributes-PrimaryAccountNumber"></a>
The Primary Account Number (PAN) of the cardholder.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 19.
Pattern: `[0-9]+`
Required: Yes

 ** CurrentPinAttributes **   <a name="paymentcryptographydata-Type-AmexAttributes-CurrentPinAttributes"></a>
The encrypted pinblock of the old pin stored on the chip card.
Type: [CurrentPinAttributes](API_CurrentPinAttributes.md) object
Required: No

## See Also
<a name="API_AmexAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payment-cryptography-data-2022-02-03/AmexAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payment-cryptography-data-2022-02-03/AmexAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payment-cryptography-data-2022-02-03/AmexAttributes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Payment Cryptography Data Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query payment-cryptography` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
