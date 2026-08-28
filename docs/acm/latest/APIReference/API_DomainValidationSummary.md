---
source_url: https://docs.aws.amazon.com/acm/latest/APIReference/API_DomainValidationSummary.html
---

# DomainValidationSummary
<a name="API_DomainValidationSummary"></a>

Contains per-domain validation information for a certificate. This structure is returned as a member of the [ListCertificateDomainValidations](API_ListCertificateDomainValidations.md) response.

## Contents
<a name="API_DomainValidationSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** DomainName **   <a name="ACM-Type-DomainValidationSummary-DomainName"></a>
The fully qualified domain name (FQDN) in the certificate for which this validation summary applies.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 253.
Pattern: `(\*\.)?(((?!-)[A-Za-z0-9-]{0,62}[A-Za-z0-9])\.)+((?!-)[A-Za-z0-9-]{1,62}[A-Za-z0-9])`
Required: Yes

 ** ActiveValidationConfiguration **   <a name="ACM-Type-DomainValidationSummary-ActiveValidationConfiguration"></a>
The validation configuration currently in effect for this domain. This reflects the validation method that ACM is currently using to validate domain ownership (for example, email or DNS).
Type: [ValidationConfiguration](API_ValidationConfiguration.md) object
Required: No

 ** RequestedValidationConfiguration **   <a name="ACM-Type-DomainValidationSummary-RequestedValidationConfiguration"></a>
The validation configuration for a pending validation method migration. This field is present only when a migration is in progress (for example, from email to DNS validation). It contains the target validation method, the current validation status, and the validation challenge details (such as the CNAME record to add to your DNS configuration).
Type: [ValidationConfiguration](API_ValidationConfiguration.md) object
Required: No

## See Also
<a name="API_DomainValidationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-2015-12-08/DomainValidationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-2015-12-08/DomainValidationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-2015-12-08/DomainValidationSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for ACM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query acm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
