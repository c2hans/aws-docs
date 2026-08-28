---
source_url: https://docs.aws.amazon.com/athena/latest/APIReference/API_QueryRuntimeStatisticsRows.html
---

# QueryRuntimeStatisticsRows
<a name="API_QueryRuntimeStatisticsRows"></a>

Statistics such as input rows and bytes read by the query, rows and bytes output by the query, and the number of rows written by the query.

## Contents
<a name="API_QueryRuntimeStatisticsRows_Contents"></a>

 ** InputBytes **   <a name="athena-Type-QueryRuntimeStatisticsRows-InputBytes"></a>
The number of bytes read to execute the query.
Type: Long
Required: No

 ** InputRows **   <a name="athena-Type-QueryRuntimeStatisticsRows-InputRows"></a>
The number of rows read to execute the query.
Type: Long
Required: No

 ** OutputBytes **   <a name="athena-Type-QueryRuntimeStatisticsRows-OutputBytes"></a>
The number of bytes returned by the query.
Type: Long
Required: No

 ** OutputRows **   <a name="athena-Type-QueryRuntimeStatisticsRows-OutputRows"></a>
The number of rows returned by the query.
Type: Long
Required: No

## See Also
<a name="API_QueryRuntimeStatisticsRows_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/athena-2017-05-18/QueryRuntimeStatisticsRows)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/athena-2017-05-18/QueryRuntimeStatisticsRows)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/athena-2017-05-18/QueryRuntimeStatisticsRows)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
