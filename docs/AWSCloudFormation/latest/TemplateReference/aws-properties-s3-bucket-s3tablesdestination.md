---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3-bucket-s3tablesdestination.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3::Bucket S3TablesDestination
<a name="aws-properties-s3-bucket-s3tablesdestination"></a>

 The destination information for a V1 S3 Metadata configuration. The destination table bucket must be in the same Region and AWS account as the general purpose bucket. The specified metadata table name must be unique within the `aws_s3_metadata` namespace in the destination table bucket.

## Syntax
<a name="aws-properties-s3-bucket-s3tablesdestination-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3-bucket-s3tablesdestination-syntax.json"></a>

```
{
  "[TableArn](#cfn-s3-bucket-s3tablesdestination-tablearn)" : {{String}},
  "[TableBucketArn](#cfn-s3-bucket-s3tablesdestination-tablebucketarn)" : {{String}},
  "[TableName](#cfn-s3-bucket-s3tablesdestination-tablename)" : {{String}},
  "[TableNamespace](#cfn-s3-bucket-s3tablesdestination-tablenamespace)" : {{String}}
}
```

### YAML
<a name="aws-properties-s3-bucket-s3tablesdestination-syntax.yaml"></a>

```
  [TableArn](#cfn-s3-bucket-s3tablesdestination-tablearn): {{String}}
  [TableBucketArn](#cfn-s3-bucket-s3tablesdestination-tablebucketarn): {{String}}
  [TableName](#cfn-s3-bucket-s3tablesdestination-tablename): {{String}}
  [TableNamespace](#cfn-s3-bucket-s3tablesdestination-tablenamespace): {{String}}
```

## Properties
<a name="aws-properties-s3-bucket-s3tablesdestination-properties"></a>

`TableArn`  <a name="cfn-s3-bucket-s3tablesdestination-tablearn"></a>
The Amazon Resource Name (ARN) for the metadata table in the metadata table configuration. The specified metadata table name must be unique within the `aws_s3_metadata` namespace in the destination table bucket.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TableBucketArn`  <a name="cfn-s3-bucket-s3tablesdestination-tablebucketarn"></a>
 The Amazon Resource Name (ARN) for the table bucket that's specified as the destination in the metadata table configuration. The destination table bucket must be in the same Region and AWS account as the general purpose bucket.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TableName`  <a name="cfn-s3-bucket-s3tablesdestination-tablename"></a>
 The name for the metadata table in your metadata table configuration. The specified metadata table name must be unique within the `aws_s3_metadata` namespace in the destination table bucket.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TableNamespace`  <a name="cfn-s3-bucket-s3tablesdestination-tablenamespace"></a>
The table bucket namespace for the metadata table in your metadata table configuration. This value is always `aws_s3_metadata`.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
