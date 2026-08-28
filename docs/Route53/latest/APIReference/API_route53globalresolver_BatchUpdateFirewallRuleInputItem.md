---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_BatchUpdateFirewallRuleInputItem.html
---

# BatchUpdateFirewallRuleInputItem
<a name="API_route53globalresolver_BatchUpdateFirewallRuleInputItem"></a>

Information for updating a firewall rule in a batch operation.

## Contents
<a name="API_route53globalresolver_BatchUpdateFirewallRuleInputItem_Contents"></a>

 ** firewallRuleId **   <a name="Route53GlobalResolver-Type-route53globalresolver_BatchUpdateFirewallRuleInputItem-firewallRuleId"></a>
The unique identifier of the firewall rule to update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[-.a-zA-Z0-9]+`
Required: Yes

 ** action **   <a name="Route53GlobalResolver-Type-route53globalresolver_BatchUpdateFirewallRuleInputItem-action"></a>
The action to take when a DNS query matches the firewall rule.
Type: String
Valid Values: `ALLOW | ALERT | BLOCK`
Required: No

 ** blockOverrideDnsType **   <a name="Route53GlobalResolver-Type-route53globalresolver_BatchUpdateFirewallRuleInputItem-blockOverrideDnsType"></a>
The DNS record type for the custom response when the action is BLOCK.
Type: String
Valid Values: `CNAME`
Required: No

 ** blockOverrideDomain **   <a name="Route53GlobalResolver-Type-route53globalresolver_BatchUpdateFirewallRuleInputItem-blockOverrideDomain"></a>
The custom domain name for the BLOCK response.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `\*?[a-zA-Z0-9!"#$%&'()*+,./:;<=>?@\[\\\]^_`{|}~-]+`
Required: No

 ** blockOverrideTtl **   <a name="Route53GlobalResolver-Type-route53globalresolver_BatchUpdateFirewallRuleInputItem-blockOverrideTtl"></a>
The TTL value for the custom response when the action is BLOCK.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 604800.
Required: No

 ** blockResponse **   <a name="Route53GlobalResolver-Type-route53globalresolver_BatchUpdateFirewallRuleInputItem-blockResponse"></a>
The type of block response to return when the action is BLOCK.
Type: String
Valid Values: `NODATA | NXDOMAIN | OVERRIDE`
Required: No

 ** confidenceThreshold **   <a name="Route53GlobalResolver-Type-route53globalresolver_BatchUpdateFirewallRuleInputItem-confidenceThreshold"></a>
The confidence threshold for advanced threat detection.
Type: String
Valid Values: `LOW | MEDIUM | HIGH`
Required: No

 ** description **   <a name="Route53GlobalResolver-Type-route53globalresolver_BatchUpdateFirewallRuleInputItem-description"></a>
A description of the firewall rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** dnsAdvancedProtection **   <a name="Route53GlobalResolver-Type-route53globalresolver_BatchUpdateFirewallRuleInputItem-dnsAdvancedProtection"></a>
Whether to enable advanced DNS threat protection for the firewall rule.
Type: String
Valid Values: `DGA | DNS_TUNNELING | DICTIONARY_DGA`
Required: No

 ** name **   <a name="Route53GlobalResolver-Type-route53globalresolver_BatchUpdateFirewallRuleInputItem-name"></a>
A name for the firewall rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `(?!^[0-9]+$)([a-zA-Z0-9-_/' ']+)`
Required: No

 ** priority **   <a name="Route53GlobalResolver-Type-route53globalresolver_BatchUpdateFirewallRuleInputItem-priority"></a>
The priority of the firewall rule.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 10000.
Required: No

## See Also
<a name="API_route53globalresolver_BatchUpdateFirewallRuleInputItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53globalresolver-2022-09-27/BatchUpdateFirewallRuleInputItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53globalresolver-2022-09-27/BatchUpdateFirewallRuleInputItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53globalresolver-2022-09-27/BatchUpdateFirewallRuleInputItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
