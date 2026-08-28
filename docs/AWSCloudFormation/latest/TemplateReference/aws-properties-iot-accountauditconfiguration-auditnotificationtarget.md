---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-accountauditconfiguration-auditnotificationtarget.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::AccountAuditConfiguration AuditNotificationTarget
<a name="aws-properties-iot-accountauditconfiguration-auditnotificationtarget"></a>

Information about the targets to which audit notifications are sent.

## Syntax
<a name="aws-properties-iot-accountauditconfiguration-auditnotificationtarget-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iot-accountauditconfiguration-auditnotificationtarget-syntax.json"></a>

```
{
  "[Enabled](#cfn-iot-accountauditconfiguration-auditnotificationtarget-enabled)" : {{Boolean}},
  "[RoleArn](#cfn-iot-accountauditconfiguration-auditnotificationtarget-rolearn)" : {{String}},
  "[TargetArn](#cfn-iot-accountauditconfiguration-auditnotificationtarget-targetarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-iot-accountauditconfiguration-auditnotificationtarget-syntax.yaml"></a>

```
  [Enabled](#cfn-iot-accountauditconfiguration-auditnotificationtarget-enabled): {{Boolean}}
  [RoleArn](#cfn-iot-accountauditconfiguration-auditnotificationtarget-rolearn): {{String}}
  [TargetArn](#cfn-iot-accountauditconfiguration-auditnotificationtarget-targetarn): {{String}}
```

## Properties
<a name="aws-properties-iot-accountauditconfiguration-auditnotificationtarget-properties"></a>

`Enabled`  <a name="cfn-iot-accountauditconfiguration-auditnotificationtarget-enabled"></a>
True if notifications to the target are enabled.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleArn`  <a name="cfn-iot-accountauditconfiguration-auditnotificationtarget-rolearn"></a>
The ARN of the role that grants permission to send notifications to the target.
*Required*: No
*Type*: String
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetArn`  <a name="cfn-iot-accountauditconfiguration-auditnotificationtarget-targetarn"></a>
The ARN of the target (SNS topic) to which audit notifications are sent.
*Required*: No
*Type*: String
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
