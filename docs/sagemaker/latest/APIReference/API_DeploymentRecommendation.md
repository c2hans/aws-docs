---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeploymentRecommendation.html
---

# DeploymentRecommendation
<a name="API_DeploymentRecommendation"></a>

A set of recommended deployment configurations for the model. To get more advanced recommendations, see [CreateInferenceRecommendationsJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateInferenceRecommendationsJob.html) to create an inference recommendation job.

## Contents
<a name="API_DeploymentRecommendation_Contents"></a>

 ** RecommendationStatus **   <a name="sagemaker-Type-DeploymentRecommendation-RecommendationStatus"></a>
Status of the deployment recommendation. The status `NOT_APPLICABLE` means that SageMaker is unable to provide a default recommendation for the model using the information provided. If the deployment status is `IN_PROGRESS`, retry your API call after a few seconds to get a `COMPLETED` deployment recommendation.
Type: String
Valid Values: `IN_PROGRESS | COMPLETED | FAILED | NOT_APPLICABLE`
Required: Yes

 ** RealTimeInferenceRecommendations **   <a name="sagemaker-Type-DeploymentRecommendation-RealTimeInferenceRecommendations"></a>
A list of [RealTimeInferenceRecommendation](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_RealTimeInferenceRecommendation.html) items.
Type: Array of [RealTimeInferenceRecommendation](API_RealTimeInferenceRecommendation.md) objects
Array Members: Minimum number of 0 items. Maximum number of 3 items.
Required: No

## See Also
<a name="API_DeploymentRecommendation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DeploymentRecommendation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DeploymentRecommendation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DeploymentRecommendation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
