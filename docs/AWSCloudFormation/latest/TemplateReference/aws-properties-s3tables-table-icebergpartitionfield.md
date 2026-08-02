---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3tables-table-icebergpartitionfield.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3Tables::Table IcebergPartitionField
<a name="aws-properties-s3tables-table-icebergpartitionfield"></a>

Defines a single partition field in an Iceberg partition specification.

## Syntax
<a name="aws-properties-s3tables-table-icebergpartitionfield-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3tables-table-icebergpartitionfield-syntax.json"></a>

```
{
  "[FieldId](#cfn-s3tables-table-icebergpartitionfield-fieldid)" : {{Integer}},
  "[Name](#cfn-s3tables-table-icebergpartitionfield-name)" : {{String}},
  "[SourceId](#cfn-s3tables-table-icebergpartitionfield-sourceid)" : {{Integer}},
  "[Transform](#cfn-s3tables-table-icebergpartitionfield-transform)" : {{String}}
}
```

### YAML
<a name="aws-properties-s3tables-table-icebergpartitionfield-syntax.yaml"></a>

```
  [FieldId](#cfn-s3tables-table-icebergpartitionfield-fieldid): {{Integer}}
  [Name](#cfn-s3tables-table-icebergpartitionfield-name): {{String}}
  [SourceId](#cfn-s3tables-table-icebergpartitionfield-sourceid): {{Integer}}
  [Transform](#cfn-s3tables-table-icebergpartitionfield-transform): {{String}}
```

## Properties
<a name="aws-properties-s3tables-table-icebergpartitionfield-properties"></a>

`FieldId`  <a name="cfn-s3tables-table-icebergpartitionfield-fieldid"></a>
An optional unique identifier for this partition field. If not specified, S3 Tables automatically assigns a field ID.
*Required*: No
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-s3tables-table-icebergpartitionfield-name"></a>
The name for this partition field. This name is used in the partitioned file paths.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SourceId`  <a name="cfn-s3tables-table-icebergpartitionfield-sourceid"></a>
The ID of the source schema field to partition by. This must reference a valid field ID from the table schema.
*Required*: Yes
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Transform`  <a name="cfn-s3tables-table-icebergpartitionfield-transform"></a>
The partition transform to apply to the source field. Supported transforms include `identity`, `year`, `month`, `day`, `hour`, `bucket`, and `truncate`. For more information, see the [Apache Iceberg partition transforms documentation](https://iceberg.apache.org/spec/#partition-transforms).
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
