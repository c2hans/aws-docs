---
source_url: https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_FirewallPolicyError.html
---

# FirewallPolicyError
<a name="API_FirewallPolicyError"></a>

A configuration error that Network Firewall detected for a firewall policy.

## Contents
<a name="API_FirewallPolicyError_Contents"></a>

 ** Code **   <a name="networkfirewall-Type-FirewallPolicyError-Code"></a>
The error code identifies the type of error. Valid values are the following:
+  `DNS_FIREWALL_RULE_GROUP_UNAVAILABLE` – The Amazon Route 53 Resolver DNS Firewall rule group that resolved IP validation references is unavailable, for example, because it was deleted or is no longer accessible from your account. Update the rule group ID or remove the resolved IP validation configuration.
+  `ROUTE53_RESOLVED_IP_VALIDATION_MISSING` – An associated stateful rule group uses the `aws_route_53_resolved_domain` keyword, but the policy doesn't have resolved IP validation configured. The affected rules are inactive until you add resolved IP validation to the policy or remove the keyword rules.
Type: String
Valid Values: `DNS_FIREWALL_RULE_GROUP_UNAVAILABLE | ROUTE53_RESOLVED_IP_VALIDATION_MISSING`
Required: Yes

 ** Message **   <a name="networkfirewall-Type-FirewallPolicyError-Message"></a>
A description of the error and how to resolve it.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^[a-zA-Z0-9- ]+$`
Required: Yes

 ** ResourceId **   <a name="networkfirewall-Type-FirewallPolicyError-ResourceId"></a>
The ID of the resource that the error relates to, when applicable. For example, for `DNS_FIREWALL_RULE_GROUP_UNAVAILABLE` this is the Amazon Route 53 Resolver DNS Firewall rule group ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^[a-zA-Z0-9:/_.-]+$`
Required: No

## See Also
<a name="API_FirewallPolicyError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/FirewallPolicyError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/FirewallPolicyError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/FirewallPolicyError)
