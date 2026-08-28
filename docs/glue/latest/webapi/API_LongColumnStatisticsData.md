---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_LongColumnStatisticsData.html
---

# LongColumnStatisticsData
<a name="API_LongColumnStatisticsData"></a>

Defines column statistics supported for integer data columns.

## Contents
<a name="API_LongColumnStatisticsData_Contents"></a>

 ** NumberOfDistinctValues **   <a name="Glue-Type-LongColumnStatisticsData-NumberOfDistinctValues"></a>
The number of distinct values in a column.
Type: Long
Valid Range: Minimum value of 0.
Required: Yes

 ** NumberOfNulls **   <a name="Glue-Type-LongColumnStatisticsData-NumberOfNulls"></a>
The number of null values in the column.
Type: Long
Valid Range: Minimum value of 0.
Required: Yes

 ** MaximumValue **   <a name="Glue-Type-LongColumnStatisticsData-MaximumValue"></a>
The highest value in the column.
Type: Long
Required: No

 ** MinimumValue **   <a name="Glue-Type-LongColumnStatisticsData-MinimumValue"></a>
The lowest value in the column.
Type: Long
Required: No

## See Also
<a name="API_LongColumnStatisticsData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/LongColumnStatisticsData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/LongColumnStatisticsData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/LongColumnStatisticsData)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
