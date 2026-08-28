---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_Behavior.html
---

# Behavior
<a name="API_Behavior"></a>

A Device Defender security profile behavior.

## Contents
<a name="API_Behavior_Contents"></a>

 ** name **   <a name="iot-Type-Behavior-name"></a>
The name you've given to the behavior.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`
Required: Yes

 ** criteria **   <a name="iot-Type-Behavior-criteria"></a>
The criteria that determine if a device is behaving normally in regard to the `metric`.
In the AWS IoT console, you can choose to be sent an alert through Amazon SNS when AWS IoT Device Defender detects that a device is behaving anomalously.
Type: [BehaviorCriteria](API_BehaviorCriteria.md) object
Required: No

 ** exportMetric **   <a name="iot-Type-Behavior-exportMetric"></a>
Value indicates exporting metrics related to the behavior when it is true.
Type: Boolean
Required: No

 ** metric **   <a name="iot-Type-Behavior-metric"></a>
What is measured by the behavior.
Type: String
Required: No

 ** metricDimension **   <a name="iot-Type-Behavior-metricDimension"></a>
The dimension for a metric in your behavior. For example, using a `TOPIC_FILTER` dimension, you can narrow down the scope of the metric to only MQTT topics where the name matches the pattern specified in the dimension. This can't be used with custom metrics.
Type: [MetricDimension](API_MetricDimension.md) object
Required: No

 ** suppressAlerts **   <a name="iot-Type-Behavior-suppressAlerts"></a>
 Suppresses alerts.
Type: Boolean
Required: No

## See Also
<a name="API_Behavior_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/Behavior)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/Behavior)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/Behavior)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
