---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-modelexplainabilityjobdefinition-stoppingcondition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::ModelExplainabilityJobDefinition StoppingCondition
<a name="aws-properties-sagemaker-modelexplainabilityjobdefinition-stoppingcondition"></a>

Specifies a limit to how long a job can run. When the job reaches the time limit, SageMaker ends the job. Use this API to cap costs.

To stop a training job, SageMaker sends the algorithm the `SIGTERM` signal, which delays job termination for 120 seconds. Algorithms can use this 120-second window to save the model artifacts, so the results of training are not lost.

The training algorithms provided by SageMaker automatically save the intermediate results of a model training job when possible. This attempt to save artifacts is only a best effort case as model might not be in a state from which it can be saved. For example, if training has just started, the model might not be ready to save. When saved, this intermediate data is a valid model artifact. You can use it to create a model with `CreateModel`.

**Note**
The Neural Topic Model (NTM) currently does not support saving intermediate model artifacts. When training NTMs, make sure that the maximum runtime is sufficient for the training job to complete.

## Syntax
<a name="aws-properties-sagemaker-modelexplainabilityjobdefinition-stoppingcondition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-modelexplainabilityjobdefinition-stoppingcondition-syntax.json"></a>

```
{
  "[MaxRuntimeInSeconds](#cfn-sagemaker-modelexplainabilityjobdefinition-stoppingcondition-maxruntimeinseconds)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-sagemaker-modelexplainabilityjobdefinition-stoppingcondition-syntax.yaml"></a>

```
  [MaxRuntimeInSeconds](#cfn-sagemaker-modelexplainabilityjobdefinition-stoppingcondition-maxruntimeinseconds): {{Integer}}
```

## Properties
<a name="aws-properties-sagemaker-modelexplainabilityjobdefinition-stoppingcondition-properties"></a>

`MaxRuntimeInSeconds`  <a name="cfn-sagemaker-modelexplainabilityjobdefinition-stoppingcondition-maxruntimeinseconds"></a>
The maximum length of time, in seconds, that a training or compilation job can run before it is stopped.
For compilation jobs, if the job does not complete during this time, a `TimeOut` error is generated. We recommend starting with 900 seconds and increasing as necessary based on your model.
For all other jobs, if the job does not complete during this time, SageMaker ends the job. When `RetryStrategy` is specified in the job request, `MaxRuntimeInSeconds` specifies the maximum time for all of the attempts in total, not each individual attempt. The default value is 1 day. The maximum value is 28 days.
The maximum time that a `TrainingJob` can run in total, including any time spent publishing metrics or archiving and uploading models after it has been stopped, is 30 days.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Maximum*: `86400`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
