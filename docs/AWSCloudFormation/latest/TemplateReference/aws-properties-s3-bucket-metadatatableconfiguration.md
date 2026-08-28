---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3-bucket-metadatatableconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3::Bucket MetadataTableConfiguration
<a name="aws-properties-s3-bucket-metadatatableconfiguration"></a>

**Important**
 We recommend that you create your S3 Metadata configurations by using the V2 [ MetadataConfiguration](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3-bucket-metadataconfiguration.html) resource type. We no longer recommend using the V1 `MetadataTableConfiguration` resource type.
If you created your S3 Metadata configuration before July 15, 2025, we recommend that you delete and re-create your configuration by using the [ MetadataConfiguration](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3-bucket-metadataconfiguration.html) resource type so that you can expire journal table records and create a live inventory table.

Creates a V1 S3 Metadata configuration for a general purpose bucket. For more information, see [Accelerating data discovery with S3 Metadata](https://docs.aws.amazon.com/AmazonS3/latest/userguide/metadata-tables-overview.html) in the *Amazon S3 User Guide*.

## Syntax
<a name="aws-properties-s3-bucket-metadatatableconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3-bucket-metadatatableconfiguration-syntax.json"></a>

```
{
  "[S3TablesDestination](#cfn-s3-bucket-metadatatableconfiguration-s3tablesdestination)" : {{S3TablesDestination}}
}
```

### YAML
<a name="aws-properties-s3-bucket-metadatatableconfiguration-syntax.yaml"></a>

```
  [S3TablesDestination](#cfn-s3-bucket-metadatatableconfiguration-s3tablesdestination): {{
    S3TablesDestination}}
```

## Properties
<a name="aws-properties-s3-bucket-metadatatableconfiguration-properties"></a>

`S3TablesDestination`  <a name="cfn-s3-bucket-metadatatableconfiguration-s3tablesdestination"></a>
 The destination information for the metadata table configuration. The destination table bucket must be in the same Region and AWS account as the general purpose bucket. The specified metadata table name must be unique within the `aws_s3_metadata` namespace in the destination table bucket.
*Required*: Yes
*Type*: [S3TablesDestination](aws-properties-s3-bucket-s3tablesdestination.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Examples
<a name="aws-properties-s3-bucket-metadatatableconfiguration--examples"></a>

### Create metadata table configuration
<a name="aws-properties-s3-bucket-metadatatableconfiguration--examples--Create_metadata_table_configuration"></a>

The following example creates an S3 Metadata configuration for the specified general purpose bucket. To use this example, replace ` amzn-s3-demo-table-bucket ` with the name of the table bucket where you want to store your metadata table, replace ` amzn-s3-demo-bucket1 ` with the name of your general purpose bucket, and replace `my_metadata_table_name` with the name that you want to use for your metadata table.

#### JSON
<a name="aws-properties-s3-bucket-metadatatableconfiguration--examples--Create_metadata_table_configuration--json"></a>

```
{
  "Resources": {
    "S3TableBucket": {
      "Type": "AWS::S3Tables::TableBucket",
      "Properties": {
        "TableBucketName": "amzn-s3-demo-table-bucket"
      }
    },
    "S3Bucket": {
      "Type": "AWS::S3::Bucket",
      "DeletionPolicy": "Retain",
      "Properties": {
        "BucketName": "amzn-s3-demo-bucket1",
        "MetadataTableConfiguration": {
          "S3TablesDestination": {
            "TableBucketArn": {
              "Fn::GetAtt": [
                "S3TableBucket",
                "TableBucketARN"
              ]
            },
            "TableName": "my_metadata_table_name",
            "TableNamespace": "aws_s3_metadata"
          }
        }
      }
    }
  }
}
```

#### YAML
<a name="aws-properties-s3-bucket-metadatatableconfiguration--examples--Create_metadata_table_configuration--yaml"></a>

```
Resources:
  S3TableBucket:
    Type: AWS::S3Tables::TableBucket
    Properties:
      TableBucketName: amzn-s3-demo-table-bucket

  S3Bucket:
    Type: AWS::S3::Bucket
    DeletionPolicy: Retain
    Properties:
      BucketName: amzn-s3-demo-bucket1
      MetadataTableConfiguration:
        S3TablesDestination:
          TableBucketArn: !GetAtt S3TableBucket.TableBucketARN
          TableName: my_metadata_table_name
          TableNamespace: aws_s3_metadata
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
