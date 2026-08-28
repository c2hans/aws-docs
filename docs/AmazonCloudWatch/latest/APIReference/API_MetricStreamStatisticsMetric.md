---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_MetricStreamStatisticsMetric.html
---

# MetricStreamStatisticsMetric
<a name="API_MetricStreamStatisticsMetric"></a>

This object contains the information for one metric that is to be streamed with additional statistics.

## Contents
<a name="API_MetricStreamStatisticsMetric_Contents"></a>

 ** MetricName **   <a name="ACW-Type-MetricStreamStatisticsMetric-MetricName"></a>
The name of the metric.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** Namespace **   <a name="ACW-Type-MetricStreamStatisticsMetric-Namespace"></a>
The namespace of the metric.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[^:].*`
Required: Yes

## See Also
<a name="API_MetricStreamStatisticsMetric_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/MetricStreamStatisticsMetric)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/MetricStreamStatisticsMetric)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/MetricStreamStatisticsMetric)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
