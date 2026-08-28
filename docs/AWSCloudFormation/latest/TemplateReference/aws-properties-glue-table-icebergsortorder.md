---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-table-icebergsortorder.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::Table IcebergSortOrder
<a name="aws-properties-glue-table-icebergsortorder"></a>

Defines the sort order specification for an Iceberg table, determining how data should be ordered within partitions to optimize query performance.

## Syntax
<a name="aws-properties-glue-table-icebergsortorder-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-table-icebergsortorder-syntax.json"></a>

```
{
  "[Fields](#cfn-glue-table-icebergsortorder-fields)" : {{[ IcebergSortField, ... ]}},
  "[OrderId](#cfn-glue-table-icebergsortorder-orderid)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-glue-table-icebergsortorder-syntax.yaml"></a>

```
  [Fields](#cfn-glue-table-icebergsortorder-fields): {{
    - IcebergSortField}}
  [OrderId](#cfn-glue-table-icebergsortorder-orderid): {{Integer}}
```

## Properties
<a name="aws-properties-glue-table-icebergsortorder-properties"></a>

`Fields`  <a name="cfn-glue-table-icebergsortorder-fields"></a>
The list of fields and their sort directions that define the ordering criteria for the Iceberg table data.
*Required*: Yes
*Type*: Array of [IcebergSortField](aws-properties-glue-table-icebergsortfield.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OrderId`  <a name="cfn-glue-table-icebergsortorder-orderid"></a>
The unique identifier for this sort order specification within the Iceberg table's metadata.
*Required*: Yes
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
