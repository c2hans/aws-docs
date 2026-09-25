---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-eventsv2-subscriber-snsparameters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EventsV2::Subscriber SnsParameters
<a name="aws-properties-eventsv2-subscriber-snsparameters"></a>

Parameters for publishing events to an Amazon SNS topic target.

## Syntax
<a name="aws-properties-eventsv2-subscriber-snsparameters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-eventsv2-subscriber-snsparameters-syntax.json"></a>

```
{
  "[MessageAttributes](#cfn-eventsv2-subscriber-snsparameters-messageattributes)" : {{{{{Key}}: {{Value}}, ...}}},
  "[MessageDeduplicationId](#cfn-eventsv2-subscriber-snsparameters-messagededuplicationid)" : {{String}},
  "[MessageGroupId](#cfn-eventsv2-subscriber-snsparameters-messagegroupid)" : {{String}},
  "[MessageStructure](#cfn-eventsv2-subscriber-snsparameters-messagestructure)" : {{String}},
  "[Subject](#cfn-eventsv2-subscriber-snsparameters-subject)" : {{String}}
}
```

### YAML
<a name="aws-properties-eventsv2-subscriber-snsparameters-syntax.yaml"></a>

```
  [MessageAttributes](#cfn-eventsv2-subscriber-snsparameters-messageattributes): {{
    {{Key}}: {{Value}}}}
  [MessageDeduplicationId](#cfn-eventsv2-subscriber-snsparameters-messagededuplicationid): {{String}}
  [MessageGroupId](#cfn-eventsv2-subscriber-snsparameters-messagegroupid): {{String}}
  [MessageStructure](#cfn-eventsv2-subscriber-snsparameters-messagestructure): {{String}}
  [Subject](#cfn-eventsv2-subscriber-snsparameters-subject): {{String}}
```

## Properties
<a name="aws-properties-eventsv2-subscriber-snsparameters-properties"></a>

`MessageAttributes`  <a name="cfn-eventsv2-subscriber-snsparameters-messageattributes"></a>
A map of message attribute names to values, with at most 50 attributes. Amazon SQS and Amazon SNS enforce their own per-message attribute limits on delivery.
*Required*: No
*Type*: Object of [MessageAttributeValue](aws-properties-eventsv2-subscriber-messageattributevalue.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MessageDeduplicationId`  <a name="cfn-eventsv2-subscriber-snsparameters-messagededuplicationid"></a>
The message deduplication ID to use when the target is a FIFO topic. Accepts a literal value or a JSONata expression.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MessageGroupId`  <a name="cfn-eventsv2-subscriber-snsparameters-messagegroupid"></a>
The message group ID to use when the target is a FIFO topic. Accepts a literal value or a JSONata expression.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MessageStructure`  <a name="cfn-eventsv2-subscriber-snsparameters-messagestructure"></a>
Set to json to send a different message per delivery protocol. Accepts a literal value or a JSONata expression.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Subject`  <a name="cfn-eventsv2-subscriber-snsparameters-subject"></a>
The subject line to use for email-protocol subscriptions. Accepts a literal value or a JSONata expression.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
