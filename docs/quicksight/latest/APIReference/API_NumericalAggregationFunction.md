---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_NumericalAggregationFunction.html
---

# NumericalAggregationFunction
<a name="API_NumericalAggregationFunction"></a>

Aggregation for numerical values.

## Contents
<a name="API_NumericalAggregationFunction_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** PercentileAggregation **   <a name="QS-Type-NumericalAggregationFunction-PercentileAggregation"></a>
An aggregation based on the percentile of values in a dimension or measure.
Type: [PercentileAggregation](API_PercentileAggregation.md) object
Required: No

 ** SimpleNumericalAggregation **   <a name="QS-Type-NumericalAggregationFunction-SimpleNumericalAggregation"></a>
Built-in aggregation functions for numerical values.
+  `SUM`: The sum of a dimension or measure.
+  `AVERAGE`: The average of a dimension or measure.
+  `MIN`: The minimum value of a dimension or measure.
+  `MAX`: The maximum value of a dimension or measure.
+  `COUNT`: The count of a dimension or measure.
+  `DISTINCT_COUNT`: The count of distinct values in a dimension or measure.
+  `VAR`: The variance of a dimension or measure.
+  `VARP`: The partitioned variance of a dimension or measure.
+  `STDEV`: The standard deviation of a dimension or measure.
+  `STDEVP`: The partitioned standard deviation of a dimension or measure.
+  `MEDIAN`: The median value of a dimension or measure.
Type: String
Valid Values: `SUM | AVERAGE | MIN | MAX | COUNT | DISTINCT_COUNT | VAR | VARP | STDEV | STDEVP | MEDIAN`
Required: No

## See Also
<a name="API_NumericalAggregationFunction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/NumericalAggregationFunction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/NumericalAggregationFunction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/NumericalAggregationFunction)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
