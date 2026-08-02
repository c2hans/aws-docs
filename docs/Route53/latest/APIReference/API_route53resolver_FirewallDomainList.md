---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_FirewallDomainList.html
---

# FirewallDomainList
<a name="API_route53resolver_FirewallDomainList"></a>

High-level information about a list of firewall domains for use in a [FirewallRule](API_route53resolver_FirewallRule.md). This is returned by [GetFirewallDomainList](API_route53resolver_GetFirewallDomainList.md).

To retrieve the domains that are defined for this domain list, call [ListFirewallDomains](API_route53resolver_ListFirewallDomains.md).

## Contents
<a name="API_route53resolver_FirewallDomainList_Contents"></a>

 ** Arn **   <a name="Route53Resolver-Type-route53resolver_FirewallDomainList-Arn"></a>
The Amazon Resource Name (ARN) of the firewall domain list.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** Category **   <a name="Route53Resolver-Type-route53resolver_FirewallDomainList-Category"></a>
The category of the domain list.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** CreationTime **   <a name="Route53Resolver-Type-route53resolver_FirewallDomainList-CreationTime"></a>
The date and time that the domain list was created, in Unix time format and Coordinated Universal Time (UTC).
Type: String
Length Constraints: Minimum length of 20. Maximum length of 40.
Required: No

 ** CreatorRequestId **   <a name="Route53Resolver-Type-route53resolver_FirewallDomainList-CreatorRequestId"></a>
A unique string defined by you to identify the request. This allows you to retry failed requests without the risk of running the operation twice. This can be any unique string, for example, a timestamp.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** DomainCount **   <a name="Route53Resolver-Type-route53resolver_FirewallDomainList-DomainCount"></a>
The number of domain names that are specified in the domain list.
Type: Integer
Required: No

 ** Id **   <a name="Route53Resolver-Type-route53resolver_FirewallDomainList-Id"></a>
The ID of the domain list.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** ManagedListType **   <a name="Route53Resolver-Type-route53resolver_FirewallDomainList-ManagedListType"></a>
The type of the managed domain list, for example `THREAT`.
Type: String
Valid Values: `THREAT | CONTENT`
Required: No

 ** ManagedOwnerName **   <a name="Route53Resolver-Type-route53resolver_FirewallDomainList-ManagedOwnerName"></a>
The owner of the list, used only for lists that are not managed by you. For example, the managed domain list `AWSManagedDomainsMalwareDomainList` has the managed owner name `Route 53 Resolver DNS Firewall`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** ModificationTime **   <a name="Route53Resolver-Type-route53resolver_FirewallDomainList-ModificationTime"></a>
The date and time that the domain list was last modified, in Unix time format and Coordinated Universal Time (UTC).
Type: String
Length Constraints: Minimum length of 20. Maximum length of 40.
Required: No

 ** Name **   <a name="Route53Resolver-Type-route53resolver_FirewallDomainList-Name"></a>
The name of the domain list.
Type: String
Length Constraints: Maximum length of 64.
Pattern: `(?!^[0-9]+$)([a-zA-Z0-9\-_' ']+)`
Required: No

 ** Status **   <a name="Route53Resolver-Type-route53resolver_FirewallDomainList-Status"></a>
The status of the domain list.
Type: String
Valid Values: `COMPLETE | COMPLETE_IMPORT_FAILED | IMPORTING | DELETING | UPDATING`
Required: No

 ** StatusMessage **   <a name="Route53Resolver-Type-route53resolver_FirewallDomainList-StatusMessage"></a>
Additional information about the status of the list, if available.
Type: String
Length Constraints: Maximum length of 255.
Required: No

## See Also
<a name="API_route53resolver_FirewallDomainList_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53resolver-2018-04-01/FirewallDomainList)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53resolver-2018-04-01/FirewallDomainList)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53resolver-2018-04-01/FirewallDomainList)
