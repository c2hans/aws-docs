---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_CloudWatchAlarmConfiguration.html
---

# CloudWatchAlarmConfiguration
<a name="API_CloudWatchAlarmConfiguration"></a>

A complex type that contains information about the CloudWatch alarm that Amazon Route 53 is monitoring for this health check.

## Contents
<a name="API_CloudWatchAlarmConfiguration_Contents"></a>

 ** ComparisonOperator **   <a name="Route53-Type-CloudWatchAlarmConfiguration-ComparisonOperator"></a>
For the metric that the CloudWatch alarm is associated with, the arithmetic operation that is used for the comparison.
Type: String
Valid Values: `GreaterThanOrEqualToThreshold | GreaterThanThreshold | LessThanThreshold | LessThanOrEqualToThreshold`
Required: Yes

 ** EvaluationPeriods **   <a name="Route53-Type-CloudWatchAlarmConfiguration-EvaluationPeriods"></a>
For the metric that the CloudWatch alarm is associated with, the number of periods that the metric is compared to the threshold.
Type: Integer
Valid Range: Minimum value of 1.
Required: Yes

 ** MetricName **   <a name="Route53-Type-CloudWatchAlarmConfiguration-MetricName"></a>
The name of the CloudWatch metric that the alarm is associated with.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** Namespace **   <a name="Route53-Type-CloudWatchAlarmConfiguration-Namespace"></a>
The namespace of the metric that the alarm is associated with. For more information, see [Amazon CloudWatch Namespaces, Dimensions, and Metrics Reference](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html) in the *Amazon CloudWatch User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** Period **   <a name="Route53-Type-CloudWatchAlarmConfiguration-Period"></a>
For the metric that the CloudWatch alarm is associated with, the duration of one evaluation period in seconds.
Type: Integer
Valid Range: Minimum value of 60.
Required: Yes

 ** Statistic **   <a name="Route53-Type-CloudWatchAlarmConfiguration-Statistic"></a>
For the metric that the CloudWatch alarm is associated with, the statistic that is applied to the metric.
Type: String
Valid Values: `Average | Sum | SampleCount | Maximum | Minimum`
Required: Yes

 ** Threshold **   <a name="Route53-Type-CloudWatchAlarmConfiguration-Threshold"></a>
For the metric that the CloudWatch alarm is associated with, the value the metric is compared with.
Type: Double
Required: Yes

 ** Dimensions **   <a name="Route53-Type-CloudWatchAlarmConfiguration-Dimensions"></a>
For the metric that the CloudWatch alarm is associated with, a complex type that contains information about the dimensions for the metric. For information, see [Amazon CloudWatch Namespaces, Dimensions, and Metrics Reference](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html) in the *Amazon CloudWatch User Guide*.
Type: Array of [Dimension](API_Dimension.md) objects
Array Members: Maximum number of 10 items.
Required: No

## See Also
<a name="API_CloudWatchAlarmConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/CloudWatchAlarmConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/CloudWatchAlarmConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/CloudWatchAlarmConfiguration)
