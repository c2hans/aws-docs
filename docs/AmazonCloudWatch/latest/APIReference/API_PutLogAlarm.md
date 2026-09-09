---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PutLogAlarm.html
---

# PutLogAlarm
<a name="API_PutLogAlarm"></a>

Creates or updates a log alarm. A log alarm evaluates the results of a CloudWatch Logs scheduled query against the configured threshold and comparison operator to determine its state.

When you create a log alarm, the operation creates a service-managed CloudWatch Logs scheduled query that runs the query string you provide on the schedule you configure. Each scheduled query execution returns one or more aggregated values determined by the `AggregationExpression`, and each aggregated value is compared against the alarm `Threshold` to determine the alarm state. The alarm uses M-out-of-N evaluation: if `QueryResultsToAlarm` out of the most recent `QueryResultsToEvaluate` query results breach the threshold, the alarm transitions to `ALARM`.

Log alarms support the alarm states (`OK`, `ALARM`, `INSUFFICIENT_DATA`). Configure transition actions using `OKActions`, `AlarmActions`, and `InsufficientDataActions`.

If you call this operation with the name of an existing log alarm, the operation replaces the previous configuration of that alarm.

 **Permissions**

To create or update a log alarm, you must have the `cloudwatch:PutLogAlarm` permission. The IAM role specified in `ScheduledQueryRoleARN` must grant the CloudWatch Alarms service permission to execute scheduled queries on the specified log groups. If you set `ActionLogLineCount`, the role specified in `ActionLogLineRoleArn` must grant permission to retrieve log events for inclusion in alarm notifications.

## Request Parameters
<a name="API_PutLogAlarm_RequestParameters"></a>

 ** ActionLogLineCount **
The number of log lines from the most recent scheduled query execution to include in alarm action notifications. Valid range is 0 through 50. The default is 0, which means no log lines are included.
Type: Integer
Required: No

 ** ActionLogLineRoleArn **
The Amazon Resource Name (ARN) of an IAM role that CloudWatch assumes to retrieve log events for inclusion in alarm action notifications. Required when `ActionLogLineCount` is greater than 0.
Type: String
Required: No

 ** ActionsEnabled **
Indicates whether actions should be executed during any changes to the alarm state. The default is `true`.
Type: Boolean
Required: No

 ** AlarmActions **
The actions to execute when this alarm transitions to the `ALARM` state from any other state. Each action is specified as an Amazon Resource Name (ARN).
Valid Values:
 **Amazon SNS actions:**
 `arn:aws:sns:region:account-id:sns-topic-name `
 **Lambda actions:**
+ Invoke the latest version of a Lambda function: `arn:aws:lambda:region:account-id:function:function-name `
+ Invoke a specific version of a Lambda function: `arn:aws:lambda:region:account-id:function:function-name:version-number `
+ Invoke a function by using an alias Lambda function: `arn:aws:lambda:region:account-id:function:function-name:alias-name `
 **Systems Manager actions:**
 `arn:aws:ssm:region:account-id:opsitem:severity `
Type: Array of strings
Array Members: Maximum number of 5 items.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** AlarmDescription **
The description for the alarm.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** AlarmName **
The name for the alarm. This name must be unique within the AWS account and Region.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** ComparisonOperator **
The arithmetic operation to use when comparing the aggregated query result and the threshold. The aggregated query result is used as the first operand. Valid values are `GreaterThanThreshold`, `GreaterThanOrEqualToThreshold`, `LessThanThreshold`, and `LessThanOrEqualToThreshold`.
Type: String
Valid Values: `GreaterThanOrEqualToThreshold | GreaterThanThreshold | LessThanThreshold | LessThanOrEqualToThreshold | LessThanLowerOrGreaterThanUpperThreshold | LessThanLowerThreshold | GreaterThanUpperThreshold`
Required: Yes

 ** InsufficientDataActions **
The actions to execute when this alarm transitions to the `INSUFFICIENT_DATA` state from any other state. Each action is specified as an Amazon Resource Name (ARN).
Valid Values:
 **Amazon SNS actions:**
 `arn:aws:sns:region:account-id:sns-topic-name `
 **Lambda actions:**
+ Invoke the latest version of a Lambda function: `arn:aws:lambda:region:account-id:function:function-name `
+ Invoke a specific version of a Lambda function: `arn:aws:lambda:region:account-id:function:function-name:version-number `
+ Invoke a function by using an alias Lambda function: `arn:aws:lambda:region:account-id:function:function-name:alias-name `
Type: Array of strings
Array Members: Maximum number of 5 items.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** OKActions **
The actions to execute when this alarm transitions to the `OK` state from any other state. Each action is specified as an Amazon Resource Name (ARN).
Valid Values:
 **Amazon SNS actions:**
 `arn:aws:sns:region:account-id:sns-topic-name `
 **Lambda actions:**
+ Invoke the latest version of a Lambda function: `arn:aws:lambda:region:account-id:function:function-name `
+ Invoke a specific version of a Lambda function: `arn:aws:lambda:region:account-id:function:function-name:version-number `
+ Invoke a function by using an alias Lambda function: `arn:aws:lambda:region:account-id:function:function-name:alias-name `
Type: Array of strings
Array Members: Maximum number of 5 items.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** QueryResultsToAlarm **
The number of query results, out of the most recent `QueryResultsToEvaluate` results, that must breach the threshold to trigger the alarm to transition to `ALARM` (the M in M-of-N evaluation). Must be less than or equal to `QueryResultsToEvaluate`.
Type: Integer
Valid Range: Minimum value of 1.
Required: Yes

 ** QueryResultsToEvaluate **
The number of most recent scheduled query results to evaluate against the threshold (the N in M-of-N evaluation). Valid range is 1 through 100.
Type: Integer
Valid Range: Minimum value of 1.
Required: Yes

 ** ScheduledQueryConfiguration **
The configuration of the underlying CloudWatch Logs scheduled query that this alarm evaluates, including the query string, log groups, schedule, and aggregation expression.
Type: [ScheduledQueryConfiguration](API_ScheduledQueryConfiguration.md) object
Required: Yes

 ** Tags **
A list of key-value pairs to associate with the alarm. You can use tags to categorize and manage your alarms.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** Threshold **
The value to compare with the aggregated query result.
Type: Double
Required: Yes

 ** TreatMissingData **
Sets how this alarm is to handle missing data points. Valid values are `breaching`, `notBreaching`, `ignore`, and `missing`. If this parameter is omitted, the default behavior of `missing` is used.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** WarmUpConfiguration **
The warm-up configuration for the alarm. A warm-up period delays alarm evaluation after you create or update the alarm. The warm-up period reduces alarm noise from missing data while a new resource or service starts publishing data.
For more information, see [Alarm warm-up periods](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/alarm-warm-up.html) in the *Amazon CloudWatch User Guide*.
Type: [WarmUpConfiguration](API_WarmUpConfiguration.md) object
Required: No

## Errors
<a name="API_PutLogAlarm_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** LimitExceeded **
The quota for alarms for this customer has already been reached.
 ** message **

HTTP Status Code: 400

 ** ResourceConflict **
The operation could not be completed because the request conflicts with the current state of the alarm or its underlying scheduled query resource.
HTTP Status Code: 409

## Examples
<a name="API_PutLogAlarm_Examples"></a>

### Create a log alarm that monitors error count
<a name="API_PutLogAlarm_Example_1"></a>

Create a log alarm that runs a CloudWatch Logs Insights query every 5 minutes counting log entries that contain "ERROR", and triggers when the count exceeds 10 in 3 of the last 5 evaluations.

#### Sample Request
<a name="API_PutLogAlarm_Example_1_Request"></a>

```
aws cloudwatch put-log-alarm \
    --alarm-name "HighErrorRateAlarm" \
    --alarm-description "Alarm when error count exceeds threshold" \
    --scheduled-query-configuration '{
        "QueryString": "fields @timestamp, @message | filter @message like /ERROR/",
        "LogGroupIdentifiers": ["arn:aws:logs:us-east-1:111122223333:log-group:/aws/lambda/my-function"],
        "ScheduledQueryRoleARN": "arn:aws:iam::111122223333:role/ScheduledQueryRole",
        "AggregationExpression": "count(*)",
        "ScheduleConfiguration": {
            "ScheduleExpression": "rate(5 minutes)",
            "StartTimeOffset": 360
        }
    }' \
    --query-results-to-alarm 3 \
    --query-results-to-evaluate 5 \
    --threshold 10.0 \
    --comparison-operator "GreaterThanThreshold" \
    --alarm-actions "arn:aws:sns:us-east-1:111122223333:my-topic" \
    --treat-missing-data "notBreaching"
```

#### Sample Response
<a name="API_PutLogAlarm_Example_1_Response"></a>

```
{
    "AlarmArn": "arn:aws:cloudwatch:us-east-1:111122223333:alarm:HighErrorRateAlarm"
}
```

## See Also
<a name="API_PutLogAlarm_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/monitoring-2010-08-01/PutLogAlarm)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/PutLogAlarm)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/PutLogAlarm)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/monitoring-2010-08-01/PutLogAlarm)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/PutLogAlarm)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/monitoring-2010-08-01/PutLogAlarm)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/monitoring-2010-08-01/PutLogAlarm)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/monitoring-2010-08-01/PutLogAlarm)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/PutLogAlarm)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/PutLogAlarm)
