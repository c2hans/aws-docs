---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTuningJobStrategyConfig.html
---

# HyperParameterTuningJobStrategyConfig
<a name="API_HyperParameterTuningJobStrategyConfig"></a>

The configuration for a training job launched by a hyperparameter tuning job. Choose `Bayesian` for Bayesian optimization, and `Random` for random search optimization. For more advanced use cases, use `Hyperband`, which evaluates objective metrics for training jobs after every epoch. For more information about strategies, see [How Hyperparameter Tuning Works](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-how-it-works.html).

## Contents
<a name="API_HyperParameterTuningJobStrategyConfig_Contents"></a>

 ** HyperbandStrategyConfig **   <a name="sagemaker-Type-HyperParameterTuningJobStrategyConfig-HyperbandStrategyConfig"></a>
The configuration for the object that specifies the `Hyperband` strategy. This parameter is only supported for the `Hyperband` selection for `Strategy` within the `HyperParameterTuningJobConfig` API.
Type: [HyperbandStrategyConfig](API_HyperbandStrategyConfig.md) object
Required: No

## See Also
<a name="API_HyperParameterTuningJobStrategyConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/HyperParameterTuningJobStrategyConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/HyperParameterTuningJobStrategyConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/HyperParameterTuningJobStrategyConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
