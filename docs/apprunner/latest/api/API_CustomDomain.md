---
source_url: https://docs.aws.amazon.com/apprunner/latest/api/API_CustomDomain.html
---

# CustomDomain
<a name="API_CustomDomain"></a>

Describes a custom domain that's associated with an AWS App Runner service.

## Contents
<a name="API_CustomDomain_Contents"></a>

 ** DomainName **   <a name="apprunner-Type-CustomDomain-DomainName"></a>
An associated custom domain endpoint. It can be a root domain (for example, `example.com`), a subdomain (for example, `login.example.com` or `admin.login.example.com`), or a wildcard (for example, `*.example.com`).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[A-Za-z0-9*.-]{1,255}`
Required: Yes

 ** EnableWWWSubdomain **   <a name="apprunner-Type-CustomDomain-EnableWWWSubdomain"></a>
When `true`, the subdomain `www.DomainName ` is associated with the App Runner service in addition to the base domain.
Type: Boolean
Required: Yes

 ** Status **   <a name="apprunner-Type-CustomDomain-Status"></a>
The current state of the domain name association.
Type: String
Valid Values: `CREATING | CREATE_FAILED | ACTIVE | DELETING | DELETE_FAILED | PENDING_CERTIFICATE_DNS_VALIDATION | BINDING_CERTIFICATE`
Required: Yes

 ** CertificateValidationRecords **   <a name="apprunner-Type-CustomDomain-CertificateValidationRecords"></a>
A list of certificate CNAME records that's used for this domain name.
Type: Array of [CertificateValidationRecord](API_CertificateValidationRecord.md) objects
Required: No

## See Also
<a name="API_CustomDomain_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apprunner-2020-05-15/CustomDomain)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apprunner-2020-05-15/CustomDomain)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apprunner-2020-05-15/CustomDomain)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS App Runner. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apprunner` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
