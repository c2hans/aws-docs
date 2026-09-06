---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-route53resolver-firewallrulegroup-firewalladvancedcontentcategoryconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Route53Resolver::FirewallRuleGroup FirewallAdvancedContentCategoryConfig
<a name="aws-properties-route53resolver-firewallrulegroup-firewalladvancedcontentcategoryconfig"></a>

The configuration for a content category-based filtering rule. This specifies which content category to use for DNS query evaluation.

## Syntax
<a name="aws-properties-route53resolver-firewallrulegroup-firewalladvancedcontentcategoryconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-route53resolver-firewallrulegroup-firewalladvancedcontentcategoryconfig-syntax.json"></a>

```
{
  "[Category](#cfn-route53resolver-firewallrulegroup-firewalladvancedcontentcategoryconfig-category)" : {{String}}
}
```

### YAML
<a name="aws-properties-route53resolver-firewallrulegroup-firewalladvancedcontentcategoryconfig-syntax.yaml"></a>

```
  [Category](#cfn-route53resolver-firewallrulegroup-firewalladvancedcontentcategoryconfig-category): {{String}}
```

## Properties
<a name="aws-properties-route53resolver-firewallrulegroup-firewalladvancedcontentcategoryconfig-properties"></a>

`Category`  <a name="cfn-route53resolver-firewallrulegroup-firewalladvancedcontentcategoryconfig-category"></a>
The content category identifier. To retrieve the list of available content categories, call ListFirewallRuleTypes with `RuleType` set to `FirewallAdvancedContentCategory`.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
