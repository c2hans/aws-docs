---
source_url: https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_CloudWatchMetricsDataSummary.html
---

# CloudWatchMetricsDataSummary
<a name="API_CloudWatchMetricsDataSummary"></a>

Contains information about the analyzed metrics that displayed anomalous behavior.

## Contents
<a name="API_CloudWatchMetricsDataSummary_Contents"></a>

 ** StatusCode **   <a name="DevOpsGuru-Type-CloudWatchMetricsDataSummary-StatusCode"></a>
This is an enum of the status showing whether the metric value pair list has partial or complete data, or if there was an error.
Type: String
Valid Values: `Complete | InternalError | PartialData`
Required: No

 ** TimestampMetricValuePairList **   <a name="DevOpsGuru-Type-CloudWatchMetricsDataSummary-TimestampMetricValuePairList"></a>
This is a list of Amazon CloudWatch metric values at given timestamp.
Type: Array of [TimestampMetricValuePair](API_TimestampMetricValuePair.md) objects
Required: No

## See Also
<a name="API_CloudWatchMetricsDataSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-guru-2020-12-01/CloudWatchMetricsDataSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-guru-2020-12-01/CloudWatchMetricsDataSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-guru-2020-12-01/CloudWatchMetricsDataSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DevOps Guru. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devops-guru` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
