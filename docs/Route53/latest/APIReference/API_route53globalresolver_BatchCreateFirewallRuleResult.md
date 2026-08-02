---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_BatchCreateFirewallRuleResult.html
---

# BatchCreateFirewallRuleResult
<a name="API_route53globalresolver_BatchCreateFirewallRuleResult"></a>

The result of creating a firewall rule in a batch operation.

## Contents
<a name="API_route53globalresolver_BatchCreateFirewallRuleResult_Contents"></a>

 ** action **   <a name="Route53GlobalResolver-Type-route53globalresolver_BatchCreateFirewallRuleResult-action"></a>
The action configured for the created firewall rule.
Type: String
Valid Values: `ALLOW | ALERT | BLOCK`
Required: Yes

 ** clientToken **   <a name="Route53GlobalResolver-Type-route53globalresolver_BatchCreateFirewallRuleResult-clientToken"></a>
The unique string that identified the request and ensured idempotency.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** dnsViewId **   <a name="Route53GlobalResolver-Type-route53globalresolver_BatchCreateFirewallRuleResult-dnsViewId"></a>
The ID of the DNS view associated with the created firewall rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[-.a-zA-Z0-9]+`
Required: Yes

 ** name **   <a name="Route53GlobalResolver-Type-route53globalresolver_BatchCreateFirewallRuleResult-name"></a>
The name of the created firewall rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `(?!^[0-9]+$)([a-zA-Z0-9-_/' ']+)`
Required: Yes

 ** blockOverrideDnsType **   <a name="Route53GlobalResolver-Type-route53globalresolver_BatchCreateFirewallRuleResult-blockOverrideDnsType"></a>
The DNS record type configured for the created firewall rule's custom response.
Type: String
Valid Values: `CNAME`
Required: No

 ** blockOverrideDomain **   <a name="Route53GlobalResolver-Type-route53globalresolver_BatchCreateFirewallRuleResult-blockOverrideDomain"></a>
The custom domain name configured for the created firewall rule's BLOCK response.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `\*?[a-zA-Z0-9!"#$%&'()*+,./:;<=>?@\[\\\]^_`{|}~-]+`
Required: No

 ** blockOverrideTtl **   <a name="Route53GlobalResolver-Type-route53globalresolver_BatchCreateFirewallRuleResult-blockOverrideTtl"></a>
The TTL value configured for the created firewall rule's custom response.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 604800.
Required: No

 ** blockResponse **   <a name="Route53GlobalResolver-Type-route53globalresolver_BatchCreateFirewallRuleResult-blockResponse"></a>
The type of block response configured for the created firewall rule.
Type: String
Valid Values: `NODATA | NXDOMAIN | OVERRIDE`
Required: No

 ** confidenceThreshold **   <a name="Route53GlobalResolver-Type-route53globalresolver_BatchCreateFirewallRuleResult-confidenceThreshold"></a>
The confidence threshold configured for the created firewall rule's advanced threat detection.
Type: String
Valid Values: `LOW | MEDIUM | HIGH`
Required: No

 ** createdAt **   <a name="Route53GlobalResolver-Type-route53globalresolver_BatchCreateFirewallRuleResult-createdAt"></a>
The date and time when the firewall rule was created.
Type: Timestamp
Required: No

 ** description **   <a name="Route53GlobalResolver-Type-route53globalresolver_BatchCreateFirewallRuleResult-description"></a>
The description of the created firewall rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** dnsAdvancedProtection **   <a name="Route53GlobalResolver-Type-route53globalresolver_BatchCreateFirewallRuleResult-dnsAdvancedProtection"></a>
Whether advanced DNS threat protection is enabled for the created firewall rule.
Type: String
Valid Values: `DGA | DNS_TUNNELING | DICTIONARY_DGA`
Required: No

 ** firewallDomainListId **   <a name="Route53GlobalResolver-Type-route53globalresolver_BatchCreateFirewallRuleResult-firewallDomainListId"></a>
The ID of the firewall domain list associated with the created firewall rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[-.a-zA-Z0-9]+`
Required: No

 ** id **   <a name="Route53GlobalResolver-Type-route53globalresolver_BatchCreateFirewallRuleResult-id"></a>
The unique identifier of the created firewall rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[-.a-zA-Z0-9]+`
Required: No

 ** managedDomainListName **   <a name="Route53GlobalResolver-Type-route53globalresolver_BatchCreateFirewallRuleResult-managedDomainListName"></a>
The name of the managed domain list associated with the created firewall rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `(?!^[0-9]+$)([a-zA-Z0-9-_/' ']+)`
Required: No

 ** priority **   <a name="Route53GlobalResolver-Type-route53globalresolver_BatchCreateFirewallRuleResult-priority"></a>
The priority of the created firewall rule.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 10000.
Required: No

 ** queryType **   <a name="Route53GlobalResolver-Type-route53globalresolver_BatchCreateFirewallRuleResult-queryType"></a>
The DNS query type that the created firewall rule matches.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 16.
Required: No

 ** status **   <a name="Route53GlobalResolver-Type-route53globalresolver_BatchCreateFirewallRuleResult-status"></a>
The current status of the created firewall rule.
Type: String
Valid Values: `CREATING | OPERATIONAL | UPDATING | DELETING`
Required: No

 ** updatedAt **   <a name="Route53GlobalResolver-Type-route53globalresolver_BatchCreateFirewallRuleResult-updatedAt"></a>
The date and time when the firewall rule was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_route53globalresolver_BatchCreateFirewallRuleResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53globalresolver-2022-09-27/BatchCreateFirewallRuleResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53globalresolver-2022-09-27/BatchCreateFirewallRuleResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53globalresolver-2022-09-27/BatchCreateFirewallRuleResult)
