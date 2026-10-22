---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_AnomalyDetectorConfiguration.html
---

# AnomalyDetectorConfiguration
<a name="API_AnomalyDetectorConfiguration"></a>

The configuration specifies details about how the anomaly detection model is to be trained, including time ranges to exclude from use for training the model and the time zone to use for the metric.

## Contents
<a name="API_AnomalyDetectorConfiguration_Contents"></a>

 ** AdaptationSpeed **   <a name="ACW-Type-AnomalyDetectorConfiguration-AdaptationSpeed"></a>
The speed at which the anomaly detection model adapts to sustained changes in the metric's baseline. Faster adaptation lets the model track shifting workloads sooner, but increases the chance that the model treats a real, lasting change as normal.
Valid values:
+  `FAST` - The model adapts quickly to sustained changes in the baseline.
+  `NORMAL` - The model adapts at a moderate pace. This is the default value.
+  `SLOW` - The model adapts slowly, reducing the risk of treating a real change as normal.
Type: String
Valid Values: `FAST | NORMAL | SLOW`
Required: No

 ** ExcludedTimeRanges **   <a name="ACW-Type-AnomalyDetectorConfiguration-ExcludedTimeRanges"></a>
An array of time ranges to exclude from use when the anomaly detection model is trained. Use this to make sure that events that could cause unusual values for the metric, such as deployments, aren't used when CloudWatch creates the model.
Type: Array of [Range](API_Range.md) objects
Required: No

 ** MetricTimezone **   <a name="ACW-Type-AnomalyDetectorConfiguration-MetricTimezone"></a>
The time zone to use for the metric. This is useful to enable the model to automatically account for daylight savings time changes if the metric is sensitive to such time changes.
To specify a time zone, use the name of the time zone as specified in the standard tz database. For more information, see [tz database](https://en.wikipedia.org/wiki/Tz_database).
Type: String
Length Constraints: Maximum length of 50.
Pattern: `.*`
Required: No

 ** OutlierFilteringStrength **   <a name="ACW-Type-AnomalyDetectorConfiguration-OutlierFilteringStrength"></a>
The aggressiveness with which CloudWatch filters outliers from the metric data that the anomaly detection model uses. Stronger filtering excludes more extreme values, which can produce a tighter band of expected values but may also suppress legitimate spikes.
Valid values:
+  `MINIMAL` - Excludes only the most extreme outliers.
+  `MODERATE` - Excludes a moderate range of outliers. This is the default value.
+  `STRICT` - Excludes a wider range of outliers, which can suppress legitimate spikes.
Type: String
Valid Values: `MINIMAL | MODERATE | STRICT`
Required: No

## See Also
<a name="API_AnomalyDetectorConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/AnomalyDetectorConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/AnomalyDetectorConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/AnomalyDetectorConfiguration)
