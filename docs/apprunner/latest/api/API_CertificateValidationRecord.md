---
source_url: https://docs.aws.amazon.com/apprunner/latest/api/API_CertificateValidationRecord.html
---

# CertificateValidationRecord
<a name="API_CertificateValidationRecord"></a>

Describes a certificate CNAME record to add to your DNS. For more information, see [AssociateCustomDomain](https://docs.aws.amazon.com/apprunner/latest/api/API_AssociateCustomDomain.html).

## Contents
<a name="API_CertificateValidationRecord_Contents"></a>

 ** Name **   <a name="apprunner-Type-CertificateValidationRecord-Name"></a>
The certificate CNAME record name.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 51200.
Pattern: `.*`
Required: No

 ** Status **   <a name="apprunner-Type-CertificateValidationRecord-Status"></a>
The current state of the certificate CNAME record validation. It should change to `SUCCESS` after App Runner completes validation with your DNS.
Type: String
Valid Values: `PENDING_VALIDATION | SUCCESS | FAILED`
Required: No

 ** Type **   <a name="apprunner-Type-CertificateValidationRecord-Type"></a>
The record type, always `CNAME`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 51200.
Pattern: `.*`
Required: No

 ** Value **   <a name="apprunner-Type-CertificateValidationRecord-Value"></a>
The certificate CNAME record value.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 51200.
Pattern: `.*`
Required: No

## See Also
<a name="API_CertificateValidationRecord_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apprunner-2020-05-15/CertificateValidationRecord)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apprunner-2020-05-15/CertificateValidationRecord)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apprunner-2020-05-15/CertificateValidationRecord)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS App Runner. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apprunner` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
