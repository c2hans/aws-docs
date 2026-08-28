---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLJobCompletionCriteria.html
---

# AutoMLJobCompletionCriteria
<a name="API_AutoMLJobCompletionCriteria"></a>

How long a job is allowed to run, or how many candidates a job is allowed to generate.

## Contents
<a name="API_AutoMLJobCompletionCriteria_Contents"></a>

 ** MaxAutoMLJobRuntimeInSeconds **   <a name="sagemaker-Type-AutoMLJobCompletionCriteria-MaxAutoMLJobRuntimeInSeconds"></a>
The maximum runtime, in seconds, an AutoML job has to complete.
If an AutoML job exceeds the maximum runtime, the job is stopped automatically and its processing is ended gracefully. The AutoML job identifies the best model whose training was completed and marks it as the best-performing model. Any unfinished steps of the job, such as automatic one-click Autopilot model deployment, are not completed.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** MaxCandidates **   <a name="sagemaker-Type-AutoMLJobCompletionCriteria-MaxCandidates"></a>
The maximum number of times a training job is allowed to run.
For text and image classification, time-series forecasting, as well as text generation (LLMs fine-tuning) problem types, the supported value is 1. For tabular problem types, the maximum value is 750.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 750.
Required: No

 ** MaxRuntimePerTrainingJobInSeconds **   <a name="sagemaker-Type-AutoMLJobCompletionCriteria-MaxRuntimePerTrainingJobInSeconds"></a>
The maximum time, in seconds, that each training job executed inside hyperparameter tuning is allowed to run as part of a hyperparameter tuning job. For more information, see the [StoppingCondition](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_StoppingCondition.html) used by the [CreateHyperParameterTuningJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateHyperParameterTuningJob.html) action.
For job V2s (jobs created by calling `CreateAutoMLJobV2`), this field controls the runtime of the job candidate.
For [TextGenerationJobConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TextClassificationJobConfig.html) problem types, the maximum time defaults to 72 hours (259200 seconds).
Type: Integer
Valid Range: Minimum value of 1.
Required: No

## See Also
<a name="API_AutoMLJobCompletionCriteria_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/AutoMLJobCompletionCriteria)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/AutoMLJobCompletionCriteria)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/AutoMLJobCompletionCriteria)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
