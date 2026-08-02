---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-networkfirewall-rulegroup-customaction.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NetworkFirewall::RuleGroup CustomAction
<a name="aws-properties-networkfirewall-rulegroup-customaction"></a>

An optional, non-standard action to use for stateless packet handling. You can define this in addition to the standard action that you must specify.

You define and name the custom actions that you want to be able to use, and then you reference them by name in your actions settings.

You can use custom actions in the following places:
+ In a `StatelessRulesAndCustomActions`. The custom actions are available for use by name inside the `StatelessRulesAndCustomActions` where you define them. You can use them for your stateless rule actions to specify what to do with a packet that matches the rule's match attributes.
+ In an firewall policy specification, in `StatelessCustomActions`. The custom actions are available for use inside the policy where you define them. You can use them for the policy's default stateless actions settings to specify what to do with packets that don't match any of the policy's stateless rules.

## Syntax
<a name="aws-properties-networkfirewall-rulegroup-customaction-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-networkfirewall-rulegroup-customaction-syntax.json"></a>

```
{
  "[ActionDefinition](#cfn-networkfirewall-rulegroup-customaction-actiondefinition)" : {{ActionDefinition}},
  "[ActionName](#cfn-networkfirewall-rulegroup-customaction-actionname)" : {{String}}
}
```

### YAML
<a name="aws-properties-networkfirewall-rulegroup-customaction-syntax.yaml"></a>

```
  [ActionDefinition](#cfn-networkfirewall-rulegroup-customaction-actiondefinition): {{
    ActionDefinition}}
  [ActionName](#cfn-networkfirewall-rulegroup-customaction-actionname): {{String}}
```

## Properties
<a name="aws-properties-networkfirewall-rulegroup-customaction-properties"></a>

`ActionDefinition`  <a name="cfn-networkfirewall-rulegroup-customaction-actiondefinition"></a>
The custom action associated with the action name.
*Required*: Yes
*Type*: [ActionDefinition](aws-properties-networkfirewall-rulegroup-actiondefinition.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ActionName`  <a name="cfn-networkfirewall-rulegroup-customaction-actionname"></a>
The descriptive name of the custom action. You can't change the name of a custom action after you create it.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
