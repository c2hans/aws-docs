---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_RecommendationJobInferenceBenchmark.html
---

# RecommendationJobInferenceBenchmark
<a name="API_RecommendationJobInferenceBenchmark"></a>

The details for a specific benchmark from an Inference Recommender job.

## Contents
<a name="API_RecommendationJobInferenceBenchmark_Contents"></a>

 ** ModelConfiguration **   <a name="sagemaker-Type-RecommendationJobInferenceBenchmark-ModelConfiguration"></a>
Defines the model configuration. Includes the specification name and environment parameters.
Type: [ModelConfiguration](API_ModelConfiguration.md) object
Required: Yes

 ** EndpointConfiguration **   <a name="sagemaker-Type-RecommendationJobInferenceBenchmark-EndpointConfiguration"></a>
The endpoint configuration made by Inference Recommender during a recommendation job.
Type: [EndpointOutputConfiguration](API_EndpointOutputConfiguration.md) object
Required: No

 ** EndpointMetrics **   <a name="sagemaker-Type-RecommendationJobInferenceBenchmark-EndpointMetrics"></a>
The metrics for an existing endpoint compared in an Inference Recommender job.
Type: [InferenceMetrics](API_InferenceMetrics.md) object
Required: No

 ** FailureReason **   <a name="sagemaker-Type-RecommendationJobInferenceBenchmark-FailureReason"></a>
The reason why a benchmark failed.
Type: String
Required: No

 ** InvocationEndTime **   <a name="sagemaker-Type-RecommendationJobInferenceBenchmark-InvocationEndTime"></a>
A timestamp that shows when the benchmark completed.
Type: Timestamp
Required: No

 ** InvocationStartTime **   <a name="sagemaker-Type-RecommendationJobInferenceBenchmark-InvocationStartTime"></a>
A timestamp that shows when the benchmark started.
Type: Timestamp
Required: No

 ** Metrics **   <a name="sagemaker-Type-RecommendationJobInferenceBenchmark-Metrics"></a>
The metrics of recommendations.
Type: [RecommendationMetrics](API_RecommendationMetrics.md) object
Required: No

## See Also
<a name="API_RecommendationJobInferenceBenchmark_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/RecommendationJobInferenceBenchmark)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/RecommendationJobInferenceBenchmark)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/RecommendationJobInferenceBenchmark)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
