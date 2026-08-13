---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-omics-task.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Omics::Task
<a name="aws-resource-omics-task"></a>

<a name="aws-resource-omics-task-description"></a>The `AWS::Omics::Task` resource Property description not available. for Omics.

## Syntax
<a name="aws-resource-omics-task-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-omics-task-syntax.json"></a>

```
{
  "Type" : "AWS::Omics::Task",
  "Properties" : {
      "[RunId](#cfn-omics-task-runid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-omics-task-syntax.yaml"></a>

```
Type: AWS::Omics::Task
Properties:
  [RunId](#cfn-omics-task-runid): {{String}}
```

## Properties
<a name="aws-resource-omics-task-properties"></a>

`RunId`  <a name="cfn-omics-task-runid"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^[0-9]+$`
*Minimum*: `1`
*Maximum*: `18`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-omics-task-return-values"></a>

### Ref
<a name="aws-resource-omics-task-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-omics-task-return-values-fn--getatt"></a>

####
<a name="aws-resource-omics-task-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`Cpus`  <a name="Cpus-fn::getatt"></a>
The task's CPU count.

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
When the task was created.

`Gpus`  <a name="Gpus-fn::getatt"></a>
 The number of Graphics Processing Units (GPU) specified for the task.

`InstanceType`  <a name="InstanceType-fn::getatt"></a>
 The instance type for a task.

`LogStream`  <a name="LogStream-fn::getatt"></a>
Property description not available.

`Memory`  <a name="Memory-fn::getatt"></a>
The task's memory use in gigabyes.

`Name`  <a name="Name-fn::getatt"></a>
The task's name.

`Status`  <a name="Status-fn::getatt"></a>
The task's status.

`TaskId`  <a name="TaskId-fn::getatt"></a>
The task's ID.
