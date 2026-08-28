---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-topicrule-snsaction.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::TopicRule SnsAction
<a name="aws-properties-iot-topicrule-snsaction"></a>

Describes an action to publish to an Amazon SNS topic.

## Syntax
<a name="aws-properties-iot-topicrule-snsaction-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iot-topicrule-snsaction-syntax.json"></a>

```
{
  "[MessageFormat](#cfn-iot-topicrule-snsaction-messageformat)" : {{String}},
  "[RoleArn](#cfn-iot-topicrule-snsaction-rolearn)" : {{String}},
  "[TargetArn](#cfn-iot-topicrule-snsaction-targetarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-iot-topicrule-snsaction-syntax.yaml"></a>

```
  [MessageFormat](#cfn-iot-topicrule-snsaction-messageformat): {{String}}
  [RoleArn](#cfn-iot-topicrule-snsaction-rolearn): {{String}}
  [TargetArn](#cfn-iot-topicrule-snsaction-targetarn): {{String}}
```

## Properties
<a name="aws-properties-iot-topicrule-snsaction-properties"></a>

`MessageFormat`  <a name="cfn-iot-topicrule-snsaction-messageformat"></a>
(Optional) The message format of the message to publish. Accepted values are "JSON" and "RAW". The default value of the attribute is "RAW". SNS uses this setting to determine if the payload should be parsed and relevant platform-specific bits of the payload should be extracted. For more information, see [Amazon SNS Message and JSON Formats](https://docs.aws.amazon.com/sns/latest/dg/json-formats.html) in the *Amazon Simple Notification Service Developer Guide*.
*Required*: No
*Type*: String
*Allowed values*: `RAW | JSON`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleArn`  <a name="cfn-iot-topicrule-snsaction-rolearn"></a>
The ARN of the IAM role that grants access.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetArn`  <a name="cfn-iot-topicrule-snsaction-targetarn"></a>
The ARN of the SNS topic.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
