---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_AggregationFunction.html
---

# AggregationFunction
<a name="API_AggregationFunction"></a>

An aggregation function aggregates values from a dimension or measure.

This is a union type structure. For this structure to be valid, only one of the attributes can be defined.

## Contents
<a name="API_AggregationFunction_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AttributeAggregationFunction **   <a name="QS-Type-AggregationFunction-AttributeAggregationFunction"></a>
Aggregation for attributes.
Type: [AttributeAggregationFunction](API_AttributeAggregationFunction.md) object
Required: No

 ** CategoricalAggregationFunction **   <a name="QS-Type-AggregationFunction-CategoricalAggregationFunction"></a>
Aggregation for categorical values.
+  `COUNT`: Aggregate by the total number of values, including duplicates.
+  `DISTINCT_COUNT`: Aggregate by the total number of distinct values.
Type: String
Valid Values: `COUNT | DISTINCT_COUNT`
Required: No

 ** DateAggregationFunction **   <a name="QS-Type-AggregationFunction-DateAggregationFunction"></a>
Aggregation for date values.
+  `COUNT`: Aggregate by the total number of values, including duplicates.
+  `DISTINCT_COUNT`: Aggregate by the total number of distinct values.
+  `MIN`: Select the smallest date value.
+  `MAX`: Select the largest date value.
Type: String
Valid Values: `COUNT | DISTINCT_COUNT | MIN | MAX`
Required: No

 ** NumericalAggregationFunction **   <a name="QS-Type-AggregationFunction-NumericalAggregationFunction"></a>
Aggregation for numerical values.
Type: [NumericalAggregationFunction](API_NumericalAggregationFunction.md) object
Required: No

## See Also
<a name="API_AggregationFunction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/AggregationFunction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/AggregationFunction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/AggregationFunction)
