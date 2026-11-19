---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_FirewallRuleDomain.html
---

# FirewallRuleDomain

A domain that DNS Firewall observed for an AutoAllowlist rule, with its review status and request volume. Counts are aggregated across all VPCs that use the rule group, through a rule group association or through a Route 53 Profile that includes the rule group, including VPCs in other accounts. The domain isn't attributed to the VPC or account in which it was observed.

## Contents
<a name="API_route53resolver_FirewallRuleDomain_Contents"></a>

 ** AddedTime **   <a name="Route53Resolver-Type-route53resolver_FirewallRuleDomain-AddedTime"></a>
The date and time when the domain was first observed and added, in RFC 3339 format.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 40.
Required: No

 ** DomainName **   <a name="Route53Resolver-Type-route53resolver_FirewallRuleDomain-DomainName"></a>
The domain name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** DomainStatus **   <a name="Route53Resolver-Type-route53resolver_FirewallRuleDomain-DomainStatus"></a>
The review status of the domain:
+  `OBSERVED` - DNS Firewall saw the domain in the VPCs' DNS traffic and you haven't allowed or denied it. The look-back window seeds the initial observed domains. After that, a domain becomes observed when any DNS Firewall rule blocks a query for it from a VPC that uses the rule group, including rules in other rule groups, or when you remove it from the managed domain list with `REMOVE`. To keep observing new domains, place a rule that blocks the domains you haven't approved after the AutoAllowlist rule. Domains from the look-back period that keep being queried and aren't blocked move to `ALLOWED` within about a day after the rule is created. Observed domains aren't evaluated for safety, so review them before you allow them.
+  `ALLOWED` - DNS Firewall allowed queries for the domain, whether or not the domain is in the rule's managed domain list. To get the domains in the managed domain list (the allowlist that the rule enforces), call [ListFirewallRuleDomains](API_route53resolver_ListFirewallRuleDomains.md) with `FirewallDomainListId`.
+  `DENIED` - The domain was denied with the `DENY` operation of [UpdateFirewallDomains](API_route53resolver_UpdateFirewallDomains.md), which also removes it from the managed domain list if it was there. A denied domain that is still queried and not blocked can move to `ALLOWED`.
Type: String
Valid Values: `OBSERVED | ALLOWED | DENIED | UNKNOWN`
Required: No

 ** Last24HourRequests **   <a name="Route53Resolver-Type-route53resolver_FirewallRuleDomain-Last24HourRequests"></a>
The number of DNS requests observed for this domain in the last 24 hours.
Type: Long
Required: No

 ** TotalRequests **   <a name="Route53Resolver-Type-route53resolver_FirewallRuleDomain-TotalRequests"></a>
The total number of DNS requests observed for this domain since it was first added, including the requests in the look-back window that seeded the rule.
Type: Long
Required: No

## See Also
<a name="API_route53resolver_FirewallRuleDomain_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53resolver-2018-04-01/FirewallRuleDomain)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53resolver-2018-04-01/FirewallRuleDomain)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53resolver-2018-04-01/FirewallRuleDomain)
