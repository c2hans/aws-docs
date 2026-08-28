---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DataPrepAggregationFunction.html
---

# DataPrepAggregationFunction
<a name="API_DataPrepAggregationFunction"></a>

Defines the type of aggregation function to apply to data during data preparation, supporting simple and list aggregations.

## Contents
<a name="API_DataPrepAggregationFunction_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ListAggregation **   <a name="QS-Type-DataPrepAggregationFunction-ListAggregation"></a>
A list aggregation function that concatenates values from multiple rows into a single delimited string.
Type: [DataPrepListAggregationFunction](API_DataPrepListAggregationFunction.md) object
Required: No

 ** SimpleAggregation **   <a name="QS-Type-DataPrepAggregationFunction-SimpleAggregation"></a>
A simple aggregation function such as `SUM`, `COUNT`, `AVERAGE`, `MIN`, `MAX`, `MEDIAN`, `VARIANCE`, or `STANDARD_DEVIATION`.
Type: [DataPrepSimpleAggregationFunction](API_DataPrepSimpleAggregationFunction.md) object
Required: No

## See Also
<a name="API_DataPrepAggregationFunction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DataPrepAggregationFunction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DataPrepAggregationFunction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DataPrepAggregationFunction)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
