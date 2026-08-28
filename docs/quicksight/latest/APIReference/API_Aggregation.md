---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_Aggregation.html
---

# Aggregation
<a name="API_Aggregation"></a>

Defines an aggregation function to be applied to grouped data, creating a new column with the calculated result.

## Contents
<a name="API_Aggregation_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AggregationFunction **   <a name="QS-Type-Aggregation-AggregationFunction"></a>
The aggregation function to apply, such as `SUM`, `COUNT`, `AVERAGE`, `MIN`, `MAX`
Type: [DataPrepAggregationFunction](API_DataPrepAggregationFunction.md) object
Required: Yes

 ** NewColumnId **   <a name="QS-Type-Aggregation-NewColumnId"></a>
A unique identifier for the new column that will contain the aggregated values.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** NewColumnName **   <a name="QS-Type-Aggregation-NewColumnName"></a>
The name for the new column that will contain the aggregated values.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

## See Also
<a name="API_Aggregation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/Aggregation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/Aggregation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/Aggregation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
