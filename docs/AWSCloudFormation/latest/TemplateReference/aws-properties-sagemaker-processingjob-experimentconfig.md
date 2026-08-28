---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-processingjob-experimentconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::ProcessingJob ExperimentConfig
<a name="aws-properties-sagemaker-processingjob-experimentconfig"></a>

Associates a SageMaker job as a trial component with an experiment and trial. Specified when you call the [CreateProcessingJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateProcessingJob.html) API.

## Syntax
<a name="aws-properties-sagemaker-processingjob-experimentconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-processingjob-experimentconfig-syntax.json"></a>

```
{
  "[ExperimentName](#cfn-sagemaker-processingjob-experimentconfig-experimentname)" : {{String}},
  "[RunName](#cfn-sagemaker-processingjob-experimentconfig-runname)" : {{String}},
  "[TrialComponentDisplayName](#cfn-sagemaker-processingjob-experimentconfig-trialcomponentdisplayname)" : {{String}},
  "[TrialName](#cfn-sagemaker-processingjob-experimentconfig-trialname)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-processingjob-experimentconfig-syntax.yaml"></a>

```
  [ExperimentName](#cfn-sagemaker-processingjob-experimentconfig-experimentname): {{String}}
  [RunName](#cfn-sagemaker-processingjob-experimentconfig-runname): {{String}}
  [TrialComponentDisplayName](#cfn-sagemaker-processingjob-experimentconfig-trialcomponentdisplayname): {{String}}
  [TrialName](#cfn-sagemaker-processingjob-experimentconfig-trialname): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-processingjob-experimentconfig-properties"></a>

`ExperimentName`  <a name="cfn-sagemaker-processingjob-experimentconfig-experimentname"></a>
The name of an existing experiment to associate with the trial component.
*Required*: No
*Type*: String
*Pattern*: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,119}`
*Maximum*: `120`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RunName`  <a name="cfn-sagemaker-processingjob-experimentconfig-runname"></a>
The name of the experiment run to associate with the trial component.
*Required*: No
*Type*: String
*Pattern*: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,119}`
*Maximum*: `120`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TrialComponentDisplayName`  <a name="cfn-sagemaker-processingjob-experimentconfig-trialcomponentdisplayname"></a>
The display name for the trial component. If this key isn't specified, the display name is the trial component name.
*Required*: No
*Type*: String
*Pattern*: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,119}`
*Maximum*: `120`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TrialName`  <a name="cfn-sagemaker-processingjob-experimentconfig-trialname"></a>
The name of an existing trial to associate the trial component with. If not specified, a new trial is created.
*Required*: No
*Type*: String
*Pattern*: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,119}`
*Maximum*: `120`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
