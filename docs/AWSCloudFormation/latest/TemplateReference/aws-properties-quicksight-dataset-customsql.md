---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dataset-customsql.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSet CustomSql
<a name="aws-properties-quicksight-dataset-customsql"></a>

A physical table type built from the results of the custom SQL query.

## Syntax
<a name="aws-properties-quicksight-dataset-customsql-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dataset-customsql-syntax.json"></a>

```
{
  "[Columns](#cfn-quicksight-dataset-customsql-columns)" : {{[ InputColumn, ... ]}},
  "[DataSourceArn](#cfn-quicksight-dataset-customsql-datasourcearn)" : {{String}},
  "[Name](#cfn-quicksight-dataset-customsql-name)" : {{String}},
  "[SqlQuery](#cfn-quicksight-dataset-customsql-sqlquery)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dataset-customsql-syntax.yaml"></a>

```
  [Columns](#cfn-quicksight-dataset-customsql-columns): {{
    - InputColumn}}
  [DataSourceArn](#cfn-quicksight-dataset-customsql-datasourcearn): {{String}}
  [Name](#cfn-quicksight-dataset-customsql-name): {{String}}
  [SqlQuery](#cfn-quicksight-dataset-customsql-sqlquery): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dataset-customsql-properties"></a>

`Columns`  <a name="cfn-quicksight-dataset-customsql-columns"></a>
The column schema from the SQL query result set.
*Required*: Yes
*Type*: Array of [InputColumn](aws-properties-quicksight-dataset-inputcolumn.md)
*Minimum*: `0`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataSourceArn`  <a name="cfn-quicksight-dataset-customsql-datasourcearn"></a>
The Amazon Resource Name (ARN) of the data source.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-quicksight-dataset-customsql-name"></a>
A display name for the SQL query result.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SqlQuery`  <a name="cfn-quicksight-dataset-customsql-sqlquery"></a>
The SQL query.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `168000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
