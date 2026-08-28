---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wafv2-webacl-overrideaction.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WAFv2::WebACL OverrideAction
<a name="aws-properties-wafv2-webacl-overrideaction"></a>

The action to use in the place of the action that results from the rule group evaluation. Set the override action to none to leave the result of the rule group alone. Set it to count to override the result to count only.

You can only use this for rule statements that reference a rule group, like `RuleGroupReferenceStatement` and `ManagedRuleGroupStatement`.

**Note**
This option is usually set to none. It does not affect how the rules in the rule group are evaluated. If you want the rules in the rule group to only count matches, do not use this and instead use the rule action override option, with `Count` action, in your rule group reference statement settings.

## Syntax
<a name="aws-properties-wafv2-webacl-overrideaction-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wafv2-webacl-overrideaction-syntax.json"></a>

```
{
  "[Count](#cfn-wafv2-webacl-overrideaction-count)" : {{Json}},
  "[None](#cfn-wafv2-webacl-overrideaction-none)" : {{Json}}
}
```

### YAML
<a name="aws-properties-wafv2-webacl-overrideaction-syntax.yaml"></a>

```
  [Count](#cfn-wafv2-webacl-overrideaction-count): {{Json}}
  [None](#cfn-wafv2-webacl-overrideaction-none): {{Json}}
```

## Properties
<a name="aws-properties-wafv2-webacl-overrideaction-properties"></a>

`Count`  <a name="cfn-wafv2-webacl-overrideaction-count"></a>
Override the rule group evaluation result to count only.
This option is usually set to none. It does not affect how the rules in the rule group are evaluated. If you want the rules in the rule group to only count matches, do not use this and instead use the rule action override option, with `Count` action, in your rule group reference statement settings.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`None`  <a name="cfn-wafv2-webacl-overrideaction-none"></a>
Don't override the rule group evaluation result. This is the most common setting.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
