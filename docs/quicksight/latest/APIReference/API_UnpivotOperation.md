---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UnpivotOperation.html
---

# UnpivotOperation
<a name="API_UnpivotOperation"></a>

A transform operation that converts columns into rows, normalizing the data structure.

## Contents
<a name="API_UnpivotOperation_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Alias **   <a name="QS-Type-UnpivotOperation-Alias"></a>
Alias for this operation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** ColumnsToUnpivot **   <a name="QS-Type-UnpivotOperation-ColumnsToUnpivot"></a>
The list of columns to unpivot from the source data.
Type: Array of [ColumnToUnpivot](API_ColumnToUnpivot.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: Yes

 ** Source **   <a name="QS-Type-UnpivotOperation-Source"></a>
The source transform operation that provides input data for unpivoting.
Type: [TransformOperationSource](API_TransformOperationSource.md) object
Required: Yes

 ** UnpivotedLabelColumnId **   <a name="QS-Type-UnpivotOperation-UnpivotedLabelColumnId"></a>
A unique identifier for the new column that will contain the unpivoted column names.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** UnpivotedLabelColumnName **   <a name="QS-Type-UnpivotOperation-UnpivotedLabelColumnName"></a>
The name for the new column that will contain the unpivoted column names.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** UnpivotedValueColumnId **   <a name="QS-Type-UnpivotOperation-UnpivotedValueColumnId"></a>
A unique identifier for the new column that will contain the unpivoted values.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** UnpivotedValueColumnName **   <a name="QS-Type-UnpivotOperation-UnpivotedValueColumnName"></a>
The name for the new column that will contain the unpivoted values.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

## See Also
<a name="API_UnpivotOperation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/UnpivotOperation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/UnpivotOperation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/UnpivotOperation)
