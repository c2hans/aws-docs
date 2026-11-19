---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_FirewallDomainListMetadata.html
---

# FirewallDomainListMetadata

Minimal high-level information for a firewall domain list. The action [ListFirewallDomainLists](API_route53resolver_ListFirewallDomainLists.md) returns an array of these objects.

To retrieve full information for a firewall domain list, call [GetFirewallDomainList](API_route53resolver_GetFirewallDomainList.md) and [ListFirewallDomains](API_route53resolver_ListFirewallDomains.md).

## Contents
<a name="API_route53resolver_FirewallDomainListMetadata_Contents"></a>

 ** Arn **   <a name="Route53Resolver-Type-route53resolver_FirewallDomainListMetadata-Arn"></a>
The Amazon Resource Name (ARN) of the firewall domain list metadata.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** Category **   <a name="Route53Resolver-Type-route53resolver_FirewallDomainListMetadata-Category"></a>
The category of the domain list.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** CreatorRequestId **   <a name="Route53Resolver-Type-route53resolver_FirewallDomainListMetadata-CreatorRequestId"></a>
A unique string defined by you to identify the request. This allows you to retry failed requests without the risk of running the operation twice. This can be any unique string, for example, a timestamp.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** FirewallRuleGroupId **   <a name="Route53Resolver-Type-route53resolver_FirewallDomainListMetadata-FirewallRuleGroupId"></a>
For an AutoAllowlist domain list, the ID of the firewall rule group that contains the auto-allowlist rule that owns this domain list. Use it to navigate to the rule group and its VPC associations. Present only when `ManagedListType` is `AUTOALLOWLIST`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** FirewallThreatProtectionId **   <a name="Route53Resolver-Type-route53resolver_FirewallDomainListMetadata-FirewallThreatProtectionId"></a>
For an AutoAllowlist domain list, the threat protection ID of the auto-allowlist rule that owns this domain list. Provide it to [ListFirewallRuleDomains](API_route53resolver_ListFirewallRuleDomains.md) to review the observed, allowed, and denied domains. Present only when `ManagedListType` is `AUTOALLOWLIST`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** Id **   <a name="Route53Resolver-Type-route53resolver_FirewallDomainListMetadata-Id"></a>
The ID of the domain list.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** ManagedListType **   <a name="Route53Resolver-Type-route53resolver_FirewallDomainListMetadata-ManagedListType"></a>
The type of the managed domain list, for example `THREAT`.
Type: String
Valid Values: `THREAT | CONTENT | AUTOALLOWLIST`
Required: No

 ** ManagedOwnerName **   <a name="Route53Resolver-Type-route53resolver_FirewallDomainListMetadata-ManagedOwnerName"></a>
The owner of the list, used only for lists that are not managed by you. For example, the managed domain list `AWSManagedDomainsMalwareDomainList` has the managed owner name `Route 53 Resolver DNS Firewall`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** Name **   <a name="Route53Resolver-Type-route53resolver_FirewallDomainListMetadata-Name"></a>
The name of the domain list.
Type: String
Length Constraints: Maximum length of 64.
Pattern: `(?!^[0-9]+$)([a-zA-Z0-9\-_' ']+)`
Required: No

 ** Status **   <a name="Route53Resolver-Type-route53resolver_FirewallDomainListMetadata-Status"></a>
For an AutoAllowlist domain list, the status of the list: `IMPORTING` while domains are being copied from the source domain list specified at rule creation, `COMPLETE_IMPORT_FAILED` if that copy failed, `UPDATING` while a change made with [UpdateFirewallDomains](API_route53resolver_UpdateFirewallDomains.md) is being applied, `COMPLETE` otherwise, and `DELETING` while the owning rule is being deleted. The first change that you make after a failed copy replaces `COMPLETE_IMPORT_FAILED` with `UPDATING` and then `COMPLETE`. Present only when `ManagedListType` is `AUTOALLOWLIST`. Use [GetFirewallDomainList](API_route53resolver_GetFirewallDomainList.md) for the status of other domain lists.
Type: String
Valid Values: `COMPLETE | COMPLETE_IMPORT_FAILED | IMPORTING | DELETING | UPDATING`
Required: No

## See Also
<a name="API_route53resolver_FirewallDomainListMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53resolver-2018-04-01/FirewallDomainListMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53resolver-2018-04-01/FirewallDomainListMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53resolver-2018-04-01/FirewallDomainListMetadata)
