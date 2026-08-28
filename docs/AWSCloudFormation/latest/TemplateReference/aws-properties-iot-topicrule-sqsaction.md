---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-topicrule-sqsaction.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::TopicRule SqsAction
<a name="aws-properties-iot-topicrule-sqsaction"></a>

Describes an action to publish data to an Amazon SQS queue.

## Syntax
<a name="aws-properties-iot-topicrule-sqsaction-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iot-topicrule-sqsaction-syntax.json"></a>

```
{
  "[QueueUrl](#cfn-iot-topicrule-sqsaction-queueurl)" : {{String}},
  "[RoleArn](#cfn-iot-topicrule-sqsaction-rolearn)" : {{String}},
  "[UseBase64](#cfn-iot-topicrule-sqsaction-usebase64)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-iot-topicrule-sqsaction-syntax.yaml"></a>

```
  [QueueUrl](#cfn-iot-topicrule-sqsaction-queueurl): {{String}}
  [RoleArn](#cfn-iot-topicrule-sqsaction-rolearn): {{String}}
  [UseBase64](#cfn-iot-topicrule-sqsaction-usebase64): {{Boolean}}
```

## Properties
<a name="aws-properties-iot-topicrule-sqsaction-properties"></a>

`QueueUrl`  <a name="cfn-iot-topicrule-sqsaction-queueurl"></a>
The URL of the Amazon SQS queue.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleArn`  <a name="cfn-iot-topicrule-sqsaction-rolearn"></a>
The ARN of the IAM role that grants access.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseBase64`  <a name="cfn-iot-topicrule-sqsaction-usebase64"></a>
Specifies whether to use Base64 encoding.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
