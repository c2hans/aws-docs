---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_FirewallRulesItem.html
---

# FirewallRulesItem
<a name="API_route53globalresolver_FirewallRulesItem"></a>

Summary information about a firewall rule.

## Contents
<a name="API_route53globalresolver_FirewallRulesItem_Contents"></a>

 ** action **   <a name="Route53GlobalResolver-Type-route53globalresolver_FirewallRulesItem-action"></a>
The action configured for the firewall rule.
Type: String
Valid Values: `ALLOW | ALERT | BLOCK`
Required: Yes

 ** createdAt **   <a name="Route53GlobalResolver-Type-route53globalresolver_FirewallRulesItem-createdAt"></a>
The date and time when the firewall rule was created.
Type: Timestamp
Required: Yes

 ** dnsViewId **   <a name="Route53GlobalResolver-Type-route53globalresolver_FirewallRulesItem-dnsViewId"></a>
The ID of the DNS view associated with the firewall rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[-.a-zA-Z0-9]+`
Required: Yes

 ** id **   <a name="Route53GlobalResolver-Type-route53globalresolver_FirewallRulesItem-id"></a>
The unique identifier of the firewall rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[-.a-zA-Z0-9]+`
Required: Yes

 ** name **   <a name="Route53GlobalResolver-Type-route53globalresolver_FirewallRulesItem-name"></a>
The name of the firewall rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `(?!^[0-9]+$)([a-zA-Z0-9-_/' ']+)`
Required: Yes

 ** priority **   <a name="Route53GlobalResolver-Type-route53globalresolver_FirewallRulesItem-priority"></a>
The priority of the firewall rule.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 10000.
Required: Yes

 ** status **   <a name="Route53GlobalResolver-Type-route53globalresolver_FirewallRulesItem-status"></a>
The current status of the firewall rule.
Type: String
Valid Values: `CREATING | OPERATIONAL | UPDATING | DELETING`
Required: Yes

 ** updatedAt **   <a name="Route53GlobalResolver-Type-route53globalresolver_FirewallRulesItem-updatedAt"></a>
The date and time when the firewall rule was last updated.
Type: Timestamp
Required: Yes

 ** blockOverrideDnsType **   <a name="Route53GlobalResolver-Type-route53globalresolver_FirewallRulesItem-blockOverrideDnsType"></a>
The DNS record type configured for the firewall rule's custom response.
Type: String
Valid Values: `CNAME`
Required: No

 ** blockOverrideDomain **   <a name="Route53GlobalResolver-Type-route53globalresolver_FirewallRulesItem-blockOverrideDomain"></a>
The custom domain name configured for the firewall rule's BLOCK response.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `\*?[a-zA-Z0-9!"#$%&'()*+,./:;<=>?@\[\\\]^_`{|}~-]+`
Required: No

 ** blockOverrideTtl **   <a name="Route53GlobalResolver-Type-route53globalresolver_FirewallRulesItem-blockOverrideTtl"></a>
The TTL value configured for the firewall rule's custom response.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 604800.
Required: No

 ** blockResponse **   <a name="Route53GlobalResolver-Type-route53globalresolver_FirewallRulesItem-blockResponse"></a>
The type of block response configured for the firewall rule.
Type: String
Valid Values: `NODATA | NXDOMAIN | OVERRIDE`
Required: No

 ** confidenceThreshold **   <a name="Route53GlobalResolver-Type-route53globalresolver_FirewallRulesItem-confidenceThreshold"></a>
The confidence threshold configured for the firewall rule's advanced threat detection.
Type: String
Valid Values: `LOW | MEDIUM | HIGH`
Required: No

 ** description **   <a name="Route53GlobalResolver-Type-route53globalresolver_FirewallRulesItem-description"></a>
The description of the firewall rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** dnsAdvancedProtection **   <a name="Route53GlobalResolver-Type-route53globalresolver_FirewallRulesItem-dnsAdvancedProtection"></a>
Whether advanced DNS threat protection is enabled for the firewall rule.
Type: String
Valid Values: `DGA | DNS_TUNNELING | DICTIONARY_DGA`
Required: No

 ** firewallDomainListId **   <a name="Route53GlobalResolver-Type-route53globalresolver_FirewallRulesItem-firewallDomainListId"></a>
The ID of the firewall domain list associated with the firewall rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[-.a-zA-Z0-9]+`
Required: No

 ** queryType **   <a name="Route53GlobalResolver-Type-route53globalresolver_FirewallRulesItem-queryType"></a>
The DNS query type that the firewall rule matches.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 16.
Required: No

## See Also
<a name="API_route53globalresolver_FirewallRulesItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53globalresolver-2022-09-27/FirewallRulesItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53globalresolver-2022-09-27/FirewallRulesItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53globalresolver-2022-09-27/FirewallRulesItem)
