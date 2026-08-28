---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3tables-table-icebergsortorder.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3Tables::Table IcebergSortOrder
<a name="aws-properties-s3tables-table-icebergsortorder"></a>

Defines the sort order for data within an Iceberg table. Sorting data can improve query performance by enabling more efficient data skipping.

## Syntax
<a name="aws-properties-s3tables-table-icebergsortorder-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3tables-table-icebergsortorder-syntax.json"></a>

```
{
  "[Fields](#cfn-s3tables-table-icebergsortorder-fields)" : {{[ IcebergSortField, ... ]}},
  "[OrderId](#cfn-s3tables-table-icebergsortorder-orderid)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-s3tables-table-icebergsortorder-syntax.yaml"></a>

```
  [Fields](#cfn-s3tables-table-icebergsortorder-fields): {{
    - IcebergSortField}}
  [OrderId](#cfn-s3tables-table-icebergsortorder-orderid): {{Integer}}
```

## Properties
<a name="aws-properties-s3tables-table-icebergsortorder-properties"></a>

`Fields`  <a name="cfn-s3tables-table-icebergsortorder-fields"></a>
The list of sort fields that define how data is sorted within files. Each field specifies a source field, sort direction, and null ordering. This field is required if `writeOrder` is provided.
*Required*: Yes
*Type*: Array of [IcebergSortField](aws-properties-s3tables-table-icebergsortfield.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`OrderId`  <a name="cfn-s3tables-table-icebergsortorder-orderid"></a>
The unique identifier for this sort order. If not specified, defaults to `1`. The order ID is used by Apache Iceberg to track sort order evolution.
*Required*: No
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
