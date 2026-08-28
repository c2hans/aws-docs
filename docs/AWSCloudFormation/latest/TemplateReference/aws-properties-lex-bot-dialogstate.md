---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lex-bot-dialogstate.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lex::Bot DialogState
<a name="aws-properties-lex-bot-dialogstate"></a>

The current state of the conversation with the user.

## Syntax
<a name="aws-properties-lex-bot-dialogstate-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lex-bot-dialogstate-syntax.json"></a>

```
{
  "[DialogAction](#cfn-lex-bot-dialogstate-dialogaction)" : {{DialogAction}},
  "[Intent](#cfn-lex-bot-dialogstate-intent)" : {{IntentOverride}},
  "[SessionAttributes](#cfn-lex-bot-dialogstate-sessionattributes)" : {{[ SessionAttribute, ... ]}}
}
```

### YAML
<a name="aws-properties-lex-bot-dialogstate-syntax.yaml"></a>

```
  [DialogAction](#cfn-lex-bot-dialogstate-dialogaction): {{
    DialogAction}}
  [Intent](#cfn-lex-bot-dialogstate-intent): {{
    IntentOverride}}
  [SessionAttributes](#cfn-lex-bot-dialogstate-sessionattributes): {{
    - SessionAttribute}}
```

## Properties
<a name="aws-properties-lex-bot-dialogstate-properties"></a>

`DialogAction`  <a name="cfn-lex-bot-dialogstate-dialogaction"></a>
Defines the action that the bot executes at runtime when the conversation reaches this step.
*Required*: No
*Type*: [DialogAction](aws-properties-lex-bot-dialogaction.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Intent`  <a name="cfn-lex-bot-dialogstate-intent"></a>
Override settings to configure the intent state.
*Required*: No
*Type*: [IntentOverride](aws-properties-lex-bot-intentoverride.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SessionAttributes`  <a name="cfn-lex-bot-dialogstate-sessionattributes"></a>
Map of key/value pairs representing session-specific context information. It contains application information passed between Amazon Lex and a client application.
*Required*: No
*Type*: Array of [SessionAttribute](aws-properties-lex-bot-sessionattribute.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
