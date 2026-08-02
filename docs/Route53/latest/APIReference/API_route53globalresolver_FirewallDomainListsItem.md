---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_FirewallDomainListsItem.html
---

# FirewallDomainListsItem
<a name="API_route53globalresolver_FirewallDomainListsItem"></a>

Summary information about a firewall domain list.

## Contents
<a name="API_route53globalresolver_FirewallDomainListsItem_Contents"></a>

 ** arn **   <a name="Route53GlobalResolver-Type-route53globalresolver_FirewallDomainListsItem-arn"></a>
The Amazon Resource Name (ARN) of the firewall domain list.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:[-.a-z0-9]{1,63}:[-.a-z0-9]{1,63}:[-.a-z0-9]{0,63}:[-.a-z0-9]{0,63}:[^/].{0,1023}`
Required: Yes

 ** createdAt **   <a name="Route53GlobalResolver-Type-route53globalresolver_FirewallDomainListsItem-createdAt"></a>
The date and time when the firewall domain list was created.
Type: Timestamp
Required: Yes

 ** globalResolverId **   <a name="Route53GlobalResolver-Type-route53globalresolver_FirewallDomainListsItem-globalResolverId"></a>
The ID of the global resolver that the firewall domain list is associated with.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[-.a-zA-Z0-9]+`
Required: Yes

 ** id **   <a name="Route53GlobalResolver-Type-route53globalresolver_FirewallDomainListsItem-id"></a>
The unique identifier of the firewall domain list.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[-.a-zA-Z0-9]+`
Required: Yes

 ** name **   <a name="Route53GlobalResolver-Type-route53globalresolver_FirewallDomainListsItem-name"></a>
The name of the firewall domain list.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `(?!^[0-9]+$)([a-zA-Z0-9-_/' ']+)`
Required: Yes

 ** status **   <a name="Route53GlobalResolver-Type-route53globalresolver_FirewallDomainListsItem-status"></a>
The current status of the firewall domain list.
Type: String
Valid Values: `CREATING | OPERATIONAL | UPDATING | DELETING`
Required: Yes

 ** updatedAt **   <a name="Route53GlobalResolver-Type-route53globalresolver_FirewallDomainListsItem-updatedAt"></a>
The date and time when the firewall domain list was last updated.
Type: Timestamp
Required: Yes

 ** description **   <a name="Route53GlobalResolver-Type-route53globalresolver_FirewallDomainListsItem-description"></a>
A description of the firewall domain list.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_route53globalresolver_FirewallDomainListsItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53globalresolver-2022-09-27/FirewallDomainListsItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53globalresolver-2022-09-27/FirewallDomainListsItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53globalresolver-2022-09-27/FirewallDomainListsItem)
