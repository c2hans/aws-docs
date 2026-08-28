---
source_url: https://docs.aws.amazon.com/timestream/latest/APIReference/API_query_ScheduledQueryDescription.html
---

# ScheduledQueryDescription
<a name="API_query_ScheduledQueryDescription"></a>

Structure that describes scheduled query.

## Contents
<a name="API_query_ScheduledQueryDescription_Contents"></a>

 ** Arn **   <a name="timestream-Type-query_ScheduledQueryDescription-Arn"></a>
Scheduled query ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** Name **   <a name="timestream-Type-query_ScheduledQueryDescription-Name"></a>
Name of the scheduled query.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9|!\-_*'\(\)]([a-zA-Z0-9]|[!\-_*'\(\)\/.])+`
Required: Yes

 ** NotificationConfiguration **   <a name="timestream-Type-query_ScheduledQueryDescription-NotificationConfiguration"></a>
Notification configuration.
Type: [NotificationConfiguration](API_query_NotificationConfiguration.md) object
Required: Yes

 ** QueryString **   <a name="timestream-Type-query_ScheduledQueryDescription-QueryString"></a>
The query to be run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 262144.
Required: Yes

 ** ScheduleConfiguration **   <a name="timestream-Type-query_ScheduledQueryDescription-ScheduleConfiguration"></a>
Schedule configuration.
Type: [ScheduleConfiguration](API_query_ScheduleConfiguration.md) object
Required: Yes

 ** State **   <a name="timestream-Type-query_ScheduledQueryDescription-State"></a>
State of the scheduled query.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: Yes

 ** CreationTime **   <a name="timestream-Type-query_ScheduledQueryDescription-CreationTime"></a>
Creation time of the scheduled query.
Type: Timestamp
Required: No

 ** ErrorReportConfiguration **   <a name="timestream-Type-query_ScheduledQueryDescription-ErrorReportConfiguration"></a>
Error-reporting configuration for the scheduled query.
Type: [ErrorReportConfiguration](API_query_ErrorReportConfiguration.md) object
Required: No

 ** KmsKeyId **   <a name="timestream-Type-query_ScheduledQueryDescription-KmsKeyId"></a>
A customer provided KMS key used to encrypt the scheduled query resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** LastRunSummary **   <a name="timestream-Type-query_ScheduledQueryDescription-LastRunSummary"></a>
Runtime summary for the last scheduled query run.
Type: [ScheduledQueryRunSummary](API_query_ScheduledQueryRunSummary.md) object
Required: No

 ** NextInvocationTime **   <a name="timestream-Type-query_ScheduledQueryDescription-NextInvocationTime"></a>
The next time the scheduled query is scheduled to run.
Type: Timestamp
Required: No

 ** PreviousInvocationTime **   <a name="timestream-Type-query_ScheduledQueryDescription-PreviousInvocationTime"></a>
Last time the query was run.
Type: Timestamp
Required: No

 ** RecentlyFailedRuns **   <a name="timestream-Type-query_ScheduledQueryDescription-RecentlyFailedRuns"></a>
Runtime summary for the last five failed scheduled query runs.
Type: Array of [ScheduledQueryRunSummary](API_query_ScheduledQueryRunSummary.md) objects
Required: No

 ** ScheduledQueryExecutionRoleArn **   <a name="timestream-Type-query_ScheduledQueryDescription-ScheduledQueryExecutionRoleArn"></a>
IAM role that Timestream uses to run the schedule query.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** TargetConfiguration **   <a name="timestream-Type-query_ScheduledQueryDescription-TargetConfiguration"></a>
Scheduled query target store configuration.
Type: [TargetConfiguration](API_query_TargetConfiguration.md) object
Required: No

## See Also
<a name="API_query_ScheduledQueryDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/timestream-query-2018-11-01/ScheduledQueryDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/timestream-query-2018-11-01/ScheduledQueryDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/timestream-query-2018-11-01/ScheduledQueryDescription)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Timestream for LiveAnalytics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query timestream` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
