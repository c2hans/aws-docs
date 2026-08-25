---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-hyperparametertuningjob-objectivestatuscounters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::HyperParameterTuningJob ObjectiveStatusCounters
<a name="aws-properties-sagemaker-hyperparametertuningjob-objectivestatuscounters"></a>

Specifies the number of training jobs that this hyperparameter tuning job launched, categorized by the status of their objective metric. The objective metric status shows whether the final objective metric for the training job has been evaluated by the tuning job and used in the hyperparameter tuning process.

## Syntax
<a name="aws-properties-sagemaker-hyperparametertuningjob-objectivestatuscounters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-hyperparametertuningjob-objectivestatuscounters-syntax.json"></a>

```
{
  "[Failed](#cfn-sagemaker-hyperparametertuningjob-objectivestatuscounters-failed)" : {{Integer}},
  "[Pending](#cfn-sagemaker-hyperparametertuningjob-objectivestatuscounters-pending)" : {{Integer}},
  "[Succeeded](#cfn-sagemaker-hyperparametertuningjob-objectivestatuscounters-succeeded)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-sagemaker-hyperparametertuningjob-objectivestatuscounters-syntax.yaml"></a>

```
  [Failed](#cfn-sagemaker-hyperparametertuningjob-objectivestatuscounters-failed): {{Integer}}
  [Pending](#cfn-sagemaker-hyperparametertuningjob-objectivestatuscounters-pending): {{Integer}}
  [Succeeded](#cfn-sagemaker-hyperparametertuningjob-objectivestatuscounters-succeeded): {{Integer}}
```

## Properties
<a name="aws-properties-sagemaker-hyperparametertuningjob-objectivestatuscounters-properties"></a>

`Failed`  <a name="cfn-sagemaker-hyperparametertuningjob-objectivestatuscounters-failed"></a>
The number of training jobs whose final objective metric was not evaluated and used in the hyperparameter tuning process. This typically occurs when the training job failed or did not emit an objective metric.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Pending`  <a name="cfn-sagemaker-hyperparametertuningjob-objectivestatuscounters-pending"></a>
The number of training jobs that are in progress and pending evaluation of their final objective metric.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Succeeded`  <a name="cfn-sagemaker-hyperparametertuningjob-objectivestatuscounters-succeeded"></a>
The number of training jobs whose final objective metric was evaluated by the hyperparameter tuning job and used in the hyperparameter tuning process.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
