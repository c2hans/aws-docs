---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cleanrooms-configuredtable-comparisoncontrols.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRooms::ConfiguredTable ComparisonControls
<a name="aws-properties-cleanrooms-configuredtable-comparisoncontrols"></a>

Specifies how a query can compare the columns in a table, including literal comparisons and column-to-column comparisons.

## Syntax
<a name="aws-properties-cleanrooms-configuredtable-comparisoncontrols-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cleanrooms-configuredtable-comparisoncontrols-syntax.json"></a>

```
{
  "[AllowedColumnComparisonColumns](#cfn-cleanrooms-configuredtable-comparisoncontrols-allowedcolumncomparisoncolumns)" : {{[ String, ... ]}},
  "[AllowedLiteralComparisonColumns](#cfn-cleanrooms-configuredtable-comparisoncontrols-allowedliteralcomparisoncolumns)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-cleanrooms-configuredtable-comparisoncontrols-syntax.yaml"></a>

```
  [AllowedColumnComparisonColumns](#cfn-cleanrooms-configuredtable-comparisoncontrols-allowedcolumncomparisoncolumns): {{
    - String}}
  [AllowedLiteralComparisonColumns](#cfn-cleanrooms-configuredtable-comparisoncontrols-allowedliteralcomparisoncolumns): {{
    - String}}
```

## Properties
<a name="aws-properties-cleanrooms-configuredtable-comparisoncontrols-properties"></a>

`AllowedColumnComparisonColumns`  <a name="cfn-cleanrooms-configuredtable-comparisoncontrols-allowedcolumncomparisoncolumns"></a>
The columns that a query can compare to another column, for example, in a join, a WHERE clause, a GROUP BY clause, or a window function. AWS Clean Rooms rejects a query that uses any other column in a column-to-column comparison. Specify an empty list to block column-to-column comparison on every column.
*Required*: Yes
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AllowedLiteralComparisonColumns`  <a name="cfn-cleanrooms-configuredtable-comparisoncontrols-allowedliteralcomparisoncolumns"></a>
The columns that a query can compare to literal values, for example, in a WHERE clause. AWS Clean Rooms rejects a query that compares any other column to a literal value. Specify an empty list to block literal comparison on every column. You can't specify a column that you also use as an identity column in an aggregation threshold.
*Required*: Yes
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
