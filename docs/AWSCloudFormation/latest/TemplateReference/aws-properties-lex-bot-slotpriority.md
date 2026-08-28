---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lex-bot-slotpriority.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lex::Bot SlotPriority
<a name="aws-properties-lex-bot-slotpriority"></a>

Sets the priority that Amazon Lex should use when eliciting slot values from a user.

## Syntax
<a name="aws-properties-lex-bot-slotpriority-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lex-bot-slotpriority-syntax.json"></a>

```
{
  "[Priority](#cfn-lex-bot-slotpriority-priority)" : {{Integer}},
  "[SlotName](#cfn-lex-bot-slotpriority-slotname)" : {{String}}
}
```

### YAML
<a name="aws-properties-lex-bot-slotpriority-syntax.yaml"></a>

```
  [Priority](#cfn-lex-bot-slotpriority-priority): {{Integer}}
  [SlotName](#cfn-lex-bot-slotpriority-slotname): {{String}}
```

## Properties
<a name="aws-properties-lex-bot-slotpriority-properties"></a>

`Priority`  <a name="cfn-lex-bot-slotpriority-priority"></a>
The priority that Amazon Lex should apply to the slot.
*Required*: Yes
*Type*: Integer
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SlotName`  <a name="cfn-lex-bot-slotpriority-slotname"></a>
The name of the slot.
*Required*: Yes
*Type*: String
*Pattern*: `^([0-9a-zA-Z][_-]?)+$`
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
