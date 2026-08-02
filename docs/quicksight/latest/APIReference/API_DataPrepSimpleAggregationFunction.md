---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DataPrepSimpleAggregationFunction.html
---

# DataPrepSimpleAggregationFunction
<a name="API_DataPrepSimpleAggregationFunction"></a>

A simple aggregation function that performs standard statistical operations on a column.

## Contents
<a name="API_DataPrepSimpleAggregationFunction_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** FunctionType **   <a name="QS-Type-DataPrepSimpleAggregationFunction-FunctionType"></a>
The type of aggregation function to perform, such as `COUNT`, `SUM`, `AVERAGE`, `MIN`, `MAX`, `MEDIAN`, `VARIANCE`, or `STANDARD_DEVIATION`.
Type: String
Valid Values: `COUNT | DISTINCT_COUNT | SUM | AVERAGE | MAX | MIN`
Required: Yes

 ** InputColumnName **   <a name="QS-Type-DataPrepSimpleAggregationFunction-InputColumnName"></a>
The name of the column on which to perform the aggregation function.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

## See Also
<a name="API_DataPrepSimpleAggregationFunction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DataPrepSimpleAggregationFunction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DataPrepSimpleAggregationFunction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DataPrepSimpleAggregationFunction)
