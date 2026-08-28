---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lex-bot-stillwaitingresponsespecification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lex::Bot StillWaitingResponseSpecification
<a name="aws-properties-lex-bot-stillwaitingresponsespecification"></a>

Defines the messages that Amazon Lex sends to a user to remind them that the bot is waiting for a response.

## Syntax
<a name="aws-properties-lex-bot-stillwaitingresponsespecification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lex-bot-stillwaitingresponsespecification-syntax.json"></a>

```
{
  "[AllowInterrupt](#cfn-lex-bot-stillwaitingresponsespecification-allowinterrupt)" : {{Boolean}},
  "[FrequencyInSeconds](#cfn-lex-bot-stillwaitingresponsespecification-frequencyinseconds)" : {{Integer}},
  "[MessageGroupsList](#cfn-lex-bot-stillwaitingresponsespecification-messagegroupslist)" : {{[ MessageGroup, ... ]}},
  "[TimeoutInSeconds](#cfn-lex-bot-stillwaitingresponsespecification-timeoutinseconds)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-lex-bot-stillwaitingresponsespecification-syntax.yaml"></a>

```
  [AllowInterrupt](#cfn-lex-bot-stillwaitingresponsespecification-allowinterrupt): {{Boolean}}
  [FrequencyInSeconds](#cfn-lex-bot-stillwaitingresponsespecification-frequencyinseconds): {{Integer}}
  [MessageGroupsList](#cfn-lex-bot-stillwaitingresponsespecification-messagegroupslist): {{
    - MessageGroup}}
  [TimeoutInSeconds](#cfn-lex-bot-stillwaitingresponsespecification-timeoutinseconds): {{Integer}}
```

## Properties
<a name="aws-properties-lex-bot-stillwaitingresponsespecification-properties"></a>

`AllowInterrupt`  <a name="cfn-lex-bot-stillwaitingresponsespecification-allowinterrupt"></a>
Indicates that the user can interrupt the response by speaking while the message is being played.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FrequencyInSeconds`  <a name="cfn-lex-bot-stillwaitingresponsespecification-frequencyinseconds"></a>
How often a message should be sent to the user. Minimum of 1 second, maximum of 5 minutes.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Maximum*: `300`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MessageGroupsList`  <a name="cfn-lex-bot-stillwaitingresponsespecification-messagegroupslist"></a>
One or more message groups, each containing one or more messages, that define the prompts that Amazon Lex sends to the user.
*Required*: Yes
*Type*: Array of [MessageGroup](aws-properties-lex-bot-messagegroup.md)
*Minimum*: `1`
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TimeoutInSeconds`  <a name="cfn-lex-bot-stillwaitingresponsespecification-timeoutinseconds"></a>
If Amazon Lex waits longer than this length of time for a response, it will stop sending messages.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Maximum*: `900`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
