---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperbandStrategyConfig.html
---

# HyperbandStrategyConfig
<a name="API_HyperbandStrategyConfig"></a>

The configuration for `Hyperband`, a multi-fidelity based hyperparameter tuning strategy. `Hyperband` uses the final and intermediate results of a training job to dynamically allocate resources to utilized hyperparameter configurations while automatically stopping under-performing configurations. This parameter should be provided only if `Hyperband` is selected as the `StrategyConfig` under the `HyperParameterTuningJobConfig` API.

## Contents
<a name="API_HyperbandStrategyConfig_Contents"></a>

 ** MaxResource **   <a name="sagemaker-Type-HyperbandStrategyConfig-MaxResource"></a>
The maximum number of resources (such as epochs) that can be used by a training job launched by a hyperparameter tuning job. Once a job reaches the `MaxResource` value, it is stopped. If a value for `MaxResource` is not provided, and `Hyperband` is selected as the hyperparameter tuning strategy, `HyperbandTraining` attempts to infer `MaxResource` from the following keys (if present) in [StaticsHyperParameters](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTrainingJobDefinition.html#sagemaker-Type-HyperParameterTrainingJobDefinition-StaticHyperParameters):
+  `epochs`
+  `numepochs`
+  `n-epochs`
+  `n_epochs`
+  `num_epochs`
If `HyperbandStrategyConfig` is unable to infer a value for `MaxResource`, it generates a validation error. The maximum value is 20,000 epochs. All metrics that correspond to an objective metric are used to derive [early stopping decisions](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-early-stopping.html). For [distributed](https://docs.aws.amazon.com/sagemaker/latest/dg/distributed-training.html) training jobs, ensure that duplicate metrics are not printed in the logs across the individual nodes in a training job. If multiple nodes are publishing duplicate or incorrect metrics, training jobs may make an incorrect stopping decision and stop the job prematurely.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** MinResource **   <a name="sagemaker-Type-HyperbandStrategyConfig-MinResource"></a>
The minimum number of resources (such as epochs) that can be used by a training job launched by a hyperparameter tuning job. If the value for `MinResource` has not been reached, the training job is not stopped by `Hyperband`.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

## See Also
<a name="API_HyperbandStrategyConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/HyperbandStrategyConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/HyperbandStrategyConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/HyperbandStrategyConfig)
