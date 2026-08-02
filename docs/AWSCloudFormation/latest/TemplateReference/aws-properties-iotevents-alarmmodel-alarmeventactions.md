---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotevents-alarmmodel-alarmeventactions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTEvents::AlarmModel AlarmEventActions
<a name="aws-properties-iotevents-alarmmodel-alarmeventactions"></a>

Contains information about one or more alarm actions.

## Syntax
<a name="aws-properties-iotevents-alarmmodel-alarmeventactions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotevents-alarmmodel-alarmeventactions-syntax.json"></a>

```
{
  "[AlarmActions](#cfn-iotevents-alarmmodel-alarmeventactions-alarmactions)" : {{[ AlarmAction, ... ]}}
}
```

### YAML
<a name="aws-properties-iotevents-alarmmodel-alarmeventactions-syntax.yaml"></a>

```
  [AlarmActions](#cfn-iotevents-alarmmodel-alarmeventactions-alarmactions): {{
    - AlarmAction}}
```

## Properties
<a name="aws-properties-iotevents-alarmmodel-alarmeventactions-properties"></a>

`AlarmActions`  <a name="cfn-iotevents-alarmmodel-alarmeventactions-alarmactions"></a>
Specifies one or more supported actions to receive notifications when the alarm state changes.
*Required*: No
*Type*: Array of [AlarmAction](aws-properties-iotevents-alarmmodel-alarmaction.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
