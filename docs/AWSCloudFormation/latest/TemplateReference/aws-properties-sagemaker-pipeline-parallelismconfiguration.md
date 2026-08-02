---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-pipeline-parallelismconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Pipeline ParallelismConfiguration
<a name="aws-properties-sagemaker-pipeline-parallelismconfiguration"></a>

Configuration that controls the parallelism of the pipeline. By default, the parallelism configuration specified applies to all executions of the pipeline unless overridden.

## Syntax
<a name="aws-properties-sagemaker-pipeline-parallelismconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-pipeline-parallelismconfiguration-syntax.json"></a>

```
{
  "[MaxParallelExecutionSteps](#cfn-sagemaker-pipeline-parallelismconfiguration-maxparallelexecutionsteps)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-sagemaker-pipeline-parallelismconfiguration-syntax.yaml"></a>

```
  [MaxParallelExecutionSteps](#cfn-sagemaker-pipeline-parallelismconfiguration-maxparallelexecutionsteps): {{Integer}}
```

## Properties
<a name="aws-properties-sagemaker-pipeline-parallelismconfiguration-properties"></a>

`MaxParallelExecutionSteps`  <a name="cfn-sagemaker-pipeline-parallelismconfiguration-maxparallelexecutionsteps"></a>
The max number of steps that can be executed in parallel.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
