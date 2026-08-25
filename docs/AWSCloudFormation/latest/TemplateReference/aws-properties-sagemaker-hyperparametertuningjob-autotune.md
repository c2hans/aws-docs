---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-hyperparametertuningjob-autotune.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::HyperParameterTuningJob Autotune
<a name="aws-properties-sagemaker-hyperparametertuningjob-autotune"></a>

A flag to indicate if you want to use Autotune to automatically find optimal values for the following fields:
+ [ParameterRanges](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTuningJobConfig.html#sagemaker-Type-HyperParameterTuningJobConfig-ParameterRanges): The names and ranges of parameters that a hyperparameter tuning job can optimize.
+ [ResourceLimits](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ResourceLimits.html): The maximum resources that can be used for a training job. These resources include the maximum number of training jobs, the maximum runtime of a tuning job, and the maximum number of training jobs to run at the same time.
+ [TrainingJobEarlyStoppingType](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTuningJobConfig.html#sagemaker-Type-HyperParameterTuningJobConfig-TrainingJobEarlyStoppingType): A flag that specifies whether or not to use early stopping for training jobs launched by a hyperparameter tuning job.
+ [RetryStrategy](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTrainingJobDefinition.html#sagemaker-Type-HyperParameterTrainingJobDefinition-RetryStrategy): The number of times to retry a training job.
+ [Strategy](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTuningJobConfig.html): Specifies how hyperparameter tuning chooses the combinations of hyperparameter values to use for the training jobs that it launches.
+ [ConvergenceDetected](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ConvergenceDetected.html): A flag to indicate that Automatic model tuning (AMT) has detected model convergence.

## Syntax
<a name="aws-properties-sagemaker-hyperparametertuningjob-autotune-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-hyperparametertuningjob-autotune-syntax.json"></a>

```
{
  "[Mode](#cfn-sagemaker-hyperparametertuningjob-autotune-mode)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-hyperparametertuningjob-autotune-syntax.yaml"></a>

```
  [Mode](#cfn-sagemaker-hyperparametertuningjob-autotune-mode): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-hyperparametertuningjob-autotune-properties"></a>

`Mode`  <a name="cfn-sagemaker-hyperparametertuningjob-autotune-mode"></a>
Set `Mode` to `Enabled` if you want to use Autotune.
*Required*: No
*Type*: String
*Allowed values*: `Enabled`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
