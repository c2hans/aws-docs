---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_CardVerificationAttributes.html
---

# CardVerificationAttributes
<a name="API_CardVerificationAttributes"></a>

Card data parameters that are requried to verify Card Verification Values (CVV/CVV2), Dynamic Card Verification Values (dCVV/dCVV2), or Card Security Codes (CSC).

## Contents
<a name="API_CardVerificationAttributes_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** AmexCardSecurityCodeVersion1 **   <a name="paymentcryptographydata-Type-CardVerificationAttributes-AmexCardSecurityCodeVersion1"></a>
Card data parameters that are required to generate a Card Security Code (CSC2) for an AMEX payment card.
Type: [AmexCardSecurityCodeVersion1](API_AmexCardSecurityCodeVersion1.md) object
Required: No

 ** AmexCardSecurityCodeVersion2 **   <a name="paymentcryptographydata-Type-CardVerificationAttributes-AmexCardSecurityCodeVersion2"></a>
Card data parameters that are required to verify a Card Security Code (CSC2) for an AMEX payment card.
Type: [AmexCardSecurityCodeVersion2](API_AmexCardSecurityCodeVersion2.md) object
Required: No

 ** CardHolderVerificationValue **   <a name="paymentcryptographydata-Type-CardVerificationAttributes-CardHolderVerificationValue"></a>
Card data parameters that are required to verify a cardholder verification value for the payment card.
Type: [CardHolderVerificationValue](API_CardHolderVerificationValue.md) object
Required: No

 ** CardVerificationValue1 **   <a name="paymentcryptographydata-Type-CardVerificationAttributes-CardVerificationValue1"></a>
Card data parameters that are required to verify Card Verification Value (CVV) for the payment card.
Type: [CardVerificationValue1](API_CardVerificationValue1.md) object
Required: No

 ** CardVerificationValue2 **   <a name="paymentcryptographydata-Type-CardVerificationAttributes-CardVerificationValue2"></a>
Card data parameters that are required to verify Card Verification Value (CVV2) for the payment card.
Type: [CardVerificationValue2](API_CardVerificationValue2.md) object
Required: No

 ** DiscoverDynamicCardVerificationCode **   <a name="paymentcryptographydata-Type-CardVerificationAttributes-DiscoverDynamicCardVerificationCode"></a>
Card data parameters that are required to verify CDynamic Card Verification Code (dCVC) for the payment card.
Type: [DiscoverDynamicCardVerificationCode](API_DiscoverDynamicCardVerificationCode.md) object
Required: No

 ** DynamicCardVerificationCode **   <a name="paymentcryptographydata-Type-CardVerificationAttributes-DynamicCardVerificationCode"></a>
Card data parameters that are required to verify CDynamic Card Verification Code (dCVC) for the payment card.
Type: [DynamicCardVerificationCode](API_DynamicCardVerificationCode.md) object
Required: No

 ** DynamicCardVerificationValue **   <a name="paymentcryptographydata-Type-CardVerificationAttributes-DynamicCardVerificationValue"></a>
Card data parameters that are required to verify CDynamic Card Verification Value (dCVV) for the payment card.
Type: [DynamicCardVerificationValue](API_DynamicCardVerificationValue.md) object
Required: No

## See Also
<a name="API_CardVerificationAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payment-cryptography-data-2022-02-03/CardVerificationAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payment-cryptography-data-2022-02-03/CardVerificationAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payment-cryptography-data-2022-02-03/CardVerificationAttributes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Payment Cryptography Data Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query payment-cryptography` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
