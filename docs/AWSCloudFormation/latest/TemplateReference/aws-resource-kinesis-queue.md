---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-kinesis-queue.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Kinesis::Queue

Creates a queue on the specified data stream. A queue delivers records from the stream to a queue consumer, tracks the delivery state of each record, and redelivers any record that is not acknowledged before its visibility timeout expires.

A queue does not extend how long the stream keeps a record. When a record reaches the end of the data stream's retention period, the queue stops delivering it.

Your queue consumer calls ReceiveQueueRecords to receive up to 10 records at a time. After it processes records, it calls AcknowledgeQueueRecords so the queue does not deliver them again.

Queues are supported only on data streams in on-demand capacity mode.

Creating a queue does not change how producers write to the stream, and it does not change how existing stream consumers read from it. A queue counts as a registered consumer on the stream and shares the stream's registered consumer limit with enhanced fan-out consumers: 20 on On-demand Standard and 50 on On-demand Advantage.

Use `StartingPosition` to set the position in the stream where delivery begins. The default is `LATEST`.

`CreateQueue` is an asynchronous operation. Upon receiving a `CreateQueue` request, Amazon Kinesis Data Streams immediately returns a queue description with a `QueueStatus` of `CREATING`. After the queue is created, Kinesis Data Streams sets the `QueueStatus` to `ACTIVE`. You can begin receiving records after the queue is `ACTIVE`. Use DescribeQueue to check the status of the queue.

Each queue has built-in dead-letter handling. When a record has been received `MaxReceiveCount` times without being acknowledged, it becomes a dead-letter record, and ReceiveQueueRecords no longer returns it. You work with dead-letter records through a separate set of operations that use the same queue ARN: ReceiveDeadLetterQueueRecords, AcknowledgeDeadLetterQueueRecords, UpdateDeadLetterQueueRecordsVisibility, and RestoreDeadLetterQueueRecords.

Dead-letter handling is enabled by default, with a `MaxReceiveCount` of 6. To use a different value, or to turn dead-letter handling off, specify `DeadLetterConfiguration` in `QueueAttributes`.

## Syntax
<a name="aws-resource-kinesis-queue-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-kinesis-queue-syntax.json"></a>

```json
{
  "Type" : "AWS::Kinesis::Queue",
  "Properties" : {
      "[QueueAttributes](#cfn-kinesis-queue-queueattributes)" : {{QueueAttributes}},
      "[QueueName](#cfn-kinesis-queue-queuename)" : {{String}},
      "[StreamConfigurationList](#cfn-kinesis-queue-streamconfigurationlist)" : {{[ QueueStreamConfiguration, ... ]}},
      "[Tags](#cfn-kinesis-queue-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-kinesis-queue-syntax.yaml"></a>

```yaml
Type: AWS::Kinesis::Queue
Properties:
  [QueueAttributes](#cfn-kinesis-queue-queueattributes): {{
    QueueAttributes}}
  [QueueName](#cfn-kinesis-queue-queuename): {{String}}
  [StreamConfigurationList](#cfn-kinesis-queue-streamconfigurationlist): {{
    - QueueStreamConfiguration}}
  [Tags](#cfn-kinesis-queue-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-kinesis-queue-properties"></a>

`QueueAttributes`  <a name="cfn-kinesis-queue-queueattributes"></a>
The configuration attributes of the queue.
*Required*: No
*Type*: [QueueAttributes](aws-properties-kinesis-queue-queueattributes.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`QueueName`  <a name="cfn-kinesis-queue-queuename"></a>
The name of the queue.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_.-]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`StreamConfigurationList`  <a name="cfn-kinesis-queue-streamconfigurationlist"></a>
The data stream the queue delivers records from, and the position in that stream where delivery begins. The list contains exactly one entry, because a queue delivers records from a single data stream.
*Required*: Yes
*Type*: Array of [QueueStreamConfiguration](aws-properties-kinesis-queue-queuestreamconfiguration.md)
*Minimum*: `1`
*Maximum*: `10000`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-kinesis-queue-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-kinesis-queue-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-kinesis-queue-return-values"></a>

### Ref
<a name="aws-resource-kinesis-queue-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-kinesis-queue-return-values-fn--getatt"></a>

####
<a name="aws-resource-kinesis-queue-return-values-fn--getatt-fn--getatt"></a>

`QueueARN`  <a name="QueueARN-fn::getatt"></a>
The ARN of the queue. The resource identifier in the ARN is generated when the queue is created and is not derived from `QueueName`. Use the returned `QueueARN` to identify the queue in subsequent requests.

`QueueCreationTimestamp`  <a name="QueueCreationTimestamp-fn::getatt"></a>
The time the queue was created.

`QueueStatus`  <a name="QueueStatus-fn::getatt"></a>
The current status of the queue.
