---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lex-bot-fulfillmentupdateresponsespecification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lex::Bot FulfillmentUpdateResponseSpecification
<a name="aws-properties-lex-bot-fulfillmentupdateresponsespecification"></a>

Provides settings for a message that is sent periodically to the user while a fulfillment Lambda function is running.

## Syntax
<a name="aws-properties-lex-bot-fulfillmentupdateresponsespecification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lex-bot-fulfillmentupdateresponsespecification-syntax.json"></a>

```
{
  "[AllowInterrupt](#cfn-lex-bot-fulfillmentupdateresponsespecification-allowinterrupt)" : {{Boolean}},
  "[FrequencyInSeconds](#cfn-lex-bot-fulfillmentupdateresponsespecification-frequencyinseconds)" : {{Integer}},
  "[MessageGroups](#cfn-lex-bot-fulfillmentupdateresponsespecification-messagegroups)" : {{[ MessageGroup, ... ]}}
}
```

### YAML
<a name="aws-properties-lex-bot-fulfillmentupdateresponsespecification-syntax.yaml"></a>

```
  [AllowInterrupt](#cfn-lex-bot-fulfillmentupdateresponsespecification-allowinterrupt): {{Boolean}}
  [FrequencyInSeconds](#cfn-lex-bot-fulfillmentupdateresponsespecification-frequencyinseconds): {{Integer}}
  [MessageGroups](#cfn-lex-bot-fulfillmentupdateresponsespecification-messagegroups): {{
    - MessageGroup}}
```

## Properties
<a name="aws-properties-lex-bot-fulfillmentupdateresponsespecification-properties"></a>

`AllowInterrupt`  <a name="cfn-lex-bot-fulfillmentupdateresponsespecification-allowinterrupt"></a>
Determines whether the user can interrupt an update message while it is playing.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FrequencyInSeconds`  <a name="cfn-lex-bot-fulfillmentupdateresponsespecification-frequencyinseconds"></a>
The frequency that a message is sent to the user. When the period ends, Amazon Lex chooses a message from the message groups and plays it to the user. If the fulfillment Lambda returns before the first period ends, an update message is not played to the user.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Maximum*: `900`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MessageGroups`  <a name="cfn-lex-bot-fulfillmentupdateresponsespecification-messagegroups"></a>
1 - 5 message groups that contain update messages. Amazon Lex chooses one of the messages to play to the user.
*Required*: Yes
*Type*: Array of [MessageGroup](aws-properties-lex-bot-messagegroup.md)
*Minimum*: `1`
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
