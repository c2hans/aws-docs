---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lex-bot-slotvalue.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lex::Bot SlotValue
<a name="aws-properties-lex-bot-slotvalue"></a>

The value to set in a slot.

## Syntax
<a name="aws-properties-lex-bot-slotvalue-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lex-bot-slotvalue-syntax.json"></a>

```
{
  "[InterpretedValue](#cfn-lex-bot-slotvalue-interpretedvalue)" : {{String}}
}
```

### YAML
<a name="aws-properties-lex-bot-slotvalue-syntax.yaml"></a>

```
  [InterpretedValue](#cfn-lex-bot-slotvalue-interpretedvalue): {{String}}
```

## Properties
<a name="aws-properties-lex-bot-slotvalue-properties"></a>

`InterpretedValue`  <a name="cfn-lex-bot-slotvalue-interpretedvalue"></a>
The value that Amazon Lex determines for the slot. The actual value depends on the setting of the value selection strategy for the bot. You can choose to use the value entered by the user, or you can have Amazon Lex choose the first value in the `resolvedValues` list.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `202`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
