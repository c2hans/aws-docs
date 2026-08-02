---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_AttributeAggregationFunction.html
---

# AttributeAggregationFunction
<a name="API_AttributeAggregationFunction"></a>

Aggregation for attributes.

## Contents
<a name="API_AttributeAggregationFunction_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** SimpleAttributeAggregation **   <a name="QS-Type-AttributeAggregationFunction-SimpleAttributeAggregation"></a>
The built-in aggregation functions for attributes.
+  `UNIQUE_VALUE`: Returns the unique value for a field, aggregated by the dimension fields.
Type: String
Valid Values: `UNIQUE_VALUE`
Required: No

 ** ValueForMultipleValues **   <a name="QS-Type-AttributeAggregationFunction-ValueForMultipleValues"></a>
Used by the `UNIQUE_VALUE` aggregation function. If there are multiple values for the field used by the aggregation, the value for this property will be returned instead. Defaults to '\*'.
Type: String
Required: No

## See Also
<a name="API_AttributeAggregationFunction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/AttributeAggregationFunction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/AttributeAggregationFunction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/AttributeAggregationFunction)
