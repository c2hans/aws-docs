---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-hyperparametertuningjob-tuningjobcompletioncriteria.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::HyperParameterTuningJob TuningJobCompletionCriteria
<a name="aws-properties-sagemaker-hyperparametertuningjob-tuningjobcompletioncriteria"></a>

The job completion criteria.

## Syntax
<a name="aws-properties-sagemaker-hyperparametertuningjob-tuningjobcompletioncriteria-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-hyperparametertuningjob-tuningjobcompletioncriteria-syntax.json"></a>

```
{
  "[BestObjectiveNotImproving](#cfn-sagemaker-hyperparametertuningjob-tuningjobcompletioncriteria-bestobjectivenotimproving)" : {{BestObjectiveNotImproving}},
  "[ConvergenceDetected](#cfn-sagemaker-hyperparametertuningjob-tuningjobcompletioncriteria-convergencedetected)" : {{ConvergenceDetected}},
  "[TargetObjectiveMetricValue](#cfn-sagemaker-hyperparametertuningjob-tuningjobcompletioncriteria-targetobjectivemetricvalue)" : {{Number}}
}
```

### YAML
<a name="aws-properties-sagemaker-hyperparametertuningjob-tuningjobcompletioncriteria-syntax.yaml"></a>

```
  [BestObjectiveNotImproving](#cfn-sagemaker-hyperparametertuningjob-tuningjobcompletioncriteria-bestobjectivenotimproving): {{
    BestObjectiveNotImproving}}
  [ConvergenceDetected](#cfn-sagemaker-hyperparametertuningjob-tuningjobcompletioncriteria-convergencedetected): {{
    ConvergenceDetected}}
  [TargetObjectiveMetricValue](#cfn-sagemaker-hyperparametertuningjob-tuningjobcompletioncriteria-targetobjectivemetricvalue): {{Number}}
```

## Properties
<a name="aws-properties-sagemaker-hyperparametertuningjob-tuningjobcompletioncriteria-properties"></a>

`BestObjectiveNotImproving`  <a name="cfn-sagemaker-hyperparametertuningjob-tuningjobcompletioncriteria-bestobjectivenotimproving"></a>
A flag to stop your hyperparameter tuning job if model performance fails to improve as evaluated against an objective function.
*Required*: No
*Type*: [BestObjectiveNotImproving](aws-properties-sagemaker-hyperparametertuningjob-bestobjectivenotimproving.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ConvergenceDetected`  <a name="cfn-sagemaker-hyperparametertuningjob-tuningjobcompletioncriteria-convergencedetected"></a>
A flag to top your hyperparameter tuning job if automatic model tuning (AMT) has detected that your model has converged as evaluated against your objective function.
*Required*: No
*Type*: [ConvergenceDetected](aws-properties-sagemaker-hyperparametertuningjob-convergencedetected.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TargetObjectiveMetricValue`  <a name="cfn-sagemaker-hyperparametertuningjob-tuningjobcompletioncriteria-targetobjectivemetricvalue"></a>
The value of the objective metric.
*Required*: No
*Type*: Number
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
