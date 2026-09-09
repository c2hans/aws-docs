---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_MetricAlarm.html
---

# MetricAlarm
<a name="API_MetricAlarm"></a>

The details about a metric alarm.

## Contents
<a name="API_MetricAlarm_Contents"></a>

 ** ActionsEnabled **   <a name="ACW-Type-MetricAlarm-ActionsEnabled"></a>
Indicates whether actions should be executed during any changes to the alarm state.
Type: Boolean
Required: No

 ** AlarmActions **   <a name="ACW-Type-MetricAlarm-AlarmActions"></a>
The actions to execute when this alarm transitions to the `ALARM` state from any other state. Each action is specified as an Amazon Resource Name (ARN).
Type: Array of strings
Array Members: Maximum number of 5 items.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** AlarmArn **   <a name="ACW-Type-MetricAlarm-AlarmArn"></a>
The Amazon Resource Name (ARN) of the alarm.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Required: No

 ** AlarmConfigurationUpdatedTimestamp **   <a name="ACW-Type-MetricAlarm-AlarmConfigurationUpdatedTimestamp"></a>
The time stamp of the last update to the alarm configuration.
Type: Timestamp
Required: No

 ** AlarmDescription **   <a name="ACW-Type-MetricAlarm-AlarmDescription"></a>
The description of the alarm.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** AlarmName **   <a name="ACW-Type-MetricAlarm-AlarmName"></a>
The name of the alarm.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** ComparisonOperator **   <a name="ACW-Type-MetricAlarm-ComparisonOperator"></a>
The arithmetic operation to use when comparing the specified statistic and threshold. The specified statistic value is used as the first operand.
Type: String
Valid Values: `GreaterThanOrEqualToThreshold | GreaterThanThreshold | LessThanThreshold | LessThanOrEqualToThreshold | LessThanLowerOrGreaterThanUpperThreshold | LessThanLowerThreshold | GreaterThanUpperThreshold`
Required: No

 ** DatapointsToAlarm **   <a name="ACW-Type-MetricAlarm-DatapointsToAlarm"></a>
The number of data points that must be breaching to trigger the alarm.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** Dimensions **   <a name="ACW-Type-MetricAlarm-Dimensions"></a>
The dimensions for the metric associated with the alarm.
Type: Array of [Dimension](API_Dimension.md) objects
Array Members: Maximum number of 30 items.
Required: No

 ** EvaluateLowSampleCountPercentile **   <a name="ACW-Type-MetricAlarm-EvaluateLowSampleCountPercentile"></a>
Used only for alarms based on percentiles. If `ignore`, the alarm state does not change during periods with too few data points to be statistically significant. If `evaluate` or this parameter is not used, the alarm is always evaluated and possibly changes state no matter how many data points are available.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** EvaluationCriteria **   <a name="ACW-Type-MetricAlarm-EvaluationCriteria"></a>
The evaluation criteria for the alarm.
Type: [EvaluationCriteria](API_EvaluationCriteria.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** EvaluationInterval **   <a name="ACW-Type-MetricAlarm-EvaluationInterval"></a>
The frequency, in seconds, at which the alarm is evaluated.
Type: Integer
Valid Range: Minimum value of 10. Maximum value of 3600.
Required: No

 ** EvaluationPeriods **   <a name="ACW-Type-MetricAlarm-EvaluationPeriods"></a>
The number of periods over which data is compared to the specified threshold.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** EvaluationState **   <a name="ACW-Type-MetricAlarm-EvaluationState"></a>
If the value of this field is `PARTIAL_DATA`, it indicates that not all the available data was able to be retrieved due to quota limitations. For more information, see [Create alarms on Metrics Insights queries](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Create_Metrics_Insights_Alarm.html).
If the value of this field is `EVALUATION_ERROR`, it indicates configuration errors in alarm setup that require review and correction. Refer to StateReason field of the alarm for more details.
If the value of this field is `EVALUATION_FAILURE`, it indicates temporary CloudWatch issues. We recommend manual monitoring until the issue is resolved
Type: String
Valid Values: `PARTIAL_DATA | EVALUATION_FAILURE | EVALUATION_ERROR`
Required: No

 ** EvaluationWindow **   <a name="ACW-Type-MetricAlarm-EvaluationWindow"></a>
The evaluation window that the alarm uses to select the range of metric data that it evaluates. This is either a sliding window or a wall clock window. For more information, see [Alarm evaluation windows](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/alarm-evaluation-window.html) in the *CloudWatch User Guide*.
Type: [EvaluationWindow](API_EvaluationWindow.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** ExtendedStatistic **   <a name="ACW-Type-MetricAlarm-ExtendedStatistic"></a>
The percentile statistic for the metric associated with the alarm. Specify a value between p0.0 and p100.
Type: String
Required: No

 ** InsufficientDataActions **   <a name="ACW-Type-MetricAlarm-InsufficientDataActions"></a>
The actions to execute when this alarm transitions to the `INSUFFICIENT_DATA` state from any other state. Each action is specified as an Amazon Resource Name (ARN).
Type: Array of strings
Array Members: Maximum number of 5 items.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** MetricName **   <a name="ACW-Type-MetricAlarm-MetricName"></a>
The name of the metric associated with the alarm, if this is an alarm based on a single metric.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** Metrics **   <a name="ACW-Type-MetricAlarm-Metrics"></a>
An array of MetricDataQuery structures, used in an alarm based on a metric math expression. Each structure either retrieves a metric or performs a math expression. One item in the Metrics array is the math expression that the alarm watches. This expression by designated by having `ReturnData` set to true.
Type: Array of [MetricDataQuery](API_MetricDataQuery.md) objects
Required: No

 ** Namespace **   <a name="ACW-Type-MetricAlarm-Namespace"></a>
The namespace of the metric associated with the alarm.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[^:].*`
Required: No

 ** OKActions **   <a name="ACW-Type-MetricAlarm-OKActions"></a>
The actions to execute when this alarm transitions to the `OK` state from any other state. Each action is specified as an Amazon Resource Name (ARN).
Type: Array of strings
Array Members: Maximum number of 5 items.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** Period **   <a name="ACW-Type-MetricAlarm-Period"></a>
The period, in seconds, over which the statistic is applied.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** StateReason **   <a name="ACW-Type-MetricAlarm-StateReason"></a>
An explanation for the alarm state, in text format.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1023.
Required: No

 ** StateReasonData **   <a name="ACW-Type-MetricAlarm-StateReasonData"></a>
An explanation for the alarm state, in JSON format.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4000.
Required: No

 ** StateTransitionedTimestamp **   <a name="ACW-Type-MetricAlarm-StateTransitionedTimestamp"></a>
The date and time that the alarm's `StateValue` most recently changed.
Type: Timestamp
Required: No

 ** StateUpdatedTimestamp **   <a name="ACW-Type-MetricAlarm-StateUpdatedTimestamp"></a>
The time stamp of the last update to the value of either the `StateValue` or `EvaluationState` parameters.
Type: Timestamp
Required: No

 ** StateValue **   <a name="ACW-Type-MetricAlarm-StateValue"></a>
The state value for the alarm.
Type: String
Valid Values: `OK | ALARM | INSUFFICIENT_DATA`
Required: No

 ** Statistic **   <a name="ACW-Type-MetricAlarm-Statistic"></a>
The statistic for the metric associated with the alarm, other than percentile. For percentile statistics, use `ExtendedStatistic`.
Type: String
Valid Values: `SampleCount | Average | Sum | Minimum | Maximum`
Required: No

 ** Threshold **   <a name="ACW-Type-MetricAlarm-Threshold"></a>
The value to compare with the specified statistic.
Type: Double
Required: No

 ** ThresholdMetricId **   <a name="ACW-Type-MetricAlarm-ThresholdMetricId"></a>
In an alarm based on an anomaly detection model, this is the ID of the `ANOMALY_DETECTION_BAND` function used as the threshold for the alarm.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** TreatMissingData **   <a name="ACW-Type-MetricAlarm-TreatMissingData"></a>
Sets how this alarm is to handle missing data points. The valid values are `breaching`, `notBreaching`, `ignore`, and `missing`. For more information, see [Configuring how CloudWatch alarms treat missing data](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html#alarms-and-missing-data).
If this parameter is omitted, the default behavior of `missing` is used.
This parameter is not applicable to PromQL alarms.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** Unit **   <a name="ACW-Type-MetricAlarm-Unit"></a>
The unit of the metric associated with the alarm.
Type: String
Valid Values: `Seconds | Microseconds | Milliseconds | Bytes | Kilobytes | Megabytes | Gigabytes | Terabytes | Bits | Kilobits | Megabits | Gigabits | Terabits | Percent | Count | Bytes/Second | Kilobytes/Second | Megabytes/Second | Gigabytes/Second | Terabytes/Second | Bits/Second | Kilobits/Second | Megabits/Second | Gigabits/Second | Terabits/Second | Count/Second | None`
Required: No

 ** WarmUpConfiguration **   <a name="ACW-Type-MetricAlarm-WarmUpConfiguration"></a>
The warm-up configuration for the alarm. A warm-up period delays alarm evaluation after you create or update the alarm. During the warm-up period, the alarm stays in `INSUFFICIENT_DATA` and does not perform alarm actions.
For more information, see [Alarm warm-up periods](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/alarm-warm-up.html) in the *Amazon CloudWatch User Guide*.
Type: [WarmUpConfiguration](API_WarmUpConfiguration.md) object
Required: No

## See Also
<a name="API_MetricAlarm_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/MetricAlarm)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/MetricAlarm)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/MetricAlarm)
