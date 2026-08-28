---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lex-bot-message.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lex::Bot Message
<a name="aws-properties-lex-bot-message"></a>

The object that provides message text and its type.

## Syntax
<a name="aws-properties-lex-bot-message-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lex-bot-message-syntax.json"></a>

```
{
  "[CustomPayload](#cfn-lex-bot-message-custompayload)" : {{CustomPayload}},
  "[ImageResponseCard](#cfn-lex-bot-message-imageresponsecard)" : {{ImageResponseCard}},
  "[PlainTextMessage](#cfn-lex-bot-message-plaintextmessage)" : {{PlainTextMessage}},
  "[SSMLMessage](#cfn-lex-bot-message-ssmlmessage)" : {{SSMLMessage}}
}
```

### YAML
<a name="aws-properties-lex-bot-message-syntax.yaml"></a>

```
  [CustomPayload](#cfn-lex-bot-message-custompayload): {{
    CustomPayload}}
  [ImageResponseCard](#cfn-lex-bot-message-imageresponsecard): {{
    ImageResponseCard}}
  [PlainTextMessage](#cfn-lex-bot-message-plaintextmessage): {{
    PlainTextMessage}}
  [SSMLMessage](#cfn-lex-bot-message-ssmlmessage): {{
    SSMLMessage}}
```

## Properties
<a name="aws-properties-lex-bot-message-properties"></a>

`CustomPayload`  <a name="cfn-lex-bot-message-custompayload"></a>
A message in a custom format defined by the client application.
*Required*: No
*Type*: [CustomPayload](aws-properties-lex-bot-custompayload.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ImageResponseCard`  <a name="cfn-lex-bot-message-imageresponsecard"></a>
A message that defines a response card that the client application can show to the user.
*Required*: No
*Type*: [ImageResponseCard](aws-properties-lex-bot-imageresponsecard.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PlainTextMessage`  <a name="cfn-lex-bot-message-plaintextmessage"></a>
A message in plain text format.
*Required*: No
*Type*: [PlainTextMessage](aws-properties-lex-bot-plaintextmessage.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SSMLMessage`  <a name="cfn-lex-bot-message-ssmlmessage"></a>
A message in Speech Synthesis Markup Language (SSML).
*Required*: No
*Type*: [SSMLMessage](aws-properties-lex-bot-ssmlmessage.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
