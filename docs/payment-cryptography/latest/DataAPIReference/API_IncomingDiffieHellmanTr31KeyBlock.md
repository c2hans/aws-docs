---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_IncomingDiffieHellmanTr31KeyBlock.html
---

# IncomingDiffieHellmanTr31KeyBlock
<a name="API_IncomingDiffieHellmanTr31KeyBlock"></a>

Parameter information of a TR31KeyBlock wrapped using an ECDH derived key.

## Contents
<a name="API_IncomingDiffieHellmanTr31KeyBlock_Contents"></a>

 ** CertificateAuthorityPublicKeyIdentifier **   <a name="paymentcryptographydata-Type-IncomingDiffieHellmanTr31KeyBlock-CertificateAuthorityPublicKeyIdentifier"></a>
The `keyArn` of the certificate that signed the client's `PublicKeyCertificate`.
Type: String
Length Constraints: Minimum length of 7. Maximum length of 322.
Pattern: `arn:aws:payment-cryptography:[a-z]{2}-[a-z]{1,16}-[0-9]+:[0-9]{12}:(key/[0-9a-zA-Z]{16,64}|alias/[a-zA-Z0-9/_-]+)$|^alias/[a-zA-Z0-9/_-]+`
Required: Yes

 ** DerivationData **   <a name="paymentcryptographydata-Type-IncomingDiffieHellmanTr31KeyBlock-DerivationData"></a>
The shared information used when deriving a key using ECDH.
Type: [DiffieHellmanDerivationData](API_DiffieHellmanDerivationData.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** DeriveKeyAlgorithm **   <a name="paymentcryptographydata-Type-IncomingDiffieHellmanTr31KeyBlock-DeriveKeyAlgorithm"></a>
The key algorithm of the derived ECDH key.
Type: String
Valid Values: `TDES_2KEY | TDES_3KEY | AES_128 | AES_192 | AES_256 | HMAC_SHA256 | HMAC_SHA384 | HMAC_SHA512 | HMAC_SHA224`
Required: Yes

 ** KeyDerivationFunction **   <a name="paymentcryptographydata-Type-IncomingDiffieHellmanTr31KeyBlock-KeyDerivationFunction"></a>
The key derivation function to use for deriving a key using ECDH.
Type: String
Valid Values: `NIST_SP800 | ANSI_X963`
Required: Yes

 ** KeyDerivationHashAlgorithm **   <a name="paymentcryptographydata-Type-IncomingDiffieHellmanTr31KeyBlock-KeyDerivationHashAlgorithm"></a>
The hash type to use for deriving a key using ECDH.
Type: String
Valid Values: `SHA_256 | SHA_384 | SHA_512`
Required: Yes

 ** PrivateKeyIdentifier **   <a name="paymentcryptographydata-Type-IncomingDiffieHellmanTr31KeyBlock-PrivateKeyIdentifier"></a>
The `keyARN` of the asymmetric ECC key pair.
Type: String
Length Constraints: Minimum length of 7. Maximum length of 322.
Pattern: `arn:aws:payment-cryptography:[a-z]{2}-[a-z]{1,16}-[0-9]+:[0-9]{12}:(key/[0-9a-zA-Z]{16,64}|alias/[a-zA-Z0-9/_-]+)$|^alias/[a-zA-Z0-9/_-]+`
Required: Yes

 ** PublicKeyCertificate **   <a name="paymentcryptographydata-Type-IncomingDiffieHellmanTr31KeyBlock-PublicKeyCertificate"></a>
The client's public key certificate in PEM format (base64 encoded) to use for ECDH key derivation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32768.
Pattern: `[^\[;\]<>]+`
Required: Yes

 ** WrappedKeyBlock **   <a name="paymentcryptographydata-Type-IncomingDiffieHellmanTr31KeyBlock-WrappedKeyBlock"></a>
The WrappedKeyBlock containing the transaction key wrapped using an ECDH dervied key.
Type: String
Length Constraints: Minimum length of 56. Maximum length of 9984.
Pattern: `[0-9a-zA-Z]+`
Required: Yes

## See Also
<a name="API_IncomingDiffieHellmanTr31KeyBlock_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payment-cryptography-data-2022-02-03/IncomingDiffieHellmanTr31KeyBlock)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payment-cryptography-data-2022-02-03/IncomingDiffieHellmanTr31KeyBlock)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payment-cryptography-data-2022-02-03/IncomingDiffieHellmanTr31KeyBlock)
