---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-eventsv2-subscriber-sqsparameters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EventsV2::Subscriber SqsParameters
<a name="aws-properties-eventsv2-subscriber-sqsparameters"></a>

Parameters for sending events to an Amazon SQS queue target.

## Syntax
<a name="aws-properties-eventsv2-subscriber-sqsparameters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-eventsv2-subscriber-sqsparameters-syntax.json"></a>

```
{
  "[DelaySeconds](#cfn-eventsv2-subscriber-sqsparameters-delayseconds)" : {{String}},
  "[MessageAttributes](#cfn-eventsv2-subscriber-sqsparameters-messageattributes)" : {{{{{Key}}: {{Value}}, ...}}},
  "[MessageDeduplicationId](#cfn-eventsv2-subscriber-sqsparameters-messagededuplicationid)" : {{String}},
  "[MessageGroupId](#cfn-eventsv2-subscriber-sqsparameters-messagegroupid)" : {{String}},
  "[MessageSystemAttributes](#cfn-eventsv2-subscriber-sqsparameters-messagesystemattributes)" : {{{{{Key}}: {{Value}}, ...}}}
}
```

### YAML
<a name="aws-properties-eventsv2-subscriber-sqsparameters-syntax.yaml"></a>

```
  [DelaySeconds](#cfn-eventsv2-subscriber-sqsparameters-delayseconds): {{String}}
  [MessageAttributes](#cfn-eventsv2-subscriber-sqsparameters-messageattributes): {{
    {{Key}}: {{Value}}}}
  [MessageDeduplicationId](#cfn-eventsv2-subscriber-sqsparameters-messagededuplicationid): {{String}}
  [MessageGroupId](#cfn-eventsv2-subscriber-sqsparameters-messagegroupid): {{String}}
  [MessageSystemAttributes](#cfn-eventsv2-subscriber-sqsparameters-messagesystemattributes): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-properties-eventsv2-subscriber-sqsparameters-properties"></a>

`DelaySeconds`  <a name="cfn-eventsv2-subscriber-sqsparameters-delayseconds"></a>
The delay in seconds for the message, written as a string. Accepts a literal value or a JSONata expression.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MessageAttributes`  <a name="cfn-eventsv2-subscriber-sqsparameters-messageattributes"></a>
A map of message attribute names to values, with at most 50 attributes. Amazon SQS and Amazon SNS enforce their own per-message attribute limits on delivery.
*Required*: No
*Type*: Object of [MessageAttributeValue](aws-properties-eventsv2-subscriber-messageattributevalue.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MessageDeduplicationId`  <a name="cfn-eventsv2-subscriber-sqsparameters-messagededuplicationid"></a>
The message deduplication ID to use when the target is a FIFO queue. Accepts a literal value or a JSONata expression.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MessageGroupId`  <a name="cfn-eventsv2-subscriber-sqsparameters-messagegroupid"></a>
The message group ID to use when the target is a FIFO queue. Accepts a literal value or a JSONata expression.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MessageSystemAttributes`  <a name="cfn-eventsv2-subscriber-sqsparameters-messagesystemattributes"></a>
A map of message attribute names to values, with at most 50 attributes. Amazon SQS and Amazon SNS enforce their own per-message attribute limits on delivery.
*Required*: No
*Type*: Object of [MessageAttributeValue](aws-properties-eventsv2-subscriber-messageattributevalue.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
