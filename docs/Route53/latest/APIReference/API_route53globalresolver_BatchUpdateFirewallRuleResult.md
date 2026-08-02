---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_BatchUpdateFirewallRuleResult.html
---

# BatchUpdateFirewallRuleResult
<a name="API_route53globalresolver_BatchUpdateFirewallRuleResult"></a>

Information about a firewall rule that was updated in a batch operation.

## Contents
<a name="API_route53globalresolver_BatchUpdateFirewallRuleResult_Contents"></a>

 ** id **   <a name="Route53GlobalResolver-Type-route53globalresolver_BatchUpdateFirewallRuleResult-id"></a>
The unique identifier of the updated firewall rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[-.a-zA-Z0-9]+`
Required: Yes

 ** action **   <a name="Route53GlobalResolver-Type-route53globalresolver_BatchUpdateFirewallRuleResult-action"></a>
The action configured for the updated firewall rule.
Type: String
Valid Values: `ALLOW | ALERT | BLOCK`
Required: No

 ** blockOverrideDnsType **   <a name="Route53GlobalResolver-Type-route53globalresolver_BatchUpdateFirewallRuleResult-blockOverrideDnsType"></a>
The DNS record type configured for the updated firewall rule's custom response.
Type: String
Valid Values: `CNAME`
Required: No

 ** blockOverrideDomain **   <a name="Route53GlobalResolver-Type-route53globalresolver_BatchUpdateFirewallRuleResult-blockOverrideDomain"></a>
The custom domain name configured for the updated firewall rule's BLOCK response.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `\*?[a-zA-Z0-9!"#$%&'()*+,./:;<=>?@\[\\\]^_`{|}~-]+`
Required: No

 ** blockOverrideTtl **   <a name="Route53GlobalResolver-Type-route53globalresolver_BatchUpdateFirewallRuleResult-blockOverrideTtl"></a>
The TTL value configured for the updated firewall rule's custom response.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 604800.
Required: No

 ** blockResponse **   <a name="Route53GlobalResolver-Type-route53globalresolver_BatchUpdateFirewallRuleResult-blockResponse"></a>
The type of block response configured for the updated firewall rule.
Type: String
Valid Values: `NODATA | NXDOMAIN | OVERRIDE`
Required: No

 ** clientToken **   <a name="Route53GlobalResolver-Type-route53globalresolver_BatchUpdateFirewallRuleResult-clientToken"></a>
The unique string that identified the request and ensured idempotency.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** confidenceThreshold **   <a name="Route53GlobalResolver-Type-route53globalresolver_BatchUpdateFirewallRuleResult-confidenceThreshold"></a>
The confidence threshold configured for the updated firewall rule's advanced threat detection.
Type: String
Valid Values: `LOW | MEDIUM | HIGH`
Required: No

 ** createdAt **   <a name="Route53GlobalResolver-Type-route53globalresolver_BatchUpdateFirewallRuleResult-createdAt"></a>
The date and time when the firewall rule was originally created.
Type: Timestamp
Required: No

 ** description **   <a name="Route53GlobalResolver-Type-route53globalresolver_BatchUpdateFirewallRuleResult-description"></a>
The description of the updated firewall rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** dnsAdvancedProtection **   <a name="Route53GlobalResolver-Type-route53globalresolver_BatchUpdateFirewallRuleResult-dnsAdvancedProtection"></a>
Whether advanced DNS threat protection is enabled for the updated firewall rule.
Type: String
Valid Values: `DGA | DNS_TUNNELING | DICTIONARY_DGA`
Required: No

 ** dnsViewId **   <a name="Route53GlobalResolver-Type-route53globalresolver_BatchUpdateFirewallRuleResult-dnsViewId"></a>
The ID of the DNS view associated with the updated firewall rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[-.a-zA-Z0-9]+`
Required: No

 ** firewallDomainListId **   <a name="Route53GlobalResolver-Type-route53globalresolver_BatchUpdateFirewallRuleResult-firewallDomainListId"></a>
The ID of the firewall domain list associated with the updated firewall rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[-.a-zA-Z0-9]+`
Required: No

 ** name **   <a name="Route53GlobalResolver-Type-route53globalresolver_BatchUpdateFirewallRuleResult-name"></a>
The name of the updated firewall rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `(?!^[0-9]+$)([a-zA-Z0-9-_/' ']+)`
Required: No

 ** priority **   <a name="Route53GlobalResolver-Type-route53globalresolver_BatchUpdateFirewallRuleResult-priority"></a>
The priority of the updated firewall rule.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 10000.
Required: No

 ** queryType **   <a name="Route53GlobalResolver-Type-route53globalresolver_BatchUpdateFirewallRuleResult-queryType"></a>
The DNS query type that the updated firewall rule matches.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 16.
Required: No

 ** status **   <a name="Route53GlobalResolver-Type-route53globalresolver_BatchUpdateFirewallRuleResult-status"></a>
The current status of the updated firewall rule.
Type: String
Valid Values: `CREATING | OPERATIONAL | UPDATING | DELETING`
Required: No

 ** updatedAt **   <a name="Route53GlobalResolver-Type-route53globalresolver_BatchUpdateFirewallRuleResult-updatedAt"></a>
The date and time when the firewall rule was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_route53globalresolver_BatchUpdateFirewallRuleResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53globalresolver-2022-09-27/BatchUpdateFirewallRuleResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53globalresolver-2022-09-27/BatchUpdateFirewallRuleResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53globalresolver-2022-09-27/BatchUpdateFirewallRuleResult)
