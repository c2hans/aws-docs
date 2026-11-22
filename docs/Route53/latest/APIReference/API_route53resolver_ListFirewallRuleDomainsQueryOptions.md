---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ListFirewallRuleDomainsQueryOptions.html
---

# ListFirewallRuleDomainsQueryOptions

Optional filters and sort order for [ListFirewallRuleDomains](API_route53resolver_ListFirewallRuleDomains.md).

## Contents
<a name="API_route53resolver_ListFirewallRuleDomainsQueryOptions_Contents"></a>

 ** DomainNameFilter **   <a name="Route53Resolver-Type-route53resolver_ListFirewallRuleDomainsQueryOptions-DomainNameFilter"></a>
Returns only the domains whose name contains this substring.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** DomainStatus **   <a name="Route53Resolver-Type-route53resolver_ListFirewallRuleDomainsQueryOptions-DomainStatus"></a>
Filters the returned domains by review status. Valid values:
+  `OBSERVED` - DNS Firewall saw the domain in the VPCs' DNS traffic and listed it for your review. The look-back window seeds the initial observed domains. After that, a domain becomes observed when any DNS Firewall rule blocks a query for it from a VPC that uses the rule group, including rules in other rule groups, or when you remove it from the managed domain list with `REMOVE`. An observed domain can already be on the managed domain list, for example when a rule that is evaluated before the AutoAllowlist rule blocks it. An `ADD` request fails as a whole if any of its domains is already on the list, so check the list first by calling [ListFirewallRuleDomains](API_route53resolver_ListFirewallRuleDomains.md) with `FirewallDomainListId`. The managed domain list returns each domain name with a trailing period (for example, `example.com.`), and the observed, allowed, and denied domains are returned without one (`example.com`), so remove the trailing period before you compare them. DNS Firewall keeps up to 10,000 domains in each status for a rule. While a status is full, a newly blocked domain might not be listed. Allowing or denying observed domains makes room, and so do observed domains that stop being queried. To find blocked domains that aren't listed, check your Resolver query logs. For more information, see [Considerations for Automated Allowlists](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/firewall-advanced-automated-allowlists.html#firewall-advanced-automated-allowlists-considerations) in the *Amazon Route 53 Developer Guide*. To keep observing new domains, place a rule that blocks the domains you haven't approved after the AutoAllowlist rule. Domains from the look-back period that keep being queried and aren't blocked move to `ALLOWED` about a day after DNS Firewall reads them from the look-back window. Observed domains can include domains that a threat protection rule blocked, and the response doesn't say which rule blocked a domain, so review them before you allow them. Place rules that block known threats before the AutoAllowlist rule in each VPC's rule evaluation order, so that an allowed domain can't bypass them.
+  `ALLOWED` - DNS Firewall allowed queries for the domain, whether or not the domain is in the rule's managed domain list. A domain that you approve with the `ADD` operation of [UpdateFirewallDomains](API_route53resolver_UpdateFirewallDomains.md) is also listed as allowed. To get the domains in the managed domain list (the allowlist that the rule enforces), call [ListFirewallRuleDomains](API_route53resolver_ListFirewallRuleDomains.md) with `FirewallDomainListId`. Names in the managed domain list end with a trailing period, and names returned for a status don't.
+  `DENIED` - The domain was denied with the `DENY` operation of [UpdateFirewallDomains](API_route53resolver_UpdateFirewallDomains.md), which also removes it from the managed domain list if it was there. A denied domain that is still queried and not blocked can move to `ALLOWED`.
If you don't specify a value, the operation returns `OBSERVED` domains.
Type: String
Valid Values: `OBSERVED | ALLOWED | DENIED`
Required: No

 ** SortBy **   <a name="Route53Resolver-Type-route53resolver_ListFirewallRuleDomainsQueryOptions-SortBy"></a>
The attribute to sort the returned domains by. Valid values:
+  `TIME_ADDED` - The `AddedTime` of the domain.
+  `DAILY_TOTAL` - The `Last24HourRequests` count.
+  `TOTAL_REQUESTS` - The `TotalRequests` count.
If you don't specify a value, the operation sorts by `TIME_ADDED`.
Type: String
Valid Values: `TIME_ADDED | DAILY_TOTAL | TOTAL_REQUESTS`
Required: No

 ** SortOrder **   <a name="Route53Resolver-Type-route53resolver_ListFirewallRuleDomainsQueryOptions-SortOrder"></a>
The sort direction: `ASC` for ascending or `DESC` for descending. If you don't specify a value, the operation sorts in descending order.
Type: String
Valid Values: `ASC | DESC`
Required: No

## See Also
<a name="API_route53resolver_ListFirewallRuleDomainsQueryOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53resolver-2018-04-01/ListFirewallRuleDomainsQueryOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53resolver-2018-04-01/ListFirewallRuleDomainsQueryOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53resolver-2018-04-01/ListFirewallRuleDomainsQueryOptions)
