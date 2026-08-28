---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ImportDiffieHellmanTr31KeyBlock.html
---

# ImportDiffieHellmanTr31KeyBlock
<a name="API_ImportDiffieHellmanTr31KeyBlock"></a>

Key derivation parameter information for key material import using asymmetric ECDH key exchange method.

## Contents
<a name="API_ImportDiffieHellmanTr31KeyBlock_Contents"></a>

 ** CertificateAuthorityPublicKeyIdentifier **   <a name="paymentcryptography-Type-ImportDiffieHellmanTr31KeyBlock-CertificateAuthorityPublicKeyIdentifier"></a>
The `keyARN` of the CA that signed the `PublicKeyCertificate` for the client's receiving ECC key pair.
Type: String
Length Constraints: Minimum length of 7. Maximum length of 322.
Pattern: `arn:aws:payment-cryptography:[a-z]{2}-[a-z]{1,16}-[0-9]+:[0-9]{12}:(key/[0-9a-zA-Z]{16,64}|alias/[a-zA-Z0-9/_-]+)$|^alias/[a-zA-Z0-9/_-]+`
Required: Yes

 ** DerivationData **   <a name="paymentcryptography-Type-ImportDiffieHellmanTr31KeyBlock-DerivationData"></a>
The shared information used when deriving a key using ECDH.
Type: [DiffieHellmanDerivationData](API_DiffieHellmanDerivationData.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** DeriveKeyAlgorithm **   <a name="paymentcryptography-Type-ImportDiffieHellmanTr31KeyBlock-DeriveKeyAlgorithm"></a>
The key algorithm of the shared derived ECDH key.
Type: String
Valid Values: `TDES_2KEY | TDES_3KEY | AES_128 | AES_192 | AES_256 | HMAC_SHA256 | HMAC_SHA384 | HMAC_SHA512 | HMAC_SHA224`
Required: Yes

 ** KeyDerivationFunction **   <a name="paymentcryptography-Type-ImportDiffieHellmanTr31KeyBlock-KeyDerivationFunction"></a>
The key derivation function to use when deriving a key using ECDH.
Type: String
Valid Values: `NIST_SP800 | ANSI_X963`
Required: Yes

 ** KeyDerivationHashAlgorithm **   <a name="paymentcryptography-Type-ImportDiffieHellmanTr31KeyBlock-KeyDerivationHashAlgorithm"></a>
The hash type to use when deriving a key using ECDH.
Type: String
Valid Values: `SHA_256 | SHA_384 | SHA_512`
Required: Yes

 ** PrivateKeyIdentifier **   <a name="paymentcryptography-Type-ImportDiffieHellmanTr31KeyBlock-PrivateKeyIdentifier"></a>
The `keyARN` of the asymmetric ECC key created within AWS Payment Cryptography.
Type: String
Length Constraints: Minimum length of 7. Maximum length of 322.
Pattern: `arn:aws:payment-cryptography:[a-z]{2}-[a-z]{1,16}-[0-9]+:[0-9]{12}:(key/[0-9a-zA-Z]{16,64}|alias/[a-zA-Z0-9/_-]+)$|^alias/[a-zA-Z0-9/_-]+`
Required: Yes

 ** PublicKeyCertificate **   <a name="paymentcryptography-Type-ImportDiffieHellmanTr31KeyBlock-PublicKeyCertificate"></a>
The public key certificate of the client's receiving ECC key pair, in PEM format (base64 encoded), to use for ECDH key derivation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32768.
Pattern: `[^\[;\]<>]+`
Required: Yes

 ** WrappedKeyBlock **   <a name="paymentcryptography-Type-ImportDiffieHellmanTr31KeyBlock-WrappedKeyBlock"></a>
The ECDH wrapped key block to import.
Type: String
Length Constraints: Minimum length of 56. Maximum length of 9984.
Pattern: `[0-9a-zA-Z]+`
Required: Yes

## See Also
<a name="API_ImportDiffieHellmanTr31KeyBlock_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payment-cryptography-2021-09-14/ImportDiffieHellmanTr31KeyBlock)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payment-cryptography-2021-09-14/ImportDiffieHellmanTr31KeyBlock)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payment-cryptography-2021-09-14/ImportDiffieHellmanTr31KeyBlock)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Payment Cryptography Control Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query payment-cryptography` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
