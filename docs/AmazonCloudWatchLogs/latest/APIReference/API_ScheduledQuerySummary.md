---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_ScheduledQuerySummary.html
---

# ScheduledQuerySummary
<a name="API_ScheduledQuerySummary"></a>

Summary information about a scheduled query, including basic configuration and execution status.

## Contents
<a name="API_ScheduledQuerySummary_Contents"></a>

 ** creationTime **   <a name="CWL-Type-ScheduledQuerySummary-creationTime"></a>
The timestamp when the scheduled query was created.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** destinationConfiguration **   <a name="CWL-Type-ScheduledQuerySummary-destinationConfiguration"></a>
Configuration for where query results are delivered.
Type: [DestinationConfiguration](API_DestinationConfiguration.md) object
Required: No

 ** lastExecutionStatus **   <a name="CWL-Type-ScheduledQuerySummary-lastExecutionStatus"></a>
The status of the most recent execution.
Type: String
Valid Values: `Running | InvalidQuery | Complete | Failed | Timeout`
Required: No

 ** lastTriggeredTime **   <a name="CWL-Type-ScheduledQuerySummary-lastTriggeredTime"></a>
The timestamp when the scheduled query was last executed.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** lastUpdatedTime **   <a name="CWL-Type-ScheduledQuerySummary-lastUpdatedTime"></a>
The timestamp when the scheduled query was last updated.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** name **   <a name="CWL-Type-ScheduledQuerySummary-name"></a>
The name of the scheduled query.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: No

 ** scheduledQueryArn **   <a name="CWL-Type-ScheduledQuerySummary-scheduledQueryArn"></a>
The ARN of the scheduled query.
Type: String
Required: No

 ** scheduleExpression **   <a name="CWL-Type-ScheduledQuerySummary-scheduleExpression"></a>
The cron expression that defines when the scheduled query runs.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** scheduleType **   <a name="CWL-Type-ScheduledQuerySummary-scheduleType"></a>
The schedule type of the scheduled query. Valid values are `CUSTOMER_MANAGED` and `AWS_MANAGED`.
Type: String
Valid Values: `CUSTOMER_MANAGED | AWS_MANAGED`
Required: No

 ** state **   <a name="CWL-Type-ScheduledQuerySummary-state"></a>
The current state of the scheduled query.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** timezone **   <a name="CWL-Type-ScheduledQuerySummary-timezone"></a>
The timezone used for evaluating the schedule expression.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## See Also
<a name="API_ScheduledQuerySummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/ScheduledQuerySummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/ScheduledQuerySummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/ScheduledQuerySummary)
