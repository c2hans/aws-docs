---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_AggFunction.html
---

# AggFunction
<a name="API_AggFunction"></a>

The definition of an Agg function.

## Contents
<a name="API_AggFunction_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Aggregation **   <a name="QS-Type-AggFunction-Aggregation"></a>
The aggregation of an Agg function.
Type: String
Valid Values: `SUM | MIN | MAX | COUNT | AVERAGE | DISTINCT_COUNT | STDEV | STDEVP | VAR | VARP | PERCENTILE | MEDIAN | PTD_SUM | PTD_MIN | PTD_MAX | PTD_COUNT | PTD_DISTINCT_COUNT | PTD_AVERAGE | COLUMN | CUSTOM`
Required: No

 ** AggregationFunctionParameters **   <a name="QS-Type-AggFunction-AggregationFunctionParameters"></a>
The aggregation parameters for an Agg function.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 256.
Value Length Constraints: Maximum length of 1024.
Required: No

 ** Period **   <a name="QS-Type-AggFunction-Period"></a>
The period of an Agg function.
Type: String
Valid Values: `SECOND | MINUTE | HOUR | DAY | WEEK | MONTH | QUARTER | YEAR`
Required: No

 ** PeriodField **   <a name="QS-Type-AggFunction-PeriodField"></a>
The period field for an Agg function.
Type: String
Length Constraints: Maximum length of 256.
Required: No

## See Also
<a name="API_AggFunction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/AggFunction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/AggFunction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/AggFunction)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
