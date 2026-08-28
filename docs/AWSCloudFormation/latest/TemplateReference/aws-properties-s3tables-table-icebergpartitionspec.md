---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3tables-table-icebergpartitionspec.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3Tables::Table IcebergPartitionSpec
<a name="aws-properties-s3tables-table-icebergpartitionspec"></a>

Defines how data in an Iceberg table is partitioned. Partitioning helps optimize query performance by organizing data into separate files based on field values. Each partition field specifies a transform to apply to a source field.

## Syntax
<a name="aws-properties-s3tables-table-icebergpartitionspec-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3tables-table-icebergpartitionspec-syntax.json"></a>

```
{
  "[Fields](#cfn-s3tables-table-icebergpartitionspec-fields)" : {{[ IcebergPartitionField, ... ]}},
  "[SpecId](#cfn-s3tables-table-icebergpartitionspec-specid)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-s3tables-table-icebergpartitionspec-syntax.yaml"></a>

```
  [Fields](#cfn-s3tables-table-icebergpartitionspec-fields): {{
    - IcebergPartitionField}}
  [SpecId](#cfn-s3tables-table-icebergpartitionspec-specid): {{Integer}}
```

## Properties
<a name="aws-properties-s3tables-table-icebergpartitionspec-properties"></a>

`Fields`  <a name="cfn-s3tables-table-icebergpartitionspec-fields"></a>
The list of partition fields that define how the table data is partitioned. Each field specifies a source field and a transform to apply. This field is required if `partitionSpec` is provided.
*Required*: Yes
*Type*: Array of [IcebergPartitionField](aws-properties-s3tables-table-icebergpartitionfield.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SpecId`  <a name="cfn-s3tables-table-icebergpartitionspec-specid"></a>
The unique identifier for this partition specification. If not specified, defaults to `0`.
*Required*: No
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
