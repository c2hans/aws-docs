---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-inferenceexperiment-inferenceexperimentschedule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::InferenceExperiment InferenceExperimentSchedule
<a name="aws-properties-sagemaker-inferenceexperiment-inferenceexperimentschedule"></a>

The start and end times of an inference experiment.

The maximum duration that you can set for an inference experiment is 30 days.

## Syntax
<a name="aws-properties-sagemaker-inferenceexperiment-inferenceexperimentschedule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-inferenceexperiment-inferenceexperimentschedule-syntax.json"></a>

```
{
  "[EndTime](#cfn-sagemaker-inferenceexperiment-inferenceexperimentschedule-endtime)" : {{String}},
  "[StartTime](#cfn-sagemaker-inferenceexperiment-inferenceexperimentschedule-starttime)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-inferenceexperiment-inferenceexperimentschedule-syntax.yaml"></a>

```
  [EndTime](#cfn-sagemaker-inferenceexperiment-inferenceexperimentschedule-endtime): {{String}}
  [StartTime](#cfn-sagemaker-inferenceexperiment-inferenceexperimentschedule-starttime): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-inferenceexperiment-inferenceexperimentschedule-properties"></a>

`EndTime`  <a name="cfn-sagemaker-inferenceexperiment-inferenceexperimentschedule-endtime"></a>
The timestamp at which the inference experiment ended or will end.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StartTime`  <a name="cfn-sagemaker-inferenceexperiment-inferenceexperimentschedule-starttime"></a>
The timestamp at which the inference experiment started or will start.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
