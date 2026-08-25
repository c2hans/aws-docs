---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-hyperparametertuningjob-bestobjectivenotimproving.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::HyperParameterTuningJob BestObjectiveNotImproving
<a name="aws-properties-sagemaker-hyperparametertuningjob-bestobjectivenotimproving"></a>

A structure that keeps track of which training jobs launched by your hyperparameter tuning job are not improving model performance as evaluated against an objective function.

## Syntax
<a name="aws-properties-sagemaker-hyperparametertuningjob-bestobjectivenotimproving-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-hyperparametertuningjob-bestobjectivenotimproving-syntax.json"></a>

```
{
  "[MaxNumberOfTrainingJobsNotImproving](#cfn-sagemaker-hyperparametertuningjob-bestobjectivenotimproving-maxnumberoftrainingjobsnotimproving)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-sagemaker-hyperparametertuningjob-bestobjectivenotimproving-syntax.yaml"></a>

```
  [MaxNumberOfTrainingJobsNotImproving](#cfn-sagemaker-hyperparametertuningjob-bestobjectivenotimproving-maxnumberoftrainingjobsnotimproving): {{Integer}}
```

## Properties
<a name="aws-properties-sagemaker-hyperparametertuningjob-bestobjectivenotimproving-properties"></a>

`MaxNumberOfTrainingJobsNotImproving`  <a name="cfn-sagemaker-hyperparametertuningjob-bestobjectivenotimproving-maxnumberoftrainingjobsnotimproving"></a>
The number of training jobs that have failed to improve model performance by 1% or greater over prior training jobs as evaluated against an objective function.
*Required*: No
*Type*: Integer
*Minimum*: `3`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
