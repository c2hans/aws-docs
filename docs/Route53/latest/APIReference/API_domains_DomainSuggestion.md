---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_DomainSuggestion.html
---

# DomainSuggestion
<a name="API_domains_DomainSuggestion"></a>

Information about one suggested domain name.

## Contents
<a name="API_domains_DomainSuggestion_Contents"></a>

 ** Availability **   <a name="Route53Domains-Type-domains_DomainSuggestion-Availability"></a>
Whether the domain name is available for registering.
You can register only the domains that are designated as `AVAILABLE`.
Valid values:
AVAILABLE
The domain name is available.
AVAILABLE\_RESERVED
The domain name is reserved under specific conditions.
AVAILABLE\_PREORDER
The domain name is available and can be preordered.
DONT\_KNOW
The TLD registry didn't reply with a definitive answer about whether the domain name is available. Route 53 can return this response for a variety of reasons, for example, the registry is performing maintenance. Try again later.
PENDING
The TLD registry didn't return a response in the expected amount of time. When the response is delayed, it usually takes just a few extra seconds. You can resubmit the request immediately.
RESERVED
The domain name has been reserved for another person or organization.
UNAVAILABLE
The domain name is not available.
UNAVAILABLE\_PREMIUM
The domain name is not available.
UNAVAILABLE\_RESTRICTED
The domain name is forbidden.
Type: String
Required: No

 ** DomainName **   <a name="Route53Domains-Type-domains_DomainSuggestion-DomainName"></a>
A suggested domain name.
Type: String
Length Constraints: Maximum length of 255.
Required: No

## See Also
<a name="API_domains_DomainSuggestion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53domains-2014-05-15/DomainSuggestion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53domains-2014-05-15/DomainSuggestion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53domains-2014-05-15/DomainSuggestion)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
