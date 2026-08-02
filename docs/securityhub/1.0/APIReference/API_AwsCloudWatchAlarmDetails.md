---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsCloudWatchAlarmDetails.html
---

# AwsCloudWatchAlarmDetails
<a name="API_AwsCloudWatchAlarmDetails"></a>

Specifies an alarm and associates it with the specified metric or metric math expression.

## Contents
<a name="API_AwsCloudWatchAlarmDetails_Contents"></a>

 ** ActionsEnabled **   <a name="securityhub-Type-AwsCloudWatchAlarmDetails-ActionsEnabled"></a>
Indicates whether actions should be executed during any changes to the alarm state.
Type: Boolean
Required: No

 ** AlarmActions **   <a name="securityhub-Type-AwsCloudWatchAlarmDetails-AlarmActions"></a>
The list of actions, specified as Amazon Resource Names (ARNs) to execute when this alarm transitions into an `ALARM` state from any other state.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** AlarmArn **   <a name="securityhub-Type-AwsCloudWatchAlarmDetails-AlarmArn"></a>
The ARN of the alarm.
Type: String
Pattern: `.*\S.*`
Required: No

 ** AlarmConfigurationUpdatedTimestamp **   <a name="securityhub-Type-AwsCloudWatchAlarmDetails-AlarmConfigurationUpdatedTimestamp"></a>
The time stamp of the last update to the alarm configuration.
Type: String
Pattern: `.*\S.*`
Required: No

 ** AlarmDescription **   <a name="securityhub-Type-AwsCloudWatchAlarmDetails-AlarmDescription"></a>
The description of the alarm.
Type: String
Pattern: `.*\S.*`
Required: No

 ** AlarmName **   <a name="securityhub-Type-AwsCloudWatchAlarmDetails-AlarmName"></a>
The name of the alarm. If you don't specify a name, CloudFront generates a unique physical ID and uses that ID for the alarm name.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ComparisonOperator **   <a name="securityhub-Type-AwsCloudWatchAlarmDetails-ComparisonOperator"></a>
The arithmetic operation to use when comparing the specified statistic and threshold. The specified statistic value is used as the first operand.
Type: String
Pattern: `.*\S.*`
Required: No

 ** DatapointsToAlarm **   <a name="securityhub-Type-AwsCloudWatchAlarmDetails-DatapointsToAlarm"></a>
The number of datapoints that must be breaching to trigger the alarm.
Type: Integer
Required: No

 ** Dimensions **   <a name="securityhub-Type-AwsCloudWatchAlarmDetails-Dimensions"></a>
The dimensions for the metric associated with the alarm.
Type: Array of [AwsCloudWatchAlarmDimensionsDetails](API_AwsCloudWatchAlarmDimensionsDetails.md) objects
Required: No

 ** EvaluateLowSampleCountPercentile **   <a name="securityhub-Type-AwsCloudWatchAlarmDetails-EvaluateLowSampleCountPercentile"></a>
Used only for alarms based on percentiles. If `ignore`, the alarm state does not change during periods with too few data points to be statistically significant. If `evaluate` or this parameter is not used, the alarm is always evaluated and possibly changes state no matter how many data points are available.
Type: String
Pattern: `.*\S.*`
Required: No

 ** EvaluationPeriods **   <a name="securityhub-Type-AwsCloudWatchAlarmDetails-EvaluationPeriods"></a>
The number of periods over which data is compared to the specified threshold.
Type: Integer
Required: No

 ** ExtendedStatistic **   <a name="securityhub-Type-AwsCloudWatchAlarmDetails-ExtendedStatistic"></a>
The percentile statistic for the metric associated with the alarm.
Type: String
Pattern: `.*\S.*`
Required: No

 ** InsufficientDataActions **   <a name="securityhub-Type-AwsCloudWatchAlarmDetails-InsufficientDataActions"></a>
The actions to execute when this alarm transitions to the `INSUFFICIENT_DATA` state from any other state. Each action is specified as an ARN.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** MetricName **   <a name="securityhub-Type-AwsCloudWatchAlarmDetails-MetricName"></a>
The name of the metric associated with the alarm. This is required for an alarm based on a metric. For an alarm based on a math expression, you use `Metrics` instead and you can't specify `MetricName`.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Namespace **   <a name="securityhub-Type-AwsCloudWatchAlarmDetails-Namespace"></a>
The namespace of the metric associated with the alarm. This is required for an alarm based on a metric. For an alarm based on a math expression, you can't specify `Namespace` and you use `Metrics` instead.
Type: String
Pattern: `.*\S.*`
Required: No

 ** OkActions **   <a name="securityhub-Type-AwsCloudWatchAlarmDetails-OkActions"></a>
The actions to execute when this alarm transitions to the `OK` state from any other state. Each action is specified as an ARN.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** Period **   <a name="securityhub-Type-AwsCloudWatchAlarmDetails-Period"></a>
The period, in seconds, over which the statistic is applied. This is required for an alarm based on a metric.
Type: Integer
Required: No

 ** Statistic **   <a name="securityhub-Type-AwsCloudWatchAlarmDetails-Statistic"></a>
The statistic for the metric associated with the alarm, other than percentile. For percentile statistics, use `ExtendedStatistic`.
For an alarm based on a metric, you must specify either `Statistic` or `ExtendedStatistic` but not both.
For an alarm based on a math expression, you can't specify `Statistic`. Instead, you use `Metrics`.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Threshold **   <a name="securityhub-Type-AwsCloudWatchAlarmDetails-Threshold"></a>
The value to compare with the specified statistic.
Type: Double
Required: No

 ** ThresholdMetricId **   <a name="securityhub-Type-AwsCloudWatchAlarmDetails-ThresholdMetricId"></a>
n an alarm based on an anomaly detection model, this is the ID of the `ANOMALY_DETECTION_BAND` function used as the threshold for the alarm.
Type: String
Pattern: `.*\S.*`
Required: No

 ** TreatMissingData **   <a name="securityhub-Type-AwsCloudWatchAlarmDetails-TreatMissingData"></a>
Sets how this alarm is to handle missing data points.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Unit **   <a name="securityhub-Type-AwsCloudWatchAlarmDetails-Unit"></a>
The unit of the metric associated with the alarm.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsCloudWatchAlarmDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsCloudWatchAlarmDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsCloudWatchAlarmDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsCloudWatchAlarmDetails)
