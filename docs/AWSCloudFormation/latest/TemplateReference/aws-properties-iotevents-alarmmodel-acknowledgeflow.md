---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotevents-alarmmodel-acknowledgeflow.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTEvents::AlarmModel AcknowledgeFlow
<a name="aws-properties-iotevents-alarmmodel-acknowledgeflow"></a>

Specifies whether to get notified for alarm state changes.

## Syntax
<a name="aws-properties-iotevents-alarmmodel-acknowledgeflow-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotevents-alarmmodel-acknowledgeflow-syntax.json"></a>

```
{
  "[Enabled](#cfn-iotevents-alarmmodel-acknowledgeflow-enabled)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-iotevents-alarmmodel-acknowledgeflow-syntax.yaml"></a>

```
  [Enabled](#cfn-iotevents-alarmmodel-acknowledgeflow-enabled): {{Boolean}}
```

## Properties
<a name="aws-properties-iotevents-alarmmodel-acknowledgeflow-properties"></a>

`Enabled`  <a name="cfn-iotevents-alarmmodel-acknowledgeflow-enabled"></a>
The value must be `TRUE` or `FALSE`. If `TRUE`, you receive a notification when the alarm state changes. You must choose to acknowledge the notification before the alarm state can return to `NORMAL`. If `FALSE`, you won't receive notifications. The alarm automatically changes to the `NORMAL` state when the input property value returns to the specified range.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
