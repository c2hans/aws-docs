---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lex-bot-waitandcontinuespecification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lex::Bot WaitAndContinueSpecification
<a name="aws-properties-lex-bot-waitandcontinuespecification"></a>

Specifies the prompts that Amazon Lex uses while a bot is waiting for customer input.

## Syntax
<a name="aws-properties-lex-bot-waitandcontinuespecification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lex-bot-waitandcontinuespecification-syntax.json"></a>

```
{
  "[ContinueResponse](#cfn-lex-bot-waitandcontinuespecification-continueresponse)" : {{ResponseSpecification}},
  "[IsActive](#cfn-lex-bot-waitandcontinuespecification-isactive)" : {{Boolean}},
  "[StillWaitingResponse](#cfn-lex-bot-waitandcontinuespecification-stillwaitingresponse)" : {{StillWaitingResponseSpecification}},
  "[WaitingResponse](#cfn-lex-bot-waitandcontinuespecification-waitingresponse)" : {{ResponseSpecification}}
}
```

### YAML
<a name="aws-properties-lex-bot-waitandcontinuespecification-syntax.yaml"></a>

```
  [ContinueResponse](#cfn-lex-bot-waitandcontinuespecification-continueresponse): {{
    ResponseSpecification}}
  [IsActive](#cfn-lex-bot-waitandcontinuespecification-isactive): {{Boolean}}
  [StillWaitingResponse](#cfn-lex-bot-waitandcontinuespecification-stillwaitingresponse): {{
    StillWaitingResponseSpecification}}
  [WaitingResponse](#cfn-lex-bot-waitandcontinuespecification-waitingresponse): {{
    ResponseSpecification}}
```

## Properties
<a name="aws-properties-lex-bot-waitandcontinuespecification-properties"></a>

`ContinueResponse`  <a name="cfn-lex-bot-waitandcontinuespecification-continueresponse"></a>
The response that Amazon Lex sends to indicate that the bot is ready to continue the conversation.
*Required*: Yes
*Type*: [ResponseSpecification](aws-properties-lex-bot-responsespecification.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IsActive`  <a name="cfn-lex-bot-waitandcontinuespecification-isactive"></a>
Specifies whether the bot will wait for a user to respond. When this field is false, wait and continue responses for a slot aren't used. If the `IsActive` field isn't specified, the default is true.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StillWaitingResponse`  <a name="cfn-lex-bot-waitandcontinuespecification-stillwaitingresponse"></a>
A response that Amazon Lex sends periodically to the user to indicate that the bot is still waiting for input from the user.
*Required*: No
*Type*: [StillWaitingResponseSpecification](aws-properties-lex-bot-stillwaitingresponsespecification.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WaitingResponse`  <a name="cfn-lex-bot-waitandcontinuespecification-waitingresponse"></a>
The response that Amazon Lex sends to indicate that the bot is waiting for the conversation to continue.
*Required*: Yes
*Type*: [ResponseSpecification](aws-properties-lex-bot-responsespecification.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
