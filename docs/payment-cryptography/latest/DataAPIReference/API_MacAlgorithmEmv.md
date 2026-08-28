---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_MacAlgorithmEmv.html
---

# MacAlgorithmEmv
<a name="API_MacAlgorithmEmv"></a>

Parameters that are required for EMV MAC generation and verification.

## Contents
<a name="API_MacAlgorithmEmv_Contents"></a>

 ** MajorKeyDerivationMode **   <a name="paymentcryptographydata-Type-MacAlgorithmEmv-MajorKeyDerivationMode"></a>
The method to use when deriving the master key for EMV MAC generation or verification.
Type: String
Valid Values: `EMV_OPTION_A | EMV_OPTION_B`
Required: Yes

 ** PanSequenceNumber **   <a name="paymentcryptographydata-Type-MacAlgorithmEmv-PanSequenceNumber"></a>
A number that identifies and differentiates payment cards with the same Primary Account Number (PAN).
Type: String
Length Constraints: Fixed length of 2.
Pattern: `[0-9]+`
Required: Yes

 ** PrimaryAccountNumber **   <a name="paymentcryptographydata-Type-MacAlgorithmEmv-PrimaryAccountNumber"></a>
The Primary Account Number (PAN), a unique identifier for a payment credit or debit card and associates the card to a specific account holder.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 19.
Pattern: `[0-9]+`
Required: Yes

 ** SessionKeyDerivationMode **   <a name="paymentcryptographydata-Type-MacAlgorithmEmv-SessionKeyDerivationMode"></a>
The method of deriving a session key for EMV MAC generation or verification.
Type: String
Valid Values: `EMV_COMMON_SESSION_KEY | EMV2000 | AMEX | MASTERCARD_SESSION_KEY | VISA`
Required: Yes

 ** SessionKeyDerivationValue **   <a name="paymentcryptographydata-Type-MacAlgorithmEmv-SessionKeyDerivationValue"></a>
Parameters that are required to generate session key for EMV generation and verification.
Type: [SessionKeyDerivationValue](API_SessionKeyDerivationValue.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

## See Also
<a name="API_MacAlgorithmEmv_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payment-cryptography-data-2022-02-03/MacAlgorithmEmv)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payment-cryptography-data-2022-02-03/MacAlgorithmEmv)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payment-cryptography-data-2022-02-03/MacAlgorithmEmv)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Payment Cryptography Data Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query payment-cryptography` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
