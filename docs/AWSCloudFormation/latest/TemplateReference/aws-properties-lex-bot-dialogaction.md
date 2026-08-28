---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lex-bot-dialogaction.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lex::Bot DialogAction
<a name="aws-properties-lex-bot-dialogaction"></a>

Defines the action that the bot executes at runtime when the conversation reaches this step.

## Syntax
<a name="aws-properties-lex-bot-dialogaction-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lex-bot-dialogaction-syntax.json"></a>

```
{
  "[SlotToElicit](#cfn-lex-bot-dialogaction-slottoelicit)" : {{String}},
  "[SuppressNextMessage](#cfn-lex-bot-dialogaction-suppressnextmessage)" : {{Boolean}},
  "[Type](#cfn-lex-bot-dialogaction-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-lex-bot-dialogaction-syntax.yaml"></a>

```
  [SlotToElicit](#cfn-lex-bot-dialogaction-slottoelicit): {{String}}
  [SuppressNextMessage](#cfn-lex-bot-dialogaction-suppressnextmessage): {{Boolean}}
  [Type](#cfn-lex-bot-dialogaction-type): {{String}}
```

## Properties
<a name="aws-properties-lex-bot-dialogaction-properties"></a>

`SlotToElicit`  <a name="cfn-lex-bot-dialogaction-slottoelicit"></a>
If the dialog action is `ElicitSlot`, defines the slot to elicit from the user.
*Required*: No
*Type*: String
*Pattern*: `^([0-9a-zA-Z][_-]?)+$`
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SuppressNextMessage`  <a name="cfn-lex-bot-dialogaction-suppressnextmessage"></a>
When true the next message for the intent is not used.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-lex-bot-dialogaction-type"></a>
The action that the bot should execute.
*Required*: Yes
*Type*: String
*Allowed values*: `CloseIntent | ConfirmIntent | ElicitIntent | ElicitSlot | StartIntent | FulfillIntent | EndConversation | EvaluateConditional | InvokeDialogCodeHook`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
