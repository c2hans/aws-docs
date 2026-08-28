---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_metrics_MetricQueryResult.html
---

# MetricQueryResult
<a name="API_metrics_MetricQueryResult"></a>

The result of a query to retrieve training metrics from SageMaker.

## Contents
<a name="API_metrics_MetricQueryResult_Contents"></a>

 ** MetricValues **   <a name="sagemaker-Type-metrics_MetricQueryResult-MetricValues"></a>
The metric values retrieved by the query.
Type: Array of doubles
Required: Yes

 ** Status **   <a name="sagemaker-Type-metrics_MetricQueryResult-Status"></a>
The status of the metric query.
Type: String
Valid Values: `Complete | Truncated | InternalError | ValidationError`
Required: Yes

 ** XAxisValues **   <a name="sagemaker-Type-metrics_MetricQueryResult-XAxisValues"></a>
The values for the x-axis of the metrics.
Type: Array of longs
Required: Yes

 ** Message **   <a name="sagemaker-Type-metrics_MetricQueryResult-Message"></a>
A message describing the status of the metric query.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `.*`
Required: No

## See Also
<a name="API_metrics_MetricQueryResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-metrics-2022-09-30/MetricQueryResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-metrics-2022-09-30/MetricQueryResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-metrics-2022-09-30/MetricQueryResult)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
