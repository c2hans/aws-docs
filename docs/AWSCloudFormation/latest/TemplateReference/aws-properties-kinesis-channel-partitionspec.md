---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesis-channel-partitionspec.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Kinesis::Channel PartitionSpec
<a name="aws-properties-kinesis-channel-partitionspec"></a>

Specifies how the destination table is partitioned.

## Syntax
<a name="aws-properties-kinesis-channel-partitionspec-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesis-channel-partitionspec-syntax.json"></a>

```
{
  "[PartitionFields](#cfn-kinesis-channel-partitionspec-partitionfields)" : {{[ PartitionField, ... ]}}
}
```

### YAML
<a name="aws-properties-kinesis-channel-partitionspec-syntax.yaml"></a>

```
  [PartitionFields](#cfn-kinesis-channel-partitionspec-partitionfields): {{
    - PartitionField}}
```

## Properties
<a name="aws-properties-kinesis-channel-partitionspec-properties"></a>

`PartitionFields`  <a name="cfn-kinesis-channel-partitionspec-partitionfields"></a>
The list of partition fields.
*Required*: Yes
*Type*: Array of [PartitionField](aws-properties-kinesis-channel-partitionfield.md)
*Minimum*: `1`
*Maximum*: `10`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
