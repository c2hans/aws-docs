---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsCertificateManagerCertificateDetails.html
---

# AwsCertificateManagerCertificateDetails
<a name="API_AwsCertificateManagerCertificateDetails"></a>

Provides details about an AWS Certificate Manager certificate.

## Contents
<a name="API_AwsCertificateManagerCertificateDetails_Contents"></a>

 ** CertificateAuthorityArn **   <a name="securityhub-Type-AwsCertificateManagerCertificateDetails-CertificateAuthorityArn"></a>
The ARN of the private certificate authority (CA) that will be used to issue the certificate.
Type: String
Pattern: `.*\S.*`
Required: No

 ** CreatedAt **   <a name="securityhub-Type-AwsCertificateManagerCertificateDetails-CreatedAt"></a>
Indicates when the certificate was requested.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
Type: String
Pattern: `.*\S.*`
Required: No

 ** DomainName **   <a name="securityhub-Type-AwsCertificateManagerCertificateDetails-DomainName"></a>
The fully qualified domain name (FQDN), such as www.example.com, that is secured by the certificate.
Type: String
Pattern: `.*\S.*`
Required: No

 ** DomainValidationOptions **   <a name="securityhub-Type-AwsCertificateManagerCertificateDetails-DomainValidationOptions"></a>
Contains information about the initial validation of each domain name that occurs as a result of the `RequestCertificate` request.
Only provided if the certificate type is `AMAZON_ISSUED`.
Type: Array of [AwsCertificateManagerCertificateDomainValidationOption](API_AwsCertificateManagerCertificateDomainValidationOption.md) objects
Required: No

 ** ExtendedKeyUsages **   <a name="securityhub-Type-AwsCertificateManagerCertificateDetails-ExtendedKeyUsages"></a>
Contains a list of Extended Key Usage X.509 v3 extension objects. Each object specifies a purpose for which the certificate public key can be used and consists of a name and an object identifier (OID).
Type: Array of [AwsCertificateManagerCertificateExtendedKeyUsage](API_AwsCertificateManagerCertificateExtendedKeyUsage.md) objects
Required: No

 ** FailureReason **   <a name="securityhub-Type-AwsCertificateManagerCertificateDetails-FailureReason"></a>
For a failed certificate request, the reason for the failure.
Valid values: `NO_AVAILABLE_CONTACTS` \| `ADDITIONAL_VERIFICATION_REQUIRED` \| `DOMAIN_NOT_ALLOWED` \| `INVALID_PUBLIC_DOMAIN` \| `DOMAIN_VALIDATION_DENIED` \| `CAA_ERROR` \| `PCA_LIMIT_EXCEEDED` \| `PCA_INVALID_ARN` \| `PCA_INVALID_STATE` \| `PCA_REQUEST_FAILED` \| `PCA_NAME_CONSTRAINTS_VALIDATION` \| `PCA_RESOURCE_NOT_FOUND` \| `PCA_INVALID_ARGS` \| `PCA_INVALID_DURATION` \| `PCA_ACCESS_DENIED` \| `SLR_NOT_FOUND` \| `OTHER`
Type: String
Pattern: `.*\S.*`
Required: No

 ** ImportedAt **   <a name="securityhub-Type-AwsCertificateManagerCertificateDetails-ImportedAt"></a>
Indicates when the certificate was imported. Provided if the certificate type is `IMPORTED`.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
Type: String
Pattern: `.*\S.*`
Required: No

 ** InUseBy **   <a name="securityhub-Type-AwsCertificateManagerCertificateDetails-InUseBy"></a>
The list of ARNs for the AWS resources that use the certificate.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** IssuedAt **   <a name="securityhub-Type-AwsCertificateManagerCertificateDetails-IssuedAt"></a>
Indicates when the certificate was issued. Provided if the certificate type is `AMAZON_ISSUED`.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
Type: String
Pattern: `.*\S.*`
Required: No

 ** Issuer **   <a name="securityhub-Type-AwsCertificateManagerCertificateDetails-Issuer"></a>
The name of the certificate authority that issued and signed the certificate.
Type: String
Pattern: `.*\S.*`
Required: No

 ** KeyAlgorithm **   <a name="securityhub-Type-AwsCertificateManagerCertificateDetails-KeyAlgorithm"></a>
The algorithm that was used to generate the public-private key pair.
Valid values: `RSA_2048` \| `RSA_1024` \|` RSA_4096` \| `EC_prime256v1` \| `EC_secp384r1` \| `EC_secp521r1`
Type: String
Pattern: `.*\S.*`
Required: No

 ** KeyUsages **   <a name="securityhub-Type-AwsCertificateManagerCertificateDetails-KeyUsages"></a>
A list of key usage X.509 v3 extension objects.
Type: Array of [AwsCertificateManagerCertificateKeyUsage](API_AwsCertificateManagerCertificateKeyUsage.md) objects
Required: No

 ** NotAfter **   <a name="securityhub-Type-AwsCertificateManagerCertificateDetails-NotAfter"></a>
The time after which the certificate becomes invalid.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
Type: String
Pattern: `.*\S.*`
Required: No

 ** NotBefore **   <a name="securityhub-Type-AwsCertificateManagerCertificateDetails-NotBefore"></a>
The time before which the certificate is not valid.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
Type: String
Pattern: `.*\S.*`
Required: No

 ** Options **   <a name="securityhub-Type-AwsCertificateManagerCertificateDetails-Options"></a>
Provides a value that specifies whether to add the certificate to a transparency log.
Type: [AwsCertificateManagerCertificateOptions](API_AwsCertificateManagerCertificateOptions.md) object
Required: No

 ** RenewalEligibility **   <a name="securityhub-Type-AwsCertificateManagerCertificateDetails-RenewalEligibility"></a>
Whether the certificate is eligible for renewal.
Valid values: `ELIGIBLE` \| `INELIGIBLE`
Type: String
Pattern: `.*\S.*`
Required: No

 ** RenewalSummary **   <a name="securityhub-Type-AwsCertificateManagerCertificateDetails-RenewalSummary"></a>
Information about the status of the AWS Certificate Manager managed renewal for the certificate. Provided only when the certificate type is `AMAZON_ISSUED`.
Type: [AwsCertificateManagerCertificateRenewalSummary](API_AwsCertificateManagerCertificateRenewalSummary.md) object
Required: No

 ** Serial **   <a name="securityhub-Type-AwsCertificateManagerCertificateDetails-Serial"></a>
The serial number of the certificate.
Type: String
Pattern: `.*\S.*`
Required: No

 ** SignatureAlgorithm **   <a name="securityhub-Type-AwsCertificateManagerCertificateDetails-SignatureAlgorithm"></a>
The algorithm that was used to sign the certificate.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Status **   <a name="securityhub-Type-AwsCertificateManagerCertificateDetails-Status"></a>
The status of the certificate.
Valid values: `PENDING_VALIDATION` \| `ISSUED` \| `INACTIVE` \| `EXPIRED` \| `VALIDATION_TIMED_OUT` \| `REVOKED` \| `FAILED`
Type: String
Pattern: `.*\S.*`
Required: No

 ** Subject **   <a name="securityhub-Type-AwsCertificateManagerCertificateDetails-Subject"></a>
The name of the entity that is associated with the public key contained in the certificate.
Type: String
Pattern: `.*\S.*`
Required: No

 ** SubjectAlternativeNames **   <a name="securityhub-Type-AwsCertificateManagerCertificateDetails-SubjectAlternativeNames"></a>
One or more domain names (subject alternative names) included in the certificate. This list contains the domain names that are bound to the public key that is contained in the certificate.
The subject alternative names include the canonical domain name (CN) of the certificate and additional domain names that can be used to connect to the website.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** Type **   <a name="securityhub-Type-AwsCertificateManagerCertificateDetails-Type"></a>
The source of the certificate. For certificates that AWS Certificate Manager provides, `Type` is `AMAZON_ISSUED`. For certificates that are imported with `ImportCertificate`, `Type` is `IMPORTED`.
Valid values: `IMPORTED` \| `AMAZON_ISSUED` \| `PRIVATE`
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsCertificateManagerCertificateDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsCertificateManagerCertificateDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsCertificateManagerCertificateDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsCertificateManagerCertificateDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
