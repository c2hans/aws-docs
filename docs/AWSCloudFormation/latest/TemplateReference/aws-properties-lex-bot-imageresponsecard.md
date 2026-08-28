---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lex-bot-imageresponsecard.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lex::Bot ImageResponseCard
<a name="aws-properties-lex-bot-imageresponsecard"></a>

A card that is shown to the user by a messaging platform. You define the contents of the card, the card is displayed by the platform.

When you use a response card, the response from the user is constrained to the text associated with a button on the card.

## Syntax
<a name="aws-properties-lex-bot-imageresponsecard-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lex-bot-imageresponsecard-syntax.json"></a>

```
{
  "[Buttons](#cfn-lex-bot-imageresponsecard-buttons)" : {{[ Button, ... ]}},
  "[ImageUrl](#cfn-lex-bot-imageresponsecard-imageurl)" : {{String}},
  "[Subtitle](#cfn-lex-bot-imageresponsecard-subtitle)" : {{String}},
  "[Title](#cfn-lex-bot-imageresponsecard-title)" : {{String}}
}
```

### YAML
<a name="aws-properties-lex-bot-imageresponsecard-syntax.yaml"></a>

```
  [Buttons](#cfn-lex-bot-imageresponsecard-buttons): {{
    - Button}}
  [ImageUrl](#cfn-lex-bot-imageresponsecard-imageurl): {{String}}
  [Subtitle](#cfn-lex-bot-imageresponsecard-subtitle): {{String}}
  [Title](#cfn-lex-bot-imageresponsecard-title): {{String}}
```

## Properties
<a name="aws-properties-lex-bot-imageresponsecard-properties"></a>

`Buttons`  <a name="cfn-lex-bot-imageresponsecard-buttons"></a>
A list of buttons that should be displayed on the response card. The arrangement of the buttons is determined by the platform that displays the button.
*Required*: No
*Type*: Array of [Button](aws-properties-lex-bot-button.md)
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ImageUrl`  <a name="cfn-lex-bot-imageresponsecard-imageurl"></a>
The URL of an image to display on the response card. The image URL must be publicly available so that the platform displaying the response card has access to the image.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `250`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Subtitle`  <a name="cfn-lex-bot-imageresponsecard-subtitle"></a>
The subtitle to display on the response card. The format of the subtitle is determined by the platform displaying the response card.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `250`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Title`  <a name="cfn-lex-bot-imageresponsecard-title"></a>
The title to display on the response card. The format of the title is determined by the platform displaying the response card.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `250`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
