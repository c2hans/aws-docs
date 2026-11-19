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
+  `OBSERVED` - Domains that DNS Firewall saw in the VPCs' DNS traffic and that you haven't allowed or denied. After the look-back window, a domain is observed when any DNS Firewall rule blocks a query for it from a VPC that uses the rule group, including rules in other rule groups, or when you remove it from the managed domain list. Domains from the look-back period that keep being queried and aren't blocked move to `ALLOWED` within about a day after the rule is created.
+  `ALLOWED` - Domains that DNS Firewall allowed queries for, whether or not they're in the rule's managed domain list.
+  `DENIED` - Domains that were denied with the `DENY` operation. A denied domain that is still queried and not blocked can move to `ALLOWED`.
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
