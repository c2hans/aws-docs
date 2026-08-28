---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lex-bot-slotvalueoverride.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lex::Bot SlotValueOverride
<a name="aws-properties-lex-bot-slotvalueoverride"></a>

The slot values that Amazon Lex uses when it sets slot values in a dialog step.

## Syntax
<a name="aws-properties-lex-bot-slotvalueoverride-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lex-bot-slotvalueoverride-syntax.json"></a>

```
{
  "[Shape](#cfn-lex-bot-slotvalueoverride-shape)" : {{String}},
  "[Value](#cfn-lex-bot-slotvalueoverride-value)" : {{SlotValue}},
  "[Values](#cfn-lex-bot-slotvalueoverride-values)" : {{[ SlotValueOverride, ... ]}}
}
```

### YAML
<a name="aws-properties-lex-bot-slotvalueoverride-syntax.yaml"></a>

```
  [Shape](#cfn-lex-bot-slotvalueoverride-shape): {{String}}
  [Value](#cfn-lex-bot-slotvalueoverride-value): {{
    SlotValue}}
  [Values](#cfn-lex-bot-slotvalueoverride-values): {{
    - SlotValueOverride}}
```

## Properties
<a name="aws-properties-lex-bot-slotvalueoverride-properties"></a>

`Shape`  <a name="cfn-lex-bot-slotvalueoverride-shape"></a>
When the shape value is `List`, it indicates that the `values` field contains a list of slot values. When the value is `Scalar`, it indicates that the `value` field contains a single value.
*Required*: No
*Type*: String
*Allowed values*: `Scalar | List`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-lex-bot-slotvalueoverride-value"></a>
The current value of the slot.
*Required*: No
*Type*: [SlotValue](aws-properties-lex-bot-slotvalue.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Values`  <a name="cfn-lex-bot-slotvalueoverride-values"></a>
A list of one or more values that the user provided for the slot. For example, for a slot that elicits pizza toppings, the values might be "pepperoni" and "pineapple."
*Required*: No
*Type*: Array of [SlotValueOverride](#aws-properties-lex-bot-slotvalueoverride)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
