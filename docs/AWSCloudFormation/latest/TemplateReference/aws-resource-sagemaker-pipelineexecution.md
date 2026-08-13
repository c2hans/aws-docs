---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-sagemaker-pipelineexecution.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::PipelineExecution
<a name="aws-resource-sagemaker-pipelineexecution"></a>

An execution of a pipeline.

## Syntax
<a name="aws-resource-sagemaker-pipelineexecution-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-sagemaker-pipelineexecution-syntax.json"></a>

```
{
  "Type" : "AWS::SageMaker::PipelineExecution"
}
```

### YAML
<a name="aws-resource-sagemaker-pipelineexecution-syntax.yaml"></a>

```
Type: AWS::SageMaker::PipelineExecution
```

## Return values
<a name="aws-resource-sagemaker-pipelineexecution-return-values"></a>

### Ref
<a name="aws-resource-sagemaker-pipelineexecution-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-sagemaker-pipelineexecution-return-values-fn--getatt"></a>

####
<a name="aws-resource-sagemaker-pipelineexecution-return-values-fn--getatt-fn--getatt"></a>

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
The creation time of the pipeline execution.

`LastModifiedTime`  <a name="LastModifiedTime-fn::getatt"></a>
The time that the pipeline execution was last modified.

`PipelineArn`  <a name="PipelineArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the pipeline that was executed.

`PipelineExecutionArn`  <a name="PipelineExecutionArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the pipeline execution.

`PipelineExecutionDescription`  <a name="PipelineExecutionDescription-fn::getatt"></a>
The description of the pipeline execution.

`PipelineExecutionDisplayName`  <a name="PipelineExecutionDisplayName-fn::getatt"></a>
The display name of the pipeline execution.

`PipelineExecutionId`  <a name="PipelineExecutionId-fn::getatt"></a>
Property description not available.

`PipelineExecutionStatus`  <a name="PipelineExecutionStatus-fn::getatt"></a>
The status of the pipeline status.

`PipelineName`  <a name="PipelineName-fn::getatt"></a>
Property description not available.

`PipelineVersionId`  <a name="PipelineVersionId-fn::getatt"></a>
The ID of the pipeline version that started this execution.

`Tags`  <a name="Tags-fn::getatt"></a>
Property description not available.
