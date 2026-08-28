---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_EcdhDerivationAttributes.html
---

# EcdhDerivationAttributes
<a name="API_EcdhDerivationAttributes"></a>

Parameters required to establish ECDH based key exchange.

## Contents
<a name="API_EcdhDerivationAttributes_Contents"></a>

 ** CertificateAuthorityPublicKeyIdentifier **   <a name="paymentcryptographydata-Type-EcdhDerivationAttributes-CertificateAuthorityPublicKeyIdentifier"></a>
The `keyArn` of the certificate that signed the client's `PublicKeyCertificate`.
Type: String
Length Constraints: Minimum length of 7. Maximum length of 322.
Pattern: `arn:aws:payment-cryptography:[a-z]{2}-[a-z]{1,16}-[0-9]+:[0-9]{12}:(key/[0-9a-zA-Z]{16,64}|alias/[a-zA-Z0-9/_-]+)$|^alias/[a-zA-Z0-9/_-]+`
Required: Yes

 ** KeyAlgorithm **   <a name="paymentcryptographydata-Type-EcdhDerivationAttributes-KeyAlgorithm"></a>
The key algorithm of the derived ECDH key.
Type: String
Valid Values: `TDES_2KEY | TDES_3KEY | AES_128 | AES_192 | AES_256 | HMAC_SHA256 | HMAC_SHA384 | HMAC_SHA512 | HMAC_SHA224`
Required: Yes

 ** KeyDerivationFunction **   <a name="paymentcryptographydata-Type-EcdhDerivationAttributes-KeyDerivationFunction"></a>
The key derivation function to use for deriving a key using ECDH.
Type: String
Valid Values: `NIST_SP800 | ANSI_X963`
Required: Yes

 ** KeyDerivationHashAlgorithm **   <a name="paymentcryptographydata-Type-EcdhDerivationAttributes-KeyDerivationHashAlgorithm"></a>
The hash type to use for deriving a key using ECDH.
Type: String
Valid Values: `SHA_256 | SHA_384 | SHA_512`
Required: Yes

 ** PublicKeyCertificate **   <a name="paymentcryptographydata-Type-EcdhDerivationAttributes-PublicKeyCertificate"></a>
The client's public key certificate in PEM format (base64 encoded) to use for ECDH key derivation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32768.
Pattern: `[^\[;\]<>]+`
Required: Yes

 ** SharedInformation **   <a name="paymentcryptographydata-Type-EcdhDerivationAttributes-SharedInformation"></a>
A byte string containing information that binds the ECDH derived key to the two parties involved or to the context of the key.
It may include details like identities of the two parties deriving the key, context of the operation, session IDs, and optionally a nonce. It must not contain zero bytes, and re-using shared information for multiple ECDH key derivations is not recommended.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 2048.
Pattern: `(?:[0-9a-fA-F][0-9a-fA-F])+`
Required: Yes

## See Also
<a name="API_EcdhDerivationAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payment-cryptography-data-2022-02-03/EcdhDerivationAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payment-cryptography-data-2022-02-03/EcdhDerivationAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payment-cryptography-data-2022-02-03/EcdhDerivationAttributes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Payment Cryptography Data Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query payment-cryptography` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
