---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-route53resolver-firewallrulegroup-firewallruletype.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Route53Resolver::FirewallRuleGroup FirewallRuleType
<a name="aws-properties-route53resolver-firewallrulegroup-firewallruletype"></a>

The rule-type configuration for a DNS Firewall rule. `FirewallRuleType` is a tagged union — exactly one member must be set per rule, and the member determines what the rule matches against. This shape is mutually exclusive with the top-level `FirewallDomainListId` and `DnsThreatProtection` fields on CreateFirewallRule and UpdateFirewallRule.

Call ListFirewallRuleTypes to discover which rule-type variants and which values within each variant are available in your account and Region.

## Syntax
<a name="aws-properties-route53resolver-firewallrulegroup-firewallruletype-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-route53resolver-firewallrulegroup-firewallruletype-syntax.json"></a>

```
{
  "[FirewallAdvancedContentCategory](#cfn-route53resolver-firewallrulegroup-firewallruletype-firewalladvancedcontentcategory)" : {{FirewallAdvancedContentCategoryConfig}},
  "[FirewallAdvancedThreatCategory](#cfn-route53resolver-firewallrulegroup-firewallruletype-firewalladvancedthreatcategory)" : {{FirewallAdvancedThreatCategoryConfig}},
  "[PartnerThreatProtection](#cfn-route53resolver-firewallrulegroup-firewallruletype-partnerthreatprotection)" : {{PartnerThreatProtectionConfig}}
}
```

### YAML
<a name="aws-properties-route53resolver-firewallrulegroup-firewallruletype-syntax.yaml"></a>

```
  [FirewallAdvancedContentCategory](#cfn-route53resolver-firewallrulegroup-firewallruletype-firewalladvancedcontentcategory): {{
    FirewallAdvancedContentCategoryConfig}}
  [FirewallAdvancedThreatCategory](#cfn-route53resolver-firewallrulegroup-firewallruletype-firewalladvancedthreatcategory): {{
    FirewallAdvancedThreatCategoryConfig}}
  [PartnerThreatProtection](#cfn-route53resolver-firewallrulegroup-firewallruletype-partnerthreatprotection): {{
    PartnerThreatProtectionConfig}}
```

## Properties
<a name="aws-properties-route53resolver-firewallrulegroup-firewallruletype-properties"></a>

`FirewallAdvancedContentCategory`  <a name="cfn-route53resolver-firewallrulegroup-firewallruletype-firewalladvancedcontentcategory"></a>
Configures the rule to match an AWS-managed content category (for example, `VIOLENCE_AND_HATE_SPEECH`). See FirewallAdvancedContentCategoryConfig.
*Required*: No
*Type*: [FirewallAdvancedContentCategoryConfig](aws-properties-route53resolver-firewallrulegroup-firewalladvancedcontentcategoryconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FirewallAdvancedThreatCategory`  <a name="cfn-route53resolver-firewallrulegroup-firewallruletype-firewalladvancedthreatcategory"></a>
Configures the rule to match an AWS-managed advanced threat category (for example, `PHISHING`). See FirewallAdvancedThreatCategoryConfig.
*Required*: No
*Type*: [FirewallAdvancedThreatCategoryConfig](aws-properties-route53resolver-firewallrulegroup-firewalladvancedthreatcategoryconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PartnerThreatProtection`  <a name="cfn-route53resolver-firewallrulegroup-firewallruletype-partnerthreatprotection"></a>
Configures the rule to match a third-party threat feed delivered through AWS Marketplace. The calling account must hold an active subscription to the partner product named in `Partner`; if the subscription is missing or revoked, the rule is created with `Status``CREATION_FAILED` and cannot be modified — only deleted. See PartnerThreatProtectionConfig.
*Required*: No
*Type*: [PartnerThreatProtectionConfig](aws-properties-route53resolver-firewallrulegroup-partnerthreatprotectionconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
