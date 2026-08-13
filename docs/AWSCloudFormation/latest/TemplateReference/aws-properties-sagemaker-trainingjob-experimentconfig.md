---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-trainingjob-experimentconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::TrainingJob ExperimentConfig
<a name="aws-properties-sagemaker-trainingjob-experimentconfig"></a>

Associates a SageMaker job as a trial component with an experiment and trial. Specified when you call the following APIs:
+  [CreateProcessingJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateProcessingJob.html)
+  [CreateTrainingJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingJob.html)
+  [CreateTransformJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTransformJob.html)

## Syntax
<a name="aws-properties-sagemaker-trainingjob-experimentconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-trainingjob-experimentconfig-syntax.json"></a>

```
{
  "[ExperimentName](#cfn-sagemaker-trainingjob-experimentconfig-experimentname)" : {{String}},
  "[RunName](#cfn-sagemaker-trainingjob-experimentconfig-runname)" : {{String}},
  "[TrialComponentDisplayName](#cfn-sagemaker-trainingjob-experimentconfig-trialcomponentdisplayname)" : {{String}},
  "[TrialName](#cfn-sagemaker-trainingjob-experimentconfig-trialname)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-trainingjob-experimentconfig-syntax.yaml"></a>

```
  [ExperimentName](#cfn-sagemaker-trainingjob-experimentconfig-experimentname): {{String}}
  [RunName](#cfn-sagemaker-trainingjob-experimentconfig-runname): {{String}}
  [TrialComponentDisplayName](#cfn-sagemaker-trainingjob-experimentconfig-trialcomponentdisplayname): {{String}}
  [TrialName](#cfn-sagemaker-trainingjob-experimentconfig-trialname): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-trainingjob-experimentconfig-properties"></a>

`ExperimentName`  <a name="cfn-sagemaker-trainingjob-experimentconfig-experimentname"></a>
The name of an existing experiment to associate with the trial component.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `120`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RunName`  <a name="cfn-sagemaker-trainingjob-experimentconfig-runname"></a>
The name of the experiment run to associate with the trial component.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `120`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TrialComponentDisplayName`  <a name="cfn-sagemaker-trainingjob-experimentconfig-trialcomponentdisplayname"></a>
The display name for the trial component. If this key isn't specified, the display name is the trial component name.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `120`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TrialName`  <a name="cfn-sagemaker-trainingjob-experimentconfig-trialname"></a>
The name of an existing trial to associate the trial component with. If not specified, a new trial is created.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `120`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
