---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emr-notebookexecution-executionengineconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMR::NotebookExecution ExecutionEngineConfig
<a name="aws-properties-emr-notebookexecution-executionengineconfig"></a>

Specifies the execution engine (cluster) to run the notebook and perform the notebook execution, for example, an Amazon EMR cluster.

## Syntax
<a name="aws-properties-emr-notebookexecution-executionengineconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emr-notebookexecution-executionengineconfig-syntax.json"></a>

```
{
  "[Id](#cfn-emr-notebookexecution-executionengineconfig-id)" : {{String}},
  "[Type](#cfn-emr-notebookexecution-executionengineconfig-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-emr-notebookexecution-executionengineconfig-syntax.yaml"></a>

```
  [Id](#cfn-emr-notebookexecution-executionengineconfig-id): {{String}}
  [Type](#cfn-emr-notebookexecution-executionengineconfig-type): {{String}}
```

## Properties
<a name="aws-properties-emr-notebookexecution-executionengineconfig-properties"></a>

`Id`  <a name="cfn-emr-notebookexecution-executionengineconfig-id"></a>
The unique identifier of the execution engine. For an Amazon EMR cluster, this is the cluster ID.
*Required*: Yes
*Type*: String
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Type`  <a name="cfn-emr-notebookexecution-executionengineconfig-type"></a>
The type of execution engine. A value of `EMR` specifies an Amazon EMR cluster.
*Required*: No
*Type*: String
*Allowed values*: `EMR`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
