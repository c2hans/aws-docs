---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_CryptogramAuthResponse.html
---

# CryptogramAuthResponse
<a name="API_CryptogramAuthResponse"></a>

Parameters that are required for Authorization Response Cryptogram (ARPC) generation after Authorization Request Cryptogram (ARQC) verification is successful.

## Contents
<a name="API_CryptogramAuthResponse_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** ArpcMethod1 **   <a name="paymentcryptographydata-Type-CryptogramAuthResponse-ArpcMethod1"></a>
Parameters that are required for ARPC response generation using method1 after ARQC verification is successful.
Type: [CryptogramVerificationArpcMethod1](API_CryptogramVerificationArpcMethod1.md) object
Required: No

 ** ArpcMethod2 **   <a name="paymentcryptographydata-Type-CryptogramAuthResponse-ArpcMethod2"></a>
Parameters that are required for ARPC response generation using method2 after ARQC verification is successful.
Type: [CryptogramVerificationArpcMethod2](API_CryptogramVerificationArpcMethod2.md) object
Required: No

## See Also
<a name="API_CryptogramAuthResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payment-cryptography-data-2022-02-03/CryptogramAuthResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payment-cryptography-data-2022-02-03/CryptogramAuthResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payment-cryptography-data-2022-02-03/CryptogramAuthResponse)
