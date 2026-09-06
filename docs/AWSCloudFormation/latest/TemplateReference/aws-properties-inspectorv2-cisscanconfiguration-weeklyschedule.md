---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-inspectorv2-cisscanconfiguration-weeklyschedule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::InspectorV2::CisScanConfiguration WeeklySchedule
<a name="aws-properties-inspectorv2-cisscanconfiguration-weeklyschedule"></a>

A weekly schedule.

## Syntax
<a name="aws-properties-inspectorv2-cisscanconfiguration-weeklyschedule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-inspectorv2-cisscanconfiguration-weeklyschedule-syntax.json"></a>

```
{
  "[Days](#cfn-inspectorv2-cisscanconfiguration-weeklyschedule-days)" : {{[ String, ... ]}},
  "[StartTime](#cfn-inspectorv2-cisscanconfiguration-weeklyschedule-starttime)" : {{Time}}
}
```

### YAML
<a name="aws-properties-inspectorv2-cisscanconfiguration-weeklyschedule-syntax.yaml"></a>

```
  [Days](#cfn-inspectorv2-cisscanconfiguration-weeklyschedule-days): {{
    - String}}
  [StartTime](#cfn-inspectorv2-cisscanconfiguration-weeklyschedule-starttime): {{
    Time}}
```

## Properties
<a name="aws-properties-inspectorv2-cisscanconfiguration-weeklyschedule-properties"></a>

`Days`  <a name="cfn-inspectorv2-cisscanconfiguration-weeklyschedule-days"></a>
The weekly schedule's days.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `7`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StartTime`  <a name="cfn-inspectorv2-cisscanconfiguration-weeklyschedule-starttime"></a>
The weekly schedule's start time.
*Required*: Yes
*Type*: [Time](aws-properties-inspectorv2-cisscanconfiguration-time.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
