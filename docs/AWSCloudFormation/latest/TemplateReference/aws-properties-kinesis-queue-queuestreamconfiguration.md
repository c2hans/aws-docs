---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesis-queue-queuestreamconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Kinesis::Queue QueueStreamConfiguration

The data stream a queue delivers records from, and the position in that stream where delivery begins.

## Syntax
<a name="aws-properties-kinesis-queue-queuestreamconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesis-queue-queuestreamconfiguration-syntax.json"></a>

```json
{
  "[StartingPosition](#cfn-kinesis-queue-queuestreamconfiguration-startingposition)" : {{QueueStartingPosition}},
  "[StreamARN](#cfn-kinesis-queue-queuestreamconfiguration-streamarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-kinesis-queue-queuestreamconfiguration-syntax.yaml"></a>

```yaml
  [StartingPosition](#cfn-kinesis-queue-queuestreamconfiguration-startingposition): {{
    QueueStartingPosition}}
  [StreamARN](#cfn-kinesis-queue-queuestreamconfiguration-streamarn): {{String}}
```

## Properties
<a name="aws-properties-kinesis-queue-queuestreamconfiguration-properties"></a>

`StartingPosition`  <a name="cfn-kinesis-queue-queuestreamconfiguration-startingposition"></a>
The position in the stream from which the queue begins delivering records. The default is `LATEST`.
*Required*: No
*Type*: [QueueStartingPosition](aws-properties-kinesis-queue-queuestartingposition.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`StreamARN`  <a name="cfn-kinesis-queue-queuestreamconfiguration-streamarn"></a>
The ARN of the data stream.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws.*:kinesis:.*:\d{12}:stream/\S+`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
