---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3tables-tablebucket-targetobjectkeyformat.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3Tables::TableBucket TargetObjectKeyFormat
<a name="aws-properties-s3tables-tablebucket-targetobjectkeyformat"></a>

The key format of the log objects. Only `PartitionedPrefix` is supported.

## Syntax
<a name="aws-properties-s3tables-tablebucket-targetobjectkeyformat-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3tables-tablebucket-targetobjectkeyformat-syntax.json"></a>

```
{
  "[PartitionedPrefix](#cfn-s3tables-tablebucket-targetobjectkeyformat-partitionedprefix)" : {{PartitionedPrefix}}
}
```

### YAML
<a name="aws-properties-s3tables-tablebucket-targetobjectkeyformat-syntax.yaml"></a>

```
  [PartitionedPrefix](#cfn-s3tables-tablebucket-targetobjectkeyformat-partitionedprefix): {{
    PartitionedPrefix}}
```

## Properties
<a name="aws-properties-s3tables-tablebucket-targetobjectkeyformat-properties"></a>

`PartitionedPrefix`  <a name="cfn-s3tables-tablebucket-targetobjectkeyformat-partitionedprefix"></a>
Partitions log object keys by date.
*Required*: Yes
*Type*: [PartitionedPrefix](aws-properties-s3tables-tablebucket-partitionedprefix.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
