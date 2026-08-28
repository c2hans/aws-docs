---
source_url: https://docs.aws.amazon.com/transfer/latest/APIReference/API_ListedCertificate.html
---

# ListedCertificate
<a name="API_ListedCertificate"></a>

Describes the properties of a certificate.

## Contents
<a name="API_ListedCertificate_Contents"></a>

 ** ActiveDate **   <a name="TransferFamily-Type-ListedCertificate-ActiveDate"></a>
An optional date that specifies when the certificate becomes active. If you do not specify a value, `ActiveDate` takes the same value as `NotBeforeDate`, which is specified by the CA.
Type: Timestamp
Required: No

 ** Arn **   <a name="TransferFamily-Type-ListedCertificate-Arn"></a>
The Amazon Resource Name (ARN) of the specified certificate.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 1600.
Pattern: `arn:\S+`
Required: No

 ** CertificateId **   <a name="TransferFamily-Type-ListedCertificate-CertificateId"></a>
An array of identifiers for the imported certificates. You use this identifier for working with profiles and partner profiles.
Type: String
Length Constraints: Fixed length of 22.
Pattern: `cert-([0-9a-f]{17})`
Required: No

 ** Description **   <a name="TransferFamily-Type-ListedCertificate-Description"></a>
The name or short description that's used to identify the certificate.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[\u0021-\u007E]+`
Required: No

 ** InactiveDate **   <a name="TransferFamily-Type-ListedCertificate-InactiveDate"></a>
An optional date that specifies when the certificate becomes inactive. If you do not specify a value, `InactiveDate` takes the same value as `NotAfterDate`, which is specified by the CA.
Type: Timestamp
Required: No

 ** Status **   <a name="TransferFamily-Type-ListedCertificate-Status"></a>
The certificate can be either `ACTIVE`, `PENDING_ROTATION`, or `INACTIVE`. `PENDING_ROTATION` means that this certificate will replace the current certificate when it expires.
Type: String
Valid Values: `ACTIVE | PENDING_ROTATION | INACTIVE`
Required: No

 ** Type **   <a name="TransferFamily-Type-ListedCertificate-Type"></a>
The type for the certificate. If a private key has been specified for the certificate, its type is `CERTIFICATE_WITH_PRIVATE_KEY`. If there is no private key, the type is `CERTIFICATE`.
Type: String
Valid Values: `CERTIFICATE | CERTIFICATE_WITH_PRIVATE_KEY`
Required: No

 ** Usage **   <a name="TransferFamily-Type-ListedCertificate-Usage"></a>
Specifies how this certificate is used. It can be used in the following ways:
+  `SIGNING`: For signing AS2 messages
+  `ENCRYPTION`: For encrypting AS2 messages
+  `TLS`: For securing AS2 communications sent over HTTPS
Type: String
Valid Values: `SIGNING | ENCRYPTION | TLS`
Required: No

## See Also
<a name="API_ListedCertificate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transfer-2018-11-05/ListedCertificate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transfer-2018-11-05/ListedCertificate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transfer-2018-11-05/ListedCertificate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Transfer Family. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query transfer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
