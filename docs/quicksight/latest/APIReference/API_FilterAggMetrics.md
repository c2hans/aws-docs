---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_FilterAggMetrics.html
---

# FilterAggMetrics
<a name="API_FilterAggMetrics"></a>

The definition for the `FilterAggMetrics`.

## Contents
<a name="API_FilterAggMetrics_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Function **   <a name="QS-Type-FilterAggMetrics-Function"></a>
The function for the `FilterAggMetrics`.
Type: String
Valid Values: `SUM | MIN | MAX | COUNT | AVERAGE | DISTINCT_COUNT | STDEV | STDEVP | VAR | VARP | PERCENTILE | MEDIAN | PTD_SUM | PTD_MIN | PTD_MAX | PTD_COUNT | PTD_DISTINCT_COUNT | PTD_AVERAGE | COLUMN | CUSTOM`
Required: No

 ** MetricOperand **   <a name="QS-Type-FilterAggMetrics-MetricOperand"></a>
The metric operand of the `FilterAggMetrics`.
Type: [Identifier](API_Identifier.md) object
Required: No

 ** SortDirection **   <a name="QS-Type-FilterAggMetrics-SortDirection"></a>
The sort direction for `FilterAggMetrics`.
Type: String
Valid Values: `ASCENDING | DESCENDING`
Required: No

## See Also
<a name="API_FilterAggMetrics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/FilterAggMetrics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/FilterAggMetrics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/FilterAggMetrics)
