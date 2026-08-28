---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lex-bot-messagegroup.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lex::Bot MessageGroup
<a name="aws-properties-lex-bot-messagegroup"></a>

Provides one or more messages that Amazon Lex should send to the user.

## Syntax
<a name="aws-properties-lex-bot-messagegroup-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lex-bot-messagegroup-syntax.json"></a>

```
{
  "[Message](#cfn-lex-bot-messagegroup-message)" : {{Message}},
  "[Variations](#cfn-lex-bot-messagegroup-variations)" : {{[ Message, ... ]}}
}
```

### YAML
<a name="aws-properties-lex-bot-messagegroup-syntax.yaml"></a>

```
  [Message](#cfn-lex-bot-messagegroup-message): {{
    Message}}
  [Variations](#cfn-lex-bot-messagegroup-variations): {{
    - Message}}
```

## Properties
<a name="aws-properties-lex-bot-messagegroup-properties"></a>

`Message`  <a name="cfn-lex-bot-messagegroup-message"></a>
The primary message that Amazon Lex should send to the user.
*Required*: Yes
*Type*: [Message](aws-properties-lex-bot-message.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Variations`  <a name="cfn-lex-bot-messagegroup-variations"></a>
Message variations to send to the user. When variations are defined, Amazon Lex chooses the primary message or one of the variations to send to the user.
*Required*: No
*Type*: Array of [Message](aws-properties-lex-bot-message.md)
*Maximum*: `2`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
