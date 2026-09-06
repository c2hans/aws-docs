---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ImportKeyCryptogram.html
---

# ImportKeyCryptogram
<a name="API_ImportKeyCryptogram"></a>

Parameter information for key material import using asymmetric RSA wrap and unwrap key exchange method.

## Contents
<a name="API_ImportKeyCryptogram_Contents"></a>

 ** Exportable **   <a name="paymentcryptography-Type-ImportKeyCryptogram-Exportable"></a>
Specifies whether the key is exportable from the service.
Type: Boolean
Required: Yes

 ** ImportToken **   <a name="paymentcryptography-Type-ImportKeyCryptogram-ImportToken"></a>
The import token that initiates key import using the asymmetric RSA wrap and unwrap key exchange method into AWS Payment Cryptography. It expires after 30 days. You can use the same import token to import multiple keys to the same service account.
Type: String
Pattern: `(import-token-[0-9a-zA-Z]{16,64})?`
Required: Yes

 ** KeyAttributes **   <a name="paymentcryptography-Type-ImportKeyCryptogram-KeyAttributes"></a>
The role of the key, the algorithm it supports, and the cryptographic operations allowed with the key. This data is immutable after the key is created.
Type: [KeyAttributes](API_KeyAttributes.md) object
Required: Yes

 ** WrappedKeyCryptogram **   <a name="paymentcryptography-Type-ImportKeyCryptogram-WrappedKeyCryptogram"></a>
The RSA wrapped key cryptogram under import.
Type: String
Length Constraints: Minimum length of 16. Maximum length of 4096.
Pattern: `[0-9A-F]+`
Required: Yes

 ** WrappingSpec **   <a name="paymentcryptography-Type-ImportKeyCryptogram-WrappingSpec"></a>
The wrapping spec for the wrapped key cryptogram.
Type: String
Valid Values: `RSA_OAEP_SHA_256 | RSA_OAEP_SHA_512`
Required: No

## See Also
<a name="API_ImportKeyCryptogram_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payment-cryptography-2021-09-14/ImportKeyCryptogram)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payment-cryptography-2021-09-14/ImportKeyCryptogram)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payment-cryptography-2021-09-14/ImportKeyCryptogram)
