---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_DomainSummary.html
---

# DomainSummary
<a name="API_domains_DomainSummary"></a>

Summary information about one domain.

## Contents
<a name="API_domains_DomainSummary_Contents"></a>

 ** AutoRenew **   <a name="Route53Domains-Type-domains_DomainSummary-AutoRenew"></a>
Indicates whether the domain is automatically renewed upon expiration.
Type: Boolean
Required: No

 ** DomainName **   <a name="Route53Domains-Type-domains_DomainSummary-DomainName"></a>
The name of the domain that the summary information applies to.
Type: String
Length Constraints: Maximum length of 255.
Required: No

 ** Expiry **   <a name="Route53Domains-Type-domains_DomainSummary-Expiry"></a>
Expiration date of the domain in Unix time format and Coordinated Universal Time (UTC).
Type: Timestamp
Required: No

 ** TransferLock **   <a name="Route53Domains-Type-domains_DomainSummary-TransferLock"></a>
Indicates whether a domain is locked from unauthorized transfer to another party.
Type: Boolean
Required: No

## See Also
<a name="API_domains_DomainSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53domains-2014-05-15/DomainSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53domains-2014-05-15/DomainSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53domains-2014-05-15/DomainSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
