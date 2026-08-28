---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lex-bot-intentoverride.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lex::Bot IntentOverride
<a name="aws-properties-lex-bot-intentoverride"></a>

Override settings to configure the intent state.

## Syntax
<a name="aws-properties-lex-bot-intentoverride-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lex-bot-intentoverride-syntax.json"></a>

```
{
  "[Name](#cfn-lex-bot-intentoverride-name)" : {{String}},
  "[Slots](#cfn-lex-bot-intentoverride-slots)" : {{[ SlotValueOverrideMap, ... ]}}
}
```

### YAML
<a name="aws-properties-lex-bot-intentoverride-syntax.yaml"></a>

```
  [Name](#cfn-lex-bot-intentoverride-name): {{String}}
  [Slots](#cfn-lex-bot-intentoverride-slots): {{
    - SlotValueOverrideMap}}
```

## Properties
<a name="aws-properties-lex-bot-intentoverride-properties"></a>

`Name`  <a name="cfn-lex-bot-intentoverride-name"></a>
The name of the intent. Only required when you're switching intents.
*Required*: No
*Type*: String
*Pattern*: `^([0-9a-zA-Z][_-]?)+$`
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Slots`  <a name="cfn-lex-bot-intentoverride-slots"></a>
A map of all of the slot value overrides for the intent. The name of the slot maps to the value of the slot. Slots that are not included in the map aren't overridden.
*Required*: No
*Type*: Array of [SlotValueOverrideMap](aws-properties-lex-bot-slotvalueoverridemap.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
