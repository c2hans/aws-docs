---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_CryptogramVerificationArpcMethod2.html
---

# CryptogramVerificationArpcMethod2
<a name="API_CryptogramVerificationArpcMethod2"></a>

Parameters that are required for ARPC response generation using method2 after ARQC verification is successful.

## Contents
<a name="API_CryptogramVerificationArpcMethod2_Contents"></a>

 ** CardStatusUpdate **   <a name="paymentcryptographydata-Type-CryptogramVerificationArpcMethod2-CardStatusUpdate"></a>
The data indicating whether the issuer approves or declines an online transaction using an EMV chip card.
Type: String
Length Constraints: Fixed length of 8.
Pattern: `[0-9a-fA-F]+`
Required: Yes

 ** ProprietaryAuthenticationData **   <a name="paymentcryptographydata-Type-CryptogramVerificationArpcMethod2-ProprietaryAuthenticationData"></a>
The proprietary authentication data used by issuer for communication during online transaction using an EMV chip card.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 16.
Pattern: `[0-9a-fA-F]+`
Required: No

## See Also
<a name="API_CryptogramVerificationArpcMethod2_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payment-cryptography-data-2022-02-03/CryptogramVerificationArpcMethod2)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payment-cryptography-data-2022-02-03/CryptogramVerificationArpcMethod2)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payment-cryptography-data-2022-02-03/CryptogramVerificationArpcMethod2)
