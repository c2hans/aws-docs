---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsCertificateManagerCertificateRenewalSummary.html
---

# AwsCertificateManagerCertificateRenewalSummary
<a name="API_AwsCertificateManagerCertificateRenewalSummary"></a>

Contains information about the AWS Certificate Manager managed renewal for an `AMAZON_ISSUED` certificate.

## Contents
<a name="API_AwsCertificateManagerCertificateRenewalSummary_Contents"></a>

 ** DomainValidationOptions **   <a name="securityhub-Type-AwsCertificateManagerCertificateRenewalSummary-DomainValidationOptions"></a>
Information about the validation of each domain name in the certificate, as it pertains to AWS Certificate Manager managed renewal. Provided only when the certificate type is `AMAZON_ISSUED`.
Type: Array of [AwsCertificateManagerCertificateDomainValidationOption](API_AwsCertificateManagerCertificateDomainValidationOption.md) objects
Required: No

 ** RenewalStatus **   <a name="securityhub-Type-AwsCertificateManagerCertificateRenewalSummary-RenewalStatus"></a>
The status of the AWS Certificate Manager managed renewal of the certificate.
Valid values: `PENDING_AUTO_RENEWAL` \| `PENDING_VALIDATION` \| `SUCCESS` \| `FAILED`
Type: String
Pattern: `.*\S.*`
Required: No

 ** RenewalStatusReason **   <a name="securityhub-Type-AwsCertificateManagerCertificateRenewalSummary-RenewalStatusReason"></a>
The reason that a renewal request was unsuccessful. This attribute is used only when `RenewalStatus` is `FAILED`.
Valid values: `NO_AVAILABLE_CONTACTS` \| `ADDITIONAL_VERIFICATION_REQUIRED` \| `DOMAIN_NOT_ALLOWED` \| `INVALID_PUBLIC_DOMAIN` \| `DOMAIN_VALIDATION_DENIED` \| `CAA_ERROR` \| `PCA_LIMIT_EXCEEDED` \| `PCA_INVALID_ARN` \| `PCA_INVALID_STATE` \| `PCA_REQUEST_FAILED` \| `PCA_NAME_CONSTRAINTS_VALIDATION` \| `PCA_RESOURCE_NOT_FOUND` \| `PCA_INVALID_ARGS` \| `PCA_INVALID_DURATION` \| `PCA_ACCESS_DENIED` \| `SLR_NOT_FOUND` \| `OTHER`
Type: String
Pattern: `.*\S.*`
Required: No

 ** UpdatedAt **   <a name="securityhub-Type-AwsCertificateManagerCertificateRenewalSummary-UpdatedAt"></a>
Indicates when the renewal summary was last updated.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsCertificateManagerCertificateRenewalSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsCertificateManagerCertificateRenewalSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsCertificateManagerCertificateRenewalSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsCertificateManagerCertificateRenewalSummary)
