---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ses-mailmanagerruleset-rule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::MailManagerRuleSet Rule
<a name="aws-properties-ses-mailmanagerruleset-rule"></a>

A rule contains conditions, "unless conditions" and actions. For each envelope recipient of an email, if all conditions match and none of the "unless conditions" match, then all of the actions are executed sequentially. If no conditions are provided, the rule always applies and the actions are implicitly executed. If only "unless conditions" are provided, the rule applies if the email does not match the evaluation of the "unless conditions".

## Syntax
<a name="aws-properties-ses-mailmanagerruleset-rule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ses-mailmanagerruleset-rule-syntax.json"></a>

```
{
  "[Actions](#cfn-ses-mailmanagerruleset-rule-actions)" : {{[ RuleAction, ... ]}},
  "[Conditions](#cfn-ses-mailmanagerruleset-rule-conditions)" : {{[ RuleCondition, ... ]}},
  "[Name](#cfn-ses-mailmanagerruleset-rule-name)" : {{String}},
  "[Unless](#cfn-ses-mailmanagerruleset-rule-unless)" : {{[ RuleCondition, ... ]}}
}
```

### YAML
<a name="aws-properties-ses-mailmanagerruleset-rule-syntax.yaml"></a>

```
  [Actions](#cfn-ses-mailmanagerruleset-rule-actions): {{
    - RuleAction}}
  [Conditions](#cfn-ses-mailmanagerruleset-rule-conditions): {{
    - RuleCondition}}
  [Name](#cfn-ses-mailmanagerruleset-rule-name): {{String}}
  [Unless](#cfn-ses-mailmanagerruleset-rule-unless): {{
    - RuleCondition}}
```

## Properties
<a name="aws-properties-ses-mailmanagerruleset-rule-properties"></a>

`Actions`  <a name="cfn-ses-mailmanagerruleset-rule-actions"></a>
The list of actions to execute when the conditions match the incoming email, and none of the "unless conditions" match.
*Required*: Yes
*Type*: Array of [RuleAction](aws-properties-ses-mailmanagerruleset-ruleaction.md)
*Minimum*: `1`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Conditions`  <a name="cfn-ses-mailmanagerruleset-rule-conditions"></a>
The conditions of this rule. All conditions must match the email for the actions to be executed. An empty list of conditions means that all emails match, but are still subject to any "unless conditions"
*Required*: No
*Type*: Array of [RuleCondition](aws-properties-ses-mailmanagerruleset-rulecondition.md)
*Minimum*: `0`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-ses-mailmanagerruleset-rule-name"></a>
The user-friendly name of the rule.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9_.-]+$`
*Minimum*: `1`
*Maximum*: `32`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Unless`  <a name="cfn-ses-mailmanagerruleset-rule-unless"></a>
The "unless conditions" of this rule. None of the conditions can match the email for the actions to be executed. If any of these conditions do match the email, then the actions are not executed.
*Required*: No
*Type*: Array of [RuleCondition](aws-properties-ses-mailmanagerruleset-rulecondition.md)
*Minimum*: `0`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
