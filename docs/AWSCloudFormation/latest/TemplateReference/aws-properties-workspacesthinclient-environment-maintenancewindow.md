---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-workspacesthinclient-environment-maintenancewindow.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WorkSpacesThinClient::Environment MaintenanceWindow
<a name="aws-properties-workspacesthinclient-environment-maintenancewindow"></a>

**Important**
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkSpaces Thin Client. After March 31, 2027, you will no longer be able to access the WorkSpaces Thin Client console or WorkSpaces Thin Client resources. For more information, see [Amazon WorkSpaces Thin Client end of support](https://docs.aws.amazon.com/workspaces-thin-client/latest/ug/workspacesthinclient-end-of-support.html).

Describes the maintenance window for a thin client device.

## Syntax
<a name="aws-properties-workspacesthinclient-environment-maintenancewindow-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-workspacesthinclient-environment-maintenancewindow-syntax.json"></a>

```
{
  "[ApplyTimeOf](#cfn-workspacesthinclient-environment-maintenancewindow-applytimeof)" : {{String}},
  "[DaysOfTheWeek](#cfn-workspacesthinclient-environment-maintenancewindow-daysoftheweek)" : {{[ String, ... ]}},
  "[EndTimeHour](#cfn-workspacesthinclient-environment-maintenancewindow-endtimehour)" : {{Integer}},
  "[EndTimeMinute](#cfn-workspacesthinclient-environment-maintenancewindow-endtimeminute)" : {{Integer}},
  "[StartTimeHour](#cfn-workspacesthinclient-environment-maintenancewindow-starttimehour)" : {{Integer}},
  "[StartTimeMinute](#cfn-workspacesthinclient-environment-maintenancewindow-starttimeminute)" : {{Integer}},
  "[Type](#cfn-workspacesthinclient-environment-maintenancewindow-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-workspacesthinclient-environment-maintenancewindow-syntax.yaml"></a>

```
  [ApplyTimeOf](#cfn-workspacesthinclient-environment-maintenancewindow-applytimeof): {{String}}
  [DaysOfTheWeek](#cfn-workspacesthinclient-environment-maintenancewindow-daysoftheweek): {{
    - String}}
  [EndTimeHour](#cfn-workspacesthinclient-environment-maintenancewindow-endtimehour): {{Integer}}
  [EndTimeMinute](#cfn-workspacesthinclient-environment-maintenancewindow-endtimeminute): {{Integer}}
  [StartTimeHour](#cfn-workspacesthinclient-environment-maintenancewindow-starttimehour): {{Integer}}
  [StartTimeMinute](#cfn-workspacesthinclient-environment-maintenancewindow-starttimeminute): {{Integer}}
  [Type](#cfn-workspacesthinclient-environment-maintenancewindow-type): {{String}}
```

## Properties
<a name="aws-properties-workspacesthinclient-environment-maintenancewindow-properties"></a>

`ApplyTimeOf`  <a name="cfn-workspacesthinclient-environment-maintenancewindow-applytimeof"></a>
The option to set the maintenance window during the device local time or Universal Coordinated Time (UTC).
*Required*: No
*Type*: String
*Allowed values*: `UTC | DEVICE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DaysOfTheWeek`  <a name="cfn-workspacesthinclient-environment-maintenancewindow-daysoftheweek"></a>
The days of the week during which the maintenance window is open.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `7`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EndTimeHour`  <a name="cfn-workspacesthinclient-environment-maintenancewindow-endtimehour"></a>
The hour for the maintenance window end (`00`-`23`).
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `23`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EndTimeMinute`  <a name="cfn-workspacesthinclient-environment-maintenancewindow-endtimeminute"></a>
The minutes for the maintenance window end (`00`-`59`).
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `59`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StartTimeHour`  <a name="cfn-workspacesthinclient-environment-maintenancewindow-starttimehour"></a>
The hour for the maintenance window start (`00`-`23`).
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `23`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StartTimeMinute`  <a name="cfn-workspacesthinclient-environment-maintenancewindow-starttimeminute"></a>
The minutes past the hour for the maintenance window start (`00`-`59`).
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `59`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-workspacesthinclient-environment-maintenancewindow-type"></a>
An option to select the default or custom maintenance window.
*Required*: Yes
*Type*: String
*Allowed values*: `SYSTEM | CUSTOM`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
