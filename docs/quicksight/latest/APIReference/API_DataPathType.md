---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DataPathType.html
---

# DataPathType
<a name="API_DataPathType"></a>

The type of the data path value.

## Contents
<a name="API_DataPathType_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** PivotTableDataPathType **   <a name="QS-Type-DataPathType-PivotTableDataPathType"></a>
The type of data path value utilized in a pivot table. Choose one of the following options:
+  `HIERARCHY_ROWS_LAYOUT_COLUMN` - The type of data path for the rows layout column, when `RowsLayout` is set to `HIERARCHY`.
+  `MULTIPLE_ROW_METRICS_COLUMN` - The type of data path for the metric column when the row is set to Metric Placement.
+  `EMPTY_COLUMN_HEADER` - The type of data path for the column with empty column header, when there is no field in `ColumnsFieldWell` and the row is set to Metric Placement.
+  `COUNT_METRIC_COLUMN` - The type of data path for the column with `COUNT` as the metric, when there is no field in the `ValuesFieldWell`.
Type: String
Valid Values: `HIERARCHY_ROWS_LAYOUT_COLUMN | MULTIPLE_ROW_METRICS_COLUMN | EMPTY_COLUMN_HEADER | COUNT_METRIC_COLUMN`
Required: No

## See Also
<a name="API_DataPathType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DataPathType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DataPathType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DataPathType)
