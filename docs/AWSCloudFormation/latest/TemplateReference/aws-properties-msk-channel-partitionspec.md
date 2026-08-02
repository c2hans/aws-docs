---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-msk-channel-partitionspec.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MSK::Channel PartitionSpec
<a name="aws-properties-msk-channel-partitionspec"></a>

<a name="aws-properties-msk-channel-partitionspec-description"></a>The `PartitionSpec` property type specifies Property description not available. for an [AWS::MSK::Channel](aws-resource-msk-channel.md).

## Syntax
<a name="aws-properties-msk-channel-partitionspec-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-msk-channel-partitionspec-syntax.json"></a>

```
{
  "[PartitionStrategy](#cfn-msk-channel-partitionspec-partitionstrategy)" : {{String}},
  "[SourceList](#cfn-msk-channel-partitionspec-sourcelist)" : {{[ PartitionSource, ... ]}}
}
```

### YAML
<a name="aws-properties-msk-channel-partitionspec-syntax.yaml"></a>

```
  [PartitionStrategy](#cfn-msk-channel-partitionspec-partitionstrategy): {{String}}
  [SourceList](#cfn-msk-channel-partitionspec-sourcelist): {{
    - PartitionSource}}
```

## Properties
<a name="aws-properties-msk-channel-partitionspec-properties"></a>

`PartitionStrategy`  <a name="cfn-msk-channel-partitionspec-partitionstrategy"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `TIME_HOUR`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SourceList`  <a name="cfn-msk-channel-partitionspec-sourcelist"></a>
Property description not available.
*Required*: No
*Type*: Array of [PartitionSource](aws-properties-msk-channel-partitionsource.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
