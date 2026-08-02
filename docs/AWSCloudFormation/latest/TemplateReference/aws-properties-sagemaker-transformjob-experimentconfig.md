---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-transformjob-experimentconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::TransformJob ExperimentConfig
<a name="aws-properties-sagemaker-transformjob-experimentconfig"></a>

Associates a SageMaker job as a trial component with an experiment and trial. Specified when you call the following APIs:
+  [CreateProcessingJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateProcessingJob.html)
+  [CreateTrainingJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingJob.html)
+  [CreateTransformJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTransformJob.html)

## Syntax
<a name="aws-properties-sagemaker-transformjob-experimentconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-transformjob-experimentconfig-syntax.json"></a>

```
{
  "[ExperimentName](#cfn-sagemaker-transformjob-experimentconfig-experimentname)" : {{String}},
  "[TrialComponentDisplayName](#cfn-sagemaker-transformjob-experimentconfig-trialcomponentdisplayname)" : {{String}},
  "[TrialName](#cfn-sagemaker-transformjob-experimentconfig-trialname)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-transformjob-experimentconfig-syntax.yaml"></a>

```
  [ExperimentName](#cfn-sagemaker-transformjob-experimentconfig-experimentname): {{String}}
  [TrialComponentDisplayName](#cfn-sagemaker-transformjob-experimentconfig-trialcomponentdisplayname): {{String}}
  [TrialName](#cfn-sagemaker-transformjob-experimentconfig-trialname): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-transformjob-experimentconfig-properties"></a>

`ExperimentName`  <a name="cfn-sagemaker-transformjob-experimentconfig-experimentname"></a>
The name of an existing experiment to associate with the trial component.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9](-*[a-zA-Z0-9]){0,119}$`
*Minimum*: `1`
*Maximum*: `120`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TrialComponentDisplayName`  <a name="cfn-sagemaker-transformjob-experimentconfig-trialcomponentdisplayname"></a>
The display name for the trial component. If this key isn't specified, the display name is the trial component name.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9](-*[a-zA-Z0-9]){0,119}$`
*Minimum*: `1`
*Maximum*: `120`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TrialName`  <a name="cfn-sagemaker-transformjob-experimentconfig-trialname"></a>
The name of an existing trial to associate the trial component with. If not specified, a new trial is created.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9](-*[a-zA-Z0-9]){0,119}$`
*Minimum*: `1`
*Maximum*: `120`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
