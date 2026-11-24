---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesis-queue-deadletterconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Kinesis::Queue DeadLetterConfiguration

The dead-letter handling configuration for a queue. Each queue has built-in dead-letter handling. When a record has been received `MaxReceiveCount` times without being acknowledged, it becomes a dead-letter record, and ReceiveQueueRecords no longer returns it. The dead-letter record stays in the same queue, and you work with it through ReceiveDeadLetterQueueRecords, AcknowledgeDeadLetterQueueRecords, UpdateDeadLetterQueueRecordsVisibility, and RestoreDeadLetterQueueRecords, which use the same queue ARN.

Dead-letter handling is enabled by default, with a `MaxReceiveCount` of 6. To use a different value, or to turn dead-letter handling off, specify this configuration in `QueueAttributes`.

## Syntax
<a name="aws-properties-kinesis-queue-deadletterconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesis-queue-deadletterconfiguration-syntax.json"></a>

```json
{
  "[MaxReceiveCount](#cfn-kinesis-queue-deadletterconfiguration-maxreceivecount)" : {{Integer}},
  "[TargetType](#cfn-kinesis-queue-deadletterconfiguration-targettype)" : {{String}}
}
```

### YAML
<a name="aws-properties-kinesis-queue-deadletterconfiguration-syntax.yaml"></a>

```yaml
  [MaxReceiveCount](#cfn-kinesis-queue-deadletterconfiguration-maxreceivecount): {{Integer}}
  [TargetType](#cfn-kinesis-queue-deadletterconfiguration-targettype): {{String}}
```

## Properties
<a name="aws-properties-kinesis-queue-deadletterconfiguration-properties"></a>

`MaxReceiveCount`  <a name="cfn-kinesis-queue-deadletterconfiguration-maxreceivecount"></a>
The number of times a record can be received without being acknowledged before it becomes a dead-letter record. Required when `TargetType` is `BUILT_IN`. A queue that you create without `DeadLetterConfiguration` gets a `MaxReceiveCount` of 6.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetType`  <a name="cfn-kinesis-queue-deadletterconfiguration-targettype"></a>
Whether dead-letter handling is enabled for the queue. `BUILT_IN` enables it: when a record has been received `MaxReceiveCount` times without being acknowledged, it becomes a dead-letter record and ReceiveQueueRecords no longer returns it. `NONE` disables it, and an unacknowledged record continues to be redelivered until it is acknowledged or its retention period ends.
*Required*: Yes
*Type*: String
*Allowed values*: `BUILT_IN | NONE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
