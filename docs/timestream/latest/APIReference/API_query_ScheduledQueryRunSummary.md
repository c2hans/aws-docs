---
source_url: https://docs.aws.amazon.com/timestream/latest/APIReference/API_query_ScheduledQueryRunSummary.html
---

# ScheduledQueryRunSummary
<a name="API_query_ScheduledQueryRunSummary"></a>

Run summary for the scheduled query

## Contents
<a name="API_query_ScheduledQueryRunSummary_Contents"></a>

 ** ErrorReportLocation **   <a name="timestream-Type-query_ScheduledQueryRunSummary-ErrorReportLocation"></a>
S3 location for error report.
Type: [ErrorReportLocation](API_query_ErrorReportLocation.md) object
Required: No

 ** ExecutionStats **   <a name="timestream-Type-query_ScheduledQueryRunSummary-ExecutionStats"></a>
Runtime statistics for a scheduled run.
Type: [ExecutionStats](API_query_ExecutionStats.md) object
Required: No

 ** FailureReason **   <a name="timestream-Type-query_ScheduledQueryRunSummary-FailureReason"></a>
Error message for the scheduled query in case of failure. You might have to look at the error report to get more detailed error reasons.
Type: String
Required: No

 ** InvocationTime **   <a name="timestream-Type-query_ScheduledQueryRunSummary-InvocationTime"></a>
InvocationTime for this run. This is the time at which the query is scheduled to run. Parameter `@scheduled_runtime` can be used in the query to get the value.
Type: Timestamp
Required: No

 ** QueryInsightsResponse **   <a name="timestream-Type-query_ScheduledQueryRunSummary-QueryInsightsResponse"></a>
Provides various insights and metrics related to the run summary of the scheduled query.
Type: [ScheduledQueryInsightsResponse](API_query_ScheduledQueryInsightsResponse.md) object
Required: No

 ** RunStatus **   <a name="timestream-Type-query_ScheduledQueryRunSummary-RunStatus"></a>
The status of a scheduled query run.
Type: String
Valid Values: `AUTO_TRIGGER_SUCCESS | AUTO_TRIGGER_FAILURE | MANUAL_TRIGGER_SUCCESS | MANUAL_TRIGGER_FAILURE`
Required: No

 ** TriggerTime **   <a name="timestream-Type-query_ScheduledQueryRunSummary-TriggerTime"></a>
The actual time when the query was run.
Type: Timestamp
Required: No

## See Also
<a name="API_query_ScheduledQueryRunSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/timestream-query-2018-11-01/ScheduledQueryRunSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/timestream-query-2018-11-01/ScheduledQueryRunSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/timestream-query-2018-11-01/ScheduledQueryRunSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Timestream for LiveAnalytics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query timestream` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
