---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-automljob-automljobcompletioncriteria.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::AutoMLJob AutoMLJobCompletionCriteria
<a name="aws-properties-sagemaker-automljob-automljobcompletioncriteria"></a>

How long a job is allowed to run, or how many candidates a job is allowed to generate.

## Syntax
<a name="aws-properties-sagemaker-automljob-automljobcompletioncriteria-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-automljob-automljobcompletioncriteria-syntax.json"></a>

```
{
  "[MaxAutoMLJobRuntimeInSeconds](#cfn-sagemaker-automljob-automljobcompletioncriteria-maxautomljobruntimeinseconds)" : {{Integer}},
  "[MaxCandidates](#cfn-sagemaker-automljob-automljobcompletioncriteria-maxcandidates)" : {{Integer}},
  "[MaxRuntimePerTrainingJobInSeconds](#cfn-sagemaker-automljob-automljobcompletioncriteria-maxruntimepertrainingjobinseconds)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-sagemaker-automljob-automljobcompletioncriteria-syntax.yaml"></a>

```
  [MaxAutoMLJobRuntimeInSeconds](#cfn-sagemaker-automljob-automljobcompletioncriteria-maxautomljobruntimeinseconds): {{Integer}}
  [MaxCandidates](#cfn-sagemaker-automljob-automljobcompletioncriteria-maxcandidates): {{Integer}}
  [MaxRuntimePerTrainingJobInSeconds](#cfn-sagemaker-automljob-automljobcompletioncriteria-maxruntimepertrainingjobinseconds): {{Integer}}
```

## Properties
<a name="aws-properties-sagemaker-automljob-automljobcompletioncriteria-properties"></a>

`MaxAutoMLJobRuntimeInSeconds`  <a name="cfn-sagemaker-automljob-automljobcompletioncriteria-maxautomljobruntimeinseconds"></a>
The maximum runtime, in seconds, an AutoML job has to complete.
If an AutoML job exceeds the maximum runtime, the job is stopped automatically and its processing is ended gracefully. The AutoML job identifies the best model whose training was completed and marks it as the best-performing model. Any unfinished steps of the job, such as automatic one-click Autopilot model deployment, are not completed.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MaxCandidates`  <a name="cfn-sagemaker-automljob-automljobcompletioncriteria-maxcandidates"></a>
The maximum number of times a training job is allowed to run.
For text and image classification, time-series forecasting, as well as text generation (LLMs fine-tuning) problem types, the supported value is 1. For tabular problem types, the maximum value is 750.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `750`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MaxRuntimePerTrainingJobInSeconds`  <a name="cfn-sagemaker-automljob-automljobcompletioncriteria-maxruntimepertrainingjobinseconds"></a>
The maximum time, in seconds, that each training job executed inside hyperparameter tuning is allowed to run as part of a hyperparameter tuning job. For more information, see the [StoppingCondition](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_StoppingCondition.html) used by the [CreateHyperParameterTuningJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateHyperParameterTuningJob.html) action.
For job V2s (jobs created by calling `CreateAutoMLJobV2`), this field controls the runtime of the job candidate.
For [TextGenerationJobConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TextClassificationJobConfig.html) problem types, the maximum time defaults to 72 hours (259200 seconds).
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
