---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DataSetNumericFilterCondition.html
---

# DataSetNumericFilterCondition
<a name="API_DataSetNumericFilterCondition"></a>

A filter condition for numeric columns, supporting both comparison and range-based filtering.

## Contents
<a name="API_DataSetNumericFilterCondition_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ColumnName **   <a name="QS-Type-DataSetNumericFilterCondition-ColumnName"></a>
The name of the numeric column to filter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** ComparisonFilterCondition **   <a name="QS-Type-DataSetNumericFilterCondition-ComparisonFilterCondition"></a>
A comparison-based filter condition for the numeric column.
Type: [DataSetNumericComparisonFilterCondition](API_DataSetNumericComparisonFilterCondition.md) object
Required: No

 ** RangeFilterCondition **   <a name="QS-Type-DataSetNumericFilterCondition-RangeFilterCondition"></a>
A range-based filter condition for the numeric column, filtering values between minimum and maximum numbers.
Type: [DataSetNumericRangeFilterCondition](API_DataSetNumericRangeFilterCondition.md) object
Required: No

## See Also
<a name="API_DataSetNumericFilterCondition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DataSetNumericFilterCondition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DataSetNumericFilterCondition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DataSetNumericFilterCondition)
