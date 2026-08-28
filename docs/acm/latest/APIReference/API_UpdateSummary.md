---
source_url: https://docs.aws.amazon.com/acm/latest/APIReference/API_UpdateSummary.html
---

# UpdateSummary
<a name="API_UpdateSummary"></a>

Contains information about the most recent certificate update, such as a domain validation method migration. This structure is returned as part of the [CertificateDetail](API_CertificateDetail.md) response from [DescribeCertificate](API_DescribeCertificate.md).

## Contents
<a name="API_UpdateSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** DomainValidationMethodUpdateSummary **   <a name="ACM-Type-UpdateSummary-DomainValidationMethodUpdateSummary"></a>
Contains information about a domain validation method migration, including the previous and target validation methods.
Type: [DomainValidationMethodUpdateSummary](API_DomainValidationMethodUpdateSummary.md) object
Required: No

 ** RequestedAt **   <a name="ACM-Type-UpdateSummary-RequestedAt"></a>
The time at which the certificate update was requested.
Type: Timestamp
Required: No

 ** Status **   <a name="ACM-Type-UpdateSummary-Status"></a>
The status of the certificate update. The following are valid values:
+  `PENDING_DOMAIN_VALIDATION` – The certificate update is waiting for domain ownership validation to complete.
+  `SUCCESS` – The certificate was updated successfully.
+  `FAILED` – The certificate update failed.
Type: String
Valid Values: `PENDING_DOMAIN_VALIDATION | SUCCESS | FAILED`
Required: No

 ** Type **   <a name="ACM-Type-UpdateSummary-Type"></a>
The type of update that was requested for the certificate. The following are valid values:
+  `DOMAIN_VALIDATION_METHOD` – The update changes the domain validation method for the certificate.
Type: String
Valid Values: `DOMAIN_VALIDATION_METHOD`
Required: No

 ** UpdatedAt **   <a name="ACM-Type-UpdateSummary-UpdatedAt"></a>
The time at which the certificate update status was last changed.
Type: Timestamp
Required: No

## See Also
<a name="API_UpdateSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-2015-12-08/UpdateSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-2015-12-08/UpdateSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-2015-12-08/UpdateSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for ACM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query acm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
