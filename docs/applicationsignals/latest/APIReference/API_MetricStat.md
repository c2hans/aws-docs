---
source_url: https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_MetricStat.html
---

# MetricStat
<a name="API_MetricStat"></a>

This structure defines the metric to be used as the service level indicator, along with the statistics, period, and unit.

## Contents
<a name="API_MetricStat_Contents"></a>

 ** Metric **   <a name="applicationsignals-Type-MetricStat-Metric"></a>
The metric to use as the service level indicator, including the metric name, namespace, and dimensions.
Type: [Metric](API_Metric.md) object
Required: Yes

 ** Period **   <a name="applicationsignals-Type-MetricStat-Period"></a>
The granularity, in seconds, to be used for the metric. For metrics with regular resolution, a period can be as short as one minute (60 seconds) and must be a multiple of 60. For high-resolution metrics that are collected at intervals of less than one minute, the period can be 1, 5, 10, 30, 60, or any multiple of 60. High-resolution metrics are those metrics stored by a `PutMetricData` call that includes a `StorageResolution` of 1 second.
Type: Integer
Valid Range: Minimum value of 1.
Required: Yes

 ** Stat **   <a name="applicationsignals-Type-MetricStat-Stat"></a>
The statistic to use for comparison to the threshold. It can be any CloudWatch statistic or extended statistic. For more information about statistics, see [CloudWatch statistics definitions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Statistics-definitions.html).
Type: String
Required: Yes

 ** Unit **   <a name="applicationsignals-Type-MetricStat-Unit"></a>
If you omit `Unit` then all data that was collected with any unit is returned, along with the corresponding units that were specified when the data was reported to CloudWatch. If you specify a unit, the operation returns only data that was collected with that unit specified. If you specify a unit that does not match the data collected, the results of the operation are null. CloudWatch does not perform unit conversions.
Type: String
Valid Values: `Microseconds | Milliseconds | Seconds | Bytes | Kilobytes | Megabytes | Gigabytes | Terabytes | Bits | Kilobits | Megabits | Gigabits | Terabits | Percent | Count | Bytes/Second | Kilobytes/Second | Megabytes/Second | Gigabytes/Second | Terabytes/Second | Bits/Second | Kilobits/Second | Megabits/Second | Gigabits/Second | Terabits/Second | Count/Second | None`
Required: No

## See Also
<a name="API_MetricStat_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-signals-2024-04-15/MetricStat)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-signals-2024-04-15/MetricStat)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-signals-2024-04-15/MetricStat)
