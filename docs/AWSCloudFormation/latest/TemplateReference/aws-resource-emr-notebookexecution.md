---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-emr-notebookexecution.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMR::NotebookExecution
<a name="aws-resource-emr-notebookexecution"></a>

A notebook execution. An execution is a specific instance that an Amazon EMR Notebook is run using the `StartNotebookExecution` action.

## Syntax
<a name="aws-resource-emr-notebookexecution-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-emr-notebookexecution-syntax.json"></a>

```
{
  "Type" : "AWS::EMR::NotebookExecution",
  "Properties" : {
      "[EnvironmentVariables](#cfn-emr-notebookexecution-environmentvariables)" : {{{{{Key}}: {{Value}}, ...}}},
      "[ExecutionEngine](#cfn-emr-notebookexecution-executionengine)" : {{ExecutionEngineConfig}},
      "[NotebookExecutionName](#cfn-emr-notebookexecution-notebookexecutionname)" : {{String}},
      "[NotebookParams](#cfn-emr-notebookexecution-notebookparams)" : {{String}},
      "[NotebookS3Location](#cfn-emr-notebookexecution-notebooks3location)" : {{NotebookS3Location}},
      "[OutputNotebookFormat](#cfn-emr-notebookexecution-outputnotebookformat)" : {{String}},
      "[OutputNotebookS3Location](#cfn-emr-notebookexecution-outputnotebooks3location)" : {{OutputNotebookS3Location}},
      "[Tags](#cfn-emr-notebookexecution-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-emr-notebookexecution-syntax.yaml"></a>

```
Type: AWS::EMR::NotebookExecution
Properties:
  [EnvironmentVariables](#cfn-emr-notebookexecution-environmentvariables): {{
    {{Key}}: {{Value}}}}
  [ExecutionEngine](#cfn-emr-notebookexecution-executionengine): {{
    ExecutionEngineConfig}}
  [NotebookExecutionName](#cfn-emr-notebookexecution-notebookexecutionname): {{String}}
  [NotebookParams](#cfn-emr-notebookexecution-notebookparams): {{String}}
  [NotebookS3Location](#cfn-emr-notebookexecution-notebooks3location): {{
    NotebookS3Location}}
  [OutputNotebookFormat](#cfn-emr-notebookexecution-outputnotebookformat): {{String}}
  [OutputNotebookS3Location](#cfn-emr-notebookexecution-outputnotebooks3location): {{
    OutputNotebookS3Location}}
  [Tags](#cfn-emr-notebookexecution-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-emr-notebookexecution-properties"></a>

`EnvironmentVariables`  <a name="cfn-emr-notebookexecution-environmentvariables"></a>
The environment variables associated with the notebook execution.
*Required*: No
*Type*: Object of String
*Pattern*: `^[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]{0,256}$`
*Maximum*: `10280`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ExecutionEngine`  <a name="cfn-emr-notebookexecution-executionengine"></a>
The execution engine, such as an Amazon EMR cluster, used to run the Amazon EMR notebook and perform the notebook execution.
*Required*: No
*Type*: [ExecutionEngineConfig](aws-properties-emr-notebookexecution-executionengineconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`NotebookExecutionName`  <a name="cfn-emr-notebookexecution-notebookexecutionname"></a>
A name for the notebook execution.
*Required*: No
*Type*: String
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`NotebookParams`  <a name="cfn-emr-notebookexecution-notebookparams"></a>
Input parameters in JSON format passed to the Amazon EMR Notebook at runtime for execution.
*Required*: No
*Type*: String
*Maximum*: `10280`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`NotebookS3Location`  <a name="cfn-emr-notebookexecution-notebooks3location"></a>
The Amazon S3 location that stores the notebook execution input.
*Required*: No
*Type*: [NotebookS3Location](aws-properties-emr-notebookexecution-notebooks3location.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`OutputNotebookFormat`  <a name="cfn-emr-notebookexecution-outputnotebookformat"></a>
The output format for the notebook execution.
*Required*: No
*Type*: String
*Allowed values*: `HTML`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`OutputNotebookS3Location`  <a name="cfn-emr-notebookexecution-outputnotebooks3location"></a>
The Amazon S3 location for the notebook execution output.
*Required*: No
*Type*: [OutputNotebookS3Location](aws-properties-emr-notebookexecution-outputnotebooks3location.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-emr-notebookexecution-tags"></a>
A list of tags associated with a notebook execution. Tags are user-defined key-value pairs that consist of a required key string with a maximum of 128 characters and an optional value string with a maximum of 256 characters.
*Required*: No
*Type*: Array of [Tag](aws-properties-emr-notebookexecution-tag.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-emr-notebookexecution-return-values"></a>

### Ref
<a name="aws-resource-emr-notebookexecution-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-emr-notebookexecution-return-values-fn--getatt"></a>

####
<a name="aws-resource-emr-notebookexecution-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the notebook execution.

`NotebookExecutionId`  <a name="NotebookExecutionId-fn::getatt"></a>
The unique identifier of a notebook execution.

`StartTime`  <a name="StartTime-fn::getatt"></a>
The timestamp when notebook execution started.

`Status`  <a name="Status-fn::getatt"></a>
The status of the notebook execution.
+ `START_PENDING` indicates that the cluster has received the execution request but execution has not begun.
+ `STARTING` indicates that the execution is starting on the cluster.
+ `RUNNING` indicates that the execution is being processed by the cluster.
+ `FINISHING` indicates that execution processing is in the final stages.
+ `FINISHED` indicates that the execution has completed without error.
+ `FAILING` indicates that the execution is failing and will not finish successfully.
+ `FAILED` indicates that the execution failed.
+ `STOP_PENDING` indicates that the cluster has received a `StopNotebookExecution` request and the stop is pending.
+ `STOPPING` indicates that the cluster is in the process of stopping the execution as a result of a `StopNotebookExecution` request.
+ `STOPPED` indicates that the execution stopped because of a `StopNotebookExecution` request.
