---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_MetricTransformation.html
---

# MetricTransformation
<a name="API_MetricTransformation"></a>

Indicates how to transform ingested log events to metric data in a CloudWatch metric.

## Contents
<a name="API_MetricTransformation_Contents"></a>

 ** metricName **   <a name="CWL-Type-MetricTransformation-metricName"></a>
The name of the CloudWatch metric.
Type: String
Length Constraints: Maximum length of 255.
Pattern: `[^:*$]*`
Required: Yes

 ** metricNamespace **   <a name="CWL-Type-MetricTransformation-metricNamespace"></a>
A custom namespace to contain your metric in CloudWatch. Use namespaces to group together metrics that are similar. For more information, see [Namespaces](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Namespace).
Type: String
Length Constraints: Maximum length of 255.
Pattern: `[^:*$]*`
Required: Yes

 ** metricValue **   <a name="CWL-Type-MetricTransformation-metricValue"></a>
The value to publish to the CloudWatch metric when a filter pattern matches a log event.
Type: String
Length Constraints: Maximum length of 100.
Required: Yes

 ** defaultValue **   <a name="CWL-Type-MetricTransformation-defaultValue"></a>
(Optional) The value to emit when a filter pattern does not match a log event. This value can be null.
Type: Double
Required: No

 ** dimensions **   <a name="CWL-Type-MetricTransformation-dimensions"></a>
The fields to use as dimensions for the metric. One metric filter can include as many as three dimensions.
Metrics extracted from log events are charged as custom metrics. To prevent unexpected high charges, do not specify high-cardinality fields such as `IPAddress` or `requestID` as dimensions. Each different value found for a dimension is treated as a separate metric and accrues charges as a separate custom metric.
CloudWatch Logs disables a metric filter if it generates 1000 different name/value pairs for your specified dimensions within a certain amount of time. This helps to prevent accidental high charges.
You can also set up a billing alarm to alert you if your charges are higher than expected. For more information, see [ Creating a Billing Alarm to Monitor Your Estimated AWS Charges](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/monitor_estimated_charges_with_cloudwatch.html).
Type: String to string map
Key Length Constraints: Maximum length of 255.
Value Length Constraints: Maximum length of 255.
Required: No

 ** unit **   <a name="CWL-Type-MetricTransformation-unit"></a>
The unit to assign to the metric. If you omit this, the unit is set as `None`.
Type: String
Valid Values: `Seconds | Microseconds | Milliseconds | Bytes | Kilobytes | Megabytes | Gigabytes | Terabytes | Bits | Kilobits | Megabits | Gigabits | Terabits | Percent | Count | Bytes/Second | Kilobytes/Second | Megabytes/Second | Gigabytes/Second | Terabytes/Second | Bits/Second | Kilobits/Second | Megabits/Second | Gigabits/Second | Terabits/Second | Count/Second | None`
Required: No

## See Also
<a name="API_MetricTransformation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/MetricTransformation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/MetricTransformation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/MetricTransformation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch Logs. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatchLogs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
