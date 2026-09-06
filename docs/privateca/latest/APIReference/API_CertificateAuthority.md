---
source_url: https://docs.aws.amazon.com/privateca/latest/APIReference/API_CertificateAuthority.html
---

# CertificateAuthority
<a name="API_CertificateAuthority"></a>

Contains information about your private certificate authority (CA). Your private CA can issue and revoke X.509 digital certificates. Digital certificates verify that the entity named in the certificate **Subject** field owns or controls the public key contained in the **Subject Public Key Info** field. Call the [CreateCertificateAuthority](https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreateCertificateAuthority.html) action to create your private CA. You must then call the [GetCertificateAuthorityCertificate](https://docs.aws.amazon.com/privateca/latest/APIReference/API_GetCertificateAuthorityCertificate.html) action to retrieve a private CA certificate signing request (CSR). Sign the CSR with your AWS Private CA-hosted or on-premises root or subordinate CA certificate. Call the [ImportCertificateAuthorityCertificate](https://docs.aws.amazon.com/privateca/latest/APIReference/API_ImportCertificateAuthorityCertificate.html) action to import the signed certificate into AWS Certificate Manager (ACM).

## Contents
<a name="API_CertificateAuthority_Contents"></a>

 ** Arn **   <a name="privateca-Type-CertificateAuthority-Arn"></a>
Amazon Resource Name (ARN) for your private certificate authority (CA). The format is ` 12345678-1234-1234-1234-123456789012 `.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 200.
Pattern: `arn:[\w+=/,.@-]+:acm-pca:[\w+=/,.@-]*:[0-9]*:[\w+=,.@-]+(/[\w+=,.@-]+)*`
Required: No

 ** CertificateAuthorityConfiguration **   <a name="privateca-Type-CertificateAuthority-CertificateAuthorityConfiguration"></a>
Your private CA configuration.
Type: [CertificateAuthorityConfiguration](API_CertificateAuthorityConfiguration.md) object
Required: No

 ** CreatedAt **   <a name="privateca-Type-CertificateAuthority-CreatedAt"></a>
Date and time at which your private CA was created.
Type: Timestamp
Required: No

 ** FailureReason **   <a name="privateca-Type-CertificateAuthority-FailureReason"></a>
Reason the request to create your private CA failed.
Type: String
Valid Values: `REQUEST_TIMED_OUT | UNSUPPORTED_ALGORITHM | OTHER`
Required: No

 ** KeyStorageSecurityStandard **   <a name="privateca-Type-CertificateAuthority-KeyStorageSecurityStandard"></a>
Defines a cryptographic key management compliance standard for handling and protecting CA keys.
Default: FIPS\_140\_2\_LEVEL\_3\_OR\_HIGHER
Starting January 26, 2023, AWS Private CA protects all CA private keys in non-China regions using hardware security modules (HSMs) that comply with FIPS PUB 140-2 Level 3.
For information about security standard support in different AWS Regions, see [Storage and security compliance of AWS Private CA private keys](https://docs.aws.amazon.com/privateca/latest/userguide/data-protection.html#private-keys).
Type: String
Valid Values: `FIPS_140_2_LEVEL_2_OR_HIGHER | FIPS_140_2_LEVEL_3_OR_HIGHER | CCPC_LEVEL_1_OR_HIGHER`
Required: No

 ** LastStateChangeAt **   <a name="privateca-Type-CertificateAuthority-LastStateChangeAt"></a>
Date and time at which your private CA was last updated.
Type: Timestamp
Required: No

 ** NotAfter **   <a name="privateca-Type-CertificateAuthority-NotAfter"></a>
Date and time after which your private CA certificate is not valid.
Type: Timestamp
Required: No

 ** NotBefore **   <a name="privateca-Type-CertificateAuthority-NotBefore"></a>
Date and time before which your private CA certificate is not valid.
Type: Timestamp
Required: No

 ** OwnerAccount **   <a name="privateca-Type-CertificateAuthority-OwnerAccount"></a>
The AWS account ID that owns the certificate authority.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]+`
Required: No

 ** RestorableUntil **   <a name="privateca-Type-CertificateAuthority-RestorableUntil"></a>
The period during which a deleted CA can be restored. For more information, see the `PermanentDeletionTimeInDays` parameter of the [DeleteCertificateAuthorityRequest](https://docs.aws.amazon.com/privateca/latest/APIReference/API_DeleteCertificateAuthorityRequest.html) action.
Type: Timestamp
Required: No

 ** RevocationConfiguration **   <a name="privateca-Type-CertificateAuthority-RevocationConfiguration"></a>
Information about the Online Certificate Status Protocol (OCSP) configuration or certificate revocation list (CRL) created and maintained by your private CA.
Type: [RevocationConfiguration](API_RevocationConfiguration.md) object
Required: No

 ** Serial **   <a name="privateca-Type-CertificateAuthority-Serial"></a>
Serial number of your private CA.
Type: String
Required: No

 ** Status **   <a name="privateca-Type-CertificateAuthority-Status"></a>
Status of your private CA.
Type: String
Valid Values: `CREATING | PENDING_CERTIFICATE | ACTIVE | DELETED | DISABLED | EXPIRED | FAILED`
Required: No

 ** Type **   <a name="privateca-Type-CertificateAuthority-Type"></a>
Type of your private CA.
Type: String
Valid Values: `ROOT | SUBORDINATE`
Required: No

 ** UsageMode **   <a name="privateca-Type-CertificateAuthority-UsageMode"></a>
Specifies whether the CA issues general-purpose certificates that typically require a revocation mechanism, or short-lived certificates that may optionally omit revocation because they expire quickly. Short-lived certificate validity is limited to seven days.
The default value is GENERAL\_PURPOSE.
Type: String
Valid Values: `GENERAL_PURPOSE | SHORT_LIVED_CERTIFICATE`
Required: No

## See Also
<a name="API_CertificateAuthority_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-pca-2017-08-22/CertificateAuthority)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-pca-2017-08-22/CertificateAuthority)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-pca-2017-08-22/CertificateAuthority)
