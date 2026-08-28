---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Autotune.html
---

# Autotune
<a name="API_Autotune"></a>

A flag to indicate if you want to use Autotune to automatically find optimal values for the following fields:
+  [ParameterRanges](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTuningJobConfig.html#sagemaker-Type-HyperParameterTuningJobConfig-ParameterRanges): The names and ranges of parameters that a hyperparameter tuning job can optimize.
+  [ResourceLimits](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ResourceLimits.html): The maximum resources that can be used for a training job. These resources include the maximum number of training jobs, the maximum runtime of a tuning job, and the maximum number of training jobs to run at the same time.
+  [TrainingJobEarlyStoppingType](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTuningJobConfig.html#sagemaker-Type-HyperParameterTuningJobConfig-TrainingJobEarlyStoppingType): A flag that specifies whether or not to use early stopping for training jobs launched by a hyperparameter tuning job.
+  [RetryStrategy](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTrainingJobDefinition.html#sagemaker-Type-HyperParameterTrainingJobDefinition-RetryStrategy): The number of times to retry a training job.
+  [Strategy](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTuningJobConfig.html): Specifies how hyperparameter tuning chooses the combinations of hyperparameter values to use for the training jobs that it launches.
+  [ConvergenceDetected](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ConvergenceDetected.html): A flag to indicate that Automatic model tuning (AMT) has detected model convergence.

## Contents
<a name="API_Autotune_Contents"></a>

 ** Mode **   <a name="sagemaker-Type-Autotune-Mode"></a>
Set `Mode` to `Enabled` if you want to use Autotune.
Type: String
Valid Values: `Enabled`
Required: Yes

## See Also
<a name="API_Autotune_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/Autotune)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/Autotune)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/Autotune)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
