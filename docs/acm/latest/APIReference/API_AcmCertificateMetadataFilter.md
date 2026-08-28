---
source_url: https://docs.aws.amazon.com/acm/latest/APIReference/API_AcmCertificateMetadataFilter.html
---

# AcmCertificateMetadataFilter
<a name="API_AcmCertificateMetadataFilter"></a>

Filters certificates by ACM metadata.

## Contents
<a name="API_AcmCertificateMetadataFilter_Contents"></a>

**Note**
In the following list, the required parameters are described first.

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** AcmeAccountId **   <a name="ACM-Type-AcmCertificateMetadataFilter-AcmeAccountId"></a>
Filter by ACME account identifier.
Type: String
Length Constraints: Fixed length of 36.
Required: No

 ** AcmeEndpointArn **   <a name="ACM-Type-AcmCertificateMetadataFilter-AcmeEndpointArn"></a>
Filter by ACME endpoint ARN.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[\w+=/,.@-]+:acm:[\w+=/,.@-]*:[0-9]+:[\w+=,.@-]+(/[\w+=,.@-]+)*`
Required: No

 ** CertificateKeyPairOrigin **   <a name="ACM-Type-AcmCertificateMetadataFilter-CertificateKeyPairOrigin"></a>
Filter by certificate key pair origin.
Type: String
Valid Values: `AWS_MANAGED | ACME | CUSTOMER_PROVIDED`
Required: No

 ** Exported **   <a name="ACM-Type-AcmCertificateMetadataFilter-Exported"></a>
Filter by whether the certificate has been exported.
Type: Boolean
Required: No

 ** ExportOption **   <a name="ACM-Type-AcmCertificateMetadataFilter-ExportOption"></a>
Filter by certificate export option.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** InUse **   <a name="ACM-Type-AcmCertificateMetadataFilter-InUse"></a>
Filter by whether the certificate is in use.
Type: Boolean
Required: No

 ** ManagedBy **   <a name="ACM-Type-AcmCertificateMetadataFilter-ManagedBy"></a>
Filter by the entity that manages the certificate.
Type: String
Valid Values: `CLOUDFRONT`
Required: No

 ** RenewalStatus **   <a name="ACM-Type-AcmCertificateMetadataFilter-RenewalStatus"></a>
Filter by certificate renewal status.
Type: String
Valid Values: `PENDING_AUTO_RENEWAL | PENDING_VALIDATION | SUCCESS | FAILED`
Required: No

 ** Status **   <a name="ACM-Type-AcmCertificateMetadataFilter-Status"></a>
Filter by certificate status.
Type: String
Valid Values: `PENDING_VALIDATION | ISSUED | INACTIVE | EXPIRED | VALIDATION_TIMED_OUT | REVOKED | FAILED`
Required: No

 ** Type **   <a name="ACM-Type-AcmCertificateMetadataFilter-Type"></a>
Filter by certificate type.
Type: String
Valid Values: `IMPORTED | AMAZON_ISSUED | PRIVATE`
Required: No

 ** ValidationMethod **   <a name="ACM-Type-AcmCertificateMetadataFilter-ValidationMethod"></a>
Filter by validation method.
Type: String
Valid Values: `EMAIL | DNS | HTTP`
Required: No

## See Also
<a name="API_AcmCertificateMetadataFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-2015-12-08/AcmCertificateMetadataFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-2015-12-08/AcmCertificateMetadataFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-2015-12-08/AcmCertificateMetadataFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for ACM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query acm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
