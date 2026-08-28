---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-table-icebergsortfield.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::Table IcebergSortField
<a name="aws-properties-glue-table-icebergsortfield"></a>

Defines a single field within an Iceberg sort order specification, including the source field, transformation, sort direction, and null value ordering.

## Syntax
<a name="aws-properties-glue-table-icebergsortfield-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-table-icebergsortfield-syntax.json"></a>

```
{
  "[Direction](#cfn-glue-table-icebergsortfield-direction)" : {{String}},
  "[NullOrder](#cfn-glue-table-icebergsortfield-nullorder)" : {{String}},
  "[SourceId](#cfn-glue-table-icebergsortfield-sourceid)" : {{Integer}},
  "[Transform](#cfn-glue-table-icebergsortfield-transform)" : {{String}}
}
```

### YAML
<a name="aws-properties-glue-table-icebergsortfield-syntax.yaml"></a>

```
  [Direction](#cfn-glue-table-icebergsortfield-direction): {{String}}
  [NullOrder](#cfn-glue-table-icebergsortfield-nullorder): {{String}}
  [SourceId](#cfn-glue-table-icebergsortfield-sourceid): {{Integer}}
  [Transform](#cfn-glue-table-icebergsortfield-transform): {{String}}
```

## Properties
<a name="aws-properties-glue-table-icebergsortfield-properties"></a>

`Direction`  <a name="cfn-glue-table-icebergsortfield-direction"></a>
The sort direction for this field, either ascending or descending.
*Required*: Yes
*Type*: String
*Allowed values*: `asc | desc`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NullOrder`  <a name="cfn-glue-table-icebergsortfield-nullorder"></a>
The ordering behavior for null values in this field, specifying whether nulls should appear first or last in the sort order.
*Required*: Yes
*Type*: String
*Allowed values*: `nulls-first | nulls-last`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceId`  <a name="cfn-glue-table-icebergsortfield-sourceid"></a>
The identifier of the source field from the table schema that this sort field is based on.
*Required*: Yes
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Transform`  <a name="cfn-glue-table-icebergsortfield-transform"></a>
The transformation function applied to the source field before sorting, such as identity, bucket, or truncate.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
