---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-hyperparametertuningjob-hyperparametertuningjobconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::HyperParameterTuningJob HyperParameterTuningJobConfig
<a name="aws-properties-sagemaker-hyperparametertuningjob-hyperparametertuningjobconfig"></a>

Configures a hyperparameter tuning job.

## Syntax
<a name="aws-properties-sagemaker-hyperparametertuningjob-hyperparametertuningjobconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-hyperparametertuningjob-hyperparametertuningjobconfig-syntax.json"></a>

```
{
  "[HyperParameterTuningJobObjective](#cfn-sagemaker-hyperparametertuningjob-hyperparametertuningjobconfig-hyperparametertuningjobobjective)" : {{HyperParameterTuningJobObjective}},
  "[ParameterRanges](#cfn-sagemaker-hyperparametertuningjob-hyperparametertuningjobconfig-parameterranges)" : {{ParameterRanges}},
  "[RandomSeed](#cfn-sagemaker-hyperparametertuningjob-hyperparametertuningjobconfig-randomseed)" : {{Integer}},
  "[ResourceLimits](#cfn-sagemaker-hyperparametertuningjob-hyperparametertuningjobconfig-resourcelimits)" : {{ResourceLimits}},
  "[Strategy](#cfn-sagemaker-hyperparametertuningjob-hyperparametertuningjobconfig-strategy)" : {{String}},
  "[StrategyConfig](#cfn-sagemaker-hyperparametertuningjob-hyperparametertuningjobconfig-strategyconfig)" : {{StrategyConfig}},
  "[TrainingJobEarlyStoppingType](#cfn-sagemaker-hyperparametertuningjob-hyperparametertuningjobconfig-trainingjobearlystoppingtype)" : {{String}},
  "[TuningJobCompletionCriteria](#cfn-sagemaker-hyperparametertuningjob-hyperparametertuningjobconfig-tuningjobcompletioncriteria)" : {{TuningJobCompletionCriteria}}
}
```

### YAML
<a name="aws-properties-sagemaker-hyperparametertuningjob-hyperparametertuningjobconfig-syntax.yaml"></a>

```
  [HyperParameterTuningJobObjective](#cfn-sagemaker-hyperparametertuningjob-hyperparametertuningjobconfig-hyperparametertuningjobobjective): {{
    HyperParameterTuningJobObjective}}
  [ParameterRanges](#cfn-sagemaker-hyperparametertuningjob-hyperparametertuningjobconfig-parameterranges): {{
    ParameterRanges}}
  [RandomSeed](#cfn-sagemaker-hyperparametertuningjob-hyperparametertuningjobconfig-randomseed): {{Integer}}
  [ResourceLimits](#cfn-sagemaker-hyperparametertuningjob-hyperparametertuningjobconfig-resourcelimits): {{
    ResourceLimits}}
  [Strategy](#cfn-sagemaker-hyperparametertuningjob-hyperparametertuningjobconfig-strategy): {{String}}
  [StrategyConfig](#cfn-sagemaker-hyperparametertuningjob-hyperparametertuningjobconfig-strategyconfig): {{
    StrategyConfig}}
  [TrainingJobEarlyStoppingType](#cfn-sagemaker-hyperparametertuningjob-hyperparametertuningjobconfig-trainingjobearlystoppingtype): {{String}}
  [TuningJobCompletionCriteria](#cfn-sagemaker-hyperparametertuningjob-hyperparametertuningjobconfig-tuningjobcompletioncriteria): {{
    TuningJobCompletionCriteria}}
```

## Properties
<a name="aws-properties-sagemaker-hyperparametertuningjob-hyperparametertuningjobconfig-properties"></a>

`HyperParameterTuningJobObjective`  <a name="cfn-sagemaker-hyperparametertuningjob-hyperparametertuningjobconfig-hyperparametertuningjobobjective"></a>
The [HyperParameterTuningJobObjective](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTuningJobObjective.html) specifies the objective metric used to evaluate the performance of training jobs launched by this tuning job.
*Required*: No
*Type*: [HyperParameterTuningJobObjective](aws-properties-sagemaker-hyperparametertuningjob-hyperparametertuningjobobjective.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ParameterRanges`  <a name="cfn-sagemaker-hyperparametertuningjob-hyperparametertuningjobconfig-parameterranges"></a>
The [ParameterRanges](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ParameterRanges.html) object that specifies the ranges of hyperparameters that this tuning job searches over to find the optimal configuration for the highest model performance against your chosen objective metric.
*Required*: No
*Type*: [ParameterRanges](aws-properties-sagemaker-hyperparametertuningjob-parameterranges.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RandomSeed`  <a name="cfn-sagemaker-hyperparametertuningjob-hyperparametertuningjobconfig-randomseed"></a>
A value used to initialize a pseudo-random number generator. Setting a random seed and using the same seed later for the same tuning job will allow hyperparameter optimization to find more a consistent hyperparameter configuration between the two runs.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ResourceLimits`  <a name="cfn-sagemaker-hyperparametertuningjob-hyperparametertuningjobconfig-resourcelimits"></a>
The [ResourceLimits](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ResourceLimits.html) object that specifies the maximum number of training and parallel training jobs that can be used for this hyperparameter tuning job.
*Required*: Yes
*Type*: [ResourceLimits](aws-properties-sagemaker-hyperparametertuningjob-resourcelimits.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Strategy`  <a name="cfn-sagemaker-hyperparametertuningjob-hyperparametertuningjobconfig-strategy"></a>
Specifies how hyperparameter tuning chooses the combinations of hyperparameter values to use for the training job it launches. For information about search strategies, see [How Hyperparameter Tuning Works](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-how-it-works.html).
*Required*: Yes
*Type*: String
*Allowed values*: `Bayesian | Random | Hyperband | Grid`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`StrategyConfig`  <a name="cfn-sagemaker-hyperparametertuningjob-hyperparametertuningjobconfig-strategyconfig"></a>
The configuration for the `Hyperband` optimization strategy. This parameter should be provided only if `Hyperband` is selected as the strategy for `HyperParameterTuningJobConfig`.
*Required*: No
*Type*: [StrategyConfig](aws-properties-sagemaker-hyperparametertuningjob-strategyconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TrainingJobEarlyStoppingType`  <a name="cfn-sagemaker-hyperparametertuningjob-hyperparametertuningjobconfig-trainingjobearlystoppingtype"></a>
Specifies whether to use early stopping for training jobs launched by the hyperparameter tuning job. Because the `Hyperband` strategy has its own advanced internal early stopping mechanism, `TrainingJobEarlyStoppingType` must be `OFF` to use `Hyperband`. This parameter can take on one of the following values (the default value is `OFF`):
OFF
Training jobs launched by the hyperparameter tuning job do not use early stopping.
AUTO
SageMaker stops training jobs launched by the hyperparameter tuning job when they are unlikely to perform better than previously completed training jobs. For more information, see [Stop Training Jobs Early](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-early-stopping.html).
*Required*: No
*Type*: String
*Allowed values*: `Off | Auto`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TuningJobCompletionCriteria`  <a name="cfn-sagemaker-hyperparametertuningjob-hyperparametertuningjobconfig-tuningjobcompletioncriteria"></a>
The tuning job's completion criteria.
*Required*: No
*Type*: [TuningJobCompletionCriteria](aws-properties-sagemaker-hyperparametertuningjob-tuningjobcompletioncriteria.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
