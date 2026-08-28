---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lex-bot-postfulfillmentstatusspecification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lex::Bot PostFulfillmentStatusSpecification
<a name="aws-properties-lex-bot-postfulfillmentstatusspecification"></a>

Provides a setting that determines whether the post-fulfillment response is sent to the user. For more information, see [https://docs.aws.amazon.com/lexv2/latest/dg/streaming-progress.html#progress-complete](https://docs.aws.amazon.com/lexv2/latest/dg/streaming-progress.html#progress-complete)

## Syntax
<a name="aws-properties-lex-bot-postfulfillmentstatusspecification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lex-bot-postfulfillmentstatusspecification-syntax.json"></a>

```
{
  "[FailureConditional](#cfn-lex-bot-postfulfillmentstatusspecification-failureconditional)" : {{ConditionalSpecification}},
  "[FailureNextStep](#cfn-lex-bot-postfulfillmentstatusspecification-failurenextstep)" : {{DialogState}},
  "[FailureResponse](#cfn-lex-bot-postfulfillmentstatusspecification-failureresponse)" : {{ResponseSpecification}},
  "[SuccessConditional](#cfn-lex-bot-postfulfillmentstatusspecification-successconditional)" : {{ConditionalSpecification}},
  "[SuccessNextStep](#cfn-lex-bot-postfulfillmentstatusspecification-successnextstep)" : {{DialogState}},
  "[SuccessResponse](#cfn-lex-bot-postfulfillmentstatusspecification-successresponse)" : {{ResponseSpecification}},
  "[TimeoutConditional](#cfn-lex-bot-postfulfillmentstatusspecification-timeoutconditional)" : {{ConditionalSpecification}},
  "[TimeoutNextStep](#cfn-lex-bot-postfulfillmentstatusspecification-timeoutnextstep)" : {{DialogState}},
  "[TimeoutResponse](#cfn-lex-bot-postfulfillmentstatusspecification-timeoutresponse)" : {{ResponseSpecification}}
}
```

### YAML
<a name="aws-properties-lex-bot-postfulfillmentstatusspecification-syntax.yaml"></a>

```
  [FailureConditional](#cfn-lex-bot-postfulfillmentstatusspecification-failureconditional): {{
    ConditionalSpecification}}
  [FailureNextStep](#cfn-lex-bot-postfulfillmentstatusspecification-failurenextstep): {{
    DialogState}}
  [FailureResponse](#cfn-lex-bot-postfulfillmentstatusspecification-failureresponse): {{
    ResponseSpecification}}
  [SuccessConditional](#cfn-lex-bot-postfulfillmentstatusspecification-successconditional): {{
    ConditionalSpecification}}
  [SuccessNextStep](#cfn-lex-bot-postfulfillmentstatusspecification-successnextstep): {{
    DialogState}}
  [SuccessResponse](#cfn-lex-bot-postfulfillmentstatusspecification-successresponse): {{
    ResponseSpecification}}
  [TimeoutConditional](#cfn-lex-bot-postfulfillmentstatusspecification-timeoutconditional): {{
    ConditionalSpecification}}
  [TimeoutNextStep](#cfn-lex-bot-postfulfillmentstatusspecification-timeoutnextstep): {{
    DialogState}}
  [TimeoutResponse](#cfn-lex-bot-postfulfillmentstatusspecification-timeoutresponse): {{
    ResponseSpecification}}
```

## Properties
<a name="aws-properties-lex-bot-postfulfillmentstatusspecification-properties"></a>

`FailureConditional`  <a name="cfn-lex-bot-postfulfillmentstatusspecification-failureconditional"></a>
A list of conditional branches to evaluate after the fulfillment code hook throws an exception or returns with the `State` field of the `Intent` object set to `Failed`.
*Required*: No
*Type*: [ConditionalSpecification](aws-properties-lex-bot-conditionalspecification.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FailureNextStep`  <a name="cfn-lex-bot-postfulfillmentstatusspecification-failurenextstep"></a>
Specifies the next step the bot runs after the fulfillment code hook throws an exception or returns with the `State` field of the `Intent` object set to `Failed`.
*Required*: No
*Type*: [DialogState](aws-properties-lex-bot-dialogstate.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FailureResponse`  <a name="cfn-lex-bot-postfulfillmentstatusspecification-failureresponse"></a>
Specifies a list of message groups that Amazon Lex uses to respond when fulfillment isn't successful.
*Required*: No
*Type*: [ResponseSpecification](aws-properties-lex-bot-responsespecification.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SuccessConditional`  <a name="cfn-lex-bot-postfulfillmentstatusspecification-successconditional"></a>
A list of conditional branches to evaluate after the fulfillment code hook finishes successfully.
*Required*: No
*Type*: [ConditionalSpecification](aws-properties-lex-bot-conditionalspecification.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SuccessNextStep`  <a name="cfn-lex-bot-postfulfillmentstatusspecification-successnextstep"></a>
Specifies the next step in the conversation that Amazon Lex invokes when the fulfillment code hook completes successfully.
*Required*: No
*Type*: [DialogState](aws-properties-lex-bot-dialogstate.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SuccessResponse`  <a name="cfn-lex-bot-postfulfillmentstatusspecification-successresponse"></a>
Specifies a list of message groups that Amazon Lex uses to respond when the fulfillment is successful.
*Required*: No
*Type*: [ResponseSpecification](aws-properties-lex-bot-responsespecification.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TimeoutConditional`  <a name="cfn-lex-bot-postfulfillmentstatusspecification-timeoutconditional"></a>
A list of conditional branches to evaluate if the fulfillment code hook times out.
*Required*: No
*Type*: [ConditionalSpecification](aws-properties-lex-bot-conditionalspecification.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TimeoutNextStep`  <a name="cfn-lex-bot-postfulfillmentstatusspecification-timeoutnextstep"></a>
Specifies the next step that the bot runs when the fulfillment code hook times out.
*Required*: No
*Type*: [DialogState](aws-properties-lex-bot-dialogstate.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TimeoutResponse`  <a name="cfn-lex-bot-postfulfillmentstatusspecification-timeoutresponse"></a>
Specifies a list of message groups that Amazon Lex uses to respond when fulfillment isn't completed within the timeout period.
*Required*: No
*Type*: [ResponseSpecification](aws-properties-lex-bot-responsespecification.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
