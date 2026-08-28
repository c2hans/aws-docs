---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cleanrooms-configuredtable-aggregatecolumn.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRooms::ConfiguredTable AggregateColumn
<a name="aws-properties-cleanrooms-configuredtable-aggregatecolumn"></a>

Column in configured table that can be used in aggregate function in query.

## Syntax
<a name="aws-properties-cleanrooms-configuredtable-aggregatecolumn-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cleanrooms-configuredtable-aggregatecolumn-syntax.json"></a>

```
{
  "[ColumnNames](#cfn-cleanrooms-configuredtable-aggregatecolumn-columnnames)" : {{[ String, ... ]}},
  "[Function](#cfn-cleanrooms-configuredtable-aggregatecolumn-function)" : {{String}}
}
```

### YAML
<a name="aws-properties-cleanrooms-configuredtable-aggregatecolumn-syntax.yaml"></a>

```
  [ColumnNames](#cfn-cleanrooms-configuredtable-aggregatecolumn-columnnames): {{
    - String}}
  [Function](#cfn-cleanrooms-configuredtable-aggregatecolumn-function): {{String}}
```

## Properties
<a name="aws-properties-cleanrooms-configuredtable-aggregatecolumn-properties"></a>

`ColumnNames`  <a name="cfn-cleanrooms-configuredtable-aggregatecolumn-columnnames"></a>
Column names in configured table of aggregate columns.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Function`  <a name="cfn-cleanrooms-configuredtable-aggregatecolumn-function"></a>
Aggregation function that can be applied to aggregate column in query.
*Required*: Yes
*Type*: String
*Allowed values*: `SUM | SUM_DISTINCT | COUNT | COUNT_DISTINCT | AVG`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
