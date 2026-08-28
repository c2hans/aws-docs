---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_RootCertificatePublicKey.html
---

# RootCertificatePublicKey
<a name="API_RootCertificatePublicKey"></a>

Parameter information for root public key certificate import.

## Contents
<a name="API_RootCertificatePublicKey_Contents"></a>

 ** KeyAttributes **   <a name="paymentcryptography-Type-RootCertificatePublicKey-KeyAttributes"></a>
The role of the key, the algorithm it supports, and the cryptographic operations allowed with the key. This data is immutable after the root public key is imported.
Type: [KeyAttributes](API_KeyAttributes.md) object
Required: Yes

 ** PublicKeyCertificate **   <a name="paymentcryptography-Type-RootCertificatePublicKey-PublicKeyCertificate"></a>
Parameter information for root public key certificate import.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32768.
Pattern: `[^\[;\]<>]+`
Required: Yes

## See Also
<a name="API_RootCertificatePublicKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payment-cryptography-2021-09-14/RootCertificatePublicKey)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payment-cryptography-2021-09-14/RootCertificatePublicKey)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payment-cryptography-2021-09-14/RootCertificatePublicKey)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Payment Cryptography Control Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query payment-cryptography` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
