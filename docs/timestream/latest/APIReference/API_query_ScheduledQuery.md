---
source_url: https://docs.aws.amazon.com/timestream/latest/APIReference/API_query_ScheduledQuery.html
---

# ScheduledQuery
<a name="API_query_ScheduledQuery"></a>

Scheduled Query

## Contents
<a name="API_query_ScheduledQuery_Contents"></a>

 ** Arn **   <a name="timestream-Type-query_ScheduledQuery-Arn"></a>
The Amazon Resource Name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** Name **   <a name="timestream-Type-query_ScheduledQuery-Name"></a>
The name of the scheduled query.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9|!\-_*'\(\)]([a-zA-Z0-9]|[!\-_*'\(\)\/.])+`
Required: Yes

 ** State **   <a name="timestream-Type-query_ScheduledQuery-State"></a>
State of scheduled query.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: Yes

 ** CreationTime **   <a name="timestream-Type-query_ScheduledQuery-CreationTime"></a>
The creation time of the scheduled query.
Type: Timestamp
Required: No

 ** ErrorReportConfiguration **   <a name="timestream-Type-query_ScheduledQuery-ErrorReportConfiguration"></a>
Configuration for scheduled query error reporting.
Type: [ErrorReportConfiguration](API_query_ErrorReportConfiguration.md) object
Required: No

 ** LastRunStatus **   <a name="timestream-Type-query_ScheduledQuery-LastRunStatus"></a>
Status of the last scheduled query run.
Type: String
Valid Values: `AUTO_TRIGGER_SUCCESS | AUTO_TRIGGER_FAILURE | MANUAL_TRIGGER_SUCCESS | MANUAL_TRIGGER_FAILURE`
Required: No

 ** NextInvocationTime **   <a name="timestream-Type-query_ScheduledQuery-NextInvocationTime"></a>
The next time the scheduled query is to be run.
Type: Timestamp
Required: No

 ** PreviousInvocationTime **   <a name="timestream-Type-query_ScheduledQuery-PreviousInvocationTime"></a>
The last time the scheduled query was run.
Type: Timestamp
Required: No

 ** TargetDestination **   <a name="timestream-Type-query_ScheduledQuery-TargetDestination"></a>
Target data source where final scheduled query result will be written.
Type: [TargetDestination](API_query_TargetDestination.md) object
Required: No

## See Also
<a name="API_query_ScheduledQuery_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/timestream-query-2018-11-01/ScheduledQuery)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/timestream-query-2018-11-01/ScheduledQuery)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/timestream-query-2018-11-01/ScheduledQuery)
