---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_BatchCreateFirewallRuleInputItem.html
---

# BatchCreateFirewallRuleInputItem
<a name="API_route53globalresolver_BatchCreateFirewallRuleInputItem"></a>

Information about a DNS Firewall rule to create in a batch operation.

## Contents
<a name="API_route53globalresolver_BatchCreateFirewallRuleInputItem_Contents"></a>

 ** action **   <a name="Route53GlobalResolver-Type-route53globalresolver_BatchCreateFirewallRuleInputItem-action"></a>
The action to take when a DNS query matches the firewall rule.
Type: String
Valid Values: `ALLOW | ALERT | BLOCK`
Required: Yes

 ** clientToken **   <a name="Route53GlobalResolver-Type-route53globalresolver_BatchCreateFirewallRuleInputItem-clientToken"></a>
A unique string that identifies the request and ensures idempotency.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** dnsViewId **   <a name="Route53GlobalResolver-Type-route53globalresolver_BatchCreateFirewallRuleInputItem-dnsViewId"></a>
The ID of the DNS view to associate the firewall rule with.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[-.a-zA-Z0-9]+`
Required: Yes

 ** name **   <a name="Route53GlobalResolver-Type-route53globalresolver_BatchCreateFirewallRuleInputItem-name"></a>
A name for the firewall rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `(?!^[0-9]+$)([a-zA-Z0-9-_/' ']+)`
Required: Yes

 ** blockOverrideDnsType **   <a name="Route53GlobalResolver-Type-route53globalresolver_BatchCreateFirewallRuleInputItem-blockOverrideDnsType"></a>
The DNS record type for the custom response when the action is BLOCK.
Type: String
Valid Values: `CNAME`
Required: No

 ** blockOverrideDomain **   <a name="Route53GlobalResolver-Type-route53globalresolver_BatchCreateFirewallRuleInputItem-blockOverrideDomain"></a>
The custom domain name for the BLOCK response.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `\*?[a-zA-Z0-9!"#$%&'()*+,./:;<=>?@\[\\\]^_`{|}~-]+`
Required: No

 ** blockOverrideTtl **   <a name="Route53GlobalResolver-Type-route53globalresolver_BatchCreateFirewallRuleInputItem-blockOverrideTtl"></a>
The TTL value for the custom response when the action is BLOCK.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 604800.
Required: No

 ** blockResponse **   <a name="Route53GlobalResolver-Type-route53globalresolver_BatchCreateFirewallRuleInputItem-blockResponse"></a>
The type of block response to return when the action is BLOCK.
Type: String
Valid Values: `NODATA | NXDOMAIN | OVERRIDE`
Required: No

 ** confidenceThreshold **   <a name="Route53GlobalResolver-Type-route53globalresolver_BatchCreateFirewallRuleInputItem-confidenceThreshold"></a>
The confidence threshold for advanced threat detection.
Type: String
Valid Values: `LOW | MEDIUM | HIGH`
Required: No

 ** description **   <a name="Route53GlobalResolver-Type-route53globalresolver_BatchCreateFirewallRuleInputItem-description"></a>
A description of the firewall rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** dnsAdvancedProtection **   <a name="Route53GlobalResolver-Type-route53globalresolver_BatchCreateFirewallRuleInputItem-dnsAdvancedProtection"></a>
Whether to enable advanced DNS threat protection for the firewall rule.
Type: String
Valid Values: `DGA | DNS_TUNNELING | DICTIONARY_DGA`
Required: No

 ** firewallDomainListId **   <a name="Route53GlobalResolver-Type-route53globalresolver_BatchCreateFirewallRuleInputItem-firewallDomainListId"></a>
The ID of the firewall domain list to associate with the rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[-.a-zA-Z0-9]+`
Required: No

 ** priority **   <a name="Route53GlobalResolver-Type-route53globalresolver_BatchCreateFirewallRuleInputItem-priority"></a>
The priority of the firewall rule.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 10000.
Required: No

 ** qType **   <a name="Route53GlobalResolver-Type-route53globalresolver_BatchCreateFirewallRuleInputItem-qType"></a>
The DNS query type that the firewall rule should match.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 16.
Required: No

## See Also
<a name="API_route53globalresolver_BatchCreateFirewallRuleInputItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53globalresolver-2022-09-27/BatchCreateFirewallRuleInputItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53globalresolver-2022-09-27/BatchCreateFirewallRuleInputItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53globalresolver-2022-09-27/BatchCreateFirewallRuleInputItem)
