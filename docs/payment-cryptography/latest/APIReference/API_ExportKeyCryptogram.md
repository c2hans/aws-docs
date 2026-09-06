---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ExportKeyCryptogram.html
---

# ExportKeyCryptogram
<a name="API_ExportKeyCryptogram"></a>

Parameter information for key material export using asymmetric RSA wrap and unwrap key exchange method.

## Contents
<a name="API_ExportKeyCryptogram_Contents"></a>

 ** CertificateAuthorityPublicKeyIdentifier **   <a name="paymentcryptography-Type-ExportKeyCryptogram-CertificateAuthorityPublicKeyIdentifier"></a>
The `KeyARN` of the certificate chain that signs the wrapping key certificate during RSA wrap and unwrap key export.
Type: String
Length Constraints: Minimum length of 7. Maximum length of 322.
Pattern: `arn:aws:payment-cryptography:[a-z]{2}-[a-z]{1,16}-[0-9]+:[0-9]{12}:(key/[0-9a-zA-Z]{16,64}|alias/[a-zA-Z0-9/_-]+)$|^alias/[a-zA-Z0-9/_-]+`
Required: Yes

 ** WrappingKeyCertificate **   <a name="paymentcryptography-Type-ExportKeyCryptogram-WrappingKeyCertificate"></a>
The wrapping key certificate in PEM format (base64 encoded). AWS Payment Cryptography uses this certificate to wrap the key under export.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32768.
Pattern: `[^\[;\]<>]+`
Required: Yes

 ** WrappingSpec **   <a name="paymentcryptography-Type-ExportKeyCryptogram-WrappingSpec"></a>
The wrapping spec for the key under export.
Type: String
Valid Values: `RSA_OAEP_SHA_256 | RSA_OAEP_SHA_512`
Required: No

## See Also
<a name="API_ExportKeyCryptogram_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payment-cryptography-2021-09-14/ExportKeyCryptogram)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payment-cryptography-2021-09-14/ExportKeyCryptogram)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payment-cryptography-2021-09-14/ExportKeyCryptogram)
