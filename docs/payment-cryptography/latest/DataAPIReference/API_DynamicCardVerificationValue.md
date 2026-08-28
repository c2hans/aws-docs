---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_DynamicCardVerificationValue.html
---

# DynamicCardVerificationValue
<a name="API_DynamicCardVerificationValue"></a>

Parameters that are required to generate or verify Dynamic Card Verification Value (dCVV).

## Contents
<a name="API_DynamicCardVerificationValue_Contents"></a>

 ** ApplicationTransactionCounter **   <a name="paymentcryptographydata-Type-DynamicCardVerificationValue-ApplicationTransactionCounter"></a>
The transaction counter value that comes from the terminal.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 4.
Pattern: `[0-9a-fA-F]+`
Required: Yes

 ** CardExpiryDate **   <a name="paymentcryptographydata-Type-DynamicCardVerificationValue-CardExpiryDate"></a>
The expiry date of a payment card.
Type: String
Length Constraints: Fixed length of 4.
Pattern: `[0-9]+`
Required: Yes

 ** PanSequenceNumber **   <a name="paymentcryptographydata-Type-DynamicCardVerificationValue-PanSequenceNumber"></a>
A number that identifies and differentiates payment cards with the same Primary Account Number (PAN).
Type: String
Length Constraints: Fixed length of 2.
Pattern: `[0-9]+`
Required: Yes

 ** ServiceCode **   <a name="paymentcryptographydata-Type-DynamicCardVerificationValue-ServiceCode"></a>
The service code of the payment card. This is different from Card Security Code (CSC).
Type: String
Length Constraints: Fixed length of 3.
Pattern: `[0-9]+`
Required: Yes

## See Also
<a name="API_DynamicCardVerificationValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payment-cryptography-data-2022-02-03/DynamicCardVerificationValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payment-cryptography-data-2022-02-03/DynamicCardVerificationValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payment-cryptography-data-2022-02-03/DynamicCardVerificationValue)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Payment Cryptography Data Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query payment-cryptography` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
