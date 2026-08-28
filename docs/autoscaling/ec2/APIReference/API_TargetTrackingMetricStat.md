---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_TargetTrackingMetricStat.html
---

# TargetTrackingMetricStat
<a name="API_TargetTrackingMetricStat"></a>

This structure defines the CloudWatch metric to return, along with the statistic and unit.

 `TargetTrackingMetricStat` is a property of the [TargetTrackingMetricDataQuery](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_TargetTrackingMetricDataQuery.html) object.

For more information about the CloudWatch terminology below, see [Amazon CloudWatch concepts](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html) in the *Amazon CloudWatch User Guide*.

## Contents
<a name="API_TargetTrackingMetricStat_Contents"></a>

 ** Metric **
The metric to use.
Type: [Metric](API_Metric.md) object
Required: Yes

 ** Stat **
The statistic to return. It can include any CloudWatch statistic or extended statistic. For a list of valid values, see the table in [Statistics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Statistic) in the *Amazon CloudWatch User Guide*.
The most commonly used metric for scaling is `Average`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: Yes

 ** Period **
 The period of the metric in seconds. The default value is 60. Accepted values are 10, 30, and 60. For high resolution metric, set the value to less than 60. For more information, see [Create a target tracking policy using high-resolution metrics for faster response](https://docs.aws.amazon.com/autoscaling/ec2/userguide/policy-creating-high-resolution-metrics.html).
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** Unit **
The unit to use for the returned data points. For a complete list of the units that CloudWatch supports, see the [MetricDatum](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_MetricDatum.html) data type in the *Amazon CloudWatch API Reference*.
Type: String
Required: No

## See Also
<a name="API_TargetTrackingMetricStat_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/TargetTrackingMetricStat)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/TargetTrackingMetricStat)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/TargetTrackingMetricStat)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
