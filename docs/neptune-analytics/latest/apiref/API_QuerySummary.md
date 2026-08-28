---
source_url: https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_QuerySummary.html
---

# QuerySummary
<a name="API_QuerySummary"></a>

Details of the query listed.

## Contents
<a name="API_QuerySummary_Contents"></a>

 ** elapsed **   <a name="neptunegraph-Type-QuerySummary-elapsed"></a>
The running time of the query, in milliseconds.
Type: Integer
Required: No

 ** id **   <a name="neptunegraph-Type-QuerySummary-id"></a>
A string representation of the id of the query.
Type: String
Required: No

 ** queryString **   <a name="neptunegraph-Type-QuerySummary-queryString"></a>
The actual query text. The `queryString` may be truncated if the actual query string is too long.
Type: String
Required: No

 ** state **   <a name="neptunegraph-Type-QuerySummary-state"></a>
State of the query.
Type: String
Valid Values: `RUNNING | WAITING | CANCELLING`
Required: No

 ** waited **   <a name="neptunegraph-Type-QuerySummary-waited"></a>
The amount of time, in milliseconds, the query has waited in the queue before being picked up by a worker thread.
Type: Integer
Required: No

## See Also
<a name="API_QuerySummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-graph-2023-11-29/QuerySummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-graph-2023-11-29/QuerySummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-graph-2023-11-29/QuerySummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for NeptuneAnalyticsAPI. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune-analytics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
