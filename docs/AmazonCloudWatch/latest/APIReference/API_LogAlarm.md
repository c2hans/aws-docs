---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_LogAlarm.html
---

# LogAlarm
<a name="API_LogAlarm"></a>

The details about a log alarm.

## Contents
<a name="API_LogAlarm_Contents"></a>

 ** ActionLogLineCount **   <a name="ACW-Type-LogAlarm-ActionLogLineCount"></a>
The number of log lines from the most recent scheduled query execution that are included in alarm action notifications. Valid range is 0 through 50. A value of 0 means no log lines are included.
Type: Integer
Required: No

 ** ActionLogLineRoleArn **   <a name="ACW-Type-LogAlarm-ActionLogLineRoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role that CloudWatch assumes to retrieve log events for inclusion in alarm action notifications. Set when `ActionLogLineCount` is greater than 0.
Type: String
Required: No

 ** ActionsEnabled **   <a name="ACW-Type-LogAlarm-ActionsEnabled"></a>
Indicates whether actions should be executed during any changes to the alarm state.
Type: Boolean
Required: No

 ** AlarmActions **   <a name="ACW-Type-LogAlarm-AlarmActions"></a>
The actions to execute when this alarm transitions to the `ALARM` state from any other state. Each action is specified as an Amazon Resource Name (ARN).
Type: Array of strings
Array Members: Maximum number of 5 items.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** AlarmArn **   <a name="ACW-Type-LogAlarm-AlarmArn"></a>
The Amazon Resource Name (ARN) of the alarm.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Required: No

 ** AlarmConfigurationUpdatedTimestamp **   <a name="ACW-Type-LogAlarm-AlarmConfigurationUpdatedTimestamp"></a>
The time stamp of the last update to the alarm configuration.
Type: Timestamp
Required: No

 ** AlarmDescription **   <a name="ACW-Type-LogAlarm-AlarmDescription"></a>
The description of the alarm.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** AlarmName **   <a name="ACW-Type-LogAlarm-AlarmName"></a>
The name of the alarm.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** ComparisonOperator **   <a name="ACW-Type-LogAlarm-ComparisonOperator"></a>
The arithmetic operation to use when comparing the aggregated query result and the threshold. The aggregated query result is used as the first operand.
Type: String
Valid Values: `GreaterThanOrEqualToThreshold | GreaterThanThreshold | LessThanThreshold | LessThanOrEqualToThreshold | LessThanLowerOrGreaterThanUpperThreshold | LessThanLowerThreshold | GreaterThanUpperThreshold`
Required: No

 ** EvaluationState **   <a name="ACW-Type-LogAlarm-EvaluationState"></a>
If the value of this field is `EVALUATION_ERROR`, it indicates configuration errors in the alarm setup that require review and correction. Refer to the `StateReason` field of the alarm for more details.
If the value of this field is `EVALUATION_FAILURE`, it indicates temporary CloudWatch issues. We recommend manual monitoring until the issue is resolved.
If the value of this field is `PARTIAL_DATA`, it indicates that the query returned the maximum 500 contributor groups but more matched. The alarm evaluates the available contributors, but results might be incomplete.
Type: String
Valid Values: `PARTIAL_DATA | EVALUATION_FAILURE | EVALUATION_ERROR`
Required: No

 ** InsufficientDataActions **   <a name="ACW-Type-LogAlarm-InsufficientDataActions"></a>
The actions to execute when this alarm transitions to the `INSUFFICIENT_DATA` state from any other state. Each action is specified as an Amazon Resource Name (ARN).
Type: Array of strings
Array Members: Maximum number of 5 items.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** OKActions **   <a name="ACW-Type-LogAlarm-OKActions"></a>
The actions to execute when this alarm transitions to the `OK` state from any other state. Each action is specified as an Amazon Resource Name (ARN).
Type: Array of strings
Array Members: Maximum number of 5 items.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** QueryResultsToAlarm **   <a name="ACW-Type-LogAlarm-QueryResultsToAlarm"></a>
The number of query results, out of the most recent `QueryResultsToEvaluate` results, that must breach the threshold to trigger the alarm to transition to `ALARM` (the M in M-of-N evaluation).
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** QueryResultsToEvaluate **   <a name="ACW-Type-LogAlarm-QueryResultsToEvaluate"></a>
The number of most recent scheduled query results that the alarm evaluates against the threshold (the N in M-of-N evaluation).
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** ScheduledQueryConfiguration **   <a name="ACW-Type-LogAlarm-ScheduledQueryConfiguration"></a>
The configuration of the underlying CloudWatch Logs scheduled query, including the query string, log groups, schedule, aggregation expression, and the ARN of the managed scheduled query.
Type: [ScheduledQueryConfiguration](API_ScheduledQueryConfiguration.md) object
Required: No

 ** StateReason **   <a name="ACW-Type-LogAlarm-StateReason"></a>
An explanation for the alarm state, in text format.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1023.
Required: No

 ** StateReasonData **   <a name="ACW-Type-LogAlarm-StateReasonData"></a>
An explanation for the alarm state, in JSON format.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4000.
Required: No

 ** StateTransitionedTimestamp **   <a name="ACW-Type-LogAlarm-StateTransitionedTimestamp"></a>
The date and time that the alarm's `StateValue` most recently changed.
Type: Timestamp
Required: No

 ** StateUpdatedTimestamp **   <a name="ACW-Type-LogAlarm-StateUpdatedTimestamp"></a>
The time stamp of the last update to the value of either the `StateValue` or `EvaluationState` parameters.
Type: Timestamp
Required: No

 ** StateValue **   <a name="ACW-Type-LogAlarm-StateValue"></a>
The state value for the alarm.
Type: String
Valid Values: `OK | ALARM | INSUFFICIENT_DATA`
Required: No

 ** Threshold **   <a name="ACW-Type-LogAlarm-Threshold"></a>
The value to compare with the aggregated query result.
Type: Double
Required: No

 ** TreatMissingData **   <a name="ACW-Type-LogAlarm-TreatMissingData"></a>
How this alarm handles missing data points. Valid values are `breaching`, `notBreaching`, `ignore`, and `missing`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

## See Also
<a name="API_LogAlarm_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/LogAlarm)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/LogAlarm)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/LogAlarm)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
