---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesis-queue-queueattributes.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Kinesis::Queue QueueAttributes

The configuration attributes for a queue.

## Syntax
<a name="aws-properties-kinesis-queue-queueattributes-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesis-queue-queueattributes-syntax.json"></a>

```json
{
  "[DeadLetterConfiguration](#cfn-kinesis-queue-queueattributes-deadletterconfiguration)" : {{DeadLetterConfiguration}},
  "[VisibilityTimeoutSeconds](#cfn-kinesis-queue-queueattributes-visibilitytimeoutseconds)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-kinesis-queue-queueattributes-syntax.yaml"></a>

```yaml
  [DeadLetterConfiguration](#cfn-kinesis-queue-queueattributes-deadletterconfiguration): {{
    DeadLetterConfiguration}}
  [VisibilityTimeoutSeconds](#cfn-kinesis-queue-queueattributes-visibilitytimeoutseconds): {{Integer}}
```

## Properties
<a name="aws-properties-kinesis-queue-queueattributes-properties"></a>

`DeadLetterConfiguration`  <a name="cfn-kinesis-queue-queueattributes-deadletterconfiguration"></a>
The dead-letter handling configuration for the queue. If you omit this attribute, dead-letter handling is enabled with a `MaxReceiveCount` of 6. If you specify it with a `TargetType` of `BUILT_IN`, you must also specify `MaxReceiveCount`.
*Required*: No
*Type*: [DeadLetterConfiguration](aws-properties-kinesis-queue-deadletterconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VisibilityTimeoutSeconds`  <a name="cfn-kinesis-queue-queueattributes-visibilitytimeoutseconds"></a>
The duration, in seconds, that a record is in flight and not visible to any consumer instance after it is received. A record that is not acknowledged before this duration elapses becomes visible in the queue again and can be received by any consumer instance. If you omit this attribute when you create a queue, the queue uses 30 seconds.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `43200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
