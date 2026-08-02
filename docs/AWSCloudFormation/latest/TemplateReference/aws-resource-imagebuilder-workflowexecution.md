---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-imagebuilder-workflowexecution.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ImageBuilder::WorkflowExecution
<a name="aws-resource-imagebuilder-workflowexecution"></a>

<a name="aws-resource-imagebuilder-workflowexecution-description"></a>The `AWS::ImageBuilder::WorkflowExecution` resource Property description not available. for ImageBuilder.

## Syntax
<a name="aws-resource-imagebuilder-workflowexecution-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-imagebuilder-workflowexecution-syntax.json"></a>

```
{
  "Type" : "AWS::ImageBuilder::WorkflowExecution",
  "Properties" : {
      "[ImageBuildVersionArn](#cfn-imagebuilder-workflowexecution-imagebuildversionarn)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-imagebuilder-workflowexecution-syntax.yaml"></a>

```
Type: AWS::ImageBuilder::WorkflowExecution
Properties:
  [ImageBuildVersionArn](#cfn-imagebuilder-workflowexecution-imagebuildversionarn): {{String}}
```

## Properties
<a name="aws-resource-imagebuilder-workflowexecution-properties"></a>

`ImageBuildVersionArn`  <a name="cfn-imagebuilder-workflowexecution-imagebuildversionarn"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-imagebuilder-workflowexecution-return-values"></a>

### Ref
<a name="aws-resource-imagebuilder-workflowexecution-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-imagebuilder-workflowexecution-return-values-fn--getatt"></a>

####
<a name="aws-resource-imagebuilder-workflowexecution-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`EndTime`  <a name="EndTime-fn::getatt"></a>
The timestamp when this runtime instance of the workflow finished.

`StartTime`  <a name="StartTime-fn::getatt"></a>
The timestamp when the runtime instance of this workflow started.

`Status`  <a name="Status-fn::getatt"></a>
The current runtime status for this workflow.

`TotalStepCount`  <a name="TotalStepCount-fn::getatt"></a>
The total number of steps in the workflow. This should equal the sum of the step counts for steps that succeeded, were skipped, and failed.

`TotalStepsFailed`  <a name="TotalStepsFailed-fn::getatt"></a>
A runtime count for the number of steps in the workflow that failed.

`TotalStepsSkipped`  <a name="TotalStepsSkipped-fn::getatt"></a>
A runtime count for the number of steps in the workflow that were skipped.

`TotalStepsSucceeded`  <a name="TotalStepsSucceeded-fn::getatt"></a>
A runtime count for the number of steps in the workflow that ran successfully.

`Type`  <a name="Type-fn::getatt"></a>
Indicates what type of workflow that Image Builder ran for this runtime instance of the workflow.

`WorkflowBuildVersionArn`  <a name="WorkflowBuildVersionArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the workflow resource build version that ran.

`WorkflowExecutionId`  <a name="WorkflowExecutionId-fn::getatt"></a>
Unique identifier that Image Builder assigns to keep track of runtime resources each time it runs a workflow.
