---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_Datapoint.html
---

# Datapoint
<a name="API_Datapoint"></a>

Encapsulates the statistical data that CloudWatch computes from metric data.

## Contents
<a name="API_Datapoint_Contents"></a>

 ** Average **   <a name="ACW-Type-Datapoint-Average"></a>
The average of the metric values that correspond to the data point.
Type: Double
Required: No

 ** ExtendedStatistics **   <a name="ACW-Type-Datapoint-ExtendedStatistics"></a>
The percentile statistic for the data point.
Type: String to double map
Required: No

 ** Maximum **   <a name="ACW-Type-Datapoint-Maximum"></a>
The maximum metric value for the data point.
Type: Double
Required: No

 ** Minimum **   <a name="ACW-Type-Datapoint-Minimum"></a>
The minimum metric value for the data point.
Type: Double
Required: No

 ** SampleCount **   <a name="ACW-Type-Datapoint-SampleCount"></a>
The number of metric values that contributed to the aggregate value of this data point.
Type: Double
Required: No

 ** Sum **   <a name="ACW-Type-Datapoint-Sum"></a>
The sum of the metric values for the data point.
Type: Double
Required: No

 ** Timestamp **   <a name="ACW-Type-Datapoint-Timestamp"></a>
The time stamp used for the data point.
Type: Timestamp
Required: No

 ** Unit **   <a name="ACW-Type-Datapoint-Unit"></a>
The standard unit for the data point.
Type: String
Valid Values: `Seconds | Microseconds | Milliseconds | Bytes | Kilobytes | Megabytes | Gigabytes | Terabytes | Bits | Kilobits | Megabits | Gigabits | Terabits | Percent | Count | Bytes/Second | Kilobytes/Second | Megabytes/Second | Gigabytes/Second | Terabytes/Second | Bits/Second | Kilobits/Second | Megabits/Second | Gigabits/Second | Terabits/Second | Count/Second | None`
Required: No

## See Also
<a name="API_Datapoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/Datapoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/Datapoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/Datapoint)
