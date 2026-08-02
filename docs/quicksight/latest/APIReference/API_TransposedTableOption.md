---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_TransposedTableOption.html
---

# TransposedTableOption
<a name="API_TransposedTableOption"></a>

The column option of the transposed table.

## Contents
<a name="API_TransposedTableOption_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ColumnType **   <a name="QS-Type-TransposedTableOption-ColumnType"></a>
The column type of the column in a transposed table. Choose one of the following options:
+  `ROW_HEADER_COLUMN`: Refers to the leftmost column of the row header in the transposed table.
+  `VALUE_COLUMN`: Refers to all value columns in the transposed table.
Type: String
Valid Values: `ROW_HEADER_COLUMN | VALUE_COLUMN`
Required: Yes

 ** ColumnIndex **   <a name="QS-Type-TransposedTableOption-ColumnIndex"></a>
The index of a columns in a transposed table. The index range is 0-9999.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 9999.
Required: No

 ** ColumnWidth **   <a name="QS-Type-TransposedTableOption-ColumnWidth"></a>
The width of a column in a transposed table.
Type: String
Required: No

## See Also
<a name="API_TransposedTableOption_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/TransposedTableOption)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/TransposedTableOption)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/TransposedTableOption)
