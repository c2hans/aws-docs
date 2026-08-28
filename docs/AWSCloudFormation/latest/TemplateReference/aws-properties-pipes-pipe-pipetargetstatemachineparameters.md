---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-pipes-pipe-pipetargetstatemachineparameters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Pipes::Pipe PipeTargetStateMachineParameters
<a name="aws-properties-pipes-pipe-pipetargetstatemachineparameters"></a>

The parameters for using a Step Functions state machine as a target.

## Syntax
<a name="aws-properties-pipes-pipe-pipetargetstatemachineparameters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-pipes-pipe-pipetargetstatemachineparameters-syntax.json"></a>

```
{
  "[InvocationType](#cfn-pipes-pipe-pipetargetstatemachineparameters-invocationtype)" : {{String}}
}
```

### YAML
<a name="aws-properties-pipes-pipe-pipetargetstatemachineparameters-syntax.yaml"></a>

```
  [InvocationType](#cfn-pipes-pipe-pipetargetstatemachineparameters-invocationtype): {{String}}
```

## Properties
<a name="aws-properties-pipes-pipe-pipetargetstatemachineparameters-properties"></a>

`InvocationType`  <a name="cfn-pipes-pipe-pipetargetstatemachineparameters-invocationtype"></a>
Specify whether to invoke the Step Functions state machine synchronously or asynchronously.
+ `REQUEST_RESPONSE` (default) - Invoke synchronously. For more information, see [StartSyncExecution](https://docs.aws.amazon.com/step-functions/latest/apireference/API_StartSyncExecution.html) in the *AWS Step Functions API Reference*.
**Note**
`REQUEST_RESPONSE` is not supported for `STANDARD` state machine workflows.
+ `FIRE_AND_FORGET` - Invoke asynchronously. For more information, see [StartExecution](https://docs.aws.amazon.com/step-functions/latest/apireference/API_StartExecution.html) in the *AWS Step Functions API Reference*.
For more information, see [Invocation types](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes.html#pipes-invocation) in the *Amazon EventBridge User Guide*.
*Required*: No
*Type*: String
*Allowed values*: `REQUEST_RESPONSE | FIRE_AND_FORGET`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
