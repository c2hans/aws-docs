---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_TriggerHistoryRecord.html
---

# TriggerHistoryRecord
<a name="API_TriggerHistoryRecord"></a>

A record of a scheduled query execution, including execution status, timestamp, and destination processing results.

## Contents
<a name="API_TriggerHistoryRecord_Contents"></a>

 ** destinations **   <a name="CWL-Type-TriggerHistoryRecord-destinations"></a>
Information about destination processing for this query execution.
Type: Array of [ScheduledQueryDestination](API_ScheduledQueryDestination.md) objects
Required: No

 ** errorMessage **   <a name="CWL-Type-TriggerHistoryRecord-errorMessage"></a>
Error message if the query execution failed.
Type: String
Required: No

 ** executionStatus **   <a name="CWL-Type-TriggerHistoryRecord-executionStatus"></a>
The execution status of the scheduled query run.
Type: String
Valid Values: `Running | InvalidQuery | Complete | Failed | Timeout`
Required: No

 ** queryId **   <a name="CWL-Type-TriggerHistoryRecord-queryId"></a>
The unique identifier for this query execution.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** triggeredTimestamp **   <a name="CWL-Type-TriggerHistoryRecord-triggeredTimestamp"></a>
The timestamp when the scheduled query execution was triggered.
Type: Long
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_TriggerHistoryRecord_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/TriggerHistoryRecord)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/TriggerHistoryRecord)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/TriggerHistoryRecord)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch Logs. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatchLogs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
