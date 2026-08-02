---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-route53resolver-firewallrulegroup-partnerthreatprotectionconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Route53Resolver::FirewallRuleGroup PartnerThreatProtectionConfig
<a name="aws-properties-route53resolver-firewallrulegroup-partnerthreatprotectionconfig"></a>

The configuration for a partner threat-protection rule. To enumerate the partners available in your account, call ListFirewallRuleTypes with `RuleType` set to `PartnerThreatProtection` — each returned FirewallRuleTypeDefinition includes a SubscriptionInfo identifying the AWS Marketplace product that backs it.

## Syntax
<a name="aws-properties-route53resolver-firewallrulegroup-partnerthreatprotectionconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-route53resolver-firewallrulegroup-partnerthreatprotectionconfig-syntax.json"></a>

```
{
  "[Partner](#cfn-route53resolver-firewallrulegroup-partnerthreatprotectionconfig-partner)" : {{String}}
}
```

### YAML
<a name="aws-properties-route53resolver-firewallrulegroup-partnerthreatprotectionconfig-syntax.yaml"></a>

```
  [Partner](#cfn-route53resolver-firewallrulegroup-partnerthreatprotectionconfig-partner): {{String}}
```

## Properties
<a name="aws-properties-route53resolver-firewallrulegroup-partnerthreatprotectionconfig-properties"></a>

`Partner`  <a name="cfn-route53resolver-firewallrulegroup-partnerthreatprotectionconfig-partner"></a>
The identifier of the partner threat-protection product, exactly as returned in the `Value` field of a FirewallRuleTypeDefinition with `RuleType` set to `PartnerThreatProtection`. The calling account must hold an active AWS Marketplace subscription to this product.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
