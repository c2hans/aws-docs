---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-durableexecution.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::DurableExecution
<a name="aws-resource-lambda-durableexecution"></a>

<a name="aws-resource-lambda-durableexecution-description"></a>The `AWS::Lambda::DurableExecution` resource Property description not available. for Lambda.

## Syntax
<a name="aws-resource-lambda-durableexecution-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-lambda-durableexecution-syntax.json"></a>

```
{
  "Type" : "AWS::Lambda::DurableExecution",
  "Properties" : {
      "[FunctionName](#cfn-lambda-durableexecution-functionname)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-lambda-durableexecution-syntax.yaml"></a>

```
Type: AWS::Lambda::DurableExecution
Properties:
  [FunctionName](#cfn-lambda-durableexecution-functionname): {{String}}
```

## Properties
<a name="aws-resource-lambda-durableexecution-properties"></a>

`FunctionName`  <a name="cfn-lambda-durableexecution-functionname"></a>
Property description not available.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-lambda-durableexecution-return-values"></a>

### Ref
<a name="aws-resource-lambda-durableexecution-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-lambda-durableexecution-return-values-fn--getatt"></a>

####
<a name="aws-resource-lambda-durableexecution-return-values-fn--getatt-fn--getatt"></a>

`DurableExecutionArn`  <a name="DurableExecutionArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the durable execution.

`DurableExecutionName`  <a name="DurableExecutionName-fn::getatt"></a>
The name of the durable execution. This is either the name you provided when invoking the function, or a system-generated unique identifier if no name was provided.

`EndTimestamp`  <a name="EndTimestamp-fn::getatt"></a>
The date and time when the durable execution ended, in Unix timestamp format. This field is only present if the execution has completed (status is `SUCCEEDED`, `FAILED`, `TIMED_OUT`, or `STOPPED`).

`FunctionArn`  <a name="FunctionArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the Lambda function that was invoked to start this durable execution.

`StartTimestamp`  <a name="StartTimestamp-fn::getatt"></a>
The date and time when the durable execution started, in Unix timestamp format.

`Status`  <a name="Status-fn::getatt"></a>
The current status of the durable execution. Valid values are `RUNNING`, `SUCCEEDED`, `FAILED`, `TIMED_OUT`, and `STOPPED`.

`Version`  <a name="Version-fn::getatt"></a>
The version of the Lambda function that was invoked for this durable execution. This ensures that all replays during the execution use the same function version.
