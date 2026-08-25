---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-hyperparametertuningjob-hyperbandstrategyconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::HyperParameterTuningJob HyperbandStrategyConfig
<a name="aws-properties-sagemaker-hyperparametertuningjob-hyperbandstrategyconfig"></a>

The configuration for `Hyperband`, a multi-fidelity based hyperparameter tuning strategy. `Hyperband` uses the final and intermediate results of a training job to dynamically allocate resources to utilized hyperparameter configurations while automatically stopping under-performing configurations. This parameter should be provided only if `Hyperband` is selected as the `StrategyConfig` under the `HyperParameterTuningJobConfig` API.

## Syntax
<a name="aws-properties-sagemaker-hyperparametertuningjob-hyperbandstrategyconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-hyperparametertuningjob-hyperbandstrategyconfig-syntax.json"></a>

```
{
  "[MaxResource](#cfn-sagemaker-hyperparametertuningjob-hyperbandstrategyconfig-maxresource)" : {{Integer}},
  "[MinResource](#cfn-sagemaker-hyperparametertuningjob-hyperbandstrategyconfig-minresource)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-sagemaker-hyperparametertuningjob-hyperbandstrategyconfig-syntax.yaml"></a>

```
  [MaxResource](#cfn-sagemaker-hyperparametertuningjob-hyperbandstrategyconfig-maxresource): {{Integer}}
  [MinResource](#cfn-sagemaker-hyperparametertuningjob-hyperbandstrategyconfig-minresource): {{Integer}}
```

## Properties
<a name="aws-properties-sagemaker-hyperparametertuningjob-hyperbandstrategyconfig-properties"></a>

`MaxResource`  <a name="cfn-sagemaker-hyperparametertuningjob-hyperbandstrategyconfig-maxresource"></a>
The maximum number of resources (such as epochs) that can be used by a training job launched by a hyperparameter tuning job. Once a job reaches the `MaxResource` value, it is stopped. If a value for `MaxResource` is not provided, and `Hyperband` is selected as the hyperparameter tuning strategy, `HyperbandTraining` attempts to infer `MaxResource` from the following keys (if present) in [StaticsHyperParameters](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTrainingJobDefinition.html#sagemaker-Type-HyperParameterTrainingJobDefinition-StaticHyperParameters):
+  `epochs`
+  `numepochs`
+  `n-epochs`
+  `n_epochs`
+  `num_epochs`
If `HyperbandStrategyConfig` is unable to infer a value for `MaxResource`, it generates a validation error. The maximum value is 20,000 epochs. All metrics that correspond to an objective metric are used to derive [early stopping decisions](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-early-stopping.html). For [distributed](https://docs.aws.amazon.com/sagemaker/latest/dg/distributed-training.html) training jobs, ensure that duplicate metrics are not printed in the logs across the individual nodes in a training job. If multiple nodes are publishing duplicate or incorrect metrics, training jobs may make an incorrect stopping decision and stop the job prematurely.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MinResource`  <a name="cfn-sagemaker-hyperparametertuningjob-hyperbandstrategyconfig-minresource"></a>
The minimum number of resources (such as epochs) that can be used by a training job launched by a hyperparameter tuning job. If the value for `MinResource` has not been reached, the training job is not stopped by `Hyperband`.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
