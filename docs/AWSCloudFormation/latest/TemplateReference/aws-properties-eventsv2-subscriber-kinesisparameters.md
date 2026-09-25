---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-eventsv2-subscriber-kinesisparameters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EventsV2::Subscriber KinesisParameters
<a name="aws-properties-eventsv2-subscriber-kinesisparameters"></a>

Parameters for writing events to an Amazon Kinesis Data Streams target.

## Syntax
<a name="aws-properties-eventsv2-subscriber-kinesisparameters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-eventsv2-subscriber-kinesisparameters-syntax.json"></a>

```
{
  "[ExplicitHashKey](#cfn-eventsv2-subscriber-kinesisparameters-explicithashkey)" : {{String}},
  "[PartitionKey](#cfn-eventsv2-subscriber-kinesisparameters-partitionkey)" : {{String}}
}
```

### YAML
<a name="aws-properties-eventsv2-subscriber-kinesisparameters-syntax.yaml"></a>

```
  [ExplicitHashKey](#cfn-eventsv2-subscriber-kinesisparameters-explicithashkey): {{String}}
  [PartitionKey](#cfn-eventsv2-subscriber-kinesisparameters-partitionkey): {{String}}
```

## Properties
<a name="aws-properties-eventsv2-subscriber-kinesisparameters-properties"></a>

`ExplicitHashKey`  <a name="cfn-eventsv2-subscriber-kinesisparameters-explicithashkey"></a>
An explicit hash key that overrides the partition key's shard assignment. Accepts a literal value or a JSONata expression.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PartitionKey`  <a name="cfn-eventsv2-subscriber-kinesisparameters-partitionkey"></a>
The partition key that determines which shard each record is written to. Accepts a literal value or a JSONata expression.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
