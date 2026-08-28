---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_PivotTableOptions.html
---

# PivotTableOptions
<a name="API_PivotTableOptions"></a>

The table options for a pivot table visual.

## Contents
<a name="API_PivotTableOptions_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CellStyle **   <a name="QS-Type-PivotTableOptions-CellStyle"></a>
The table cell style of cells.
Type: [TableCellStyle](API_TableCellStyle.md) object
Required: No

 ** CollapsedRowDimensionsVisibility **   <a name="QS-Type-PivotTableOptions-CollapsedRowDimensionsVisibility"></a>
The visibility setting of a pivot table's collapsed row dimension fields. If the value of this structure is `HIDDEN`, all collapsed columns in a pivot table are automatically hidden. The default value is `VISIBLE`.
Type: String
Valid Values: `HIDDEN | VISIBLE`
Required: No

 ** ColumnHeaderStyle **   <a name="QS-Type-PivotTableOptions-ColumnHeaderStyle"></a>
The table cell style of the column header.
Type: [TableCellStyle](API_TableCellStyle.md) object
Required: No

 ** ColumnNamesVisibility **   <a name="QS-Type-PivotTableOptions-ColumnNamesVisibility"></a>
The visibility of the column names.
Type: String
Valid Values: `HIDDEN | VISIBLE`
Required: No

 ** DefaultCellWidth **   <a name="QS-Type-PivotTableOptions-DefaultCellWidth"></a>
The default cell width of the pivot table.
Type: String
Required: No

 ** MetricPlacement **   <a name="QS-Type-PivotTableOptions-MetricPlacement"></a>
The metric placement (row, column) options.
Type: String
Valid Values: `ROW | COLUMN`
Required: No

 ** RowAlternateColorOptions **   <a name="QS-Type-PivotTableOptions-RowAlternateColorOptions"></a>
The row alternate color options (widget status, row alternate colors).
Type: [RowAlternateColorOptions](API_RowAlternateColorOptions.md) object
Required: No

 ** RowFieldNamesStyle **   <a name="QS-Type-PivotTableOptions-RowFieldNamesStyle"></a>
The table cell style of row field names.
Type: [TableCellStyle](API_TableCellStyle.md) object
Required: No

 ** RowHeaderStyle **   <a name="QS-Type-PivotTableOptions-RowHeaderStyle"></a>
The table cell style of the row headers.
Type: [TableCellStyle](API_TableCellStyle.md) object
Required: No

 ** RowsLabelOptions **   <a name="QS-Type-PivotTableOptions-RowsLabelOptions"></a>
The options for the label that is located above the row headers. This option is only applicable when `RowsLayout` is set to `HIERARCHY`.
Type: [PivotTableRowsLabelOptions](API_PivotTableRowsLabelOptions.md) object
Required: No

 ** RowsLayout **   <a name="QS-Type-PivotTableOptions-RowsLayout"></a>
The layout for the row dimension headers of a pivot table. Choose one of the following options.
+  `TABULAR`: (Default) Each row field is displayed in a separate column.
+  `HIERARCHY`: All row fields are displayed in a single column. Indentation is used to differentiate row headers of different fields.
Type: String
Valid Values: `TABULAR | HIERARCHY`
Required: No

 ** SingleMetricVisibility **   <a name="QS-Type-PivotTableOptions-SingleMetricVisibility"></a>
The visibility of the single metric options.
Type: String
Valid Values: `HIDDEN | VISIBLE`
Required: No

 ** ToggleButtonsVisibility **   <a name="QS-Type-PivotTableOptions-ToggleButtonsVisibility"></a>
Determines the visibility of the pivot table.
Type: String
Valid Values: `HIDDEN | VISIBLE`
Required: No

## See Also
<a name="API_PivotTableOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/PivotTableOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/PivotTableOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/PivotTableOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
