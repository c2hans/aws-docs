---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-table-icebergpartitionspec.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::Table IcebergPartitionSpec
<a name="aws-properties-glue-table-icebergpartitionspec"></a>

Defines the partitioning specification for an Iceberg table, determining how table data will be organized and partitioned for optimal query performance.

## Syntax
<a name="aws-properties-glue-table-icebergpartitionspec-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-table-icebergpartitionspec-syntax.json"></a>

```
{
  "[Fields](#cfn-glue-table-icebergpartitionspec-fields)" : {{[ IcebergPartitionField, ... ]}},
  "[SpecId](#cfn-glue-table-icebergpartitionspec-specid)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-glue-table-icebergpartitionspec-syntax.yaml"></a>

```
  [Fields](#cfn-glue-table-icebergpartitionspec-fields): {{
    - IcebergPartitionField}}
  [SpecId](#cfn-glue-table-icebergpartitionspec-specid): {{Integer}}
```

## Properties
<a name="aws-properties-glue-table-icebergpartitionspec-properties"></a>

`Fields`  <a name="cfn-glue-table-icebergpartitionspec-fields"></a>
The list of partition fields that define how the table data should be partitioned, including source fields and their transformations.
*Required*: Yes
*Type*: Array of [IcebergPartitionField](aws-properties-glue-table-icebergpartitionfield.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SpecId`  <a name="cfn-glue-table-icebergpartitionspec-specid"></a>
The unique identifier for this partition specification within the Iceberg table's metadata history.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
