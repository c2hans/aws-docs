---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3-bucket-targetobjectkeyformat.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3::Bucket TargetObjectKeyFormat
<a name="aws-properties-s3-bucket-targetobjectkeyformat"></a>

Amazon S3 key format for log objects. Only one format, PartitionedPrefix or SimplePrefix, is allowed.

## Syntax
<a name="aws-properties-s3-bucket-targetobjectkeyformat-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3-bucket-targetobjectkeyformat-syntax.json"></a>

```
{
  "[PartitionedPrefix](#cfn-s3-bucket-targetobjectkeyformat-partitionedprefix)" : {{PartitionedPrefix}},
  "[SimplePrefix](#cfn-s3-bucket-targetobjectkeyformat-simpleprefix)" : {{Json}}
}
```

### YAML
<a name="aws-properties-s3-bucket-targetobjectkeyformat-syntax.yaml"></a>

```
  [PartitionedPrefix](#cfn-s3-bucket-targetobjectkeyformat-partitionedprefix): {{
    PartitionedPrefix}}
  [SimplePrefix](#cfn-s3-bucket-targetobjectkeyformat-simpleprefix): {{Json}}
```

## Properties
<a name="aws-properties-s3-bucket-targetobjectkeyformat-properties"></a>

`PartitionedPrefix`  <a name="cfn-s3-bucket-targetobjectkeyformat-partitionedprefix"></a>
Partitioned S3 key for log objects.
*Required*: No
*Type*: [PartitionedPrefix](aws-properties-s3-bucket-partitionedprefix.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SimplePrefix`  <a name="cfn-s3-bucket-targetobjectkeyformat-simpleprefix"></a>
To use the simple format for S3 keys for log objects. To specify SimplePrefix format, set SimplePrefix to {}.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
