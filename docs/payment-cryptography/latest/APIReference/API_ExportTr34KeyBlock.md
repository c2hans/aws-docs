---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ExportTr34KeyBlock.html
---

# ExportTr34KeyBlock
<a name="API_ExportTr34KeyBlock"></a>

Parameter information for key material export using the asymmetric TR-34 key exchange method.

## Contents
<a name="API_ExportTr34KeyBlock_Contents"></a>

 ** CertificateAuthorityPublicKeyIdentifier **   <a name="paymentcryptography-Type-ExportTr34KeyBlock-CertificateAuthorityPublicKeyIdentifier"></a>
The `KeyARN` of the certificate chain that signs the wrapping key certificate during TR-34 key export.
Type: String
Length Constraints: Minimum length of 7. Maximum length of 322.
Pattern: `arn:aws:payment-cryptography:[a-z]{2}-[a-z]{1,16}-[0-9]+:[0-9]{12}:(key/[0-9a-zA-Z]{16,64}|alias/[a-zA-Z0-9/_-]+)$|^alias/[a-zA-Z0-9/_-]+`
Required: Yes

 ** KeyBlockFormat **   <a name="paymentcryptography-Type-ExportTr34KeyBlock-KeyBlockFormat"></a>
The format of key block that AWS Payment Cryptography will use during key export.
Type: String
Valid Values: `X9_TR34_2012`
Required: Yes

 ** WrappingKeyCertificate **   <a name="paymentcryptography-Type-ExportTr34KeyBlock-WrappingKeyCertificate"></a>
The `KeyARN` of the wrapping key certificate. AWS Payment Cryptography uses this certificate to wrap the key under export.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32768.
Pattern: `[^\[;\]<>]+`
Required: Yes

 ** ExportToken **   <a name="paymentcryptography-Type-ExportTr34KeyBlock-ExportToken"></a>
The export token to initiate key export from AWS Payment Cryptography. It also contains the signing key certificate that will sign the wrapped key during TR-34 key block generation. Call [GetParametersForExport](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetParametersForExport.html) to receive an export token. It expires after 30 days. You can use the same export token to export multiple keys from the same service account.
Type: String
Pattern: `(export-token-[0-9a-zA-Z]{16,64})?`
Required: No

 ** KeyBlockHeaders **   <a name="paymentcryptography-Type-ExportTr34KeyBlock-KeyBlockHeaders"></a>
Optional metadata for export associated with the key material. This data is signed but transmitted in clear text.
Type: [KeyBlockHeaders](API_KeyBlockHeaders.md) object
Required: No

 ** RandomNonce **   <a name="paymentcryptography-Type-ExportTr34KeyBlock-RandomNonce"></a>
A random number value that is unique to the TR-34 key block generated using 2 pass. The operation will fail, if a random nonce value is not provided for a TR-34 key block generated using 2 pass.
Type: String
Length Constraints: Minimum length of 16. Maximum length of 32.
Pattern: `(?:[0-9a-fA-F][0-9a-fA-F])+`
Required: No

 ** SigningKeyCertificate **   <a name="paymentcryptography-Type-ExportTr34KeyBlock-SigningKeyCertificate"></a>
The certificate used to sign the TR-34 key block.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32768.
Pattern: `[^\[;\]<>]+`
Required: No

 ** SigningKeyIdentifier **   <a name="paymentcryptography-Type-ExportTr34KeyBlock-SigningKeyIdentifier"></a>
Key Identifier used for signing the export key
Type: String
Length Constraints: Minimum length of 7. Maximum length of 322.
Pattern: `arn:aws:payment-cryptography:[a-z]{2}-[a-z]{1,16}-[0-9]+:[0-9]{12}:(key/[0-9a-zA-Z]{16,64}|alias/[a-zA-Z0-9/_-]+)$|^alias/[a-zA-Z0-9/_-]+`
Required: No

## See Also
<a name="API_ExportTr34KeyBlock_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payment-cryptography-2021-09-14/ExportTr34KeyBlock)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payment-cryptography-2021-09-14/ExportTr34KeyBlock)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payment-cryptography-2021-09-14/ExportTr34KeyBlock)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Payment Cryptography Control Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query payment-cryptography` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
