---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_CloudwatchMetricAction.html
---

# CloudwatchMetricAction
<a name="API_CloudwatchMetricAction"></a>

Describes an action that captures a CloudWatch metric.

## Contents
<a name="API_CloudwatchMetricAction_Contents"></a>

 ** metricName **   <a name="iot-Type-CloudwatchMetricAction-metricName"></a>
The CloudWatch metric name.
Type: String
Required: Yes

 ** metricNamespace **   <a name="iot-Type-CloudwatchMetricAction-metricNamespace"></a>
The CloudWatch metric namespace name.
Type: String
Required: Yes

 ** metricUnit **   <a name="iot-Type-CloudwatchMetricAction-metricUnit"></a>
The [metric unit](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#Unit) supported by CloudWatch.
Type: String
Required: Yes

 ** metricValue **   <a name="iot-Type-CloudwatchMetricAction-metricValue"></a>
The CloudWatch metric value.
Type: String
Required: Yes

 ** roleArn **   <a name="iot-Type-CloudwatchMetricAction-roleArn"></a>
The IAM role that allows access to the CloudWatch metric.
Type: String
Required: Yes

 ** metricTimestamp **   <a name="iot-Type-CloudwatchMetricAction-metricTimestamp"></a>
An optional [Unix timestamp](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#about_timestamp).
Type: String
Required: No

## See Also
<a name="API_CloudwatchMetricAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/CloudwatchMetricAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/CloudwatchMetricAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/CloudwatchMetricAction)
