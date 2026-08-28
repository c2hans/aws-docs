---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsCertificateManagerCertificateDomainValidationOption.html
---

# AwsCertificateManagerCertificateDomainValidationOption
<a name="API_AwsCertificateManagerCertificateDomainValidationOption"></a>

Contains information about one of the following:
+ The initial validation of each domain name that occurs as a result of the `RequestCertificate` request
+ The validation of each domain name in the certificate, as it pertains to AWS Certificate Manager managed renewal

## Contents
<a name="API_AwsCertificateManagerCertificateDomainValidationOption_Contents"></a>

 ** DomainName **   <a name="securityhub-Type-AwsCertificateManagerCertificateDomainValidationOption-DomainName"></a>
A fully qualified domain name (FQDN) in the certificate.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ResourceRecord **   <a name="securityhub-Type-AwsCertificateManagerCertificateDomainValidationOption-ResourceRecord"></a>
The CNAME record that is added to the DNS database for domain validation.
Type: [AwsCertificateManagerCertificateResourceRecord](API_AwsCertificateManagerCertificateResourceRecord.md) object
Required: No

 ** ValidationDomain **   <a name="securityhub-Type-AwsCertificateManagerCertificateDomainValidationOption-ValidationDomain"></a>
The domain name that AWS Certificate Manager uses to send domain validation emails.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ValidationEmails **   <a name="securityhub-Type-AwsCertificateManagerCertificateDomainValidationOption-ValidationEmails"></a>
A list of email addresses that AWS Certificate Manager uses to send domain validation emails.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** ValidationMethod **   <a name="securityhub-Type-AwsCertificateManagerCertificateDomainValidationOption-ValidationMethod"></a>
The method used to validate the domain name.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ValidationStatus **   <a name="securityhub-Type-AwsCertificateManagerCertificateDomainValidationOption-ValidationStatus"></a>
The validation status of the domain name.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsCertificateManagerCertificateDomainValidationOption_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsCertificateManagerCertificateDomainValidationOption)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsCertificateManagerCertificateDomainValidationOption)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsCertificateManagerCertificateDomainValidationOption)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
