---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-securityprofile-alerttarget.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::SecurityProfile AlertTarget
<a name="aws-properties-iot-securityprofile-alerttarget"></a>

A structure containing the alert target ARN and the role ARN.

## Syntax
<a name="aws-properties-iot-securityprofile-alerttarget-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iot-securityprofile-alerttarget-syntax.json"></a>

```
{
  "[AlertTargetArn](#cfn-iot-securityprofile-alerttarget-alerttargetarn)" : {{String}},
  "[RoleArn](#cfn-iot-securityprofile-alerttarget-rolearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-iot-securityprofile-alerttarget-syntax.yaml"></a>

```
  [AlertTargetArn](#cfn-iot-securityprofile-alerttarget-alerttargetarn): {{String}}
  [RoleArn](#cfn-iot-securityprofile-alerttarget-rolearn): {{String}}
```

## Properties
<a name="aws-properties-iot-securityprofile-alerttarget-properties"></a>

`AlertTargetArn`  <a name="cfn-iot-securityprofile-alerttarget-alerttargetarn"></a>
The Amazon Resource Name (ARN) of the notification target to which alerts are sent.
*Required*: Yes
*Type*: String
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleArn`  <a name="cfn-iot-securityprofile-alerttarget-rolearn"></a>
The ARN of the role that grants permission to send alerts to the notification target.
*Required*: Yes
*Type*: String
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
