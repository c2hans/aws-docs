---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-pipes-pipe-pipetargetsagemakerpipelineparameters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Pipes::Pipe PipeTargetSageMakerPipelineParameters
<a name="aws-properties-pipes-pipe-pipetargetsagemakerpipelineparameters"></a>

The parameters for using a SageMaker AI pipeline as a target.

## Syntax
<a name="aws-properties-pipes-pipe-pipetargetsagemakerpipelineparameters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-pipes-pipe-pipetargetsagemakerpipelineparameters-syntax.json"></a>

```
{
  "[PipelineParameterList](#cfn-pipes-pipe-pipetargetsagemakerpipelineparameters-pipelineparameterlist)" : {{[ SageMakerPipelineParameter, ... ]}}
}
```

### YAML
<a name="aws-properties-pipes-pipe-pipetargetsagemakerpipelineparameters-syntax.yaml"></a>

```
  [PipelineParameterList](#cfn-pipes-pipe-pipetargetsagemakerpipelineparameters-pipelineparameterlist): {{
    - SageMakerPipelineParameter}}
```

## Properties
<a name="aws-properties-pipes-pipe-pipetargetsagemakerpipelineparameters-properties"></a>

`PipelineParameterList`  <a name="cfn-pipes-pipe-pipetargetsagemakerpipelineparameters-pipelineparameterlist"></a>
List of Parameter names and values for SageMaker AI Model Building Pipeline execution.
*Required*: No
*Type*: Array of [SageMakerPipelineParameter](aws-properties-pipes-pipe-sagemakerpipelineparameter.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
