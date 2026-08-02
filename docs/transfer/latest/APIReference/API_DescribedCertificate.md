---
source_url: https://docs.aws.amazon.com/transfer/latest/APIReference/API_DescribedCertificate.html
---

# DescribedCertificate
<a name="API_DescribedCertificate"></a>

Describes the properties of a certificate.

## Contents
<a name="API_DescribedCertificate_Contents"></a>

 ** Arn **   <a name="TransferFamily-Type-DescribedCertificate-Arn"></a>
The unique Amazon Resource Name (ARN) for the certificate.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 1600.
Pattern: `arn:\S+`
Required: Yes

 ** ActiveDate **   <a name="TransferFamily-Type-DescribedCertificate-ActiveDate"></a>
An optional date that specifies when the certificate becomes active. If you do not specify a value, `ActiveDate` takes the same value as `NotBeforeDate`, which is specified by the CA.
Type: Timestamp
Required: No

 ** Certificate **   <a name="TransferFamily-Type-DescribedCertificate-Certificate"></a>
The file name for the certificate.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 16384.
Pattern: `[\t\n\r\u0020-\u00FF]+`
Required: No

 ** CertificateChain **   <a name="TransferFamily-Type-DescribedCertificate-CertificateChain"></a>
The list of certificates that make up the chain for the certificate.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2097152.
Pattern: `[\t\n\r\u0020-\u00FF]+`
Required: No

 ** CertificateId **   <a name="TransferFamily-Type-DescribedCertificate-CertificateId"></a>
An array of identifiers for the imported certificates. You use this identifier for working with profiles and partner profiles.
Type: String
Length Constraints: Fixed length of 22.
Pattern: `cert-([0-9a-f]{17})`
Required: No

 ** Description **   <a name="TransferFamily-Type-DescribedCertificate-Description"></a>
The name or description that's used to identity the certificate.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[\u0021-\u007E]+`
Required: No

 ** InactiveDate **   <a name="TransferFamily-Type-DescribedCertificate-InactiveDate"></a>
An optional date that specifies when the certificate becomes inactive. If you do not specify a value, `InactiveDate` takes the same value as `NotAfterDate`, which is specified by the CA.
Type: Timestamp
Required: No

 ** NotAfterDate **   <a name="TransferFamily-Type-DescribedCertificate-NotAfterDate"></a>
The final date that the certificate is valid.
Type: Timestamp
Required: No

 ** NotBeforeDate **   <a name="TransferFamily-Type-DescribedCertificate-NotBeforeDate"></a>
The earliest date that the certificate is valid.
Type: Timestamp
Required: No

 ** Serial **   <a name="TransferFamily-Type-DescribedCertificate-Serial"></a>
The serial number for the certificate.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 48.
Pattern: `[0-9a-fA-F{}:?]*`
Required: No

 ** Status **   <a name="TransferFamily-Type-DescribedCertificate-Status"></a>
A certificate's status can be either `ACTIVE` or `INACTIVE`.
You can set `ActiveDate` and `InactiveDate` in the `UpdateCertificate` call. If you set values for these parameters, those values are used to determine whether the certificate has a status of `ACTIVE` or `INACTIVE`.
If you don't set values for `ActiveDate` and `InactiveDate`, we use the `NotBefore` and `NotAfter` date as specified on the X509 certificate to determine when a certificate is active and when it is inactive.
Type: String
Valid Values: `ACTIVE | PENDING_ROTATION | INACTIVE`
Required: No

 ** Tags **   <a name="TransferFamily-Type-DescribedCertificate-Tags"></a>
Key-value pairs that can be used to group and search for certificates.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: No

 ** Type **   <a name="TransferFamily-Type-DescribedCertificate-Type"></a>
If a private key has been specified for the certificate, its type is `CERTIFICATE_WITH_PRIVATE_KEY`. If there is no private key, the type is `CERTIFICATE`.
Type: String
Valid Values: `CERTIFICATE | CERTIFICATE_WITH_PRIVATE_KEY`
Required: No

 ** Usage **   <a name="TransferFamily-Type-DescribedCertificate-Usage"></a>
Specifies how this certificate is used. It can be used in the following ways:
+  `SIGNING`: For signing AS2 messages
+  `ENCRYPTION`: For encrypting AS2 messages
+  `TLS`: For securing AS2 communications sent over HTTPS
Type: String
Valid Values: `SIGNING | ENCRYPTION | TLS`
Required: No

## See Also
<a name="API_DescribedCertificate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transfer-2018-11-05/DescribedCertificate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transfer-2018-11-05/DescribedCertificate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transfer-2018-11-05/DescribedCertificate)
