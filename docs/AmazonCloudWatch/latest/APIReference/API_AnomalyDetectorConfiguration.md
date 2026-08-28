---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_AnomalyDetectorConfiguration.html
---

# AnomalyDetectorConfiguration
<a name="API_AnomalyDetectorConfiguration"></a>

The configuration specifies details about how the anomaly detection model is to be trained, including time ranges to exclude from use for training the model and the time zone to use for the metric.

## Contents
<a name="API_AnomalyDetectorConfiguration_Contents"></a>

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

## See Also
<a name="API_AnomalyDetectorConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/AnomalyDetectorConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/AnomalyDetectorConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/AnomalyDetectorConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
