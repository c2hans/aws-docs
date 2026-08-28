---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-pipes-pipe-pipetargetlambdafunctionparameters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Pipes::Pipe PipeTargetLambdaFunctionParameters
<a name="aws-properties-pipes-pipe-pipetargetlambdafunctionparameters"></a>

The parameters for using a Lambda function as a target.

## Syntax
<a name="aws-properties-pipes-pipe-pipetargetlambdafunctionparameters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-pipes-pipe-pipetargetlambdafunctionparameters-syntax.json"></a>

```
{
  "[InvocationType](#cfn-pipes-pipe-pipetargetlambdafunctionparameters-invocationtype)" : {{String}}
}
```

### YAML
<a name="aws-properties-pipes-pipe-pipetargetlambdafunctionparameters-syntax.yaml"></a>

```
  [InvocationType](#cfn-pipes-pipe-pipetargetlambdafunctionparameters-invocationtype): {{String}}
```

## Properties
<a name="aws-properties-pipes-pipe-pipetargetlambdafunctionparameters-properties"></a>

`InvocationType`  <a name="cfn-pipes-pipe-pipetargetlambdafunctionparameters-invocationtype"></a>
Specify whether to invoke the function synchronously or asynchronously.
+ `REQUEST_RESPONSE` (default) - Invoke synchronously. This corresponds to the `RequestResponse` option in the `InvocationType` parameter for the Lambda [Invoke](https://docs.aws.amazon.com/lambda/latest/dg/API_Invoke.html#API_Invoke_RequestSyntax) API.
+ `FIRE_AND_FORGET` - Invoke asynchronously. This corresponds to the `Event` option in the `InvocationType` parameter for the Lambda [Invoke](https://docs.aws.amazon.com/lambda/latest/dg/API_Invoke.html#API_Invoke_RequestSyntax) API.
For more information, see [Invocation types](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes.html#pipes-invocation) in the *Amazon EventBridge User Guide*.
*Required*: No
*Type*: String
*Allowed values*: `REQUEST_RESPONSE | FIRE_AND_FORGET`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
