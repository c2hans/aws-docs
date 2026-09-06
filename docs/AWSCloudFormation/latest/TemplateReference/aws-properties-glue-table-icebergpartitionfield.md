---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-table-icebergpartitionfield.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::Table IcebergPartitionField
<a name="aws-properties-glue-table-icebergpartitionfield"></a>

Defines a single partition field within an Iceberg partition specification, including the source field, transformation function, partition name, and unique identifier.

## Syntax
<a name="aws-properties-glue-table-icebergpartitionfield-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-table-icebergpartitionfield-syntax.json"></a>

```
{
  "[FieldId](#cfn-glue-table-icebergpartitionfield-fieldid)" : {{Integer}},
  "[Name](#cfn-glue-table-icebergpartitionfield-name)" : {{String}},
  "[SourceId](#cfn-glue-table-icebergpartitionfield-sourceid)" : {{Integer}},
  "[Transform](#cfn-glue-table-icebergpartitionfield-transform)" : {{String}}
}
```

### YAML
<a name="aws-properties-glue-table-icebergpartitionfield-syntax.yaml"></a>

```
  [FieldId](#cfn-glue-table-icebergpartitionfield-fieldid): {{Integer}}
  [Name](#cfn-glue-table-icebergpartitionfield-name): {{String}}
  [SourceId](#cfn-glue-table-icebergpartitionfield-sourceid): {{Integer}}
  [Transform](#cfn-glue-table-icebergpartitionfield-transform): {{String}}
```

## Properties
<a name="aws-properties-glue-table-icebergpartitionfield-properties"></a>

`FieldId`  <a name="cfn-glue-table-icebergpartitionfield-fieldid"></a>
The unique identifier assigned to this partition field within the Iceberg table's partition specification.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-glue-table-icebergpartitionfield-name"></a>
The name of the partition field as it will appear in the partitioned table structure.
*Required*: Yes
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceId`  <a name="cfn-glue-table-icebergpartitionfield-sourceid"></a>
The identifier of the source field from the table schema that this partition field is based on.
*Required*: Yes
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Transform`  <a name="cfn-glue-table-icebergpartitionfield-transform"></a>
The transformation function applied to the source field to create the partition, such as identity, bucket, truncate, year, month, day, or hour.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
