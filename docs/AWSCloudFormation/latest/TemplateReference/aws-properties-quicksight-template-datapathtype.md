---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-datapathtype.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template DataPathType
<a name="aws-properties-quicksight-template-datapathtype"></a>

The type of the data path value.

## Syntax
<a name="aws-properties-quicksight-template-datapathtype-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-datapathtype-syntax.json"></a>

```
{
  "[PivotTableDataPathType](#cfn-quicksight-template-datapathtype-pivottabledatapathtype)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-template-datapathtype-syntax.yaml"></a>

```
  [PivotTableDataPathType](#cfn-quicksight-template-datapathtype-pivottabledatapathtype): {{String}}
```

## Properties
<a name="aws-properties-quicksight-template-datapathtype-properties"></a>

`PivotTableDataPathType`  <a name="cfn-quicksight-template-datapathtype-pivottabledatapathtype"></a>
The type of data path value utilized in a pivot table. Choose one of the following options:
+ `HIERARCHY_ROWS_LAYOUT_COLUMN` - The type of data path for the rows layout column, when `RowsLayout` is set to `HIERARCHY`.
+ `MULTIPLE_ROW_METRICS_COLUMN` - The type of data path for the metric column when the row is set to Metric Placement.
+ `EMPTY_COLUMN_HEADER` - The type of data path for the column with empty column header, when there is no field in `ColumnsFieldWell` and the row is set to Metric Placement.
+ `COUNT_METRIC_COLUMN` - The type of data path for the column with `COUNT` as the metric, when there is no field in the `ValuesFieldWell`.
*Required*: No
*Type*: String
*Allowed values*: `HIERARCHY_ROWS_LAYOUT_COLUMN | MULTIPLE_ROW_METRICS_COLUMN | EMPTY_COLUMN_HEADER | COUNT_METRIC_COLUMN`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
