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
The types of targets to inspect for. Valid values are `TLS_SNI` and `HTTP_HOST`.
*Required*: Yes
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
