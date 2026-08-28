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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
