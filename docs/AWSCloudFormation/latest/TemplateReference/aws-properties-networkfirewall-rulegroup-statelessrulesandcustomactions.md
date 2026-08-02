---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-networkfirewall-rulegroup-statelessrulesandcustomactions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NetworkFirewall::RuleGroup StatelessRulesAndCustomActions
<a name="aws-properties-networkfirewall-rulegroup-statelessrulesandcustomactions"></a>

Stateless inspection criteria. Each stateless rule group uses exactly one of these data types to define its stateless rules.

## Syntax
<a name="aws-properties-networkfirewall-rulegroup-statelessrulesandcustomactions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-networkfirewall-rulegroup-statelessrulesandcustomactions-syntax.json"></a>

```
{
  "[CustomActions](#cfn-networkfirewall-rulegroup-statelessrulesandcustomactions-customactions)" : {{[ CustomAction, ... ]}},
  "[StatelessRules](#cfn-networkfirewall-rulegroup-statelessrulesandcustomactions-statelessrules)" : {{[ StatelessRule, ... ]}}
}
```

### YAML
<a name="aws-properties-networkfirewall-rulegroup-statelessrulesandcustomactions-syntax.yaml"></a>

```
  [CustomActions](#cfn-networkfirewall-rulegroup-statelessrulesandcustomactions-customactions): {{
    - CustomAction}}
  [StatelessRules](#cfn-networkfirewall-rulegroup-statelessrulesandcustomactions-statelessrules): {{
    - StatelessRule}}
```

## Properties
<a name="aws-properties-networkfirewall-rulegroup-statelessrulesandcustomactions-properties"></a>

`CustomActions`  <a name="cfn-networkfirewall-rulegroup-statelessrulesandcustomactions-customactions"></a>
Defines an array of individual custom action definitions that are available for use by the stateless rules in this `StatelessRulesAndCustomActions` specification. You name each custom action that you define, and then you can use it by name in your stateless rule definition `Actions` specification.
*Required*: No
*Type*: Array of [CustomAction](aws-properties-networkfirewall-rulegroup-customaction.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StatelessRules`  <a name="cfn-networkfirewall-rulegroup-statelessrulesandcustomactions-statelessrules"></a>
Defines the set of stateless rules for use in a stateless rule group.
*Required*: Yes
*Type*: Array of [StatelessRule](aws-properties-networkfirewall-rulegroup-statelessrule.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
