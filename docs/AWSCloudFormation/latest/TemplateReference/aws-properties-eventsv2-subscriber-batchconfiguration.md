---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-eventsv2-subscriber-batchconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EventsV2::Subscriber BatchConfiguration
<a name="aws-properties-eventsv2-subscriber-batchconfiguration"></a>

Configuration for batching events into a single delivery.

## Syntax
<a name="aws-properties-eventsv2-subscriber-batchconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-eventsv2-subscriber-batchconfiguration-syntax.json"></a>

```
{
  "[MaxBatchSize](#cfn-eventsv2-subscriber-batchconfiguration-maxbatchsize)" : {{Integer}},
  "[MaxBatchWindowInSeconds](#cfn-eventsv2-subscriber-batchconfiguration-maxbatchwindowinseconds)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-eventsv2-subscriber-batchconfiguration-syntax.yaml"></a>

```
  [MaxBatchSize](#cfn-eventsv2-subscriber-batchconfiguration-maxbatchsize): {{Integer}}
  [MaxBatchWindowInSeconds](#cfn-eventsv2-subscriber-batchconfiguration-maxbatchwindowinseconds): {{Integer}}
```

## Properties
<a name="aws-properties-eventsv2-subscriber-batchconfiguration-properties"></a>

`MaxBatchSize`  <a name="cfn-eventsv2-subscriber-batchconfiguration-maxbatchsize"></a>
The maximum number of events in a single batch delivered to the target. The maximum depends on the target: 500 for Kinesis Data Streams and Amazon Data Firehose, 100 for Lambda, Step Functions, and `AWS::EventsV2::EventBus` targets, 10 for Amazon SQS, Amazon SNS, and `AWS::Events::EventBus` targets, and 1 for API Gateway, API destinations, and universal service integration targets. The service rejects a value above the target's maximum. Fewer events may be delivered when the batch window elapses. When omitted, the default is 10 for Lambda and Step Functions targets and the target's maximum for other targets. The resolved value applied by the service is returned on read.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaxBatchWindowInSeconds`  <a name="cfn-eventsv2-subscriber-batchconfiguration-maxbatchwindowinseconds"></a>
The maximum time in seconds to wait for a batch to fill before delivering it, 0-300. The default is 0 (no wait). The resolved value applied by the service is returned on read.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `300`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
