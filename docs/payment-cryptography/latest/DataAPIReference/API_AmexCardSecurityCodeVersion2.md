---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_AmexCardSecurityCodeVersion2.html
---

# AmexCardSecurityCodeVersion2
<a name="API_AmexCardSecurityCodeVersion2"></a>

Card data parameters that are required to generate a Card Security Code (CSC2) for an AMEX payment card.

## Contents
<a name="API_AmexCardSecurityCodeVersion2_Contents"></a>

 ** CardExpiryDate **   <a name="paymentcryptographydata-Type-AmexCardSecurityCodeVersion2-CardExpiryDate"></a>
The expiry date of a payment card.
Type: String
Length Constraints: Fixed length of 4.
Pattern: `[0-9]+`
Required: Yes

 ** ServiceCode **   <a name="paymentcryptographydata-Type-AmexCardSecurityCodeVersion2-ServiceCode"></a>
The service code of the AMEX payment card. This is different from the Card Security Code (CSC).
Type: String
Length Constraints: Fixed length of 3.
Pattern: `[0-9]+`
Required: Yes

## See Also
<a name="API_AmexCardSecurityCodeVersion2_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payment-cryptography-data-2022-02-03/AmexCardSecurityCodeVersion2)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payment-cryptography-data-2022-02-03/AmexCardSecurityCodeVersion2)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payment-cryptography-data-2022-02-03/AmexCardSecurityCodeVersion2)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Payment Cryptography Data Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query payment-cryptography` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
