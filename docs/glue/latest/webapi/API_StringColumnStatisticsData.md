---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_StringColumnStatisticsData.html
---

# StringColumnStatisticsData
<a name="API_StringColumnStatisticsData"></a>

Defines column statistics supported for character sequence data values.

## Contents
<a name="API_StringColumnStatisticsData_Contents"></a>

 ** AverageLength **   <a name="Glue-Type-StringColumnStatisticsData-AverageLength"></a>
The average string length in the column.
Type: Double
Valid Range: Minimum value of 0.0.
Required: Yes

 ** MaximumLength **   <a name="Glue-Type-StringColumnStatisticsData-MaximumLength"></a>
The size of the longest string in the column.
Type: Long
Valid Range: Minimum value of 0.
Required: Yes

 ** NumberOfDistinctValues **   <a name="Glue-Type-StringColumnStatisticsData-NumberOfDistinctValues"></a>
The number of distinct values in a column.
Type: Long
Valid Range: Minimum value of 0.
Required: Yes

 ** NumberOfNulls **   <a name="Glue-Type-StringColumnStatisticsData-NumberOfNulls"></a>
The number of null values in the column.
Type: Long
Valid Range: Minimum value of 0.
Required: Yes

## See Also
<a name="API_StringColumnStatisticsData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/StringColumnStatisticsData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/StringColumnStatisticsData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/StringColumnStatisticsData)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
