---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DataPrepListAggregationFunction.html
---

# DataPrepListAggregationFunction
<a name="API_DataPrepListAggregationFunction"></a>

An aggregation function that concatenates values from multiple rows into a single string with a specified separator.

## Contents
<a name="API_DataPrepListAggregationFunction_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Distinct **   <a name="QS-Type-DataPrepListAggregationFunction-Distinct"></a>
Whether to include only distinct values in the concatenated result, removing duplicates.
Type: Boolean
Required: Yes

 ** Separator **   <a name="QS-Type-DataPrepListAggregationFunction-Separator"></a>
The string used to separate values in the concatenated result.
Type: String
Required: Yes

 ** InputColumnName **   <a name="QS-Type-DataPrepListAggregationFunction-InputColumnName"></a>
The name of the column containing values to be concatenated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

## See Also
<a name="API_DataPrepListAggregationFunction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DataPrepListAggregationFunction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DataPrepListAggregationFunction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DataPrepListAggregationFunction)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
