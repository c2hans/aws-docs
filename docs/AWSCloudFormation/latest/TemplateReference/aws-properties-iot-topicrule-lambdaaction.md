---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-topicrule-lambdaaction.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::TopicRule LambdaAction
<a name="aws-properties-iot-topicrule-lambdaaction"></a>

Describes an action to invoke a Lambda function.

## Syntax
<a name="aws-properties-iot-topicrule-lambdaaction-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iot-topicrule-lambdaaction-syntax.json"></a>

```
{
  "[FunctionArn](#cfn-iot-topicrule-lambdaaction-functionarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-iot-topicrule-lambdaaction-syntax.yaml"></a>

```
  [FunctionArn](#cfn-iot-topicrule-lambdaaction-functionarn): {{String}}
```

## Properties
<a name="aws-properties-iot-topicrule-lambdaaction-properties"></a>

`FunctionArn`  <a name="cfn-iot-topicrule-lambdaaction-functionarn"></a>
The ARN of the Lambda function.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
