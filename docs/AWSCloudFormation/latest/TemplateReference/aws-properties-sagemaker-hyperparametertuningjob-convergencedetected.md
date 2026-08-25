---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-hyperparametertuningjob-convergencedetected.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::HyperParameterTuningJob ConvergenceDetected
<a name="aws-properties-sagemaker-hyperparametertuningjob-convergencedetected"></a>

A flag to indicating that automatic model tuning (AMT) has detected model convergence, defined as a lack of significant improvement (1% or less) against an objective metric.

## Syntax
<a name="aws-properties-sagemaker-hyperparametertuningjob-convergencedetected-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-hyperparametertuningjob-convergencedetected-syntax.json"></a>

```
{
  "[CompleteOnConvergence](#cfn-sagemaker-hyperparametertuningjob-convergencedetected-completeonconvergence)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-hyperparametertuningjob-convergencedetected-syntax.yaml"></a>

```
  [CompleteOnConvergence](#cfn-sagemaker-hyperparametertuningjob-convergencedetected-completeonconvergence): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-hyperparametertuningjob-convergencedetected-properties"></a>

`CompleteOnConvergence`  <a name="cfn-sagemaker-hyperparametertuningjob-convergencedetected-completeonconvergence"></a>
A flag to stop a tuning job once AMT has detected that the job has converged.
*Required*: No
*Type*: String
*Allowed values*: `Disabled | Enabled`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
