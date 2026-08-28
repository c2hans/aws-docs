---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTuningJobCompletionDetails.html
---

# HyperParameterTuningJobCompletionDetails
<a name="API_HyperParameterTuningJobCompletionDetails"></a>

A structure that contains runtime information about both current and completed hyperparameter tuning jobs.

## Contents
<a name="API_HyperParameterTuningJobCompletionDetails_Contents"></a>

 ** ConvergenceDetectedTime **   <a name="sagemaker-Type-HyperParameterTuningJobCompletionDetails-ConvergenceDetectedTime"></a>
The time in timestamp format that AMT detected model convergence, as defined by a lack of significant improvement over time based on criteria developed over a wide range of diverse benchmarking tests.
Type: Timestamp
Required: No

 ** NumberOfTrainingJobsObjectiveNotImproving **   <a name="sagemaker-Type-HyperParameterTuningJobCompletionDetails-NumberOfTrainingJobsObjectiveNotImproving"></a>
The number of training jobs launched by a tuning job that are not improving (1% or less) as measured by model performance evaluated against an objective function.
Type: Integer
Required: No

## See Also
<a name="API_HyperParameterTuningJobCompletionDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/HyperParameterTuningJobCompletionDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/HyperParameterTuningJobCompletionDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/HyperParameterTuningJobCompletionDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
