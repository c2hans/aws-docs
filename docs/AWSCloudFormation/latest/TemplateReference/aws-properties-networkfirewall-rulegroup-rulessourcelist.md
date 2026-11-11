---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-networkfirewall-rulegroup-rulessourcelist.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NetworkFirewall::RuleGroup RulesSourceList
<a name="aws-properties-networkfirewall-rulegroup-rulessourcelist"></a>

Stateful inspection criteria for a domain list rule group.

For HTTPS traffic, domain filtering is SNI-based. It uses the server name indicator extension of the TLS handshake.

By default, Network Firewall domain list inspection only includes traffic coming from the VPC where you deploy the firewall. To inspect traffic from IP addresses outside of the deployment VPC, you set the `HOME_NET` rule variable to include the CIDR range of the deployment VPC plus the other CIDR ranges. For more information, see `RuleVariables` in this guide and [Stateful domain list rule groups in AWS Network Firewall](https://docs.aws.amazon.com/network-firewall/latest/developerguide/stateful-rule-groups-domain-names.html) in the *Network Firewall Developer Guide*

## Syntax
<a name="aws-properties-networkfirewall-rulegroup-rulessourcelist-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-networkfirewall-rulegroup-rulessourcelist-syntax.json"></a>

```
{
  "[GeneratedRulesType](#cfn-networkfirewall-rulegroup-rulessourcelist-generatedrulestype)" : {{String}},
  "[Targets](#cfn-networkfirewall-rulegroup-rulessourcelist-targets)" : {{[ String, ... ]}},
  "[TargetTypes](#cfn-networkfirewall-rulegroup-rulessourcelist-targettypes)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-networkfirewall-rulegroup-rulessourcelist-syntax.yaml"></a>

```
  [GeneratedRulesType](#cfn-networkfirewall-rulegroup-rulessourcelist-generatedrulestype): {{String}}
  [Targets](#cfn-networkfirewall-rulegroup-rulessourcelist-targets): {{
    - String}}
  [TargetTypes](#cfn-networkfirewall-rulegroup-rulessourcelist-targettypes): {{
    - String}}
```

## Properties
<a name="aws-properties-networkfirewall-rulegroup-rulessourcelist-properties"></a>

`GeneratedRulesType`  <a name="cfn-networkfirewall-rulegroup-rulessourcelist-generatedrulestype"></a>
Whether you want to apply allow, reject, alert, or drop behavior to the domains in your target list.
When logging is enabled and you choose Alert, traffic that matches the domain specifications generates an alert in the firewall's logs. Then, traffic either passes, is rejected, or drops based on other rules in the firewall policy.
*Required*: Yes
*Type*: String
*Allowed values*: `ALLOWLIST | DENYLIST | ALERTLIST | REJECTLIST`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Targets`  <a name="cfn-networkfirewall-rulegroup-rulessourcelist-targets"></a>
The domains that you want to inspect for in your traffic flows. Valid domain specifications are the following:
+ Explicit names. For example, `abc.example.com` matches only the domain `abc.example.com`.
+ Names that use a domain wildcard, which you indicate with an initial '`.`'. For example,`.example.com` matches `example.com` and matches all subdomains of `example.com`, such as `abc.example.com` and `www.example.com`.
*Required*: Yes
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetTypes`  <a name="cfn-networkfirewall-rulegroup-rulessourcelist-targettypes"></a>
The types of matching to perform against the domains in `Targets`. You can specify any combination of the following:
+ `AWS_ROUTE_53_RESOLVED_DOMAIN` – Match the domain against the domain that the Amazon Route 53 Resolver resolved the connection's destination IP address for.
+ `HTTP_HOST` – Match the domain against the `Host` header of HTTP traffic.
+ `TLS_SNI` – Match the domain against the Server Name Indication (SNI) of HTTPS traffic.
`AWS_ROUTE_53_RESOLVED_DOMAIN` matches on how the destination IP address was resolved, rather than on the domain that the client asserts in its TLS SNI or HTTP `Host` header. This target type takes effect when you configure resolved IP validation on the firewall policy. For more information, see the `Route53ResolvedIPValidation` firewall policy setting.
Whether you include `AWS_ROUTE_53_RESOLVED_DOMAIN` changes what the generated rules match, together with `GeneratedRulesType`:
+ In an `ALLOWLIST`, combining `AWS_ROUTE_53_RESOLVED_DOMAIN` with `TLS_SNI` or `HTTP_HOST` requires both conditions to match: the SNI or `Host` header matches the domain, **and** the Route 53 Resolver resolved the destination IP address for that domain. Network Firewall allows the traffic only when both conditions match, so it blocks traffic that matches just one—for example, a spoofed `Host` header sent to an unresolved IP address.
+ In a `DENYLIST`, or when `AWS_ROUTE_53_RESOLVED_DOMAIN` is the only target type, Network Firewall evaluates each condition independently: a match on either the domain (SNI or `Host`) or the resolved destination IP address triggers the rule.
+ When you don't include `AWS_ROUTE_53_RESOLVED_DOMAIN`, the generated rules match only on the SNI or `Host` header, without checking how the destination IP address was resolved.
An `ALLOWLIST` whose only target type is `AWS_ROUTE_53_RESOLVED_DOMAIN` is additive: it allows matching traffic but doesn't generate a default rule that drops non-matching traffic. Only the `TLS_SNI` and `HTTP_HOST` target types generate that default drop. To allow only the resolved domains and drop all other traffic, include a protocol target type as well.
*Required*: Yes
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
