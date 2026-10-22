---
source_url: https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_RulesSourceList.html
---

# RulesSourceList
<a name="API_RulesSourceList"></a>

Stateful inspection criteria for a domain list rule group.

For HTTPS traffic, domain filtering is SNI-based. It uses the server name indicator extension of the TLS handshake.

By default, Network Firewall domain list inspection only includes traffic coming from the VPC where you deploy the firewall. To inspect traffic from IP addresses outside of the deployment VPC, you set the `HOME_NET` rule variable to include the CIDR range of the deployment VPC plus the other CIDR ranges. For more information, see [RuleVariables](API_RuleVariables.md) in this guide and [Stateful domain list rule groups in AWS Network Firewall](https://docs.aws.amazon.com/network-firewall/latest/developerguide/stateful-rule-groups-domain-names.html) in the *Network Firewall Developer Guide*.

## Contents
<a name="API_RulesSourceList_Contents"></a>

 ** GeneratedRulesType **   <a name="networkfirewall-Type-RulesSourceList-GeneratedRulesType"></a>
Whether you want to apply allow, reject, alert, or drop behavior to the domains in your target list.
When logging is enabled and you choose Alert, traffic that matches the domain specifications generates an alert in the firewall's logs. Then, traffic either passes, is rejected, or drops based on other rules in the firewall policy.
Type: String
Valid Values: `ALLOWLIST | DENYLIST | REJECTLIST | ALERTLIST`
Required: Yes

 ** Targets **   <a name="networkfirewall-Type-RulesSourceList-Targets"></a>
The domains that you want to inspect for in your traffic flows. Valid domain specifications are the following:
+ Explicit names. For example, `abc.example.com` matches only the domain `abc.example.com`.
+ Names that use a domain wildcard, which you indicate with an initial '`.`'. For example,`.example.com` matches `example.com` and matches all subdomains of `example.com`, such as `abc.example.com` and `www.example.com`.
Type: Array of strings
Required: Yes

 ** TargetTypes **   <a name="networkfirewall-Type-RulesSourceList-TargetTypes"></a>
The types of matching to perform against the domains in `Targets`. You can specify any combination of the following:
+  `AWS_ROUTE_53_RESOLVED_DOMAIN` – Match the domain against the domain that the Amazon Route 53 Resolver resolved the connection's destination IP address for.
+  `HTTP_HOST` – Match the domain against the `Host` header of HTTP traffic.
+  `TLS_SNI` – Match the domain against the Server Name Indication (SNI) of HTTPS traffic.
 `AWS_ROUTE_53_RESOLVED_DOMAIN` matches on how the destination IP address was resolved, rather than on the domain that the client asserts in its TLS SNI or HTTP `Host` header. This target type takes effect when you configure resolved IP validation on the firewall policy. For more information, see [Route53ResolvedIPValidation](API_Route53ResolvedIPValidation.md).
Whether you include `AWS_ROUTE_53_RESOLVED_DOMAIN` changes what the generated rules match, together with `GeneratedRulesType`:
+ Combining `AWS_ROUTE_53_RESOLVED_DOMAIN` with `TLS_SNI` or `HTTP_HOST` in an `ALLOWLIST` requires both conditions to match. The SNI or `Host` header must match the domain, **and** the Route 53 Resolver must have resolved the destination IP address for that domain. Network Firewall allows traffic only in that case. Traffic that matches one condition, such as a spoofed `Host` header sent to an unresolved IP address, is not allowed.
+ In a `DENYLIST`, or when `AWS_ROUTE_53_RESOLVED_DOMAIN` is the only target type, Network Firewall evaluates each condition independently: a match on either the domain (SNI or `Host`) or the resolved destination IP address triggers the rule.
+ When you don't include `AWS_ROUTE_53_RESOLVED_DOMAIN`, the generated rules match only on the SNI or `Host` header, without checking how the destination IP address was resolved.
An `ALLOWLIST` whose only target type is `AWS_ROUTE_53_RESOLVED_DOMAIN` is additive: it allows matching traffic but doesn't generate a default rule that drops non-matching traffic. Only the `TLS_SNI` and `HTTP_HOST` target types generate that default drop. To allow only the resolved domains and drop all other traffic, include a protocol target type as well.
Type: Array of strings
Valid Values: `TLS_SNI | HTTP_HOST | AWS_ROUTE_53_RESOLVED_DOMAIN`
Required: Yes

## See Also
<a name="API_RulesSourceList_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/RulesSourceList)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/RulesSourceList)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/RulesSourceList)
