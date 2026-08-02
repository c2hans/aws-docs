---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-imagebuilder-workflowstepexecution.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ImageBuilder::WorkflowStepExecution
<a name="aws-resource-imagebuilder-workflowstepexecution"></a>

Contains runtime details for an instance of a workflow that ran for the associated image build version.

## Syntax
<a name="aws-resource-imagebuilder-workflowstepexecution-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-imagebuilder-workflowstepexecution-syntax.json"></a>

```
{
  "Type" : "AWS::ImageBuilder::WorkflowStepExecution"
}
```

### YAML
<a name="aws-resource-imagebuilder-workflowstepexecution-syntax.yaml"></a>

```
Type: AWS::ImageBuilder::WorkflowStepExecution
```

## Return values
<a name="aws-resource-imagebuilder-workflowstepexecution-return-values"></a>

### Ref
<a name="aws-resource-imagebuilder-workflowstepexecution-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-imagebuilder-workflowstepexecution-return-values-fn--getatt"></a>

####
<a name="aws-resource-imagebuilder-workflowstepexecution-return-values-fn--getatt-fn--getatt"></a>

`Action`  <a name="Action-fn::getatt"></a>
The name of the step action.

`EndTime`  <a name="EndTime-fn::getatt"></a>
Property description not available.

`ImageBuildVersionArn`  <a name="ImageBuildVersionArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the image build version that ran the workflow.

`Inputs`  <a name="Inputs-fn::getatt"></a>
Property description not available.

`Name`  <a name="Name-fn::getatt"></a>
The name of the workflow step.

`OnFailure`  <a name="OnFailure-fn::getatt"></a>
Property description not available.

`Outputs`  <a name="Outputs-fn::getatt"></a>
Property description not available.

`StartTime`  <a name="StartTime-fn::getatt"></a>
The timestamp when the workflow step started.

`Status`  <a name="Status-fn::getatt"></a>
Property description not available.

`StepExecutionId`  <a name="StepExecutionId-fn::getatt"></a>
Uniquely identifies the workflow step that ran for the associated image build version.

`TimeoutSeconds`  <a name="TimeoutSeconds-fn::getatt"></a>
Property description not available.

`WorkflowBuildVersionArn`  <a name="WorkflowBuildVersionArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the workflow resource that ran.

`WorkflowExecutionId`  <a name="WorkflowExecutionId-fn::getatt"></a>
Uniquely identifies the runtime instance of the workflow that contains the workflow step that ran for the associated image build version.
