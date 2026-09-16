---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesis-channel-partitionfield.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Kinesis::Channel PartitionField
<a name="aws-properties-kinesis-channel-partitionfield"></a>

Specifies a single partition field.

## Syntax
<a name="aws-properties-kinesis-channel-partitionfield-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesis-channel-partitionfield-syntax.json"></a>

```
{
  "[SourceName](#cfn-kinesis-channel-partitionfield-sourcename)" : {{String}},
  "[Transform](#cfn-kinesis-channel-partitionfield-transform)" : {{String}}
}
```

### YAML
<a name="aws-properties-kinesis-channel-partitionfield-syntax.yaml"></a>

```
  [SourceName](#cfn-kinesis-channel-partitionfield-sourcename): {{String}}
  [Transform](#cfn-kinesis-channel-partitionfield-transform): {{String}}
```

## Properties
<a name="aws-properties-kinesis-channel-partitionfield-properties"></a>

`SourceName`  <a name="cfn-kinesis-channel-partitionfield-sourcename"></a>
The name of the source column used for partitioning. This column must be of the `timestamptz` type.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9._]+$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Transform`  <a name="cfn-kinesis-channel-partitionfield-transform"></a>
The partition transform to apply. The only valid value is `TIME_HOUR`.
*Required*: Yes
*Type*: String
*Allowed values*: `TIME_HOUR`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
