---
source_url: https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_CloudWatchMetricsDetail.html
---

# CloudWatchMetricsDetail
<a name="API_CloudWatchMetricsDetail"></a>

 Information about an Amazon CloudWatch metric.

## Contents
<a name="API_CloudWatchMetricsDetail_Contents"></a>

 ** Dimensions **   <a name="DevOpsGuru-Type-CloudWatchMetricsDetail-Dimensions"></a>
 An array of CloudWatch dimensions associated with
Type: Array of [CloudWatchMetricsDimension](API_CloudWatchMetricsDimension.md) objects
Required: No

 ** MetricDataSummary **   <a name="DevOpsGuru-Type-CloudWatchMetricsDetail-MetricDataSummary"></a>
This object returns anomaly metric data.
Type: [CloudWatchMetricsDataSummary](API_CloudWatchMetricsDataSummary.md) object
Required: No

 ** MetricName **   <a name="DevOpsGuru-Type-CloudWatchMetricsDetail-MetricName"></a>
 The name of the CloudWatch metric.
Type: String
Required: No

 ** Namespace **   <a name="DevOpsGuru-Type-CloudWatchMetricsDetail-Namespace"></a>
 The namespace of the CloudWatch metric. A namespace is a container for CloudWatch metrics.
Type: String
Required: No

 ** Period **   <a name="DevOpsGuru-Type-CloudWatchMetricsDetail-Period"></a>
 The length of time associated with the CloudWatch metric in number of seconds.
Type: Integer
Required: No

 ** Stat **   <a name="DevOpsGuru-Type-CloudWatchMetricsDetail-Stat"></a>
 The type of statistic associated with the CloudWatch metric. For more information, see [Statistics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Statistic) in the *Amazon CloudWatch User Guide*.
Type: String
Valid Values: `Sum | Average | SampleCount | Minimum | Maximum | p99 | p90 | p50`
Required: No

 ** Unit **   <a name="DevOpsGuru-Type-CloudWatchMetricsDetail-Unit"></a>
 The unit of measure used for the CloudWatch metric. For example, `Bytes`, `Seconds`, `Count`, and `Percent`.
Type: String
Required: No

## See Also
<a name="API_CloudWatchMetricsDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-guru-2020-12-01/CloudWatchMetricsDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-guru-2020-12-01/CloudWatchMetricsDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-guru-2020-12-01/CloudWatchMetricsDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DevOps Guru. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devops-guru` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
