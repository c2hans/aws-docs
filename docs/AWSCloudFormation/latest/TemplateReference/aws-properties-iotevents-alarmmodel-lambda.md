---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotevents-alarmmodel-lambda.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTEvents::AlarmModel Lambda
<a name="aws-properties-iotevents-alarmmodel-lambda"></a>

Calls a Lambda function, passing in information about the detector model instance and the event that triggered the action.

## Syntax
<a name="aws-properties-iotevents-alarmmodel-lambda-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotevents-alarmmodel-lambda-syntax.json"></a>

```
{
  "[FunctionArn](#cfn-iotevents-alarmmodel-lambda-functionarn)" : {{String}},
  "[Payload](#cfn-iotevents-alarmmodel-lambda-payload)" : {{Payload}}
}
```

### YAML
<a name="aws-properties-iotevents-alarmmodel-lambda-syntax.yaml"></a>

```
  [FunctionArn](#cfn-iotevents-alarmmodel-lambda-functionarn): {{String}}
  [Payload](#cfn-iotevents-alarmmodel-lambda-payload): {{
    Payload}}
```

## Properties
<a name="aws-properties-iotevents-alarmmodel-lambda-properties"></a>

`FunctionArn`  <a name="cfn-iotevents-alarmmodel-lambda-functionarn"></a>
The ARN of the Lambda function that is executed.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Payload`  <a name="cfn-iotevents-alarmmodel-lambda-payload"></a>
You can configure the action payload when you send a message to a Lambda function.
*Required*: No
*Type*: [Payload](aws-properties-iotevents-alarmmodel-payload.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
