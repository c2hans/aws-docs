---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ImportKeyMaterial.html
---

# ImportKeyMaterial
<a name="API_ImportKeyMaterial"></a>

Parameter information for key material import into AWS Payment Cryptography using TR-31 or TR-34 or RSA wrap and unwrap key exchange method.

## Contents
<a name="API_ImportKeyMaterial_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** As2805KeyCryptogram **   <a name="paymentcryptography-Type-ImportKeyMaterial-As2805KeyCryptogram"></a>
Parameter information for key material import using AS2805 key cryptogram format.
Type: [ImportAs2805KeyCryptogram](API_ImportAs2805KeyCryptogram.md) object
Required: No

 ** DiffieHellmanTr31KeyBlock **   <a name="paymentcryptography-Type-ImportKeyMaterial-DiffieHellmanTr31KeyBlock"></a>
Key derivation parameter information for key material import using asymmetric ECDH key exchange method.
Type: [ImportDiffieHellmanTr31KeyBlock](API_ImportDiffieHellmanTr31KeyBlock.md) object
Required: No

 ** KeyCryptogram **   <a name="paymentcryptography-Type-ImportKeyMaterial-KeyCryptogram"></a>
Parameter information for key material import using asymmetric RSA wrap and unwrap key exchange method.
Type: [ImportKeyCryptogram](API_ImportKeyCryptogram.md) object
Required: No

 ** RootCertificatePublicKey **   <a name="paymentcryptography-Type-ImportKeyMaterial-RootCertificatePublicKey"></a>
Parameter information for root public key certificate import.
Type: [RootCertificatePublicKey](API_RootCertificatePublicKey.md) object
Required: No

 ** Tr31KeyBlock **   <a name="paymentcryptography-Type-ImportKeyMaterial-Tr31KeyBlock"></a>
Parameter information for key material import using symmetric TR-31 key exchange method.
Type: [ImportTr31KeyBlock](API_ImportTr31KeyBlock.md) object
Required: No

 ** Tr34KeyBlock **   <a name="paymentcryptography-Type-ImportKeyMaterial-Tr34KeyBlock"></a>
Parameter information for key material import using the asymmetric TR-34 key exchange method.
Type: [ImportTr34KeyBlock](API_ImportTr34KeyBlock.md) object
Required: No

 ** TrustedCertificatePublicKey **   <a name="paymentcryptography-Type-ImportKeyMaterial-TrustedCertificatePublicKey"></a>
Parameter information for trusted public key certificate import.
Type: [TrustedCertificatePublicKey](API_TrustedCertificatePublicKey.md) object
Required: No

## See Also
<a name="API_ImportKeyMaterial_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payment-cryptography-2021-09-14/ImportKeyMaterial)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payment-cryptography-2021-09-14/ImportKeyMaterial)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payment-cryptography-2021-09-14/ImportKeyMaterial)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Payment Cryptography Control Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query payment-cryptography` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
