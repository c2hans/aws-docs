---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wafv2-webacl-ruleactionoverride.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WAFv2::WebACL RuleActionOverride
<a name="aws-properties-wafv2-webacl-ruleactionoverride"></a>

Action setting to use in the place of a rule action that is configured inside the rule group. You specify one override for each rule whose action you want to change.

You can use overrides for testing, for example you can override all of rule actions to `Count` and then monitor the resulting count metrics to understand how the rule group would handle your web traffic. You can also permanently override some or all actions, to modify how the rule group manages your web traffic.

## Syntax
<a name="aws-properties-wafv2-webacl-ruleactionoverride-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wafv2-webacl-ruleactionoverride-syntax.json"></a>

```
{
  "[ActionToUse](#cfn-wafv2-webacl-ruleactionoverride-actiontouse)" : {{RuleAction}},
  "[Name](#cfn-wafv2-webacl-ruleactionoverride-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-wafv2-webacl-ruleactionoverride-syntax.yaml"></a>

```
  [ActionToUse](#cfn-wafv2-webacl-ruleactionoverride-actiontouse): {{
    RuleAction}}
  [Name](#cfn-wafv2-webacl-ruleactionoverride-name): {{String}}
```

## Properties
<a name="aws-properties-wafv2-webacl-ruleactionoverride-properties"></a>

`ActionToUse`  <a name="cfn-wafv2-webacl-ruleactionoverride-actiontouse"></a>
The override action to use, in place of the configured action of the rule in the rule group.
*Required*: Yes
*Type*: [RuleAction](aws-properties-wafv2-webacl-ruleaction.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-wafv2-webacl-ruleactionoverride-name"></a>
The name of the rule to override.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9A-Za-z_-]{1,128}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
