---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ImportTr34KeyBlock.html
---

# ImportTr34KeyBlock
<a name="API_ImportTr34KeyBlock"></a>

Parameter information for key material import using the asymmetric TR-34 key exchange method.

## Contents
<a name="API_ImportTr34KeyBlock_Contents"></a>

 ** CertificateAuthorityPublicKeyIdentifier **   <a name="paymentcryptography-Type-ImportTr34KeyBlock-CertificateAuthorityPublicKeyIdentifier"></a>
The `KeyARN` of the certificate chain that signs the signing key certificate during TR-34 key import.
Type: String
Length Constraints: Minimum length of 7. Maximum length of 322.
Pattern: `arn:aws:payment-cryptography:[a-z]{2}-[a-z]{1,16}-[0-9]+:[0-9]{12}:(key/[0-9a-zA-Z]{16,64}|alias/[a-zA-Z0-9/_-]+)$|^alias/[a-zA-Z0-9/_-]+`
Required: Yes

 ** KeyBlockFormat **   <a name="paymentcryptography-Type-ImportTr34KeyBlock-KeyBlockFormat"></a>
The key block format to use during key import. The only value allowed is `X9_TR34_2012`.
Type: String
Valid Values: `X9_TR34_2012`
Required: Yes

 ** SigningKeyCertificate **   <a name="paymentcryptography-Type-ImportTr34KeyBlock-SigningKeyCertificate"></a>
The public key component in PEM certificate format of the private key that signs the KDH TR-34 WrappedKeyBlock.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32768.
Pattern: `[^\[;\]<>]+`
Required: Yes

 ** WrappedKeyBlock **   <a name="paymentcryptography-Type-ImportTr34KeyBlock-WrappedKeyBlock"></a>
The TR-34 wrapped key block to import.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 4096.
Pattern: `[0-9A-F]+`
Required: Yes

 ** ImportToken **   <a name="paymentcryptography-Type-ImportTr34KeyBlock-ImportToken"></a>
The import token that initiates key import using the asymmetric TR-34 key exchange method into AWS Payment Cryptography. It expires after 30 days. You can use the same import token to import multiple keys to the same service account.
Type: String
Pattern: `(import-token-[0-9a-zA-Z]{16,64})?`
Required: No

 ** RandomNonce **   <a name="paymentcryptography-Type-ImportTr34KeyBlock-RandomNonce"></a>
A random number value that is unique to the TR-34 key block generated using 2 pass. The operation will fail, if a random nonce value is not provided for a TR-34 key block generated using 2 pass.
Type: String
Length Constraints: Minimum length of 16. Maximum length of 32.
Pattern: `(?:[0-9a-fA-F][0-9a-fA-F])+`
Required: No

 ** WrappingKeyCertificate **   <a name="paymentcryptography-Type-ImportTr34KeyBlock-WrappingKeyCertificate"></a>
The certificate used to wrap the TR-34 key block.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32768.
Pattern: `[^\[;\]<>]+`
Required: No

 ** WrappingKeyIdentifier **   <a name="paymentcryptography-Type-ImportTr34KeyBlock-WrappingKeyIdentifier"></a>
Key Identifier used for unwrapping the import key
Type: String
Length Constraints: Minimum length of 7. Maximum length of 322.
Pattern: `arn:aws:payment-cryptography:[a-z]{2}-[a-z]{1,16}-[0-9]+:[0-9]{12}:(key/[0-9a-zA-Z]{16,64}|alias/[a-zA-Z0-9/_-]+)$|^alias/[a-zA-Z0-9/_-]+`
Required: No

## See Also
<a name="API_ImportTr34KeyBlock_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payment-cryptography-2021-09-14/ImportTr34KeyBlock)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payment-cryptography-2021-09-14/ImportTr34KeyBlock)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payment-cryptography-2021-09-14/ImportTr34KeyBlock)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Payment Cryptography Control Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query payment-cryptography` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
