---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_AutoAllowlistConfig.html
---

# AutoAllowlistConfig
<a name="API_route53resolver_AutoAllowlistConfig"></a>

The configuration for an AutoAllowlist firewall rule, which observes the DNS traffic of the VPCs that use the rule group, through a rule group association or a Route 53 Profile. The rule allows the domains on its managed domain list. When you create the rule, DNS Firewall seeds the observed domains from the look-back window of each VPC. After that, a domain is listed as observed when any DNS Firewall rule blocks a query for it from a VPC that uses the rule group, including rules in other rule groups, so place a rule that blocks the domains you haven't approved after the AutoAllowlist rule. To review the observed domains, call [ListFirewallRuleDomains](API_route53resolver_ListFirewallRuleDomains.md). To approve or deny them, call [UpdateFirewallDomains](API_route53resolver_UpdateFirewallDomains.md) on the rule's managed domain list.

An AutoAllowlist rule uses the `ALLOW` action, applies to all query types, and always inspects redirection domains. You can't set `Qtype`, `FirewallDomainRedirectionAction`, `BlockResponse`, or the DNS Firewall Advanced settings on it. A rule group can contain one AutoAllowlist rule.

A new AutoAllowlist rule has status `CREATING` while DNS Firewall reads the look-back window of each VPC that uses the rule group, which can take hours for a rule group that many VPCs use. Until the status is `COMPLETE`, the observed domains and request counts are partial and [UpdateFirewallRule](API_route53resolver_UpdateFirewallRule.md) rejects the rule. You can approve, remove, and deny domains while the rule is `CREATING`.

## Contents
<a name="API_route53resolver_AutoAllowlistConfig_Contents"></a>

 ** InitialDataTimeframeHours **   <a name="Route53Resolver-Type-route53resolver_AutoAllowlistConfig-InitialDataTimeframeHours"></a>
The look-back window, in hours, of historical DNS traffic that DNS Firewall uses to seed the initial set of observed domains when you create the rule. Valid values are from `1` to `168` (7 days). You can't change this value after you create the rule.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 168.
Required: Yes

 ** AutoAllowlistFirewallDomainListId **   <a name="Route53Resolver-Type-route53resolver_AutoAllowlistConfig-AutoAllowlistFirewallDomainListId"></a>
The ID of the managed domain list that DNS Firewall creates and maintains for this AutoAllowlist rule. The list is named `AutoAllowlist - ` followed by the rule name, cut to 64 characters, and is renamed when you rename the rule. DNS Firewall returns this value in responses. You can't set it.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** ImportFromFirewallDomainListId **   <a name="Route53Resolver-Type-route53resolver_AutoAllowlistConfig-ImportFromFirewallDomainListId"></a>
The ID of a domain list whose domains DNS Firewall copies into the AutoAllowlist rule's managed domain list after you create the rule. You must own the source list, and it must be in `COMPLETE` status, in the same Region, and not a managed or AutoAllowlist list. DNS Firewall reads the source list while the copy runs, so don't change or delete it until the managed list's status is no longer `IMPORTING`. A change made to the source list during the copy can be reflected in the managed list, and deleting the source list fails the copy. The managed list then has status `COMPLETE`, or `COMPLETE_IMPORT_FAILED` if the copy failed. DNS Firewall uses this value only when you create the rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

## See Also
<a name="API_route53resolver_AutoAllowlistConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53resolver-2018-04-01/AutoAllowlistConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53resolver-2018-04-01/AutoAllowlistConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53resolver-2018-04-01/AutoAllowlistConfig)
