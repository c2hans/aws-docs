---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesisfirehose-deliverystream-partitionfield.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KinesisFirehose::DeliveryStream PartitionField
<a name="aws-properties-kinesisfirehose-deliverystream-partitionfield"></a>

Represents a single field in a `PartitionSpec`.

Amazon Data Firehose is in preview release and is subject to change.

## Syntax
<a name="aws-properties-kinesisfirehose-deliverystream-partitionfield-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesisfirehose-deliverystream-partitionfield-syntax.json"></a>

```
{
  "[SourceName](#cfn-kinesisfirehose-deliverystream-partitionfield-sourcename)" : {{String}}
}
```

### YAML
<a name="aws-properties-kinesisfirehose-deliverystream-partitionfield-syntax.yaml"></a>

```
  [SourceName](#cfn-kinesisfirehose-deliverystream-partitionfield-sourcename): {{String}}
```

## Properties
<a name="aws-properties-kinesisfirehose-deliverystream-partitionfield-properties"></a>

`SourceName`  <a name="cfn-kinesisfirehose-deliverystream-partitionfield-sourcename"></a>
 The column name to be configured in partition spec.
Amazon Data Firehose is in preview release and is subject to change.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
