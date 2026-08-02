---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-pipeline-pipelinedefinition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Pipeline PipelineDefinition
<a name="aws-properties-sagemaker-pipeline-pipelinedefinition"></a>

The definition of the pipeline. This can be either a JSON string or an Amazon S3 location.

## Syntax
<a name="aws-properties-sagemaker-pipeline-pipelinedefinition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-pipeline-pipelinedefinition-syntax.json"></a>

```
{
  "[PipelineDefinitionBody](#cfn-sagemaker-pipeline-pipelinedefinition-pipelinedefinitionbody)" : {{String}},
  "[PipelineDefinitionS3Location](#cfn-sagemaker-pipeline-pipelinedefinition-pipelinedefinitions3location)" : {{S3Location}}
}
```

### YAML
<a name="aws-properties-sagemaker-pipeline-pipelinedefinition-syntax.yaml"></a>

```
  [PipelineDefinitionBody](#cfn-sagemaker-pipeline-pipelinedefinition-pipelinedefinitionbody): {{String}}
  [PipelineDefinitionS3Location](#cfn-sagemaker-pipeline-pipelinedefinition-pipelinedefinitions3location): {{
    S3Location}}
```

## Properties
<a name="aws-properties-sagemaker-pipeline-pipelinedefinition-properties"></a>

`PipelineDefinitionBody`  <a name="cfn-sagemaker-pipeline-pipelinedefinition-pipelinedefinitionbody"></a>
The [JSON pipeline definition](https://aws-sagemaker-mlops.github.io/sagemaker-model-building-pipeline-definition-JSON-schema/) of the pipeline.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PipelineDefinitionS3Location`  <a name="cfn-sagemaker-pipeline-pipelinedefinition-pipelinedefinitions3location"></a>
The location of the pipeline definition stored in Amazon S3. If specified, SageMaker retrieves the pipeline definition from this location.
*Required*: No
*Type*: [S3Location](aws-properties-sagemaker-pipeline-s3location.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
