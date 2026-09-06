---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-multiplexprogram-multiplexprogrampipelinedetail.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Multiplexprogram MultiplexProgramPipelineDetail
<a name="aws-properties-medialive-multiplexprogram-multiplexprogrampipelinedetail"></a>

The current source for one of the pipelines in the multiplex.

## Syntax
<a name="aws-properties-medialive-multiplexprogram-multiplexprogrampipelinedetail-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-multiplexprogram-multiplexprogrampipelinedetail-syntax.json"></a>

```
{
  "[ActiveChannelPipeline](#cfn-medialive-multiplexprogram-multiplexprogrampipelinedetail-activechannelpipeline)" : {{String}},
  "[PipelineId](#cfn-medialive-multiplexprogram-multiplexprogrampipelinedetail-pipelineid)" : {{String}}
}
```

### YAML
<a name="aws-properties-medialive-multiplexprogram-multiplexprogrampipelinedetail-syntax.yaml"></a>

```
  [ActiveChannelPipeline](#cfn-medialive-multiplexprogram-multiplexprogrampipelinedetail-activechannelpipeline): {{String}}
  [PipelineId](#cfn-medialive-multiplexprogram-multiplexprogrampipelinedetail-pipelineid): {{String}}
```

## Properties
<a name="aws-properties-medialive-multiplexprogram-multiplexprogrampipelinedetail-properties"></a>

`ActiveChannelPipeline`  <a name="cfn-medialive-multiplexprogram-multiplexprogrampipelinedetail-activechannelpipeline"></a>
Identifies the channel pipeline that is currently active for the pipeline (identified by PipelineId) in the multiplex.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PipelineId`  <a name="cfn-medialive-multiplexprogram-multiplexprogrampipelinedetail-pipelineid"></a>
Identifies a specific pipeline in the multiplex.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
