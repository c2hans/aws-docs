---
source_url: https://docs.aws.amazon.com/timestream/latest/APIReference/API_query_QueryTemporalRange.html
---

# QueryTemporalRange
<a name="API_query_QueryTemporalRange"></a>

Provides insights into the temporal range of the query, including the table with the largest (max) time range.

## Contents
<a name="API_query_QueryTemporalRange_Contents"></a>

 ** Max **   <a name="timestream-Type-query_QueryTemporalRange-Max"></a>
Encapsulates the following properties that provide insights into the most sub-optimal performing table on the temporal axis:
+  `Value` – The maximum duration in nanoseconds between the start and end of the query.
+  `TableArn` – The Amazon Resource Name (ARN) of the table which is queried with the largest time range.
Type: [QueryTemporalRangeMax](API_query_QueryTemporalRangeMax.md) object
Required: No

## See Also
<a name="API_query_QueryTemporalRange_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/timestream-query-2018-11-01/QueryTemporalRange)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/timestream-query-2018-11-01/QueryTemporalRange)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/timestream-query-2018-11-01/QueryTemporalRange)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Timestream for LiveAnalytics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query timestream` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
