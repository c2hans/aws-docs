---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_InferenceRecommendationsJobStep.html
---

# InferenceRecommendationsJobStep
<a name="API_InferenceRecommendationsJobStep"></a>

A returned array object for the `Steps` response field in the [ListInferenceRecommendationsJobSteps](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListInferenceRecommendationsJobSteps.html) API command.

## Contents
<a name="API_InferenceRecommendationsJobStep_Contents"></a>

 ** JobName **   <a name="sagemaker-Type-InferenceRecommendationsJobStep-JobName"></a>
The name of the Inference Recommender job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,63}`
Required: Yes

 ** Status **   <a name="sagemaker-Type-InferenceRecommendationsJobStep-Status"></a>
The current status of the benchmark.
Type: String
Valid Values: `PENDING | IN_PROGRESS | COMPLETED | FAILED | STOPPING | STOPPED | DELETING | DELETED`
Required: Yes

 ** StepType **   <a name="sagemaker-Type-InferenceRecommendationsJobStep-StepType"></a>
The type of the subtask.
 `BENCHMARK`: Evaluate the performance of your model on different instance types.
Type: String
Valid Values: `BENCHMARK`
Required: Yes

 ** InferenceBenchmark **   <a name="sagemaker-Type-InferenceRecommendationsJobStep-InferenceBenchmark"></a>
The details for a specific benchmark.
Type: [RecommendationJobInferenceBenchmark](API_RecommendationJobInferenceBenchmark.md) object
Required: No

## See Also
<a name="API_InferenceRecommendationsJobStep_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/InferenceRecommendationsJobStep)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/InferenceRecommendationsJobStep)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/InferenceRecommendationsJobStep)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
