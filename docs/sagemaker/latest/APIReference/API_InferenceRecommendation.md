---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_InferenceRecommendation.html
---

# InferenceRecommendation
<a name="API_InferenceRecommendation"></a>

A list of recommendations made by Amazon SageMaker Inference Recommender.

## Contents
<a name="API_InferenceRecommendation_Contents"></a>

 ** EndpointConfiguration **   <a name="sagemaker-Type-InferenceRecommendation-EndpointConfiguration"></a>
Defines the endpoint configuration parameters.
Type: [EndpointOutputConfiguration](API_EndpointOutputConfiguration.md) object
Required: Yes

 ** ModelConfiguration **   <a name="sagemaker-Type-InferenceRecommendation-ModelConfiguration"></a>
Defines the model configuration.
Type: [ModelConfiguration](API_ModelConfiguration.md) object
Required: Yes

 ** InvocationEndTime **   <a name="sagemaker-Type-InferenceRecommendation-InvocationEndTime"></a>
A timestamp that shows when the benchmark completed.
Type: Timestamp
Required: No

 ** InvocationStartTime **   <a name="sagemaker-Type-InferenceRecommendation-InvocationStartTime"></a>
A timestamp that shows when the benchmark started.
Type: Timestamp
Required: No

 ** Metrics **   <a name="sagemaker-Type-InferenceRecommendation-Metrics"></a>
The metrics used to decide what recommendation to make.
Type: [RecommendationMetrics](API_RecommendationMetrics.md) object
Required: No

 ** RecommendationId **   <a name="sagemaker-Type-InferenceRecommendation-RecommendationId"></a>
The recommendation ID which uniquely identifies each recommendation.
Type: String
Required: No

## See Also
<a name="API_InferenceRecommendation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/InferenceRecommendation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/InferenceRecommendation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/InferenceRecommendation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
