---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-datapathtype.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis DataPathType
<a name="aws-properties-quicksight-analysis-datapathtype"></a>

The type of the data path value.

## Syntax
<a name="aws-properties-quicksight-analysis-datapathtype-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-datapathtype-syntax.json"></a>

```
{
  "[PivotTableDataPathType](#cfn-quicksight-analysis-datapathtype-pivottabledatapathtype)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-datapathtype-syntax.yaml"></a>

```
  [PivotTableDataPathType](#cfn-quicksight-analysis-datapathtype-pivottabledatapathtype): {{String}}
```

## Properties
<a name="aws-properties-quicksight-analysis-datapathtype-properties"></a>

`PivotTableDataPathType`  <a name="cfn-quicksight-analysis-datapathtype-pivottabledatapathtype"></a>
The type of data path value utilized in a pivot table. Choose one of the following options:
+ `HIERARCHY_ROWS_LAYOUT_COLUMN` - The type of data path for the rows layout column, when `RowsLayout` is set to `HIERARCHY`.
+ `MULTIPLE_ROW_METRICS_COLUMN` - The type of data path for the metric column when the row is set to Metric Placement.
+ `EMPTY_COLUMN_HEADER` - The type of data path for the column with empty column header, when there is no field in `ColumnsFieldWell` and the row is set to Metric Placement.
+ `COUNT_METRIC_COLUMN` - The type of data path for the column with `COUNT` as the metric, when there is no field in the `ValuesFieldWell`.
*Required*: No
*Type*: String
*Allowed values*: `HIERARCHY_ROWS_LAYOUT_COLUMN | MULTIPLE_ROW_METRICS_COLUMN | EMPTY_COLUMN_HEADER | COUNT_METRIC_COLUMN`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
