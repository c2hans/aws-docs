---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_ManagedFirewallDomainListsItem.html
---

# ManagedFirewallDomainListsItem
<a name="API_route53globalresolver_ManagedFirewallDomainListsItem"></a>

Summary information about a managed firewall domain list.

## Contents
<a name="API_route53globalresolver_ManagedFirewallDomainListsItem_Contents"></a>

 ** id **   <a name="Route53GlobalResolver-Type-route53globalresolver_ManagedFirewallDomainListsItem-id"></a>
The unique identifier of the managed firewall domain list.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[-.a-zA-Z0-9]+`
Required: Yes

 ** managedListType **   <a name="Route53GlobalResolver-Type-route53globalresolver_ManagedFirewallDomainListsItem-managedListType"></a>
The type of the managed firewall domain list.
Type: String
Required: Yes

 ** name **   <a name="Route53GlobalResolver-Type-route53globalresolver_ManagedFirewallDomainListsItem-name"></a>
The name of the managed firewall domain list.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `(?!^[0-9]+$)([a-zA-Z0-9-_/' ']+)`
Required: Yes

 ** description **   <a name="Route53GlobalResolver-Type-route53globalresolver_ManagedFirewallDomainListsItem-description"></a>
A description of the managed firewall domain list.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_route53globalresolver_ManagedFirewallDomainListsItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53globalresolver-2022-09-27/ManagedFirewallDomainListsItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53globalresolver-2022-09-27/ManagedFirewallDomainListsItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53globalresolver-2022-09-27/ManagedFirewallDomainListsItem)
