---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-sagemaker-hyperparametertuningjob.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::HyperParameterTuningJob
<a name="aws-resource-sagemaker-hyperparametertuningjob"></a>

Starts a hyperparameter tuning job. A hyperparameter tuning job finds the best version of a model by running many training jobs on your dataset using the algorithm you choose and values for hyperparameters within ranges that you specify. It then chooses the hyperparameter values that result in a model that performs the best, as measured by an objective metric that you choose.

A hyperparameter tuning job automatically creates Amazon SageMaker experiments, trials, and trial components for each training job that it runs. You can view these entities in Amazon SageMaker Studio. For more information, see [View Experiments, Trials, and Trial Components](https://docs.aws.amazon.com/sagemaker/latest/dg/experiments-view-compare.html#experiments-view).

**Important**
Do not include any security-sensitive information including account access IDs, secrets, or tokens in any hyperparameter fields. As part of the shared responsibility model, you are responsible for any potential exposure, unauthorized access, or compromise of your sensitive data if caused by any security-sensitive information included in the request hyperparameter variable or plain text fields..

## Syntax
<a name="aws-resource-sagemaker-hyperparametertuningjob-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-sagemaker-hyperparametertuningjob-syntax.json"></a>

```
{
  "Type" : "AWS::SageMaker::HyperParameterTuningJob",
  "Properties" : {
      "[Autotune](#cfn-sagemaker-hyperparametertuningjob-autotune)" : {{Autotune}},
      "[HyperParameterTuningJobConfig](#cfn-sagemaker-hyperparametertuningjob-hyperparametertuningjobconfig)" : {{HyperParameterTuningJobConfig}},
      "[HyperParameterTuningJobName](#cfn-sagemaker-hyperparametertuningjob-hyperparametertuningjobname)" : {{String}},
      "[Tags](#cfn-sagemaker-hyperparametertuningjob-tags)" : {{[ Tag, ... ]}},
      "[TrainingJobDefinition](#cfn-sagemaker-hyperparametertuningjob-trainingjobdefinition)" : {{TrainingJobDefinition}},
      "[TrainingJobDefinitions](#cfn-sagemaker-hyperparametertuningjob-trainingjobdefinitions)" : {{[ TrainingJobDefinition, ... ]}},
      "[WarmStartConfig](#cfn-sagemaker-hyperparametertuningjob-warmstartconfig)" : {{HyperParameterTuningJobWarmStartConfig}}
    }
}
```

### YAML
<a name="aws-resource-sagemaker-hyperparametertuningjob-syntax.yaml"></a>

```
Type: AWS::SageMaker::HyperParameterTuningJob
Properties:
  [Autotune](#cfn-sagemaker-hyperparametertuningjob-autotune): {{
    Autotune}}
  [HyperParameterTuningJobConfig](#cfn-sagemaker-hyperparametertuningjob-hyperparametertuningjobconfig): {{
    HyperParameterTuningJobConfig}}
  [HyperParameterTuningJobName](#cfn-sagemaker-hyperparametertuningjob-hyperparametertuningjobname): {{String}}
  [Tags](#cfn-sagemaker-hyperparametertuningjob-tags): {{
    - Tag}}
  [TrainingJobDefinition](#cfn-sagemaker-hyperparametertuningjob-trainingjobdefinition): {{
    TrainingJobDefinition}}
  [TrainingJobDefinitions](#cfn-sagemaker-hyperparametertuningjob-trainingjobdefinitions): {{
    - TrainingJobDefinition}}
  [WarmStartConfig](#cfn-sagemaker-hyperparametertuningjob-warmstartconfig): {{
    HyperParameterTuningJobWarmStartConfig}}
```

## Properties
<a name="aws-resource-sagemaker-hyperparametertuningjob-properties"></a>

`Autotune`  <a name="cfn-sagemaker-hyperparametertuningjob-autotune"></a>
A flag to indicate if you want to use Autotune to automatically find optimal values for the following fields:
+ [ParameterRanges](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTuningJobConfig.html#sagemaker-Type-HyperParameterTuningJobConfig-ParameterRanges): The names and ranges of parameters that a hyperparameter tuning job can optimize.
+ [ResourceLimits](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ResourceLimits.html): The maximum resources that can be used for a training job. These resources include the maximum number of training jobs, the maximum runtime of a tuning job, and the maximum number of training jobs to run at the same time.
+ [TrainingJobEarlyStoppingType](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTuningJobConfig.html#sagemaker-Type-HyperParameterTuningJobConfig-TrainingJobEarlyStoppingType): A flag that specifies whether or not to use early stopping for training jobs launched by a hyperparameter tuning job.
+ [RetryStrategy](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTrainingJobDefinition.html#sagemaker-Type-HyperParameterTrainingJobDefinition-RetryStrategy): The number of times to retry a training job.
+ [Strategy](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTuningJobConfig.html): Specifies how hyperparameter tuning chooses the combinations of hyperparameter values to use for the training jobs that it launches.
+ [ConvergenceDetected](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ConvergenceDetected.html): A flag to indicate that Automatic model tuning (AMT) has detected model convergence.
*Required*: No
*Type*: [Autotune](aws-properties-sagemaker-hyperparametertuningjob-autotune.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`HyperParameterTuningJobConfig`  <a name="cfn-sagemaker-hyperparametertuningjob-hyperparametertuningjobconfig"></a>
Configures a hyperparameter tuning job.
*Required*: Yes
*Type*: [HyperParameterTuningJobConfig](aws-properties-sagemaker-hyperparametertuningjob-hyperparametertuningjobconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`HyperParameterTuningJobName`  <a name="cfn-sagemaker-hyperparametertuningjob-hyperparametertuningjobname"></a>
The name of a hyperparameter tuning job.
*Required*: Yes
*Type*: String
*Pattern*: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,31}`
*Minimum*: `1`
*Maximum*: `32`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-sagemaker-hyperparametertuningjob-tags"></a>
The tags associated with a hyperparameter tuning job. For more information see [Tagging AWS resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html).
*Required*: No
*Type*: Array of [Tag](aws-properties-sagemaker-hyperparametertuningjob-tag.md)
*Maximum*: `50`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TrainingJobDefinition`  <a name="cfn-sagemaker-hyperparametertuningjob-trainingjobdefinition"></a>
Defines the input needed to run a training job using the algorithm.
*Required*: No
*Type*: [TrainingJobDefinition](aws-properties-sagemaker-hyperparametertuningjob-trainingjobdefinition.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TrainingJobDefinitions`  <a name="cfn-sagemaker-hyperparametertuningjob-trainingjobdefinitions"></a>
The job definitions included in a hyperparameter tuning job.
*Required*: No
*Type*: Array of [TrainingJobDefinition](aws-properties-sagemaker-hyperparametertuningjob-trainingjobdefinition.md)
*Minimum*: `1`
*Maximum*: `10`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`WarmStartConfig`  <a name="cfn-sagemaker-hyperparametertuningjob-warmstartconfig"></a>
Property description not available.
*Required*: No
*Type*: [HyperParameterTuningJobWarmStartConfig](aws-properties-sagemaker-hyperparametertuningjob-hyperparametertuningjobwarmstartconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-sagemaker-hyperparametertuningjob-return-values"></a>

### Ref
<a name="aws-resource-sagemaker-hyperparametertuningjob-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-sagemaker-hyperparametertuningjob-return-values-fn--getatt"></a>

####
<a name="aws-resource-sagemaker-hyperparametertuningjob-return-values-fn--getatt-fn--getatt"></a>

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
The time that a hyperparameter tuning job was created.

`HyperParameterTuningJobArn`  <a name="HyperParameterTuningJobArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of a hyperparameter tuning job.

`HyperParameterTuningJobStatus`  <a name="HyperParameterTuningJobStatus-fn::getatt"></a>
The status of a hyperparameter tuning job.
