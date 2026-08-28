---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_edge_EdgeMetric.html
---

# EdgeMetric
<a name="API_edge_EdgeMetric"></a>

Information required for edge device metrics.

## Contents
<a name="API_edge_EdgeMetric_Contents"></a>

 ** Dimension **   <a name="sagemaker-Type-edge_EdgeMetric-Dimension"></a>
The dimension of metrics published.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `^[a-zA-Z0-9](-*[a-zA-Z0-9\/])*$`
Required: No

 ** MetricName **   <a name="sagemaker-Type-edge_EdgeMetric-MetricName"></a>
Returns the name of the metric.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 100.
Pattern: `^[a-zA-Z0-9](-*[a-zA-Z0-9])*$`
Required: No

 ** Timestamp **   <a name="sagemaker-Type-edge_EdgeMetric-Timestamp"></a>
Timestamp of when the metric was requested.
Type: Timestamp
Required: No

 ** Value **   <a name="sagemaker-Type-edge_EdgeMetric-Value"></a>
Returns the value of the metric.
Type: Double
Required: No

## See Also
<a name="API_edge_EdgeMetric_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-edge-2020-09-23/EdgeMetric)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-edge-2020-09-23/EdgeMetric)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-edge-2020-09-23/EdgeMetric)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
