---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-pipelineexecution-parallelismconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::PipelineExecution ParallelismConfiguration
<a name="aws-properties-sagemaker-pipelineexecution-parallelismconfiguration"></a>

Configuration that controls the parallelism of the pipeline. By default, the parallelism configuration specified applies to all executions of the pipeline unless overridden.

## Syntax
<a name="aws-properties-sagemaker-pipelineexecution-parallelismconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-pipelineexecution-parallelismconfiguration-syntax.json"></a>

```
{
  "[MaxParallelExecutionSteps](#cfn-sagemaker-pipelineexecution-parallelismconfiguration-maxparallelexecutionsteps)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-sagemaker-pipelineexecution-parallelismconfiguration-syntax.yaml"></a>

```
  [MaxParallelExecutionSteps](#cfn-sagemaker-pipelineexecution-parallelismconfiguration-maxparallelexecutionsteps): {{Integer}}
```

## Properties
<a name="aws-properties-sagemaker-pipelineexecution-parallelismconfiguration-properties"></a>

`MaxParallelExecutionSteps`  <a name="cfn-sagemaker-pipelineexecution-parallelismconfiguration-maxparallelexecutionsteps"></a>
The max number of steps that can be executed in parallel.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
