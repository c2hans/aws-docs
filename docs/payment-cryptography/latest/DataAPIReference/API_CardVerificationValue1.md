---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_CardVerificationValue1.html
---

# CardVerificationValue1
<a name="API_CardVerificationValue1"></a>

Card data parameters that are required to verify CVV (Card Verification Value) for the payment card.

## Contents
<a name="API_CardVerificationValue1_Contents"></a>

 ** CardExpiryDate **   <a name="paymentcryptographydata-Type-CardVerificationValue1-CardExpiryDate"></a>
The expiry date of a payment card.
Type: String
Length Constraints: Fixed length of 4.
Pattern: `[0-9]+`
Required: Yes

 ** ServiceCode **   <a name="paymentcryptographydata-Type-CardVerificationValue1-ServiceCode"></a>
The service code of the payment card. This is different from Card Security Code (CSC).
Type: String
Length Constraints: Fixed length of 3.
Pattern: `[0-9]+`
Required: Yes

## See Also
<a name="API_CardVerificationValue1_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payment-cryptography-data-2022-02-03/CardVerificationValue1)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payment-cryptography-data-2022-02-03/CardVerificationValue1)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payment-cryptography-data-2022-02-03/CardVerificationValue1)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Payment Cryptography Data Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query payment-cryptography` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
