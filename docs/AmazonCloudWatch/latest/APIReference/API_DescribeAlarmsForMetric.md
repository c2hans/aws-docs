---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DescribeAlarmsForMetric.html
---

# DescribeAlarmsForMetric
<a name="API_DescribeAlarmsForMetric"></a>

Retrieves the alarms for the specified metric. To filter the results, specify a statistic, period, or unit.

This operation retrieves only standard alarms that are based on the specified metric. It does not return alarms based on math expressions that use the specified metric, or composite alarms that use the specified metric.

## Request Syntax
<a name="API_DescribeAlarmsForMetric_RequestSyntax"></a>

```
{
   "Dimensions": [
      {
         "Name": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "ExtendedStatistic": "{{string}}",
   "MetricName": "{{string}}",
   "Namespace": "{{string}}",
   "Period": {{number}},
   "Statistic": "{{string}}",
   "Unit": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeAlarmsForMetric_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Dimensions](#API_DescribeAlarmsForMetric_RequestSyntax) **   <a name="ACW-DescribeAlarmsForMetric-request-Dimensions"></a>
The dimensions associated with the metric. If the metric has any associated dimensions, you must specify them in order for the call to succeed.
Type: Array of [Dimension](API_Dimension.md) objects
Array Members: Maximum number of 30 items.
Required: No

 ** [ExtendedStatistic](#API_DescribeAlarmsForMetric_RequestSyntax) **   <a name="ACW-DescribeAlarmsForMetric-request-ExtendedStatistic"></a>
The percentile statistic for the metric. Specify a value between p0.0 and p100.
Type: String
Required: No

 ** [MetricName](#API_DescribeAlarmsForMetric_RequestSyntax) **   <a name="ACW-DescribeAlarmsForMetric-request-MetricName"></a>
The name of the metric.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** [Namespace](#API_DescribeAlarmsForMetric_RequestSyntax) **   <a name="ACW-DescribeAlarmsForMetric-request-Namespace"></a>
The namespace of the metric.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[^:].*`
Required: Yes

 ** [Period](#API_DescribeAlarmsForMetric_RequestSyntax) **   <a name="ACW-DescribeAlarmsForMetric-request-Period"></a>
The period, in seconds, over which the statistic is applied.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** [Statistic](#API_DescribeAlarmsForMetric_RequestSyntax) **   <a name="ACW-DescribeAlarmsForMetric-request-Statistic"></a>
The statistic for the metric, other than percentiles. For percentile statistics, use `ExtendedStatistics`.
Type: String
Valid Values: `SampleCount | Average | Sum | Minimum | Maximum`
Required: No

 ** [Unit](#API_DescribeAlarmsForMetric_RequestSyntax) **   <a name="ACW-DescribeAlarmsForMetric-request-Unit"></a>
The unit for the metric.
Type: String
Valid Values: `Seconds | Microseconds | Milliseconds | Bytes | Kilobytes | Megabytes | Gigabytes | Terabytes | Bits | Kilobits | Megabits | Gigabits | Terabits | Percent | Count | Bytes/Second | Kilobytes/Second | Megabytes/Second | Gigabytes/Second | Terabytes/Second | Bits/Second | Kilobits/Second | Megabits/Second | Gigabits/Second | Terabits/Second | Count/Second | None`
Required: No

## Response Syntax
<a name="API_DescribeAlarmsForMetric_ResponseSyntax"></a>

```
{
   "MetricAlarms": [
      {
         "ActionsEnabled": boolean,
         "AlarmActions": [ "string" ],
         "AlarmArn": "string",
         "AlarmConfigurationUpdatedTimestamp": number,
         "AlarmDescription": "string",
         "AlarmName": "string",
         "ComparisonOperator": "string",
         "DatapointsToAlarm": number,
         "Dimensions": [
            {
               "Name": "string",
               "Value": "string"
            }
         ],
         "EvaluateLowSampleCountPercentile": "string",
         "EvaluationCriteria": { ... },
         "EvaluationInterval": number,
         "EvaluationPeriods": number,
         "EvaluationState": "string",
         "EvaluationWindow": { ... },
         "ExtendedStatistic": "string",
         "InsufficientDataActions": [ "string" ],
         "MetricName": "string",
         "Metrics": [
            {
               "AccountId": "string",
               "Expression": "string",
               "Id": "string",
               "Label": "string",
               "MetricStat": {
                  "Metric": {
                     "Dimensions": [
                        {
                           "Name": "string",
                           "Value": "string"
                        }
                     ],
                     "MetricName": "string",
                     "Namespace": "string"
                  },
                  "Period": number,
                  "Stat": "string",
                  "Unit": "string"
               },
               "Period": number,
               "ReturnData": boolean
            }
         ],
         "Namespace": "string",
         "OKActions": [ "string" ],
         "Period": number,
         "StateReason": "string",
         "StateReasonData": "string",
         "StateTransitionedTimestamp": number,
         "StateUpdatedTimestamp": number,
         "StateValue": "string",
         "Statistic": "string",
         "Threshold": number,
         "ThresholdMetricId": "string",
         "TreatMissingData": "string",
         "Unit": "string",
         "WarmUpConfiguration": {
            "OnlyStartEvaluatingAfterWarmUpPeriodEnds": boolean,
            "WarmUpPeriodDurationInMinutes": number
         }
      }
   ]
}
```

## Response Elements
<a name="API_DescribeAlarmsForMetric_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [MetricAlarms](#API_DescribeAlarmsForMetric_ResponseSyntax) **   <a name="ACW-DescribeAlarmsForMetric-response-MetricAlarms"></a>
The information for each alarm with the specified metric.
Type: Array of [MetricAlarm](API_MetricAlarm.md) objects

## Errors
<a name="API_DescribeAlarmsForMetric_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_DescribeAlarmsForMetric_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/monitoring-2010-08-01/DescribeAlarmsForMetric)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/DescribeAlarmsForMetric)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/DescribeAlarmsForMetric)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/monitoring-2010-08-01/DescribeAlarmsForMetric)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/DescribeAlarmsForMetric)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/monitoring-2010-08-01/DescribeAlarmsForMetric)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/monitoring-2010-08-01/DescribeAlarmsForMetric)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/monitoring-2010-08-01/DescribeAlarmsForMetric)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/DescribeAlarmsForMetric)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/DescribeAlarmsForMetric)
