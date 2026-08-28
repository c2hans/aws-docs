---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3tables-table-icebergsortfield.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3Tables::Table IcebergSortField
<a name="aws-properties-s3tables-table-icebergsortfield"></a>

Defines a single sort field in an Iceberg sort order specification.

## Syntax
<a name="aws-properties-s3tables-table-icebergsortfield-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3tables-table-icebergsortfield-syntax.json"></a>

```
{
  "[Direction](#cfn-s3tables-table-icebergsortfield-direction)" : {{String}},
  "[NullOrder](#cfn-s3tables-table-icebergsortfield-nullorder)" : {{String}},
  "[SourceId](#cfn-s3tables-table-icebergsortfield-sourceid)" : {{Integer}},
  "[Transform](#cfn-s3tables-table-icebergsortfield-transform)" : {{String}}
}
```

### YAML
<a name="aws-properties-s3tables-table-icebergsortfield-syntax.yaml"></a>

```
  [Direction](#cfn-s3tables-table-icebergsortfield-direction): {{String}}
  [NullOrder](#cfn-s3tables-table-icebergsortfield-nullorder): {{String}}
  [SourceId](#cfn-s3tables-table-icebergsortfield-sourceid): {{Integer}}
  [Transform](#cfn-s3tables-table-icebergsortfield-transform): {{String}}
```

## Properties
<a name="aws-properties-s3tables-table-icebergsortfield-properties"></a>

`Direction`  <a name="cfn-s3tables-table-icebergsortfield-direction"></a>
The sort direction. Valid values are `asc` for ascending order or `desc` for descending order.
*Required*: Yes
*Type*: String
*Allowed values*: `asc | desc`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`NullOrder`  <a name="cfn-s3tables-table-icebergsortfield-nullorder"></a>
Specifies how null values are ordered. Valid values are `nulls-first` to place nulls before non-null values, or `nulls-last` to place nulls after non-null values.
*Required*: Yes
*Type*: String
*Allowed values*: `nulls-first | nulls-last`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SourceId`  <a name="cfn-s3tables-table-icebergsortfield-sourceid"></a>
The ID of the source schema field to sort by. This must reference a valid field ID from the table schema.
*Required*: Yes
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Transform`  <a name="cfn-s3tables-table-icebergsortfield-transform"></a>
The transform to apply to the source field before sorting. Use `identity` to sort by the field value directly, or specify other transforms as needed.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
