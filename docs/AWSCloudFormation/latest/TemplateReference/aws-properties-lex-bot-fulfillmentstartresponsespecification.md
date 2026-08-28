---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lex-bot-fulfillmentstartresponsespecification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lex::Bot FulfillmentStartResponseSpecification
<a name="aws-properties-lex-bot-fulfillmentstartresponsespecification"></a>

Provides settings for a message that is sent to the user when a fulfillment Lambda function starts running.

## Syntax
<a name="aws-properties-lex-bot-fulfillmentstartresponsespecification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lex-bot-fulfillmentstartresponsespecification-syntax.json"></a>

```
{
  "[AllowInterrupt](#cfn-lex-bot-fulfillmentstartresponsespecification-allowinterrupt)" : {{Boolean}},
  "[DelayInSeconds](#cfn-lex-bot-fulfillmentstartresponsespecification-delayinseconds)" : {{Integer}},
  "[MessageGroups](#cfn-lex-bot-fulfillmentstartresponsespecification-messagegroups)" : {{[ MessageGroup, ... ]}}
}
```

### YAML
<a name="aws-properties-lex-bot-fulfillmentstartresponsespecification-syntax.yaml"></a>

```
  [AllowInterrupt](#cfn-lex-bot-fulfillmentstartresponsespecification-allowinterrupt): {{Boolean}}
  [DelayInSeconds](#cfn-lex-bot-fulfillmentstartresponsespecification-delayinseconds): {{Integer}}
  [MessageGroups](#cfn-lex-bot-fulfillmentstartresponsespecification-messagegroups): {{
    - MessageGroup}}
```

## Properties
<a name="aws-properties-lex-bot-fulfillmentstartresponsespecification-properties"></a>

`AllowInterrupt`  <a name="cfn-lex-bot-fulfillmentstartresponsespecification-allowinterrupt"></a>
Determines whether the user can interrupt the start message while it is playing.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DelayInSeconds`  <a name="cfn-lex-bot-fulfillmentstartresponsespecification-delayinseconds"></a>
The delay between when the Lambda fulfillment function starts running and the start message is played. If the Lambda function returns before the delay is over, the start message isn't played.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Maximum*: `900`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MessageGroups`  <a name="cfn-lex-bot-fulfillmentstartresponsespecification-messagegroups"></a>
1 - 5 message groups that contain start messages. Amazon Lex chooses one of the messages to play to the user.
*Required*: Yes
*Type*: Array of [MessageGroup](aws-properties-lex-bot-messagegroup.md)
*Minimum*: `1`
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
