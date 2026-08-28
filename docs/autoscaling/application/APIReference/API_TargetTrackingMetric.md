---
source_url: https://docs.aws.amazon.com/autoscaling/application/APIReference/API_TargetTrackingMetric.html
---

# TargetTrackingMetric
<a name="API_TargetTrackingMetric"></a>

Represents a specific metric.

Metric is a property of the [TargetTrackingMetricStat](API_TargetTrackingMetricStat.md) object.

## Contents
<a name="API_TargetTrackingMetric_Contents"></a>

 ** Dimensions **   <a name="autoscaling-Type-TargetTrackingMetric-Dimensions"></a>
The dimensions for the metric. For the list of available dimensions, see the AWS documentation available from the table in [AWS services that publish CloudWatch metrics ](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/aws-services-cloudwatch-metrics.html) in the *Amazon CloudWatch User Guide*.
Conditional: If you published your metric with dimensions, you must specify the same dimensions in your scaling policy.
Type: Array of [TargetTrackingMetricDimension](API_TargetTrackingMetricDimension.md) objects
Required: No

 ** MetricName **   <a name="autoscaling-Type-TargetTrackingMetric-MetricName"></a>
The name of the metric.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** Namespace **   <a name="autoscaling-Type-TargetTrackingMetric-Namespace"></a>
The namespace of the metric. For more information, see the table in [AWS services that publish CloudWatch metrics ](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/aws-services-cloudwatch-metrics.html) in the *Amazon CloudWatch User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

## See Also
<a name="API_TargetTrackingMetric_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-autoscaling-2016-02-06/TargetTrackingMetric)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-autoscaling-2016-02-06/TargetTrackingMetric)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-autoscaling-2016-02-06/TargetTrackingMetric)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
