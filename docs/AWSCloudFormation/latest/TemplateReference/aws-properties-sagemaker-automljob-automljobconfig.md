---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-automljob-automljobconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::AutoMLJob AutoMLJobConfig
<a name="aws-properties-sagemaker-automljob-automljobconfig"></a>

A collection of settings used for an AutoML job.

## Syntax
<a name="aws-properties-sagemaker-automljob-automljobconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-automljob-automljobconfig-syntax.json"></a>

```
{
  "[CandidateGenerationConfig](#cfn-sagemaker-automljob-automljobconfig-candidategenerationconfig)" : {{AutoMLCandidateGenerationConfig}},
  "[CompletionCriteria](#cfn-sagemaker-automljob-automljobconfig-completioncriteria)" : {{AutoMLJobCompletionCriteria}},
  "[DataSplitConfig](#cfn-sagemaker-automljob-automljobconfig-datasplitconfig)" : {{AutoMLDataSplitConfig}},
  "[Mode](#cfn-sagemaker-automljob-automljobconfig-mode)" : {{String}},
  "[SecurityConfig](#cfn-sagemaker-automljob-automljobconfig-securityconfig)" : {{AutoMLSecurityConfig}}
}
```

### YAML
<a name="aws-properties-sagemaker-automljob-automljobconfig-syntax.yaml"></a>

```
  [CandidateGenerationConfig](#cfn-sagemaker-automljob-automljobconfig-candidategenerationconfig): {{
    AutoMLCandidateGenerationConfig}}
  [CompletionCriteria](#cfn-sagemaker-automljob-automljobconfig-completioncriteria): {{
    AutoMLJobCompletionCriteria}}
  [DataSplitConfig](#cfn-sagemaker-automljob-automljobconfig-datasplitconfig): {{
    AutoMLDataSplitConfig}}
  [Mode](#cfn-sagemaker-automljob-automljobconfig-mode): {{String}}
  [SecurityConfig](#cfn-sagemaker-automljob-automljobconfig-securityconfig): {{
    AutoMLSecurityConfig}}
```

## Properties
<a name="aws-properties-sagemaker-automljob-automljobconfig-properties"></a>

`CandidateGenerationConfig`  <a name="cfn-sagemaker-automljob-automljobconfig-candidategenerationconfig"></a>
The configuration for generating a candidate for an AutoML job (optional).
*Required*: No
*Type*: [AutoMLCandidateGenerationConfig](aws-properties-sagemaker-automljob-automlcandidategenerationconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CompletionCriteria`  <a name="cfn-sagemaker-automljob-automljobconfig-completioncriteria"></a>
How long an AutoML job is allowed to run, or how many candidates a job is allowed to generate.
*Required*: No
*Type*: [AutoMLJobCompletionCriteria](aws-properties-sagemaker-automljob-automljobcompletioncriteria.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DataSplitConfig`  <a name="cfn-sagemaker-automljob-automljobconfig-datasplitconfig"></a>
The configuration for splitting the input training dataset.
Type: AutoMLDataSplitConfig
*Required*: No
*Type*: [AutoMLDataSplitConfig](aws-properties-sagemaker-automljob-automldatasplitconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Mode`  <a name="cfn-sagemaker-automljob-automljobconfig-mode"></a>
The method that Autopilot uses to train the data. You can either specify the mode manually or let Autopilot choose for you based on the dataset size by selecting `AUTO`. In `AUTO` mode, Autopilot chooses `ENSEMBLING` for datasets smaller than 100 MB, and `HYPERPARAMETER_TUNING` for larger ones.
The `ENSEMBLING` mode uses a multi-stack ensemble model to predict classification and regression tasks directly from your dataset. This machine learning mode combines several base models to produce an optimal predictive model. It then uses a stacking ensemble method to combine predictions from contributing members. A multi-stack ensemble model can provide better performance over a single model by combining the predictive capabilities of multiple models. See [Autopilot algorithm support](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-model-support-validation.html#autopilot-algorithm-support) for a list of algorithms supported by `ENSEMBLING` mode.
The `HYPERPARAMETER_TUNING` (HPO) mode uses the best hyperparameters to train the best version of a model. HPO automatically selects an algorithm for the type of problem you want to solve. Then HPO finds the best hyperparameters according to your objective metric. See [Autopilot algorithm support](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-model-support-validation.html#autopilot-algorithm-support) for a list of algorithms supported by `HYPERPARAMETER_TUNING` mode.
*Required*: No
*Type*: String
*Allowed values*: `AUTO | ENSEMBLING | HYPERPARAMETER_TUNING`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SecurityConfig`  <a name="cfn-sagemaker-automljob-automljobconfig-securityconfig"></a>
The security configuration for traffic encryption or Amazon VPC settings.
*Required*: No
*Type*: [AutoMLSecurityConfig](aws-properties-sagemaker-automljob-automlsecurityconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
