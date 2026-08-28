---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_FirewallDomainListMetadata.html
---

# FirewallDomainListMetadata
<a name="API_route53resolver_FirewallDomainListMetadata"></a>

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

 ** Id **   <a name="Route53Resolver-Type-route53resolver_FirewallDomainListMetadata-Id"></a>
The ID of the domain list.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** ManagedListType **   <a name="Route53Resolver-Type-route53resolver_FirewallDomainListMetadata-ManagedListType"></a>
The type of the managed domain list, for example `THREAT`.
Type: String
Valid Values: `THREAT | CONTENT`
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

## See Also
<a name="API_route53resolver_FirewallDomainListMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53resolver-2018-04-01/FirewallDomainListMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53resolver-2018-04-01/FirewallDomainListMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53resolver-2018-04-01/FirewallDomainListMetadata)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
