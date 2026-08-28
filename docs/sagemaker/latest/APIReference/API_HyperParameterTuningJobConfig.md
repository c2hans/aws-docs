---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTuningJobConfig.html
---

# HyperParameterTuningJobConfig
<a name="API_HyperParameterTuningJobConfig"></a>

Configures a hyperparameter tuning job.

## Contents
<a name="API_HyperParameterTuningJobConfig_Contents"></a>

 ** ResourceLimits **   <a name="sagemaker-Type-HyperParameterTuningJobConfig-ResourceLimits"></a>
The [ResourceLimits](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ResourceLimits.html) object that specifies the maximum number of training and parallel training jobs that can be used for this hyperparameter tuning job.
Type: [ResourceLimits](API_ResourceLimits.md) object
Required: Yes

 ** Strategy **   <a name="sagemaker-Type-HyperParameterTuningJobConfig-Strategy"></a>
Specifies how hyperparameter tuning chooses the combinations of hyperparameter values to use for the training job it launches. For information about search strategies, see [How Hyperparameter Tuning Works](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-how-it-works.html).
Type: String
Valid Values: `Bayesian | Random | Hyperband | Grid`
Required: Yes

 ** HyperParameterTuningJobObjective **   <a name="sagemaker-Type-HyperParameterTuningJobConfig-HyperParameterTuningJobObjective"></a>
The [HyperParameterTuningJobObjective](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTuningJobObjective.html) specifies the objective metric used to evaluate the performance of training jobs launched by this tuning job.
Type: [HyperParameterTuningJobObjective](API_HyperParameterTuningJobObjective.md) object
Required: No

 ** ParameterRanges **   <a name="sagemaker-Type-HyperParameterTuningJobConfig-ParameterRanges"></a>
The [ParameterRanges](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ParameterRanges.html) object that specifies the ranges of hyperparameters that this tuning job searches over to find the optimal configuration for the highest model performance against your chosen objective metric.
Type: [ParameterRanges](API_ParameterRanges.md) object
Required: No

 ** RandomSeed **   <a name="sagemaker-Type-HyperParameterTuningJobConfig-RandomSeed"></a>
A value used to initialize a pseudo-random number generator. Setting a random seed and using the same seed later for the same tuning job will allow hyperparameter optimization to find more a consistent hyperparameter configuration between the two runs.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** StrategyConfig **   <a name="sagemaker-Type-HyperParameterTuningJobConfig-StrategyConfig"></a>
The configuration for the `Hyperband` optimization strategy. This parameter should be provided only if `Hyperband` is selected as the strategy for `HyperParameterTuningJobConfig`.
Type: [HyperParameterTuningJobStrategyConfig](API_HyperParameterTuningJobStrategyConfig.md) object
Required: No

 ** TrainingJobEarlyStoppingType **   <a name="sagemaker-Type-HyperParameterTuningJobConfig-TrainingJobEarlyStoppingType"></a>
Specifies whether to use early stopping for training jobs launched by the hyperparameter tuning job. Because the `Hyperband` strategy has its own advanced internal early stopping mechanism, `TrainingJobEarlyStoppingType` must be `OFF` to use `Hyperband`. This parameter can take on one of the following values (the default value is `OFF`):
OFF
Training jobs launched by the hyperparameter tuning job do not use early stopping.
AUTO
SageMaker stops training jobs launched by the hyperparameter tuning job when they are unlikely to perform better than previously completed training jobs. For more information, see [Stop Training Jobs Early](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-early-stopping.html).
Type: String
Valid Values: `Off | Auto`
Required: No

 ** TuningJobCompletionCriteria **   <a name="sagemaker-Type-HyperParameterTuningJobConfig-TuningJobCompletionCriteria"></a>
The tuning job's completion criteria.
Type: [TuningJobCompletionCriteria](API_TuningJobCompletionCriteria.md) object
Required: No

## See Also
<a name="API_HyperParameterTuningJobConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/HyperParameterTuningJobConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/HyperParameterTuningJobConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/HyperParameterTuningJobConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
