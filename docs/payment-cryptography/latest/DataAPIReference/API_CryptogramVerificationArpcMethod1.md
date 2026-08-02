---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_CryptogramVerificationArpcMethod1.html
---

# CryptogramVerificationArpcMethod1
<a name="API_CryptogramVerificationArpcMethod1"></a>

Parameters that are required for ARPC response generation using method1 after ARQC verification is successful.

## Contents
<a name="API_CryptogramVerificationArpcMethod1_Contents"></a>

 ** AuthResponseCode **   <a name="paymentcryptographydata-Type-CryptogramVerificationArpcMethod1-AuthResponseCode"></a>
The auth code used to calculate APRC after ARQC verification is successful. This is the same auth code used for ARQC generation outside of AWS Payment Cryptography.
Type: String
Length Constraints: Fixed length of 4.
Pattern: `[0-9a-fA-F]+`
Required: Yes

## See Also
<a name="API_CryptogramVerificationArpcMethod1_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payment-cryptography-data-2022-02-03/CryptogramVerificationArpcMethod1)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payment-cryptography-data-2022-02-03/CryptogramVerificationArpcMethod1)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payment-cryptography-data-2022-02-03/CryptogramVerificationArpcMethod1)
