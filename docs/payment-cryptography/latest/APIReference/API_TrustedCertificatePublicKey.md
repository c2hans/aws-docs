---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_TrustedCertificatePublicKey.html
---

# TrustedCertificatePublicKey
<a name="API_TrustedCertificatePublicKey"></a>

Parameter information for trusted public key certificate import.

## Contents
<a name="API_TrustedCertificatePublicKey_Contents"></a>

 ** CertificateAuthorityPublicKeyIdentifier **   <a name="paymentcryptography-Type-TrustedCertificatePublicKey-CertificateAuthorityPublicKeyIdentifier"></a>
The `KeyARN` of the root public key certificate or certificate chain that signs the trusted public key certificate import.
Type: String
Length Constraints: Minimum length of 7. Maximum length of 322.
Pattern: `arn:aws:payment-cryptography:[a-z]{2}-[a-z]{1,16}-[0-9]+:[0-9]{12}:(key/[0-9a-zA-Z]{16,64}|alias/[a-zA-Z0-9/_-]+)$|^alias/[a-zA-Z0-9/_-]+`
Required: Yes

 ** KeyAttributes **   <a name="paymentcryptography-Type-TrustedCertificatePublicKey-KeyAttributes"></a>
The role of the key, the algorithm it supports, and the cryptographic operations allowed with the key. This data is immutable after a trusted public key is imported.
Type: [KeyAttributes](API_KeyAttributes.md) object
Required: Yes

 ** PublicKeyCertificate **   <a name="paymentcryptography-Type-TrustedCertificatePublicKey-PublicKeyCertificate"></a>
Parameter information for trusted public key certificate import.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32768.
Pattern: `[^\[;\]<>]+`
Required: Yes

## See Also
<a name="API_TrustedCertificatePublicKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payment-cryptography-2021-09-14/TrustedCertificatePublicKey)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payment-cryptography-2021-09-14/TrustedCertificatePublicKey)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payment-cryptography-2021-09-14/TrustedCertificatePublicKey)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Payment Cryptography Control Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query payment-cryptography` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
