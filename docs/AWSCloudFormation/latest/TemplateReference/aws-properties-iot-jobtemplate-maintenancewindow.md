---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-jobtemplate-maintenancewindow.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::JobTemplate MaintenanceWindow
<a name="aws-properties-iot-jobtemplate-maintenancewindow"></a>

An optional configuration within the `SchedulingConfig` to setup a recurring maintenance window with a predetermined start time and duration for the rollout of a job document to all devices in a target group for a job.

## Syntax
<a name="aws-properties-iot-jobtemplate-maintenancewindow-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iot-jobtemplate-maintenancewindow-syntax.json"></a>

```
{
  "[DurationInMinutes](#cfn-iot-jobtemplate-maintenancewindow-durationinminutes)" : {{Integer}},
  "[StartTime](#cfn-iot-jobtemplate-maintenancewindow-starttime)" : {{String}}
}
```

### YAML
<a name="aws-properties-iot-jobtemplate-maintenancewindow-syntax.yaml"></a>

```
  [DurationInMinutes](#cfn-iot-jobtemplate-maintenancewindow-durationinminutes): {{Integer}}
  [StartTime](#cfn-iot-jobtemplate-maintenancewindow-starttime): {{String}}
```

## Properties
<a name="aws-properties-iot-jobtemplate-maintenancewindow-properties"></a>

`DurationInMinutes`  <a name="cfn-iot-jobtemplate-maintenancewindow-durationinminutes"></a>
Displays the duration of the next maintenance window.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `1430`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`StartTime`  <a name="cfn-iot-jobtemplate-maintenancewindow-starttime"></a>
Displays the start time of the next maintenance window.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
