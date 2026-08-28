---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-processingjob-stoppingcondition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::ProcessingJob StoppingCondition
<a name="aws-properties-sagemaker-processingjob-stoppingcondition"></a>

Configures conditions under which the processing job should be stopped, such as how long the processing job has been running. After the condition is met, the processing job is stopped.

## Syntax
<a name="aws-properties-sagemaker-processingjob-stoppingcondition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-processingjob-stoppingcondition-syntax.json"></a>

```
{
  "[MaxRuntimeInSeconds](#cfn-sagemaker-processingjob-stoppingcondition-maxruntimeinseconds)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-sagemaker-processingjob-stoppingcondition-syntax.yaml"></a>

```
  [MaxRuntimeInSeconds](#cfn-sagemaker-processingjob-stoppingcondition-maxruntimeinseconds): {{Integer}}
```

## Properties
<a name="aws-properties-sagemaker-processingjob-stoppingcondition-properties"></a>

`MaxRuntimeInSeconds`  <a name="cfn-sagemaker-processingjob-stoppingcondition-maxruntimeinseconds"></a>
The maximum length of time, in seconds, that a training or compilation job can run before it is stopped.
For compilation jobs, if the job does not complete during this time, a `TimeOut` error is generated. We recommend starting with 900 seconds and increasing as necessary based on your model.
For all other jobs, if the job does not complete during this time, SageMaker ends the job. When `RetryStrategy` is specified in the job request, `MaxRuntimeInSeconds` specifies the maximum time for all of the attempts in total, not each individual attempt. The default value is 1 day. The maximum value is 28 days.
The maximum time that a `TrainingJob` can run in total, including any time spent publishing metrics or archiving and uploading models after it has been stopped, is 30 days.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Maximum*: `777600`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
