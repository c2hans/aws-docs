---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ExportKeyMaterial.html
---

# ExportKeyMaterial
<a name="API_ExportKeyMaterial"></a>

Parameter information for key material export from AWS Payment Cryptography using TR-31 or TR-34 or RSA wrap and unwrap key exchange method.

## Contents
<a name="API_ExportKeyMaterial_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** As2805KeyCryptogram **   <a name="paymentcryptography-Type-ExportKeyMaterial-As2805KeyCryptogram"></a>
Parameter information for key material export using AS2805 key cryptogram format.
Type: [ExportAs2805KeyCryptogram](API_ExportAs2805KeyCryptogram.md) object
Required: No

 ** DiffieHellmanTr31KeyBlock **   <a name="paymentcryptography-Type-ExportKeyMaterial-DiffieHellmanTr31KeyBlock"></a>
Key derivation parameter information for key material export using asymmetric ECDH key exchange method.
Type: [ExportDiffieHellmanTr31KeyBlock](API_ExportDiffieHellmanTr31KeyBlock.md) object
Required: No

 ** KeyCryptogram **   <a name="paymentcryptography-Type-ExportKeyMaterial-KeyCryptogram"></a>
Parameter information for key material export using asymmetric RSA wrap and unwrap key exchange method
Type: [ExportKeyCryptogram](API_ExportKeyCryptogram.md) object
Required: No

 ** Tr31KeyBlock **   <a name="paymentcryptography-Type-ExportKeyMaterial-Tr31KeyBlock"></a>
Parameter information for key material export using symmetric TR-31 key exchange method.
Type: [ExportTr31KeyBlock](API_ExportTr31KeyBlock.md) object
Required: No

 ** Tr34KeyBlock **   <a name="paymentcryptography-Type-ExportKeyMaterial-Tr34KeyBlock"></a>
Parameter information for key material export using the asymmetric TR-34 key exchange method.
Type: [ExportTr34KeyBlock](API_ExportTr34KeyBlock.md) object
Required: No

## See Also
<a name="API_ExportKeyMaterial_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payment-cryptography-2021-09-14/ExportKeyMaterial)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payment-cryptography-2021-09-14/ExportKeyMaterial)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payment-cryptography-2021-09-14/ExportKeyMaterial)
