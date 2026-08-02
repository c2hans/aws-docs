---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-scheduler-schedule-sagemakerpipelineparameters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Scheduler::Schedule SageMakerPipelineParameters
<a name="aws-properties-scheduler-schedule-sagemakerpipelineparameters"></a>

The templated target type for the Amazon SageMaker [https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_StartPipelineExecution.html](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_StartPipelineExecution.html) API operation.

## Syntax
<a name="aws-properties-scheduler-schedule-sagemakerpipelineparameters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-scheduler-schedule-sagemakerpipelineparameters-syntax.json"></a>

```
{
  "[PipelineParameterList](#cfn-scheduler-schedule-sagemakerpipelineparameters-pipelineparameterlist)" : {{[ SageMakerPipelineParameter, ... ]}}
}
```

### YAML
<a name="aws-properties-scheduler-schedule-sagemakerpipelineparameters-syntax.yaml"></a>

```
  [PipelineParameterList](#cfn-scheduler-schedule-sagemakerpipelineparameters-pipelineparameterlist): {{
    - SageMakerPipelineParameter}}
```

## Properties
<a name="aws-properties-scheduler-schedule-sagemakerpipelineparameters-properties"></a>

`PipelineParameterList`  <a name="cfn-scheduler-schedule-sagemakerpipelineparameters-pipelineparameterlist"></a>
List of parameter names and values to use when executing the SageMaker Model Building Pipeline.
*Required*: No
*Type*: Array of [SageMakerPipelineParameter](aws-properties-scheduler-schedule-sagemakerpipelineparameter.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
