---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesis-channel-s3tableconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Kinesis::Channel S3TableConfiguration
<a name="aws-properties-kinesis-channel-s3tableconfiguration"></a>

<a name="aws-properties-kinesis-channel-s3tableconfiguration-description"></a>The `S3TableConfiguration` property type specifies Property description not available. for an [AWS::Kinesis::Channel](aws-resource-kinesis-channel.md).

## Syntax
<a name="aws-properties-kinesis-channel-s3tableconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesis-channel-s3tableconfiguration-syntax.json"></a>

```
{
  "[CompressionType](#cfn-kinesis-channel-s3tableconfiguration-compressiontype)" : {{String}},
  "[Namespace](#cfn-kinesis-channel-s3tableconfiguration-namespace)" : {{String}},
  "[PartitionSpec](#cfn-kinesis-channel-s3tableconfiguration-partitionspec)" : {{PartitionSpec}},
  "[TableBucketARN](#cfn-kinesis-channel-s3tableconfiguration-tablebucketarn)" : {{String}},
  "[TableName](#cfn-kinesis-channel-s3tableconfiguration-tablename)" : {{String}}
}
```

### YAML
<a name="aws-properties-kinesis-channel-s3tableconfiguration-syntax.yaml"></a>

```
  [CompressionType](#cfn-kinesis-channel-s3tableconfiguration-compressiontype): {{String}}
  [Namespace](#cfn-kinesis-channel-s3tableconfiguration-namespace): {{String}}
  [PartitionSpec](#cfn-kinesis-channel-s3tableconfiguration-partitionspec): {{
    PartitionSpec}}
  [TableBucketARN](#cfn-kinesis-channel-s3tableconfiguration-tablebucketarn): {{String}}
  [TableName](#cfn-kinesis-channel-s3tableconfiguration-tablename): {{String}}
```

## Properties
<a name="aws-properties-kinesis-channel-s3tableconfiguration-properties"></a>

`CompressionType`  <a name="cfn-kinesis-channel-s3tableconfiguration-compressiontype"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `NONE | ZSTD | SNAPPY`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Namespace`  <a name="cfn-kinesis-channel-s3tableconfiguration-namespace"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9a-z_]+$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PartitionSpec`  <a name="cfn-kinesis-channel-s3tableconfiguration-partitionspec"></a>
Property description not available.
*Required*: No
*Type*: [PartitionSpec](aws-properties-kinesis-channel-partitionspec.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TableBucketARN`  <a name="cfn-kinesis-channel-s3tableconfiguration-tablebucketarn"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[-a-z0-9]*:s3tables:[-a-z0-9]+:[0-9]{12}:bucket/[a-z0-9_-]{3,63}$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TableName`  <a name="cfn-kinesis-channel-s3tableconfiguration-tablename"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9a-z_]+$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
